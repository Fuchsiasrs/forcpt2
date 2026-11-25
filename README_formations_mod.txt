Formations and AI Mods by Motomataru
v. 5
02/22/16

This kit contains two minimods by motomataru. It is presented in source code for addition to larger mods.

Only Warband 1.168 and later is supported. I've added the necessary operator definition for use with the outdated mod sys.

1. A formations mod, contained in files formations_*.py
2. An extension mod to replace Native AI, contained in files formAI_*.py
3. Also Native 1.166 source prepped with modmerger (see below). Of course, for other M&B versions, you'll need to prep that version of Native source with modmerger yourself.

The formations mod is an extensive reworking of the original simple interface by Mirathei. At a command, infantry can form in ranks by level, ranks by shield/weapon, wedge by level, or square. Cavalry can form a wedge. Formations follow all battlefield commands. Native AI is given the ability to make the same formations.

The formations AI replaces Native AI. It makes decisions based primarily on army size rather than army composition. Each type of unit has different objectives. The intent was to make the AI smarter AND more proactive.


INSTALLATION:
The source files here are prepped for use with modmerger by sphere. I provide alternative instructions in case a modder wishes to install by manual edit.

Modmerger
1. If you wish to start using modmerger, obtain if from http://www.mbrepository.com/file.php?id=2151. Install it according to the directions in its readme file.

2. Copy the formations_*.py and formAI_*.py files to the compile directory (where you installed modmerger).

3. Update the modmerger_options.py file as follows:
	- change "version" to 1011 ONLY IF you are installing for M&B 1.011 (NOT supported for FormAI v5)
	- change "version" to 1143 ONLY IF you are installing for WFaS 1.143 (NOT supported for FormAI v5)
	- add "formations" and (if desired) "formAI" to the mods_active list. See included version of this file for a sample mods_active list.

4. Run build_module!

For updates to either mod, simply replace the formations_*.py or formAI_*.py files.


Notes:
1. The compiler generates menu options which have the player start the battle holding a position by the entry point. These are basically copies of the "charge" options with the single line (assign, "$player_deploy_troops", 1) added. See formations_game_menus_wb.py

2. The entire weapons table is copied, stripped of swing characteristics, and placed AFTER itm_items_end. This tends to cause problems with save games during development. My recommendation is to comment that out until the items table is set. See formations_items.py

3. The battle presentation is replaced with an improved version. If you already replaced it, comment out or rename the one in formations_presentations.py.

4. The replacement battle presentation references flags for ALL divisions (not just Infantry, Archers, and Cavalry). You will need to make the actual meshes (based on flag_infantry, etc.). See formations_meshes_wb.py.

5. To eliminate conflicts between presentations in a scene, a switching system has been made (common_presentation_switcher). This requires that calls to start the battle presentation be deleted and replaced by the set of triggers in battle_panel_triggers. See formations_mission_templates_wb.py.

6. Formations_constants.py includes an operator missing from the 1166 header_operations.py

7. FormAI_scripts_wb.py guts the Native AI scripts because they conflict with the new AI scripts.


Manual Install
1. Append the constants listed in form*_constants.py files to module.constants.py.

2. Add the scripts from form*_scripts.py to module_scripts.py. Also add the python definition make_noswing_weapons after the headers at the top of the file.

For the two battle_tactic* functions listed, you'll have to change the name of the originals by prefixing them with "orig_". That, is, they should end up named "orig_battle_tactic_init_aux" and "orig_battle_tactic_apply_aux".

Then add the line
(call_script, "script_player_order_formations", ":order"),	#for formations
before the last command of the existing team_give_order_from_order_panel script (i.e. before the set_show_messages call).

Finally, place the line
(assign, "$first_time", 0),	#squelch compiler warnings
in script_game_start, anywhere it will get called.

3. For formations_presentations, add the various presentations to module_presentations. Skip the improved battle presentation if you don't want it.

4. Add the new meshes to module_meshes. Be aware that you will have to generate new flags meshes for the flag meshes. Use flag_infantry, etc. as a basis.

5. Add the lists of triggers from form*_mission_templates.py to module_mission_templates.py right before the list of mission templates (i.e., right above where it says "mission_templates = [").

