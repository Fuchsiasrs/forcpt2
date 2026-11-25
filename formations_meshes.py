# Formations AI by Motomataru
# rel. 08/31/2012

from module_constants import *

# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1153 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "meshes"
		orig_meshes = var_set[var_name_1]

		# START do your own stuff to do merging

		if (version > 1011): # assume warband or wfas
			from formations_meshes_wb import modmerge_formations_meshes
			logger.info("Version is warband, merging %s using warband routine."% var_name_1)
			modmerge_formations_meshes(orig_meshes)
		# else:
			# from formations_meshes_mb import modmerge_formations_meshes
			# logger.info("Version is not warband, merging %s using vanilla routine."% var_name_1)

		# modmerge_formations_meshes(orig_meshes)

		# END do your own stuff
            
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)
