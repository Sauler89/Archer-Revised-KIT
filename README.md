# Archer Revised KIT

A standalone Archer overhaul for **Baldur's Gate: Enhanced Edition**, **Siege of Dragonspear**, **Baldur's Gate II: Enhanced Edition**, and **Enhanced Edition Trilogy (EET)**.

> **Development status:** v0.1.0-dev — gameplay implementation complete, installation/gameplay testing still required.

## Goal

Archer Revised combines two complementary design directions:

- the long-term scaling, special shots, elemental ammunition, critical-hit progression, and missile defense of **Argent77's Improved Archer Kit**;
- the rapid-fire / marksman identity associated with **The Artisan's Kitpack Archer Overhaul**, reimplemented independently for this project.

The result is intended to remain recognizably an Archer while staying useful throughout a full EET campaign.

## v0.1 ruleset

### Advantages

- +1 to hit and damage with missile weapons at level 1, with another +1 every 4 levels thereafter.
- +1 AC vs. missile weapons every 6 levels.
- +5% critical-hit chance at levels 13 and 18.
- Grand Mastery with longbows, shortbows, and crossbows.
- **Farsighted:** +2 visual range, increasing to +4 while hidden or invisible.
- **Rapid Shot:** toggleable stance; +1 APR with bows/crossbows, with a +4 ranged THAC0 penalty that improves to +2 at level 12.
- **Shared Special Shot pool:** 1 use at level 4 and +1 use every 4 levels. Called Shot + Rooting Shot unlock at level 4; Power Shot + Explosive Shot join the same pool at level 8.
- **Called Shot:** 10-second ranged on-hit window. Its level-based DEX, movement and APR debuffs refresh rather than stack; level 16 adds +2 missile damage per hit.
- **Conjure Elemental Ammunition:** retained from the Improved Archer foundation.
- **Manyshot (compatibility-first implementation):** +1/2 APR with bows/crossbows at levels 7, 13 and 20, for +1.5 APR total at level 20.
- **Sniper (level 16):** ranged attacks while invisible or improved invisible are guaranteed critical hits.
- Archer-specific HLAs:
  - **Greater Called Shot:** applies the full Called Shot package on every successful ranged hit, plus +4 missile damage and a 1-second stun.
  - **Sure Shot Revised:** 2 rounds; +1 APR, +4 to hit with missile weapons, guaranteed ranged critical hits, and movement locked to zero. Special Shots are blocked for the duration.

### Disadvantages

- d8 Hit Die.
- +3 melee THAC0 penalty.
- May only become Proficient with melee weapons.
- May not gain proficiency in Two-Weapon Style.
- May not use Charm Animal.
- May not wear metal armor.

The Improved Archer -1 Constitution penalty is intentionally removed because the d8 Hit Die already supplies the survivability trade-off.

## Manyshot design note

The Artisan implementation uses custom combat-round animation resources and patches bow/crossbow items. Archer Revised does not redistribute those resources. Instead, Manyshot is reimplemented as a launcher-gated APR progression that works without EEex and does not require repatching every mod-added bow or crossbow.

## Compatibility target

Primary target:

- BG2EE 2.7.x
- EET
- WeiDU
- Infinity UI++ compatible
- EEex optional, never required

BGEE/SoD support is retained where practical through the Improved Archer foundation.

Do not install Archer Revised together with the A7 Improved Archer component or Artisan's Archer Overhaul component. The installer explicitly blocks these combinations because all three replace the same Archer kit resources.

## Credits and provenance

**Improved Archer Kit** by Argent77 is the technical starting point for this project and is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.

**The Artisan's Kitpack** by Artemius_I / The Artisan is used as a design reference for Rapid Shot, Manyshot, Sniper, Farsighted, Called Shot progression, and the d8/melee trade-off. Artisan binary resources and implementation files are not redistributed by Archer Revised.

## License

Because Archer Revised is derived from Improved Archer Kit, this project is distributed under **CC BY-SA 4.0**.

See `LICENSE` and `CREDITS.md` for details.