The formations triggers can then be added to any mission template by "adding" them to the end of the triggers list for that template, like so:
"    ] + utility_triggers + extended_battle_menu + common_division_data + division_order_processing + real_deployment + formations_triggers + AI_triggers"

If you wish to keep the battle presentation from conflicting with the formations menu, delete all calls to start it. Then add the trigger set battle_panel_triggers to every mission template those calls were deleted. NB: this trigger pack also includes one to initialize agent slots properly.

6. If you use the AI in a mission template, comment out any competing Native AI triggers. In the lead_charge template, for example, there are two of them, but DO NOT comment out the morale/courage triggers inserted between them! See top of formAI_mission_templates_*.py for example.

7. There is a formations options menu that you can add somewhere (typically to the camp menu).
    ("formation_mod_option",[],"Formations mod options.", [(start_presentation, "prsnt_formation_mod_option")]),

One also may add options to start battles in Hold position. To do this, locate the options that call mt_lead_charge. Copy them, rename them, and use something like "Start battle holding position." To the consequences operation block, add the line
(assign, "$player_deploy_troops", 1)
anywhere that it will be called.

8. Add the documentation in formations_strings and formations_info_pages.

9. Add the python section of formationss_items.py that adds items to the end of module_items.py. This will prevent troops in tight formations from trying in vain to swing their weapons.

For updates to either mod, you'll have to manually replace these code sections.


KNOWN CONFLICTS:
Player's initial formation conflicts with Caba'drin's prebattle orders. Comment out the generation of the "Hold Position" menu options in formations_game_menus_wb.py


TWEAKS:
The constants source files conveniently have a number of settings that you can tweak. I recommend SAVING a copy of your tweaks against having them overwritten by a mod update.

formations_constants.py
formation_minimum_spacing: minimum number of centimeters between troops in formation
formation_minimum_spacing_horse_length: minimum number of centimeters between cavalry in formation
formation_minimum_spacing_horse_width: minimum number of centimeters between cavalry in formation
formation_start_spread_out: number of half-meters to add between troops in a NEW formation (for ease of maneuvering). Set to 0, all spreading out and coming together must be done by the player
formation_min_foot_troops: minimum number of troops for anything but cavalry formation
formation_min_cavalry_troops: minimum number of troops for cavalry formation
formation_native_ai_use_formation: set to 1 for Native AI to use formations, 0 otherwise
formation_delay_for_spawn: for use by M&B 1.011 which lacks ti_after_battle_start trigger
formation_reequip: flag TRUE to have troops reassess equipment when making a formation (may conflict with other autoequips in your mod)
formation_reform_interval: amount of time before formation adjusts for casualties, etc. Not working for longer intervals due to difficulty assessing division movement rates.
formation_rethink_for_formations_only: flag whether or not the rethink based on closest enemy will be restricted to agents in formation
AI_charge_distance: centimeters under which melee troops consider themselves under attack
command keys (M&B): keys for specifying each formation (or none/unform)
Third_Max_Weapon_Length: should be 1/3 of the length of the longest weapon in your mod
slots and positions: make sure they don't conflict with others used by your mod

formAI_constants.py
AI_long_range: centimeters archers will first set up position
AI_firing_distance: centimeters archers will try to maintain to target
AI_for_kingdoms_only: set to 1 for AI for kingdoms and deserters only, 0 otherwise
Percentage_Cav_For_New_Dest: percent of formation at destination required to select a new one. The higher you make this, the more cavalry will wait to form up before next action.
Hold_Point: ratio compared to largest team under which AI will take defensive
AI_Max_Reinforcements: number of waves of reinforcements your mod allows
AI_Replace_Dead_Player: flag TRUE to have AI take over player troops after player dies (if your mod allows the battle to continue)
AI_Poor_Troop_Level: level under which troops are considered "poor"

positions: chosen for lack of use in Native scripts, but you may want to double-check that the longer-term ones don't conflict with any others in your specific mod.

In formations_scripts.py, you may want to change the switch in script_get_default_formation to change default formations (or add new ones for mod factions)


