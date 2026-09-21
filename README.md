# Archer Revised KIT

A standalone overhaul of the vanilla **Archer** ranger kit for **Baldur's Gate: Enhanced Edition**, **Siege of Dragonspear**, **Baldur's Gate II: Enhanced Edition**, and **Enhanced Edition Trilogy (EET)**.

> **Current status:** `v0.1.0-dev` — the implementation has undergone a detailed static audit, but a clean WeiDU installation and full in-game progression test are still required before the first public release.

> **Language:** English only.

## Contents

- [Design goal](#design-goal)
- [Supported games](#supported-games)
- [Complete ruleset](#complete-ruleset)
- [Level progression](#level-progression)
- [Special Shot system](#special-shot-system)
- [Conjure Elemental Ammunition](#conjure-elemental-ammunition)
- [Manyshot](#manyshot)
- [High-Level Abilities](#high-level-abilities)
- [Installation and components](#installation-and-components)
- [Recommended install order](#recommended-install-order)
- [Compatibility](#compatibility)
- [Technical notes](#technical-notes)
- [Development and testing status](#development-and-testing-status)
- [Credits and provenance](#credits-and-provenance)
- [License](#license)

## Design goal

Archer Revised combines two complementary Archer designs:

- the long-term ranged scaling, Special Shots, elemental ammunition, missile defense, and critical-hit progression of **Argent77's Improved Archer Kit**;
- the rapid-fire / marksman identity associated with **The Artisan's Kitpack Archer Overhaul**, reimplemented independently for this project.

The goal is an Archer that remains recognizably a Baldur's Gate Archer while gaining useful progression throughout an entire BGEE → SoD → BG2EE / EET campaign.

Archer Revised replaces the **vanilla Archer kit itself**. It is not a separate additional ranger kit.

## Supported games

The installer currently accepts:

- **Baldur's Gate: Enhanced Edition**
- **Siege of Dragonspear** as part of BGEE
- **Baldur's Gate II: Enhanced Edition**
- **Enhanced Edition Trilogy (EET)**

Primary development targets are **BG2EE 2.7.x** and **EET**.

The mod uses WeiDU and does **not** require EEex. Infinity UI++ is intended to be compatible.

**Icewind Dale: Enhanced Edition is not currently supported by Archer Revised**, even though part of the technical foundation originates from a mod that supports IWDEE.

## Complete ruleset

### Advantages

- **Level 1 ranged accuracy:** +1 to ranged attack rolls.
- **Missile scaling:** +1 to hit and +1 damage with missile weapons at levels 4, 8, 12, 16, 20, and every 4 levels thereafter.
- **Missile defense:** +1 AC vs. missile weapons every 6 levels.
- **Critical progression:** +5% critical-hit chance at level 13 and another +5% at level 18.
- May achieve **Grand Mastery (5 slots)** with:
  - Longbows
  - Shortbows
  - Crossbows
- **Farsighted:** +2 visual range; while hidden or invisible an additional +2 is applied.
- **Rapid Shot:** toggleable firing stance:
  - +1 attack per round while a bow or crossbow is equipped.
  - -4 penalty to ranged attack rolls.
  - At level 12 the penalty improves to -2.
- Gains a **shared Special Shot pool**:
  - Called Shot and Rooting Shot unlock at level 4.
  - Power Shot and Explosive Shot unlock at level 8.
  - 1 shared use at level 4 and +1 use every 4 levels thereafter.
- Retains **Conjure Elemental Ammunition** from Improved Archer.
- Gains the compatibility-first version of **Manyshot**:
  - Level 7: +25% missile damage.
  - Level 13: +40% total missile damage.
  - Level 20: +60% total missile damage.
  - Only while using a patched bow or crossbow.
- **Sniper** at level 16:
  - ranged attacks made while invisible or improved invisible are guaranteed critical hits.
- Retains the normal Ranger HLA selection, including **Hardiness**.
- Adds **Greater Called Shot** and **Sure Shot** to the HLA table.

### Disadvantages

- **Hit Die: d8.**
  - d8 rolls through level 9.
  - +3 HP per level from level 10 onward.
- **+3 melee THAC0 penalty.**
- May only become **Proficient (1 slot)** with melee weapon categories.
- May not gain proficiency in **Two-Weapon Style**.
- May not use **Charm Animal**.
- May not wear **metal armor**.

### Ability requirements

Archer Revised intentionally restores the normal vanilla Archer minimum requirements:

- **DEX 13**
- **CON 14**

The **-1 Constitution penalty** used by Improved Archer is intentionally removed. The reduced d8 Hit Die is the durability trade-off instead.

## Level progression

| Level | New or improved feature |
| ---: | --- |
| 1 | +1 ranged attack bonus; d8 Hit Die; +3 melee THAC0 penalty; Farsighted; Rapid Shot available |
| 4 | +1 missile hit/damage; 1 shared Special Shot use; Called Shot + Rooting Shot; first Conjure Elemental Ammunition use |
| 6 | +1 AC vs. missile weapons |
| 7 | Manyshot: +25% missile damage with patched bows/crossbows |
| 8 | +1 missile hit/damage; Special Shot pool becomes 2 uses; Power Shot + Explosive Shot added |
| 12 | +1 missile hit/damage; +1 AC vs. missiles; 3 Special Shot uses; Rapid Shot penalty improves from -4 to -2; second Conjure Elemental Ammunition use |
| 13 | +5% critical-hit chance; Manyshot increases to +40% total |
| 16 | +1 missile hit/damage; 4 Special Shot uses; Called Shot gains +2 missile weapon damage; Sniper |
| 18 | +1 AC vs. missiles; another +5% critical-hit chance |
| 20 | +1 missile hit/damage; 5 Special Shot uses; Manyshot increases to +60% total; third Conjure Elemental Ammunition use |
| 24+ | Missile hit/damage continues every 4 levels; missile AC continues every 6 levels; Special Shot uses continue every 4 levels; Elemental Ammunition uses continue every 8 levels |

The CLAB is defined through level 50 so these repeating progressions continue in high-XP installations.

## Special Shot system

Archer Revised replaces the separate A7 shot-use progression with **one shared pool of daily uses**.

At level 4 the Special Shot selector offers:

- Called Shot
- Rooting Shot

At level 8 it expands to:

- Called Shot
- Rooting Shot
- Power Shot
- Explosive Shot

The pool progresses as follows:

- Level 4: 1 use
- Level 8: 2 uses
- Level 12: 3 uses
- Level 16: 4 uses
- Level 20: 5 uses
- +1 use every 4 levels thereafter

Normal Special Shots are mutually exclusive. While one is active, the selector and other shot techniques are blocked so another daily use cannot accidentally be consumed.

### Called Shot

Duration: **10 seconds**.

Every successful ranged attack during the activation applies level-dependent effects to the target. Persistent target debuffs last **1 turn** and are **refreshed rather than stacked** by repeated hits.

- **Level 4:** target Dexterity is reduced to 50%.
- **Level 8:** movement rate is also reduced to 25%.
- **Level 12:** target also loses 1 attack per round.
- **Level 16+:** while Called Shot is active, the Archer gains **+2 missile weapon damage** for the 10-second firing window.

The level-16 damage bonus modifies ranged weapon damage directly through `MISSILE_DAMAGE_BONUS` rather than adding a separate damage packet. It therefore participates in critical-hit multipliers.

Archer Revised uses its own Called Shot resource, `ARCALLD`, instead of relying on the vanilla `SPCL121`.

### Rooting Shot

Duration of the firing window: **12 seconds**.

Successful ranged attacks attempt to entangle the target:

- **Level 4:** entangled for 3 rounds on failed save vs. Spell.
- **Level 8:** 3 rounds, save vs. Spell at -1.
- **Level 12:** 4 rounds, save vs. Spell at -1.
- **Level 16:** 4 rounds, save vs. Spell at -2.
- **Level 20+:** 5 rounds, save vs. Spell at -2.

### Power Shot

Duration of the firing window: **12 seconds**.

Successful ranged attacks can knock the target back:

- **Level 8:** knockback on failed save vs. Breath.
- **Level 12:** save vs. Breath at -1.
- **Level 16:** save vs. Breath at -2.
- **Level 20+:** save vs. Breath at -3.

### Explosive Shot

Duration of the firing window: **12 seconds**.

Successful ranged attacks explode on impact and inflict physical damage on creatures around the impact point in roughly a 15-foot radius:

- **Level 8:** 1d4 damage.
- **Level 12:** 1d4+2 damage.
- **Level 16:** 1d4+4 damage.
- **Level 20+:** 1d4+6 damage.

Explosive Shot can damage **enemies, allies, and innocent bystanders**.

## Conjure Elemental Ammunition

This ability is retained from Improved Archer.

The Archer gains one use at level 4 and another use every 8 levels:

- Level 4
- Level 12
- Level 20
- Level 28
- and so on

The ammunition created depends on the Archer's current level.

### Level 4

- +1 enchantment
- +1 to hit
- +1d3 fire damage

### Level 8

- +2 enchantment
- +2 to hit
- +1d3 fire damage
- +1d3 cold damage
- Can entangle unnatural creatures for 2 rounds on a failed save vs. Spell

### Level 12

- +2 enchantment
- +2 to hit
- +1d3 fire damage
- +1d3 cold damage
- +1d3 acid damage
- Can blind unnatural creatures for 2 rounds on a failed save vs. Spell

### Level 16

- +3 enchantment
- +3 to hit
- +1d3 fire damage
- +1d3 cold damage
- +1d3 acid damage
- +1d3 electrical damage
- Can slow unnatural creatures for 2 rounds on a failed save vs. Spell at -2

### Level 20+

- +4 enchantment
- +4 to hit
- +1d3+2 fire damage
- +1d3+2 cold damage
- +1d3+2 acid damage
- +1d3+2 electrical damage
- Can slow and blind unnatural creatures for 2 rounds on a failed save vs. Spell at -4

The conjured ammunition lasts **8 hours**. The original Improved Archer charge progression is retained: one score of charges initially, doubling at levels 8 and 16.

## Manyshot

### Why Archer Revised does not copy Artisan's Manyshot

The Artisan implementation creates additional independently rolled projectiles through custom combat-round animation resources and per-launcher patching.

Archer Revised does **not** redistribute that implementation or those Artisan resources.

An earlier Archer Revised prototype tried to represent Manyshot through additional APR. That approach was rejected because normal BG2EE/EET combat is constrained by the standard APR ceiling, making high-level Manyshot overlap with or waste Rapid Shot.

The current implementation instead uses **launcher-gated missile-damage scaling**:

- **Level 7:** +25%
- **Level 13:** +15% additional, for **+40% total**
- **Level 20:** +20% additional, for **+60% total**

The three level-gated effects are cumulative.

### How it works

Every bow and crossbow present when Archer Revised is installed is patched with Archer-only equipped effects.

The effects:

- apply only to the vanilla Archer kit identifier, `FERALAN`;
- activate at their own minimum levels;
- do not affect other kits;
- are removed and reapplied safely when Archer Revised performs its own refresh.

This makes the item patcher **idempotent**.

### Important difference from true multi-projectile Manyshot

Archer Revised Manyshot:

- does **not** create extra attack rolls;
- does **not** fire extra physical projectiles;
- does **not** consume extra ammunition;
- does **not** duplicate every on-hit rider exactly as Artisan's true Manyshot does.

It intentionally models the offensive scaling as additional missile damage for better compatibility with large EET installations.

## High-Level Abilities

Archer Revised retains the normal Ranger HLA table and adds two Archer-specific HLAs.

### Greater Called Shot

May be selected multiple times.

Duration: **10 seconds**.

While active:

- base weapon damage is maximized;
- the Archer gains +2 missile weapon damage;
- every successful ranged hit applies the complete level-16 Called Shot debuff package;
- every successful ranged hit also stuns the target for **3 seconds**.

Repeated hits refresh the persistent Called Shot debuffs rather than stacking them.

Activating Greater Called Shot supersedes active normal Special Shots and prevents normal Special Shots for its duration.

### Sure Shot

May be selected **once**.

**Prerequisite: Critical Strike.**

Duration: **2 rounds**.

While active:

- +1 APR while a bow or crossbow is equipped;
- +4 to ranged attack rolls;
- every ranged attack is a guaranteed critical hit;
- movement rate is reduced to zero.

Sure Shot is an exclusive firing stance. Activating it ends:

- Rapid Shot;
- normal Special Shots;
- Greater Called Shot.

Those abilities are blocked until Sure Shot expires.

### Hardiness

**Hardiness remains available.**

Archer Revised deliberately retains `SPCL907` in the Ranger HLA table. An earlier development audit had incorrectly identified that resource as Set Spike Trap; that was corrected before the current implementation.

## Installation and components

Archer Revised currently contains two WeiDU components.

### Component 0 — Archer Revised - Combined Archer Overhaul

This is the required core component.

It installs the complete kit overhaul, including:

- Archer rule-table changes;
- revised CLAB;
- Special Shots;
- Called Shot;
- Rapid Shot;
- Manyshot resources and initial launcher patch;
- Farsighted;
- Sniper;
- Elemental Ammunition;
- revised HLA table;
- d8 HP progression;
- proficiency and requirement changes.

### Component 10 — Patch mod-added bows and crossbows for Manyshot

This component requires component 0.

Its purpose is to patch bows and crossbows installed **after** Archer Revised core.

Install it near the end of a large mod order, after mods that add or replace launchers.

It rebuilds Archer Revised's Manyshot resources and refreshes the Archer Revised effects on all current bow/crossbow items.

### Installing from a packaged release

A release package should be extracted into the game directory so that the game folder contains at least:

- `ArcherRevised/`
- `setup-ArcherRevised.tp2`
- a WeiDU installer executable named `setup-ArcherRevised.exe`

Run `setup-ArcherRevised.exe` and select the desired components.

### Installing from the source repository

The GitHub source repository contains the mod files and TP2 but may not include a WeiDU executable. To install directly from source, provide a compatible WeiDU executable as `setup-ArcherRevised.exe` in the game directory.

## Recommended install order

For a normal installation:

1. Install the game / EET normally.
2. Install prerequisite framework and UI mods as appropriate for your setup.
3. Install other class/kit overhauls that do **not** replace the Archer.
4. Install **Archer Revised component 0**.
5. Install content and item mods, including mods that add bows or crossbows.
6. Near the end of the item/content section, install **Archer Revised component 10**.
7. Continue with later tweaks that do not replace the Archer or overwrite its resources.

For a large EET setup, component 10 is specifically intended to solve the common problem of bows/crossbows being introduced after the core kit component.

## Compatibility

### A7 Improved Archer

**Incompatible.**

Do not install Archer Revised together with **Improved Archer Kit component 0**.

Both projects replace the same Archer resources. Archer Revised explicitly checks for the A7 component and aborts rather than attempting to overwrite it.

This applies regardless of install order: do not install A7 Improved Archer after Archer Revised either.

### The Artisan's Kitpack — Archer Overhaul

**Incompatible.**

Do not install Archer Revised together with:

- **Artisan's Kitpack component 2010 — Archer Overhaul**

Both replace the vanilla Archer kit.

Archer Revised explicitly blocks installation if component 2010 is already present. Likewise, do not install Artisan's Archer Overhaul after Archer Revised.

Other Artisan kits/components that do not replace the Archer are not inherently blocked by Archer Revised.

### Artisan's late Manyshot tweak

Do **not** install:

- **ArtisansKitpack_tweak component 20101 — Archer - Apply Manyshot to mod-added items**

That component installs Artisan-specific `C0ARCPxx` / `C0MSHOxx` logic intended for Artisan's Archer.

Archer Revised explicitly blocks it.

Use **Archer Revised component 10** instead.

### ZSTweaks component 2232

ZSTweaks component:

- **2232 — Make Called Shot directly increase ranged weapon damage**

is **not required for Archer Revised**.

Archer Revised already implements the same design goal natively from level 16 onward by applying +2 to `MISSILE_DAMAGE_BONUS`.

In addition, ZSTweaks 2232 patches the vanilla `SPCL121` Called Shot resource, whereas Archer Revised uses its own `ARCALLD` implementation. Therefore it does not provide the Archer Revised kit with an additional benefit.

### Infinity UI++

Intended to be compatible.

Archer Revised does not require UI.MENU patching and does not require Infinity UI++.

### EEex

Optional.

Archer Revised does not require EEex for its core rules or abilities.

### Item/content mods

Generally compatible.

The principal issue is install order for bows/crossbows added after the core component. Use component 10 after those mods so their launchers receive Archer Revised Manyshot support.

### Other tweaks to Archer tables

Mods that alter `WEAPPROF.2DA`, Archer requirements, HP tables, CLAB entries, HLA tables, or Archer-specific resources can conflict depending on install order.

Archer Revised deliberately locates the Archer proficiency column by kit symbol rather than relying on a hard-coded WEAPPROF column. If it cannot identify the Archer column safely, installation aborts instead of modifying an unrelated kit.

## Technical notes

### Kit identity

Archer Revised replaces the vanilla Archer and recognizes the relevant kit row as either:

- `FERALAN`
- `ARCHER`

where appropriate.

Manyshot item effects filter directly for `KIT.IDS = FERALAN`, which is the vanilla Archer kit identifier used by the game.

### Rapid Shot

Rapid Shot uses weapon-type-gated effects so the APR and ranged THAC0 modifiers only apply when a **bow or crossbow** is equipped.

The level-12 upgrade removes the previous stance when the level is reached so the improved -2 version is applied cleanly when Rapid Shot is reactivated.

### Called Shot refresh logic

Called Shot uses an external on-hit EFF that casts the appropriate debuff spell at the Archer's caster level.

The debuff spell removes its own previous application before applying the current one. This is why repeated hits **refresh** Dexterity, movement, and APR penalties rather than stacking multiple copies.

### Sniper and Farsighted

Both abilities use periodic state checks rather than EEex.

Farsighted checks the hidden/invisible state and applies the enhanced short-duration visual-range bonus while that state is true.

Sniper checks the not-visible state and refreshes a short-duration ranged critical-hit modifier while the Archer remains hidden or invisible.

### HLA table

If the Archer is still using the default Ranger HLA table, Archer Revised creates its own derived table and adds the two custom Archer HLAs while preserving normal Ranger choices such as Hardiness.

### Resource provenance

Most A7-derived binary gameplay resources intentionally left unchanged are byte-identical to the current Improved Archer upstream files.

Archer Revised-specific resources are generated or patched by WeiDU under the `AR...` / `AR#...` namespace.

## Development and testing status

The current `v0.1.0-dev` implementation has undergone a detailed static audit covering:

- WeiDU TP2/TPH structure;
- CLAB progression through level 50;
- HLA table construction;
- SPL and EFF structure;
- THAC0 modifier signs;
- APR behavior;
- missile-damage modifiers;
- saving throws;
- ability durations;
- shared Special Shot progression;
- Archer proficiency-table targeting;
- component conflict checks;
- TRA references;
- local file/resource references;
- imported A7 resource integrity;
- Manyshot compatibility with late-added launchers;
- interaction with Artisan's late Manyshot tweak;
- interaction with ZSTweaks 2232.

Important corrections already made during development include:

- corrected Called Shot header handling for the intended level 4/8/12/16 tiers;
- corrected ranged and melee THAC0 modifier signs;
- removed the abandoned APR-based Manyshot prototype;
- restored Hardiness after correcting the earlier `SPCL907` identification error;
- restricted Sure Shot's APR bonus to bows/crossbows;
- made Sure Shot, Greater Called Shot, Rapid Shot, and normal Special Shots mutually exclusive where required;
- removed unsafe hard-coded WEAPPROF fallback behavior;
- removed unused legacy A7 Sure Shot / Missile Trap installation resources;
- added the idempotent late-item Manyshot refresh component;
- integrated the useful behavior of ZSTweaks 2232 directly into Archer Revised Called Shot.

### Still requiring real in-game verification

Static inspection cannot completely replace Infinity Engine runtime testing.

Before the first release, the following should be tested in BG2EE/EET:

- clean WeiDU installation and uninstall/reinstall;
- character creation requirements and proficiency caps;
- HP gains from level 1 onward;
- ranged and melee THAC0 values;
- Rapid Shot at levels 1 and 12;
- shared Special Shot uses at levels 4/8/12/16/20;
- every Called Shot tier;
- Rooting, Power, and Explosive Shot saving throws and durations;
- Elemental Ammunition at each breakpoint;
- Manyshot damage at levels 7/13/20;
- component 10 on mod-added bows/crossbows;
- Farsighted visual-range behavior;
- Sniper when entering and breaking invisibility;
- critical-hit progression at levels 13 and 18;
- Greater Called Shot repeated activation behavior;
- Sure Shot and its mutual exclusions;
- HLA availability, including Hardiness and the Critical Strike prerequisite;
- save/load persistence of modal/passive effects.

Until those tests are complete, the project remains **development status** rather than a final release.

## Credits and provenance

### Improved Archer Kit — Argent77

Archer Revised uses **Improved Archer Kit by Argent77** as its technical foundation for the Special Shot framework, elemental ammunition, associated Infinity Engine resources, and portions of the installation logic.

Source:
https://github.com/Argent77/A7-ImprovedArcher

Improved Archer is distributed under **CC BY-SA 4.0**.

### The Artisan's Kitpack — Artemius_I / The Artisan

**The Artisan's Kitpack** is used as a design reference for concepts including:

- d8 Archer durability;
- ranged accuracy identity;
- Farsighted;
- Rapid Shot;
- Called Shot progression;
- Manyshot;
- Sniper;
- Greater Called Shot;
- the melee proficiency / THAC0 trade-off.

Archer Revised does **not** intentionally redistribute Artisan binary resources or copy Artisan implementation files. These mechanics are independently implemented for this project.

Source:
https://github.com/TheArtisanBG/The-Artisan-s-Kitpack

### ZSTweaks — szaumoor

ZSTweaks component 2232 was used as a compatibility/design reference for applying Called Shot's high-level damage bonus directly to ranged weapon damage instead of adding a separate damage packet.

Source:
https://github.com/szaumoor/ZSTweaks

## License

Archer Revised KIT is distributed under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** because it incorporates and adapts material from Argent77's Improved Archer Kit.

See:

- `LICENSE`
- `CREDITS.md`

for attribution and licensing details.
