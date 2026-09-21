# Archer Revised KIT

A standalone Archer overhaul for **Baldur's Gate: Enhanced Edition**, **Siege of Dragonspear**, **Baldur's Gate II: Enhanced Edition**, and **Enhanced Edition Trilogy (EET)**.

> **Development status:** v0.1.0-dev — implementation is under active audit; real WeiDU installation and in-game testing are still required.

> **Language:** English only for now.

## Goal

Archer Revised combines two complementary design directions:

- the long-term scaling, special shots, elemental ammunition, critical-hit progression, and missile defense of **Argent77's Improved Archer Kit**;
- the rapid-fire / marksman identity associated with **The Artisan's Kitpack Archer Overhaul**, independently reimplemented for this project.

The result is intended to remain recognizably an Archer while staying useful throughout a full EET campaign.

## v0.1 ruleset

### Advantages

- **Level 1 accuracy:** +1 to ranged attack rolls.
- **Missile scaling:** +1 to hit and +1 damage with missile weapons at levels 4, 8, 12, 16, 20, and every 4 levels thereafter.
- **Missile defense:** +1 AC vs. missile weapons every 6 levels.
- **Critical progression:** +5% critical-hit chance at levels 13 and 18.
- May achieve **Grand Mastery (5 slots)** with longbows, shortbows, and crossbows.
- **Farsighted:** +2 visual range, increasing to +4 while hidden or invisible.
- **Rapid Shot:** toggleable stance. While a bow or crossbow is equipped, grants +1 APR and imposes a -4 penalty to ranged attack rolls; from level 12 onward the penalty improves to -2.
- **Shared Special Shot pool:** 1 use at level 4 and +1 use every 4 levels. Called Shot and Rooting Shot unlock at level 4; Power Shot and Explosive Shot join the same pool at level 8. Normal Special Shots are mutually exclusive.
- **Called Shot:** for 10 seconds, successful ranged attacks apply level-dependent debuffs for 1 turn. Dexterity is reduced to 50% at level 4, movement to 25% at level 8, and APR by 1 at level 12; level 16 also adds +2 missile damage per hit. Repeated hits refresh rather than stack the persistent debuffs.
- **Conjure Elemental Ammunition:** retained from the Improved Archer foundation.
- **Manyshot — compatibility-first implementation:** while using a bow or crossbow, missile damage is increased by 25% at level 7, 40% total at level 13, and 60% total at level 20.
- **Sniper (level 16):** ranged attacks made while invisible or improved invisible are guaranteed critical hits.
- Retains the normal Ranger HLA selection, including **Hardiness**, and adds:
  - **Greater Called Shot:** for 10 seconds, maximizes base weapon damage; every successful ranged hit applies the complete Called Shot package and stuns the target for 3 seconds.
  - **Sure Shot Revised:** for 2 rounds, grants +1 APR while a bow or crossbow is equipped, +4 to hit with missile weapons, guaranteed ranged critical hits, and prevents movement. Rapid Shot, normal Special Shots, and Greater Called Shot are mutually exclusive with Sure Shot.

### Disadvantages

- Hit Die: **d8**.
- **+3 melee THAC0 penalty**.
- May only become Proficient (one slot) with melee weapons.
- May not gain proficiency in Two-Weapon Style.
- May not use Charm Animal.
- May not wear metal armor.

The Improved Archer -1 Constitution penalty is intentionally removed because the d8 Hit Die already supplies the survivability trade-off. Vanilla Archer minimum requirements are retained: **DEX 13 / CON 14**.

## Manyshot design note

The Artisan implementation creates additional independently rolled projectiles through custom combat-round animation resources and bow/crossbow patching. Archer Revised does not redistribute those resources.

A simple +APR replacement was rejected during audit because BG2EE/EET normally caps base APR at 5, causing high-level Manyshot to overlap with or waste Rapid Shot. Archer Revised therefore models Manyshot as launcher-gated missile-damage scaling: **+25% at level 7, +40% total at level 13, and +60% total at level 20**.

This keeps Rapid Shot useful, requires no EEex dependency, and works with mod-added bows and crossbows without globally patching every launcher.

This compatibility-first Manyshot does **not** create extra attack rolls, consume extra ammunition, or duplicate non-missile riders exactly as Artisan's true multi-projectile implementation does.

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

**The Artisan's Kitpack** by Artemius_I / The Artisan is used as a design reference for Rapid Shot, Manyshot, Sniper, Farsighted, Called Shot progression, Greater Called Shot, and the d8/melee trade-off. Artisan binary resources and implementation files are not redistributed by Archer Revised.

## License

Because Archer Revised is derived from Improved Archer Kit, this project is distributed under **CC BY-SA 4.0**.

See `LICENSE` and `CREDITS.md` for details.
