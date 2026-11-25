from header_troops import *
from cstm_header_troops import *
from header_operations import *
from ID_factions import *

def average_face(face_1, face_2):
  age_and_skin_mask = 0xfffffffffffffffff00000000000000000000000000000000000000000000000
  average_features = 0x000000000000000006db6db6db6db6db00000000000db6db0000000000000000
  return (((face_1 + face_2) / 2) & age_and_skin_mask) + average_features

## If you're going to add more skins, make sure to add the facecodes to these lists
tier_1_faces = [(man_face_younger_1, man_face_middle_2), (woman_face_younger_1, woman_face_middle_2)]
tier_2_faces = [(man_face_young_1, man_face_old_2), (woman_face_young_1, woman_face_old_2)]
tier_3_faces = [(man_face_young_1, man_face_old_2), (woman_face_young_1, woman_face_old_2)]
tier_4_faces = [(man_face_middle_1, man_face_older_2), (woman_face_middle_1, woman_face_older_2)]
tier_5_faces = [(man_face_middle_1, man_face_older_2), (woman_face_middle_1, woman_face_older_2)]
tier_6_faces = [(man_face_middle_1, man_face_older_2), (woman_face_middle_1, woman_face_older_2)]
tier_7_faces = [(man_face_old_1, man_face_older_2), (woman_face_old_1, woman_face_older_2)]

## This class is an abstraction of a custom troop tree, laying out the upgrade structure
## From this abstraction, concrete lists of troops can be derived and the desired upgrades applied
class CustomTroopTree:
  ## The constructor takes in a list of custom troops and creates a tree structure with the first custom troop as the root and each subsequent troop as the left sub-tree, with each branch having an empty right sub-tree
  def __init__(self, custom_troops):
    self.root = custom_troops.pop(0)
    if len(custom_troops) > 0:
      self.left_sub_tree = CustomTroopTree(custom_troops)
    else:
      self.left_sub_tree = None
    self.right_sub_tree = None
    self.desc = "A Troop Tree"
  
  ## Returns every troop in the tree in module_troops format with the specified skin
  def troop_list(self, skin):
    list = [self.root.troop(skin)]
    if self.left_sub_tree != None:
      list.extend(self.left_sub_tree.troop_list(skin))
    if self.right_sub_tree != None:
      list.extend(self.right_sub_tree.troop_list(skin))
    
    return list
  
  ## Returns the dummy troop of every troop in the tree in module_troops format with the specified skin
  def dummy_list(self, skin):
    list = [self.root.dummy(skin)]
    if self.left_sub_tree != None:
      list.extend(self.left_sub_tree.dummy_list(skin))
    if self.right_sub_tree != None:
      list.extend(self.right_sub_tree.dummy_list(skin))
    
    return list
  
  ## Returns a list of all troops (as CustomTroop objects, not in module_troops format) in the tree of a specified tier (1 being the base recruit)
  def troops_of_tier(self, tier):
    if tier > 1:
      if self.right_sub_tree != None:
        return self.left_sub_tree.troops_of_tier(tier - 1) + self.right_sub_tree.troops_of_tier(tier - 1)
      elif self.left_sub_tree != None:
        return self.left_sub_tree.troops_of_tier(tier - 1)
      else:
        return []
    elif tier == 1:
      return [self.root]
    else:
      return []
  
  ## Returns the id of last troop of the right-most tree with the specified skin, which would be the last troop in the list returned by troop_list(skin)
  def last_troop_id(self, skin):
    if self.right_sub_tree != None:
      return self.right_sub_tree.last_troop_id(skin)
    elif self.left_sub_tree != None:
      return self.left_sub_tree.last_troop_id(skin)
    else:
      return self.root.troop_id(skin)
  
  ## Returns the number of troops in the tree
  def size(self):
    if self.right_sub_tree != None:
      return self.right_sub_tree.size() + self.left_sub_tree.size() + 1
    elif self.left_sub_tree != None:
      return self.left_sub_tree.size() + 1
    else:
      return 1
  
  ## After the custom troops with a specified skin are generated with troop_list(skin) and inserted into the mod's troop list, this method takes the mod's troop list and applies the upgrade and upgrade2 functions to ensure the custom troops upgrade appropriately
  def upgrade_all(self, troop_list, skin):
    if self.left_sub_tree != None and self.right_sub_tree != None:
      upgrade2(troop_list, self.root.troop_id(skin), self.left_sub_tree.root.troop_id(skin), self.right_sub_tree.root.troop_id(skin))
      self.left_sub_tree.upgrade_all(troop_list, skin)
      self.right_sub_tree.upgrade_all(troop_list, skin)
    elif self.left_sub_tree != None:
      upgrade(troop_list, self.root.troop_id(skin), self.left_sub_tree.root.troop_id(skin))
      self.left_sub_tree.upgrade_all(troop_list, skin)
  
  ## Returns the list of slot operations needed to connect each custom troop with the specified skin to its corresponding dummy troop
  ## Must be passed the relevant slot numbers
  def start_slot_operations(self, skin, cstm_slot_troop_dummy, cstm_slot_troop_custom_troop):
    operations = self.root.start_slot_operations(skin, cstm_slot_troop_dummy, cstm_slot_troop_custom_troop)
    if self.left_sub_tree != None:
      operations.extend(self.left_sub_tree.start_slot_operations(skin, cstm_slot_troop_dummy, cstm_slot_troop_custom_troop))
    if self.right_sub_tree != None:
      operations.extend(self.right_sub_tree.start_slot_operations(skin, cstm_slot_troop_dummy, cstm_slot_troop_custom_troop))
    
    return operations

