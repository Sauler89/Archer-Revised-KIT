"""Run the real WeiDU installer against synthetic, redistributable EE data.

These tests validate installation, generated binary resources and rollback.
They do not run the Infinity Engine or certify in-game behavior.
Set WEIDU to an absolute WeiDU executable path before running unittest.
"""
import os
from pathlib import Path
import shutil
import struct
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
WEIDU = os.environ.get("WEIDU") or shutil.which("weidu")
TP2 = "archerrevised/setup-archerrevised.tp2"


class ResourceDirectory(type(Path())):
    """Resolve resource names as the engine does, across WeiDU casing rules."""
    def __truediv__(self, name):
        direct = Path(super().__truediv__(name))
        if direct.exists() or not self.exists():
            return direct
        matches = [p for p in self.iterdir() if p.name.lower() == str(name).lower()]
        return Path(matches[0]) if matches else direct


def rows(path):
    return [line.split() for line in path.read_text().splitlines()[3:] if line.strip()]


def table(header, data, default="*"):
    return "2DA V1.0\n" + default + "\n " + header + "\n" + "\n".join(data) + "\n"


def resref(data):
    return data.split(b"\0", 1)[0].decode("ascii").upper()


def effect(data, offset, v2=False):
    if v2:
        return dict(op=struct.unpack_from("<I", data, offset)[0],
                    p1=struct.unpack_from("<i", data, offset + 12)[0],
                    p2=struct.unpack_from("<i", data, offset + 16)[0],
                    duration=struct.unpack_from("<I", data, offset + 24)[0],
                    resource=resref(data[offset + 32:offset + 40]),
                    special=struct.unpack_from("<I", data, offset + 56)[0])
    return dict(op=struct.unpack_from("<H", data, offset)[0],
                p1=struct.unpack_from("<i", data, offset + 4)[0],
                p2=struct.unpack_from("<i", data, offset + 8)[0],
                duration=struct.unpack_from("<I", data, offset + 14)[0],
                resource=resref(data[offset + 20:offset + 28]),
                special=struct.unpack_from("<I", data, offset + 44)[0])


def spell(path):
    data = path.read_bytes()
    assert data[:8] == b"SPL V1  "
    start = struct.unpack_from("<I", data, 0x64)[0]
    count = struct.unpack_from("<H", data, 0x68)[0]
    fx = struct.unpack_from("<I", data, 0x6a)[0]
    result = []
    for n in range(count):
        h = start + n * 0x28
        num, idx = struct.unpack_from("<HH", data, h + 0x1e)
        assert h + 0x28 <= len(data) and fx + (idx + num) * 0x30 <= len(data)
        result.append((struct.unpack_from("<H", data, h + 0x10)[0],
                       [effect(data, fx + (idx + i) * 0x30) for i in range(num)]))
    return result


def item(category=15):
    # A pre-existing, unrelated equipped effect must survive Manyshot patching.
    data = bytearray(0x72 + 0x30)
    data[:8] = b"ITM V1  "
    struct.pack_into("<H", data, 0x1c, category)
    struct.pack_into("<I", data, 0x64, 0x72)
    struct.pack_into("<I", data, 0x6a, 0x72)
    struct.pack_into("<H", data, 0x70, 1)
    struct.pack_into("<H", data, 0x72, 142)
    data[0x74] = 1
    return bytes(data)


def item_effects(path):
    data = path.read_bytes()
    fx = struct.unpack_from("<I", data, 0x6a)[0]
    first, count = struct.unpack_from("<HH", data, 0x6e)
    assert fx + (first + count) * 0x30 <= len(data)
    return [effect(data, fx + (first + i) * 0x30) for i in range(count)]


