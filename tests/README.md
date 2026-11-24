# Installer and resource regression tests

The tests use the real WeiDU executable and a Python standard-library harness.
Fixtures contain tiny generated KEY/TLK/2DA/item files, not commercial game data.
They exercise BGEE, BG2EE, EET and IWDEE detection and installation paths.

Run from the repository root, with Python 3.9+:

```sh
WEIDU=/absolute/path/to/weidu python -m unittest discover -s tests -v
```

Validated on Linux with WeiDU 24900 and 25100. The harness resolves generated
resource names case-insensitively, while explicitly rejecting duplicate names
that differ only by case. This accommodates WeiDU's differing Linux filename
handling. Every parse check must report that it actually parsed the file; an
exit code alone is not sufficient when testing mixed-case paths with WeiDU 249.

The suite checks installer execution, four-game detection, binary SPL/EFF/item
structure, native Tracking, HP/proficiency requirements, progression through
level 50, prerequisite availability, private versus shared CLAB/HLA tables,
missing optional tables, preserved foreign entries, late Manyshot items,
idempotent refresh, conflict failure, rollback, uninstall and reinstall.

The fixture HLA variations model table shapes used by other mods; they do not
install Skills and Abilities or IWDEE-Tweaks-and-Fixes themselves. A green test
run does not certify arbitrary complete mod installations.

## Required manual engine checks

- On clean BG2EE/EET and IWDEE installations, create a new Archer and verify
  ability minimums, d8 HP gains, proficiency caps and melee/ranged THAC0.
- Level through 4/7/8/12/13/16/18/20, then the higher repeating progression.
  Verify shared Special Shot uses, all Called Shot tiers and elemental ammo.
- At levels 7/13/20, compare Manyshot damage with normal, magical, mod-added
  and self-ammunition bows/crossbows. Switch to melee/slings/darts and verify
  launcher bonuses end. Test before/after levelling with the same bow equipped.
- Toggle Rapid Shot, then switch weapons, level to 12, save/load, die/revive,
  and test with Haste/Improved Haste and the ordinary APR cap.
- Enter/break normal and improved invisibility, with and without Haste/Slow,
  and verify Farsighted/Sniper activation, cleanup and absence of combat-log
  spam. Polling is nominally one second and is not an instantaneous state hook.
- Activate Special Shots, Greater Called Shot and Sure Shot in competing
  orders; test repeated uses, movement restrictions, critical immunity,
  successful hits and misses, and save/load during active effects.
- In IWDEE verify native Tracking once, no redundant Tracking HLA, and no HLA
  progression enabled by this mod alone. With HLA support installed before
  the kit, verify Archer-only additions, Hardiness where present and the
  Critical Strike prerequisite for Sure Shot.
- Test any existing development-version characters separately. The installer
  does not rebuild permanent bonuses already saved in a character file.
