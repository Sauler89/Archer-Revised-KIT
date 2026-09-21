# Archer Revised KIT

A standalone Archer overhaul for **Baldur's Gate: Enhanced Edition**, **Siege of Dragonspear**, **Baldur's Gate II: Enhanced Edition**, and **Enhanced Edition Trilogy (EET)**.

> **Development status:** v0.1.0-dev — work in progress.

## Goal

Archer Revised combines two complementary design directions:

- the long-term scaling, special shots, elemental ammunition, critical-hit progression, and missile defense of **Argent77's Improved Archer Kit**;
- the rapid-fire / marksman identity associated with **The Artisan's Kitpack Archer Overhaul** (Rapid Shot, Manyshot, Sniper, and an expanded Called Shot concept), reimplemented independently for this project.

The result is intended to stay recognizably an Archer while remaining useful throughout an entire EET campaign.

## Planned v0.1 ruleset

### Advantages

- +1 to hit and damage with missile weapons at level 1, with an additional +1 every 4 levels thereafter.
- +1 AC vs. missile weapons every 6 levels.
- Expanded critical-hit range at levels 13 and 18.
- Grand Mastery with longbows, shortbows, and crossbows.
- Rapid Shot stance (**implemented**): +1 APR; -4 ranged THAC0, improving to -2 at level 12. Melee attacks receive an additional -6 THAC0 while the stance is active.
- Shared Special Shot pool (**implemented**): 1 use at level 4, +1 use every 4 levels; Called Shot + Rooting Shot at level 4, adding Power Shot + Explosive Shot at level 8.
- Conjure Elemental Ammunition.
- Manyshot progression.
- Sniper at high level.
- Archer-specific HLAs.

### Disadvantages

- d8 Hit Die.
- -3 THAC0 while using melee weapons.
- May only become Proficient with melee weapons.
- May not gain proficiency in Two-Weapon Style.
- May not use Charm Animal.
- May not wear metal armor.

The previous Improved Archer -1 Constitution penalty is intentionally not part of Archer Revised because the d8 Hit Die already fills the survivability trade-off.

## Current implementation status

The current v0.1-dev core includes the A7-derived shot effects / Elemental Ammunition foundation, a unified Special Shot pool, d8 Hit Die, revised proficiencies, the -3 melee THAC0 drawback, and a native Rapid Shot toggle. Called Shot currently uses the base-game effect while its final Revised mechanics are still being rebuilt. Manyshot, Sniper, and native revised HLAs are still under development.

## Compatibility target

Primary target:

- BG2EE 2.7.x
- EET
- WeiDU
- Infinity UI++ compatible
- EEex optional, never required

BGEE/SoD support is retained where practical through the Improved Archer base.

## Credits and provenance

**Improved Archer Kit** by Argent77 is the technical starting point for this project and is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.

The Artisan's Kitpack by Artemius_I / The Artisan is used as a *design reference only* for several Archer concepts. No Artisan binary resources are intended to be redistributed here unless explicit permission or a compatible license is established. Artisan-inspired mechanics are reimplemented independently.

## License

Because Archer Revised is derived from Improved Archer Kit, this project is distributed under **CC BY-SA 4.0**.

See `LICENSE` and `CREDITS.md` for details.
