# v0.2.0-beta1 validation — 2026-11-24

Baseline reviewed: `75d489b359557b1dfbcee3fdaa4d8bc90f569350`.

The baseline failed real WeiDU 249/251 parsing in `called_shot.tph`,
`passives.tph` and `hla.tph`. Its installer stopped in Called Shot and rolled
back. The four offending negative argument expressions are corrected.

Final regression results on Linux:

| Executable | Test methods | Result |
| --- | ---: | --- |
| WeiDU 24900 | 12 | PASS |
| WeiDU 25100 | 12 | PASS |

Each run includes a subtest matrix installing both components for BGEE,
BG2EE, EET and IWDEE, plus parsing all 15 TP2/TPH files. The other scenarios
cover missing optional HLA data, a missing HP kit mapping, custom shared
HLA tables with extra columns, the ARCHER alias, exact-symbol precedence,
unavailable Critical Strike, native Tracking, generated resource references,
silent state polling, late-added bows, repeated refresh, full uninstall and
reinstall, conflicting kit components, and rollback after a missing proficiency
column. The original shared CLAB/HLA tables and unrelated item effects are
checked for preservation.

This is an installer/resource validation record using synthetic fixtures. No
Infinity Engine executable or commercial game data was used. It does not
certify real damage rolls, movement, critical hits, invisibility transitions,
save-game migration, or a full third-party mod installation. The manual
checklist in [README.md](README.md#required-manual-engine-checks) remains open;
the release is deliberately marked beta.