QUICK PLAY GUIDE:
For Hold and Follow commands, default division placement around the player is: infantry to the left, cavalry to the right, and archers up front. Additional infantry divisions set up further left, additional cavalry further right, and additional ranged further forward. So, for example, if you would like TWO ranged divisions and want the one with thrown weapons further forward, make sure the archers are in Division 3 and the skirmishers in a Division 4-9.

Troop divisions that for whatever reason are NOT in formation will attempt to integrate with the other divisions in the "Hold" position. These divisions will maintain the same FACING that the player had unless the player checks the autorotate option in the Formations Options Menu under the Camp Menu.

The player may override default placement through the additional F2 Menu command to memorize division(s) placement relative to the player. So if you prefer, for example, your cavalry in front and your archers behind, rearrange these divisions during a quiet battle and then press F2-F7. Just make sure to stand toward the rear when memorizing and pad your new arrangement with plenty of space, as changes in division sizes, position rotations, and map borders affect the precision of memorized placement.

Placement is overridden for any division the player chooses to personally head through the Formations Options menu.

There are no assumptions about division type beyond the first (infantry). The system types them as the following:

- majority HEROES: majority skilled, Support; otherwise Bodyguard

- majority HORSES: majority with bows, Mounted Archers; otherwise regular Cavalry

- majority RANGED: with thrown weapon, Skirmishers; otherwise regular Ranged

- none of the above: majority with polearms, Polearms; otherwise regular Infantry

You have to bear this typing scheme in mind when composing divisions; otherwise an additional Infantry division may suddenly become some sort of Ranged. Also be aware that certain mods autoequip troops at the start of battle, thereby changing their type.

Hero-type divisions and more notably Skirmishers make infantry-type formations. Skirmishers will revert to type Infantry (and change default placement on "Hold" to the players LEFT instead of FORWARD) when they use up their ammunition.

Whenever a unit first forms a particular formation, troops may spread out for ease of forming up (depending on mod design). They may also change weapons as befitting their new positions within their formation. The mod also strips swing capability from stabbing weapons for infantry in formation, the better to use in close quarters. You may wish to experiment with formation spacing to see which works best for its majority weapon. Rhodoks with glaives, for example, benefit from a couple extra spaces to swing in.

The "ranks" command for archers puts them in a staggered line.

Cavalry will not make any formation other than the wedge.

Charge (and Dismount for cavalry) will undo a formation. The player may Advance multiple times to have a formation move toward the average position of the enemy. Or use the order panel or Hold-F1 to place them (or sweep them across the enemy in the case of the cavalry wedge).

Speaking of which, the Hold-F1 command has been expanded: when done on an enemy formation, player divisions will attack it. Infantry formations will advance into melee without breaking formation, cavalry will revert into a Native style charge after closing, and archers will advance until they start shooting. In any case, if the target is wiped out, the player division will return to the player.

If the player increases battle size beyond the WB maximum, there's a small chance large battles will stutter every second. The player may remove the stutter (and some AI functionality) on the mod option menu.

Horsemen that lose their mounts now gather around the player in a new division.


DETAILS:
Formations v. 5

The main change for this version was to break down the mission template components so that they don't have to all be used. This allows, for example, for creating an alternative GUI interface or a troop placement game state at the start of battle (you'll see a portion of the code that did this, now commented out).

Performance has improved, thanks to Taleworlds support during Viking Conquest development.

Beyond that, the code was extensively tested through its release as part of Caribbean! and Viking Conquest.


ACKNOWLEDGEMENTS:
Mirathei - for original concept and code
Caba'drin - order menu interface, conversion to slots, weapon swing strip, division typing, much more
Sphere - modmerger installation system, auto options menu (now replaced), and suggestions
Rubik - portions of his Improved Autoloot (now replaced)
Idibil - for enthusiastically cracking the whip in order to use these mods in Brytenwalda
Othr, Dunde, Treebeard - for understanding my code well enough to fix it
Brytenwalda betatesters
HokieBT - hosting AI prototype in SWC
Cem Çimenbiçer at Taleworlds - for adding many helpful operators
Viking Conquest players - for placing this code through the fire
Many players from the forum that made great suggestions, only a small portion of which I had time to implement
