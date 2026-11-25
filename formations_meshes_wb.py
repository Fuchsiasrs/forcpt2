# Formations for Warband by Motomataru
# rel. 12/26/10

formations_meshes = [
("order_frame", 0, "order_frame", 0, 0, 0, 0, 0, 0, 1, 1, 1)
]

from util_common import add_objects

def modmerge_formations_meshes(orig_meshes):
	add_objects(orig_meshes, formations_meshes, True)
