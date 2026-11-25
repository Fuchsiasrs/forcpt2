# Formations AI by Motomataru
# rel. 08/31/2012

from module_constants import *

####################################################################################################################
#  Each quest record contains the following fields:
#  1) Info page id: used for referencing info pages in other files. The prefix ip_ is automatically added before each info page id.
#  2) Info page name: Name displayed in the info page screen.
#
####################################################################################################################

info_pages = [
 ("formations", "Formations", "The formations mod is an extensive reworking of the original simple interface by Mirathei. At a command, infantry can form in ranks by level, ranks by shield/weapon, wedge by level, or square. Cavalry can form a wedge. Formations follow all battlefield commands, including from the battle panel. Native AI is given the ability to make the same formations.^^\
 For Hold and Follow commands, default division placement around the player is: infantry to the left, cavalry to the right, and archers up front. Additional infantry divisions set up further left, additional cavalry further right, and additional ranged further forward. So, for example, if you would like TWO ranged divisions and want the one with thrown weapons further forward, make sure the archers are in Division 3 and the skirmishers in a Division 4-9.^^\
 Troop divisions that for whatever reason are NOT in formation will attempt to integrate with the other divisions in the \"Hold\" position. These divisions will maintain the same FACING that the player had unless the player checks the autorotate option in the Formations Options Menu under the Camp Menu.^^\
 The player may override default placement through the additional F2 Menu command to memorize division(s) placement relative to the player. So if you prefer, for example, your cavalry in front and your archers behind, rearrange these divisions during a quiet battle and then press F2-F7. Just make sure to stand toward the rear when memorizing and pad your new arrangement with plenty of space, as changes in division sizes, position rotations, and map borders affect the precision of memorized placement.^^\
 Player troops start every battle in Hold position around the player, utilizing either default or memorized placement and formation.^^\
 Placement is overridden for any division the player chooses to personally head through the Formations Options menu.^^\
 There are no assumptions about division type beyond the first THREE. The system types them as the following:^^    - majority HEROES: majority skilled, Support; otherwise Bodyguard^^    - majority HORSES: majority with bows, Mounted Archers; otherwise regular Cavalry^^    - majority RANGED: with thrown weapon, Skirmishers; otherwise regular Ranged^^    - none of the above: majority with polearms, Polearms; otherwise regular Infantry^^\
 You have to bear this typing scheme in mind when composing divisions; otherwise an additional Infantry division may suddenly become some sort of Ranged. Also be aware that certain mods autoequip troops at the start of battle, thereby changing their type.^^\
 Hero-type divisions and more notably Skirmishers make infantry-type formations. Skirmishers will revert to type Infantry (and change default placement on \"Hold\" to the players LEFT instead of FORWARD) when they use up their ammunition.^^\
 Whenever a unit first forms a particular formation, troops may spread out for ease of forming up (depending on mod design). They may also change weapons as befitting their new positions within their formation. The mod also strips swing capability from stabbing weapons for infantry in formation, the better to use in close quarters. You may wish to experiment with formation spacing to see which works best for its majority weapon. Rhodoks with glaives, for example, benefit from a couple extra spaces to swing in.^^\
 The \"ranks\" command for archers puts them in a staggered line.^^\
 Cavalry will not make any formation other than the wedge.^^\
 Charge (and Dismount for cavalry) will undo a formation. The player may Advance multiple times to have a formation move toward the average position of the enemy. Or use the order panel or Hold-F1 to place them (or sweep them across the enemy in the case of the cavalry wedge).^^\
 Speaking of which, the Hold-F1 command has been expanded: when done on an enemy formation, player divisions will attack it. Infantry formations will advance into melee without breaking formation, cavalry will revert into a Native style charge after closing, and archers will advance until they start shooting. In any case, if the target is wiped out, the player division will return to the player.^^\
 If the player increases battle size beyond the WB maximum, there's a good chance large battles will stutter every second. The player may remove the stutter (and some AI functionality) on the mod option menu."),
]

# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
	try:
		var_name_1 = "info_pages"
		orig_info_pages = var_set[var_name_1]

		# START do your own stuff to do merging

		orig_info_pages.extend(info_pages) # Use this only if there are no replacements (i.e. no duplicated item names)

		# END do your own stuff
            
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)