## This class is an abstraction of a troop in a custom troop tree, from which concrete troops and their corresponding dummies with a specified skin can be derived
## The only attributes that need to be defined are the id, names, level and facecodes
class CustomTroop:
  def __init__(self, id, name, plural_name, level, facecodes):
    self.id = id
    self.name = name
    self.plural_name = plural_name
    self.level = level
    self.facecodes = facecodes
  
  def troop_id(self, skin):
    return self.id + "_" + str(skin)
  
  def troop(self, skin):
    return [self.troop_id(skin), self.name, self.plural_name, tf_guarantee_all|skin, 0, 0, fac_player_supporters_faction, [], level(self.level)|def_attrib, wp(0), 0, self.facecodes[skin][0], self.facecodes[skin][1]]
    
  def dummy(self, skin):
    return [self.troop_id(skin) + "_dummy", self.name, self.plural_name, tf_hero|skin, 0, 0, fac_player_supporters_faction, [], level(self.level)|def_attrib, wp(0), 0, average_face(self.facecodes[skin][0], self.facecodes[skin][1])]
  
  ## Returns the slot operations needed to connect this custom troop with the specified skin to its corresponding dummy troop
  ## Must be passed the relevant slot numbers
  def start_slot_operations(self, skin, cstm_slot_troop_dummy, cstm_slot_troop_custom_troop):
    operations = [
      (troop_set_slot, "trp_" + self.troop_id(skin), cstm_slot_troop_dummy, "trp_" + self.troop_id(skin) + "_dummy"),
      (troop_set_slot, "trp_" + self.troop_id(skin) + "_dummy", cstm_slot_troop_custom_troop, "trp_" + self.troop_id(skin))
    ]
    return operations


## Below is where the actual troop tree structure options are defined

custom_troop_trees = []

## TROOP TREE WITH 1 BRANCH AND 7 TIERS ##

branch = [
  CustomTroop("custom_troop_1_1_1", "Recruit", "Recruits", 5, tier_1_faces),
  CustomTroop("custom_troop_1_1_2", "Tier 2 Troop", "Tier 2 Troops", 10, tier_2_faces),
  CustomTroop("custom_troop_1_1_3", "Tier 3 Troop", "Tier 3 Troops", 15, tier_3_faces),
  CustomTroop("custom_troop_1_1_4", "Tier 4 Troop", "Tier 4 Troops", 20, tier_4_faces),
  CustomTroop("custom_troop_1_1_5", "Tier 5 Troop", "Tier 5 Troops", 25, tier_5_faces),
  CustomTroop("custom_troop_1_1_6", "Tier 6 Troop", "Tier 6 Troops", 30, tier_6_faces),
  CustomTroop("custom_troop_1_1_7", "Tier 7 Troop", "Tier 7 Troops", 35, tier_7_faces)
]