class Game:
    def __init__(self, game="bg2ee", symbol="FERALAN", hla=True,
                 critical=True, hp_row=True, clab_levels=40,
                 hla_abbrev="Ra0", hla_extra=False, mixed_alias=False):
        self.temp = tempfile.TemporaryDirectory(prefix="archer-ee-")
        self.path = Path(self.temp.name)
        self.override = ResourceDirectory(self.path / "override")
        self.override.mkdir()
        self.game = game
        self.symbol = symbol
        marker, kind = {"bgee": ("OH1000", 0x3f2),
                        "bg2ee": ("OH6000", 0x3f2),
                        "eet": ("OH6000", 0x3f2),
                        "iwdee": ("HOWPARTY", 0x3f4),
                        "unsupported": ("AR0104A", 0x3f2)}[game]
        (self.path / "chitin.key").write_bytes(
            b"KEY V1  " + struct.pack("<4I", 0, 1, 24, 24) +
            marker.encode().ljust(8, b"\0") + struct.pack("<HI", kind, 0))
        lang = self.path / "lang/en_us"
        lang.mkdir(parents=True)
        (lang / "dialog.tlk").write_bytes(b"TLK V1  " + struct.pack("<HII", 0, 0, 18))
        if game == "iwdee":
            self.put("howparty.2da", table("VALUE", ["0 1"]))
        if game == "eet":
            self.put("eet.flag", "EET")
        self.put("achievem.2da", table("VALUE", ["0 1"]))
        shutil.copytree(ROOT / "ArcherRevised", self.path / "archerrevised")
        # WeiDU 249 on Linux uses the traditional tolower filesystem layout.
        for f in sorted((self.path / "archerrevised").rglob("*"),
                        key=lambda f: len(f.parts), reverse=True):
            if f.name != f.name.lower():
                f.rename(f.with_name(f.name.lower()))
        self.put("kitlist.2da", table(
            "ROWNAME LOWER MIXED HELP ABILITIES PROFICIENCY UNUSABLE CLASS",
            [f"12 {symbol} 0 0 0 CLABRN02 36 0x4000 12",
             "13 OTHER 0 0 0 CLABRN02 37 0x4001 12"]))
        prof = "FERALAN" if mixed_alias else symbol
        self.put("weapprof.2da", table(f"ID FIGHTER RANGER {prof} OTHER", [
            f"{name} {n} 5 2 2 4" for n, name in enumerate([
                "CROSSBOW", "LONGBOW", "SHORTBOW", "LONGSWORD", "MACE",
                "QUARTERSTAFF", "2HANDED", "SWORDANDSHIELD", "SINGLEWEAPON",
                "2WEAPON", "SLING", "DART"], 100)]))
        self.put("abclasrq.2da", table("STR DEX CON INT WIS CHR",
                                     [f"{symbol} 13 0 0 0 14 0"]))
        self.put("abclsmod.2da", table("STR DEX CON INT WIS CHR",
                                     [f"{symbol} 0 0 -1 0 0 0"]))
        self.put("hpclass.2da", table("TABLE", ["RANGER HPRANG"] +
                                     ([f"{symbol} HPRANG"] if hp_row else [])))
        self.put("kit.ids", f"IDS V1.0\n0x400c {symbol}\n")
        self.put("projectl.ids", "IDS V1.0\n0 ARROW\n1 A7#IN03\n")
        self.put("statdesc.2da", table("STRREF BAM", ["82 0 STATES"], default="*"))
        self.put("splprot.2da", table("STAT VALUE RELATION", [
            "0 0x10a 0 4", "OTHER_RULE 40 20 4"]))
        missile = "SPCL124" if game == "iwdee" else "SPCL122"
        self.put("clabrn02.2da", table(" ".join(map(str, range(1, clab_levels + 1))), [
            "ABILITY1 " + " ".join("AP_" + missile if i % 3 == 0 else "****"
                                    for i in range(1, clab_levels + 1)),
            "ABILITY2 " + " ".join("GA_SPCL121" if i % 4 == 0 else "****"
                                    for i in range(1, clab_levels + 1)),
            "ABILITY3 " + " ".join("GA_SPCL922" if i == 1 and game == "iwdee"
                                    else "AP_CUSTOM" if i == 11 else "****"
                                    for i in range(1, clab_levels + 1))], default="****"))
        if hla:
            self.put("luabbr.2da", table("VALUE", [f"{symbol} {hla_abbrev}",
                                                      f"OTHER {hla_abbrev}",
                                                      f"RANGER {hla_abbrev}"]))
            extra = " MOD_EXTRA" if hla_extra else ""
            abilities = ["GA_SPCL907", "GA_CUSTOM", "GA_SPCL922"]
            if critical:
                abilities += ["GA_SPCL905"]
            self.put(f"lu{hla_abbrev}.2da", table(
                "ABILITY ICON STRREF MIN_LEV MAX_LEVEL NUM_ALLOWED PREREQUISITE EXCLUDED_BY ALIGNMENT_RESTRICT" + extra,
                [f"{n * 3} {a} * * 1 99 20 * * *" + (" KEEP" if hla_extra else "")
                 for n, a in enumerate(abilities)]))
        self.put("testbow.itm", item(15))
        self.put("testxbow.itm", item(27))
        self.put("testmelee.itm", item(19))
        self.before = {p.name: p.read_bytes() for p in self.override.iterdir()}
        self.hla_source = f"lu{hla_abbrev}.2da".lower()

    def put(self, name, content):
        (self.override / name.lower()).write_bytes(content if isinstance(content, bytes) else content.encode())

    def run(self, *args, success=True):
        result = subprocess.run([WEIDU, TP2, *args, "--no-exit-pause", "--use-lang",
                                 "en_us", "--language", "0"], cwd=self.path,
                                input="", text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, timeout=40)
        if success and result.returncode:
            raise AssertionError(result.stdout)
        if not success and result.returncode == 0:
            raise AssertionError("Expected WeiDU to fail:\n" + result.stdout)
        names = [p.name.lower() for p in self.override.iterdir()]
        if len(set(names)) != len(names):
            raise AssertionError("Duplicate resource names differing only in case")
        return result.stdout

    def install(self, *components, success=True):
        out = self.run("--force-install-list", *map(str, components), success=success)
        if success and "SUCCESSFULLY INSTALLED" not in out:
            raise AssertionError("Installer did not actually install anything:\n" + out)
        return out

    def close(self):
        self.temp.cleanup()


