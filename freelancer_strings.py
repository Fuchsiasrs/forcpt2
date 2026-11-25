
strings = [
###########################################################################################################################
#####                                                COMMON STRINGS                                                   #####
###########################################################################################################################
	("freelancer_ccr", "CURRENT COMMANDER'S REPORT!"),
	("freelancer_ycomm", "Your Commander: {s19}"),
	("freelancer_commrel", "Commander Relation: {reg0}"),
	("freelancer_enlisted", "You have been enlisted!"),
	("freelancer_grantle", "You have been granted leave!"),
	("freelancer_enlfact", "Enlisted Faction: {s20}"),
	("freelancer_enlfact2", "Enlisted Faction: {s14}"),
    ("freelancer_currank", "Current Rank: {s21}"),
    ("freelancer_exppromo", "Experience to next promotion: {s1}"),	
	("freelancer_dayservice", "Days in service: {reg20}"),
	("freelancer_curwage", "Current Wage: {reg23} denars."),
	("freelancer_nextpay", "Next Pay/Promotion day: {s25}"),
	("freelancer_armysize", "Army size: {reg26}"),
	("freelancer_commarmy", "Commander's Army"),
	("freelance_leftcomm", "You have left your commander!"),
	("freelance_ifdesert", "If you do not return to your commander in time, you will be declared a deserter."),
	("freelance_rejoincomm", "You have rejoined your commander!"),
	("freelance_captcomm", "You have been captured! Escape and rejoin your commander!"),
	("freelance_ifdontreturn", "If you do not return to your commander in time, you will be declared a deserter."),
	("freelance_ifdontreturn2", "If you do not return to your commander in time, you will be declared a deserter."),
    ("freelance_equipassign", "The equipment of a {s1}: {s2} is assigned to you."),
	("freelance_equiptaken", "The equipment of a {s1}: {s2} is taken from you."),
	("freelance_youdesert", "You have deserted from the party of {s13}!"),
	("freelance_notice", "Notice!"),
	("freelance_currank", "Current rank: {s5}"),
	("freelance_enlistof", "Enlisted as a {s5} in the party of {s13} of {s14}."),
	("freelance_youwanted", "You have deserted, and are now wanted!"),
	("freelance_5days", "You have 5 days remaining in your leave from the party of {s13} before you will be declared a deserter."),
	("freelance_5daysend", "You have {reg0} days left until you are declared as a deserter!"),
	("freelance_1dayleft", "You must check in with your commander {s13} immediately or you will be declared a deserter!"),
	("freelancer_relprisoner", "The released prisoners were not be trusted and they are preparing to attack you!"),
	("freelancer_relprisoner2", "The released prisoners scattered as soon as the battle finished. You will not be seeing them again."),
	("freelancer_relprisoner3", "The released prisoners have remained loyal and will join your party."),
	("freelance_nowdecdes", "You have now been declared as a deserter!"),
	("freelance_warning", "Warning!"),
	("freelance_done", "Done"),
	("freelance_na", "N/A"),
	("freelance_melee", "You are not strong enough to lift a weapon fit for your promotion!"),
	("freelance_armor", "You are not strong enough to hold all that weight required with promotion!"),
	("freelance_ranged", "Your arms are to weak to advance in the artillery at this moment."),
	("freelance_riding", "You require more horse riding skills to fit your next position!"),
]

from util_common import *

def modmerge_strings(orig_strings):
    # add remaining strings
    from util_common import add_objects
    num_appended, num_replaced, num_ignored = add_objects(orig_strings, strings)
    #print num_appended, num_replaced, num_ignored
	
	
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "strings"
        orig_strings = var_set[var_name_1]
        modmerge_strings(orig_strings)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)