troop_tree = CustomTroopTree(branch)
troop_tree.desc = "1 Branch With 7 Tiers"

custom_troop_trees.append(troop_tree)

## TROOP TREE WITH 2 BRANCHES AND 6 TIERS ##

branch_1 = [
  CustomTroop("custom_troop_2_1_1", "Recruit", "Recruits", 5, tier_1_faces),
  
  CustomTroop("custom_troop_2_1_2", "A2 Troop", "A2 Troops", 10, tier_2_faces),
  CustomTroop("custom_troop_2_1_3", "A3 Troop", "A3 Troops", 15, tier_3_faces),
  CustomTroop("custom_troop_2_1_4", "A4 Troop", "A4 Troops", 20, tier_4_faces),
  CustomTroop("custom_troop_2_1_5", "A5 Troop", "A5 Troops", 25, tier_5_faces),
  CustomTroop("custom_troop_2_1_6", "A6 Troop", "A6 Troops", 30, tier_6_faces)
]

branch_2 = [
  CustomTroop("custom_troop_2_2_2", "B2 Troop", "B2 Troops", 10, tier_2_faces),
  CustomTroop("custom_troop_2_2_3", "B3 Troop", "B3 Troops", 15, tier_3_faces),
  CustomTroop("custom_troop_2_2_4", "B4 Troop", "B4 Troops", 20, tier_4_faces),
  CustomTroop("custom_troop_2_2_5", "B5 Troop", "B5 Troops", 25, tier_5_faces),
  CustomTroop("custom_troop_2_2_6", "B6 Troop", "B6 Troops", 30, tier_6_faces)
]

troop_tree = CustomTroopTree(branch_1)
troop_tree.right_sub_tree = CustomTroopTree(branch_2)
troop_tree.desc = "2 Branches With 6 Tiers"

custom_troop_trees.append(troop_tree)

## TROOP TREE WITH 3 BRANCHES AND 5 TIERS ##

branch_1 = [
  CustomTroop("custom_troop_3_1_1", "Recruit", "Recruits", 5, tier_1_faces),
  
  CustomTroop("custom_troop_3_1_2", "A2 Troop", "A2 Troops", 10, tier_2_faces),
  CustomTroop("custom_troop_3_1_3", "A3 Troop", "A3 Troops", 15, tier_3_faces),
  CustomTroop("custom_troop_3_1_4", "A4 Troop", "A4 Troops", 20, tier_4_faces),
  CustomTroop("custom_troop_3_1_5", "A5 Troop", "A5 Troops", 25, tier_5_faces)
]

branch_2 = [
  CustomTroop("custom_troop_3_2_2", "B2 Troop", "B2 Troops", 10, tier_2_faces),
  CustomTroop("custom_troop_3_2_3", "B3 Troop", "B3 Troops", 15, tier_3_faces),
  CustomTroop("custom_troop_3_2_4", "B4 Troop", "B4 Troops", 20, tier_4_faces),
  CustomTroop("custom_troop_3_2_5", "B5 Troop", "B5 Troops", 25, tier_5_faces)
]

branch_3 = [
  CustomTroop("custom_troop_3_3_3", "C3 Troop", "C3 Troops", 15, tier_3_faces),
  CustomTroop("custom_troop_3_3_4", "C4 Troop", "C4 Troops", 20, tier_4_faces),
  CustomTroop("custom_troop_3_3_5", "C5 Troop", "C5 Troops", 25, tier_5_faces)
]

troop_tree = CustomTroopTree(branch_1)
troop_tree.right_sub_tree = CustomTroopTree(branch_2)
troop_tree.right_sub_tree.right_sub_tree = CustomTroopTree(branch_3)
troop_tree.desc = "3 Branches With 5 Tiers"

custom_troop_trees.append(troop_tree)