# Formations AI v5 by Motomataru
# rel. 02/14/2016

formations_strings = [
  ("tactical_controls", "Use the keyboard NUMBERS to select a division. Press 0 to select your entire force.^^\
Use F1-F4 to order selected divisions. Keep the F1 key down to place selected divisions. One may target an enemy division through this mechanism.^^\
Pressing the ENTER key often initiates an overhead Strategy Camera.^^\
Pressing the BACKSPACE key often initiates a Battle Command Display with 'radar.'"),
  ("division_placement", "When ONE division is selected, the center of its front rank is placed at the spot indicated.^^\
When MANY divisions are selected, they are separated and spread out as if the player were standing at the spot indicated.^^\
One may memorize the placement of selected divisions relative to the player by pressing F2, F7. Default is infantry to the left, cavalry right, and ranged forward."),
  ("formations", "The Complex Formations on the Battle Menu are:^^\
- RANKS with best troops up front^\
- SHIELD WALL, ranks with shields in front and longer weapons in back^\
- WEDGE with best troops up front^\
- SQUARE in no particular order^\
- NO FORMATION^^\
Even in the last case, the player can make formations up to four lines by ordering Stand Closer enough times."),
]

from util_common import add_objects

def modmerge_formations_strings(orig_strings):
	add_objects(orig_strings, formations_strings, True)