@unittest.skipUnless(WEIDU, "Set WEIDU to a real WeiDU executable")
class InstallationTests(unittest.TestCase):
    def game(self, *args, **kwargs):
        game = Game(*args, **kwargs)
        self.addCleanup(game.close)
        return game

    def test_all_sources_parse(self):
        g = self.game()
        for f in sorted((g.path / "archerrevised").rglob("*")):
            if f.suffix not in (".tp2", ".tph"):
                continue
            with self.subTest(file=f.name):
                r = subprocess.run([WEIDU, "--nogame", "--parse-check",
                                    "TP2" if f.suffix == ".tp2" else "TPA", str(f)],
                                   cwd=g.path, input="", capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
                self.assertIn("successfully parsed", r.stdout + r.stderr)

    def test_supported_game_matrix(self):
        for name in ("bgee", "bg2ee", "eet", "iwdee"):
            with self.subTest(game=name):
                g = self.game(name)
                g.install(0, 10)
                self.check_rules(g)
                self.check_abilities(g)

    def check_rules(self, g):
        ov = g.override
        kit = next(r for r in rows(ov / "kitlist.2da") if r[1] == g.symbol)
        self.assertEqual(kit[5].upper(), "ARCLAB")
        clab = rows(ov / "arclab.2da")
        self.assertTrue(all(len(r) >= 51 for r in clab))
        level_entries = lambda n: [r[n].upper() for r in clab]
        missile = "AP_SPCL124" if g.game == "iwdee" else "AP_SPCL122"
        for level in range(1, 51):
            entries = level_entries(level)
            self.assertEqual(entries.count(missile), int(level % 4 == 0))
            self.assertNotIn("GA_SPCL121", entries)
        self.assertIn("AP_CUSTOM", level_entries(11))
        tracking = sum(r[1:].count("GA_SPCL922") for r in clab)
        self.assertEqual(tracking, int(g.game == "iwdee"))
        for level, count in [(4, 1), (7, 1), (8, 2), (12, 3), (16, 4), (20, 5), (48, 12)]:
            # At level 8, migration transfers the level-4 use to ARINS1.
            gains = sum(x in ("GA_ARIN4", "GA_ARINS1") for r in clab for x in r[1:level + 1])
            self.assertEqual(gains, count)
        self.assertEqual((ov / "clabrn02.2da").read_bytes(), g.before["clabrn02.2da"])
        prof = {r[0]: r for r in rows(ov / "weapprof.2da")}
        for category in ("CROSSBOW", "LONGBOW", "SHORTBOW"):
            self.assertEqual(prof[category][4:], ["5", "4"])
        for category in ("LONGSWORD", "MACE", "QUARTERSTAFF"):
            self.assertEqual(prof[category][4:], ["1", "4"])
        self.assertEqual(prof["2WEAPON"][4], "0")
        self.assertEqual(rows(ov / "abclasrq.2da")[0][2:4], ["13", "14"])
        self.assertEqual(rows(ov / "abclsmod.2da")[0][3], "0")
        self.assertIn([g.symbol, "HPARCH"], rows(ov / "hpclass.2da"))
        hp = rows(ov / "hparch.2da")
        self.assertEqual(hp[8][1:], ["8", "1", "0"])
        self.assertEqual(hp[9][1:], ["8", "0", "3"])
        self.assertEqual((ov / g.hla_source).read_bytes(), g.before[g.hla_source])
        abilities = [r[1] for r in rows(ov / "luarrev.2da")]
        for ability in ("GA_SPCL907", "GA_CUSTOM", "GA_ARGCALS", "GA_ARSURE"):
            self.assertEqual(abilities.count(ability), 1)
        if g.game == "iwdee":
            self.assertNotIn("GA_SPCL922", abilities)
        routes = dict(rows(ov / "luabbr.2da"))
        self.assertEqual(routes[g.symbol], "ARREV")
        self.assertNotEqual(routes["OTHER"], "ARREV")
        icons = rows(ov / "statdesc.2da")
        self.assertEqual(len(icons), 4)
        for f in ("testbow.itm", "testxbow.itm"):
            fx = item_effects(ov / f)
            self.assertEqual(sum(e["op"] == 142 for e in fx), 1)
            self.assertEqual(sorted(e["resource"] for e in fx if e["op"] == 177),
                             ["ARMSH07", "ARMSH13", "ARMSH20"])
        self.assertEqual((ov / "testmelee.itm").read_bytes(), g.before["testmelee.itm"])

    def check_abilities(self, g):
        ov = g.override
        tiers = spell(ov / "arcalfx.spl")
        self.assertEqual([n for n, _ in tiers], [4, 8, 12, 16])
        for level, fx in tiers:
            self.assertEqual(fx[0]["op"], 321)
            self.assertEqual(sum(e["op"] == 15 for e in fx), 1)
            self.assertEqual(sum(e["op"] == 176 for e in fx), int(level >= 8))
            apr = [e for e in fx if e["op"] == 1]
            self.assertEqual(len(apr), int(level >= 12))
            if apr:
                self.assertEqual(apr[0]["p1"], -1)
        for level, fx in spell(ov / "arcalld.spl"):
            self.assertEqual(fx[-1]["resource"], "ARCALLD")
            self.assertEqual(sum(e["op"] == 286 for e in fx), int(level >= 16))
        for name, last in (("argcals.spl", "ARGCALS"), ("arsure.spl", "ARSURE")):
            for _, fx in spell(ov / name):
                self.assertEqual((fx[-1]["op"], fx[-1]["resource"]), (206, last))
        for name, amount in (("ar#th4.eff", 4), ("ar#th2.eff", 2)):
            self.assertEqual(effect((ov / name).read_bytes(), 0x10, True)["p1"], amount)
        for level, amount in ((7, 25), (13, 15), (20, 20)):
            data = (ov / f"armsh{level:02}.eff").read_bytes()
            fx = effect(data, 0x10, True)
            self.assertEqual((fx["op"], fx["p1"], fx["p2"]), (332, amount, 10))
            self.assertEqual(struct.unpack_from("<I", data, 0x54)[0], level)
        for tick, buff, opcode in (("arfarch", "arfaron", 262),
                                    ("arsnchk", "arsnon", 301)):
            fx = spell(ov / f"{tick}.spl")[0][1]
            self.assertEqual([e["op"] for e in fx], [321, 326])
            self.assertEqual(fx[0]["resource"], buff.upper())
            rule = rows(ov / "splprot.2da")[fx[1]["p2"]]
            self.assertEqual([int(x, 0) for x in rule[1:]], [0x111, 0x400010, 8])
            payload = spell(ov / f"{buff}.spl")[0][1]
            self.assertEqual(payload[0]["op"], opcode)
        # All levels of elemental ammunition use this game's projectile IDs.
        for prefix, expected in (("a7#inra", 5 if g.game == "iwdee" else None),
                                 ("a7#inro", 12 if g.game == "iwdee" else None)):
            for tier in range(1, 6):
                data = (ov / f"{prefix}{tier}.itm").read_bytes()
                start = struct.unpack_from("<I", data, 0x64)[0]
                count = struct.unpack_from("<H", data, 0x68)[0]
                for n in range(count):
                    projectile = struct.unpack_from("<H", data, start + n * 0x38 + 0x2a)[0]
                    if expected is not None:
                        self.assertEqual(projectile, expected)

    def test_iwdee_without_hla_tables_and_hp_kit_row(self):
        g = self.game("iwdee", hla=False, hp_row=False)
        out = g.install(0, 10)
        self.assertIn("without changing HLA progression", out)
        self.assertFalse((g.override / "luabbr.2da").exists())
        self.assertIn(["FERALAN", "HPARCH"], rows(g.override / "hpclass.2da"))
        self.assertIn("GA_SPCL922", (g.override / "arclab.2da").read_text())
        self.assertNotIn("AP_SPCL122", (g.override / "arclab.2da").read_text())

    def test_custom_shared_hla_table_and_archer_alias(self):
        g = self.game("iwdee", symbol="ARCHER", mixed_alias=True,
                      hla_abbrev="CUSTOM", hla_extra=True, hp_row=False)
        g.install(0, 10)
        self.check_rules(g)
        own = rows(g.override / "luarrev.2da")
        self.assertTrue(all(len(r) == 11 for r in own))
        self.assertEqual(own[0][-1], "KEEP")
        self.assertEqual({e["p1"] for e in item_effects(g.override / "testbow.itm") if e["op"] == 177}, {0x400c})

    def test_missing_critical_strike_does_not_add_unreachable_sure_shot(self):
        g = self.game("iwdee", critical=False)
        g.install(0)
        abilities = [r[1] for r in rows(g.override / "luarrev.2da")]
        self.assertIn("GA_ARGCALS", abilities)
        self.assertNotIn("GA_ARSURE", abilities)

    def test_manyshot_refresh_late_items_and_reinstall(self):
        g = self.game("iwdee")
        g.install(0)
        g.put("latebow.itm", item())
        g.install(10)
        first = (g.override / "latebow.itm").read_bytes()
        self.assertEqual(len(item_effects(g.override / "latebow.itm")), 4)
        g.install(10)
        self.assertEqual((g.override / "latebow.itm").read_bytes(), first)
        g.run("--force-uninstall-list", "10", "0")
        for name, data in g.before.items():
            self.assertEqual((g.override / name).read_bytes(), data, name)
        self.assertFalse((g.override / "arclab.2da").exists())
        self.assertFalse((g.override / "luarrev.2da").exists())
        g.install(0, 10)
        self.check_rules(g)

    def test_conflicting_archer_components_fail_without_changes(self):
        conflicts = [("A7#IMPROVEDARCHER/A7#IMPROVEDARCHER.TP2", 0),
                     ("ARTISANSKITPACK/ARTISANSKITPACK.TP2", 2010),
                     ("ARTISANSKITPACK_TWEAK/ARTISANSKITPACK_TWEAK.TP2", 20101)]
        for tp2, component in conflicts:
            with self.subTest(tp2=tp2):
                g = self.game("iwdee")
                (g.path / "weidu.log").write_text(f"~{tp2}~ #0 #{component} // Existing mod\n")
                g.install(0, success=False)
                for name, data in g.before.items():
                    self.assertEqual((g.override / name).read_bytes(), data)

    def test_missing_proficiency_column_rolls_back(self):
        g = self.game("iwdee")
        g.put("weapprof.2da", table("ID FIGHTER RANGER OTHER", ["LONGBOW 100 5 2 4"]))
        out = g.install(0, success=False)
        self.assertIn("could not locate the Archer proficiency column", out)
        self.assertFalse((g.override / "arclab.2da").exists())
        self.assertEqual((g.override / "kitlist.2da").read_bytes(), g.before["kitlist.2da"])

    def test_generated_resource_references(self):
        g = self.game("iwdee")
        g.install(0, 10)
        targets = {146: ".spl", 177: ".eff", 183: ".eff", 249: ".eff",
                   272: ".eff", 214: ".2da", 122: ".itm", 111: ".itm", 171: ".spl"}
        available = {p.name.upper() for p in g.override.iterdir()}
        for p in g.override.iterdir():
            if p.suffix.lower() == ".spl":
                fx = [e for _, es in spell(p) for e in es]
            elif p.suffix.lower() == ".eff":
                fx = [effect(p.read_bytes(), 0x10, True)]
            elif p.suffix.lower() == ".itm":
                data = p.read_bytes()
                offset = struct.unpack_from("<I", data, 0x6a)[0]
                self.assertEqual((len(data) - offset) % 0x30, 0, p.name)
                fx = [effect(data, n) for n in range(offset, len(data), 0x30)]
            else:
                continue
            for e in fx:
                if e["op"] in targets and e["resource"].startswith(("AR", "A7#")):
                    with self.subTest(source=p.name, target=e["resource"]):
                        self.assertIn(e["resource"] + targets[e["op"]].upper(), available)

    def test_existing_splprot_rule_is_reused_and_polling_is_silent(self):
        g = self.game("iwdee")
        g.put("splprot.2da", table("STAT VALUE RELATION", [
            "0 0x10a 0 4", "CUSTOM_INVISIBLE 273 4194320 8"]))
        g.install(0)
        self.assertEqual(len(rows(g.override / "splprot.2da")), 2)
        for name in ("arfarch", "arsnchk", "arfaron", "arsnon"):
            data = (g.override / f"{name}.spl").read_bytes()
            self.assertEqual(struct.unpack_from("<i", data, 8)[0], -1)
            self.assertEqual(struct.unpack_from("<H", data, 0x22)[0], 65535)
        for name, eff in (("armele03", "ARFAREFF"), ("arsnip", "ARSNEFF")):
            tick = [e for e in spell(g.override / f"{name}.spl")[0][1] if e["op"] == 272]
            self.assertEqual(len(tick), 1)
            self.assertEqual((tick[0]["p1"], tick[0]["p2"], tick[0]["resource"]), (1, 0, eff))

    def test_absent_original_clab_and_hla_fallback(self):
        g = self.game("iwdee")
        (g.override / "clabrn02.2da").unlink()
        g.put("luabbr.2da", table("VALUE", ["RANGER Ra0", "OTHER Ra0"]))
        g.install(0)
        self.assertIn(["FERALAN", "ARREV"], rows(g.override / "luabbr.2da"))
        self.assertIn("GA_SPCL922", (g.override / "arclab.2da").read_text())
        self.assertNotIn("GA_SPCL922", [r[1] for r in rows(g.override / "luarrev.2da")])

    def test_exact_kit_symbol_takes_priority_over_alias(self):
        g = self.game("iwdee")
        g.put("kitlist.2da", table(
            "ROWNAME LOWER MIXED HELP ABILITIES PROFICIENCY UNUSABLE CLASS",
            ["11 ARCHER 0 0 777 CLABOTHER 35 0x400b 2",
             "12 FERALAN 0 0 0 CLABRN02 36 0x400c 12"]))
        g.put("weapprof.2da", table("ID FIGHTER RANGER ARCHER FERALAN OTHER", [
            "LONGBOW 100 5 2 4 2 4", "LONGSWORD 101 5 2 4 2 4"]))
        g.put("luabbr.2da", table("VALUE", ["FERALAN Ra0", "RANGER Ra0", "ARCHER CUSTOM"]))
        g.put("lucustom.2da", table(
            "ABILITY ICON STRREF MIN_LEV MAX_LEVEL NUM_ALLOWED PREREQUISITE EXCLUDED_BY ALIGNMENT_RESTRICT",
            ["0 GA_FOREIGN * * 1 99 1 * * *"]))
        g.install(0)
        prof = rows(g.override / "weapprof.2da")
        self.assertEqual(prof[0][4:6], ["4", "5"])
        self.assertEqual(prof[1][4:6], ["4", "1"])
        routes = dict(rows(g.override / "luabbr.2da"))
        self.assertEqual(routes["FERALAN"], "ARREV")
        self.assertEqual(routes["ARCHER"], "CUSTOM")
        foreign = rows(g.override / "kitlist.2da")[0]
        self.assertEqual(foreign[4:6], ["777", "CLABOTHER"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
