# v0.2.0-beta2 validation — 2026-11-24

Ordering baseline: `34759b95669e7f5c5f3712777b015602db986fa9` (beta1).
The earlier v0.1.0-dev baseline `75d489b` also had the four parser errors
documented in the beta1 changelog.

## Final regression results

| Executable | Test methods | Result |
| --- | ---: | --- |
| WeiDU 24900 | 18 | PASS |
| WeiDU 25100 | 18 | PASS |

Both runs used the supplied S&A/IWDEE-Tweaks source paths and a Lua 5.4
shared library: all 18 methods ran without skips. The four-game matrix
installs core 0 first and then late components 10/20 for BGEE, BG2EE, EET
and IWDEE. All 16 TP2/TPH files are parsed by real WeiDU.

Ordering regressions verify that later proficiency, HP, KITLIST and CLAB
changes survive component 20 unchanged; late-added HLA support is detected;
empty HLA rows cannot hide subsequent choices; the Archer catalog is updated
without changing other classes or symbol maps; repeat installation is
idempotent; uninstall restores the previous catalog/routes; unsupported
catalog data triggers rollback. The other beta1 installer/resource tests
remain in the suite.

## Source-backed integration stages

The optional integration executes these actual supplied stages in order:

1. Archer Revised core 0.
2. S&A component-600 HLA exporter (`hla.tpa`), using its `hla-data.lua`.
3. The IWDEE-Tweaks `IWTF_REFRESH_FEAT_HLAS` function after modeled rule/table changes.
4. Archer Revised component 20.
5. Execute the resulting Lua and verify the Archer choices and class symbols.

Only the exporter/refresh stages are run; the surrounding test TP2 wrappers
are fixtures. These are not full S&A/IWDEE-Tweaks installations. Third-party
source files are supplied externally and are not redistributed here.

| Supplied file | SHA-256 |
| --- | --- |
| `components/feats/hla.tpa` | `a76efd9f9ea662af8cb7e9731604c660295e890778b2822c2a706466da8c7738` |
| `components/feats/hla-data.lua` | `c721d10b646fc8847899a90bc13e4e911a633339dc690c8eac869e07a5aad85d` |
| `IWDEE-Tweaks-and-Fixes/lib/hla_compat.tpa` | `690f4eedc3981d07521847cb61847056319f58cc519527cabc6bec2537deb3ee` |

No Infinity Engine executable or commercial game data was used. This does
not certify real damage rolls, movement, critical hits, invisibility transitions,
save-game migration, or a full third-party mod installation. The manual
checklist in [README.md](README.md#required-manual-engine-checks) remains open;
the release is marked beta.
