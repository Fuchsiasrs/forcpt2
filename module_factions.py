from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0xFF7878),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",  "{!}culture_1", 0, 0.9, [], []),
  ("culture_2",  "{!}culture_2", 0, 0.9, [], []),
  ("culture_3",  "{!}culture_3", 0, 0.9, [], []),
  ("culture_4",  "{!}culture_4", 0, 0.9, [], []),
  ("culture_5",  "{!}culture_5", 0, 0.9, [], []),
  ("culture_6",  "{!}culture_6", 0, 0.9, [], []),
  ## ZZ Custom Kingdom Troops begin
  ("culture_player",  "{!}culture_7", 0, 0.9, [], []),
## ZZ Custom Kingdom Troops end
  ("culture_8",  "{!}culture_8", 0, 0.9, [], []),
  ("culture_9",  "{!}culture_9", 0, 0.9, [], []),
  ("culture_10",  "{!}culture_10", 0, 0.9, [], []),
    ("culture_12",  "{!}culture_12", 0, 0.9, [], []),
    ("culture_13",  "{!}culture_13", 0, 0.9, [], []),
    ("culture_14",  "{!}culture_14", 0, 0.9, [], []),
    ("culture_15",  "{!}culture_15", 0, 0.9, [], []),
    ("culture_16",  "{!}culture_16", 0, 0.9, [], []),


#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xFF4433), #changed name so that can tell difference if shows up on map
   ("kingdom_1",  "Crusader States", 0, 0.9, [("koylu_isyani",-0.05),("kingdom_6",-0.05),("outlaws",-0.05),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),], [], 0xFFFFFF),
   ("kingdom_2",  "SelJuk Sultanate",    0, 0.9, [("koylu_isyani",-0.05),("kingdom_12",-0.05),("kingdom_5",-0.05),("outlaws",-0.05),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),], [], 0x0DDFC3),
   ("kingdom_3",  "Mongol Empire", 0, 0.9, [("koylu_isyani",-0.05),("kingdom_8",-0.05),("kingdom_4",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),], [], 0xCC99FF),
   ("kingdom_4",  "Assassins",    0, 0.9, [("koylu_isyani",-0.05),("kingdom_3",-0.05),("outlaws",-0.09),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xABE518),
   ("kingdom_5",  "Byzantine Empire",  0, 0.9, [("koylu_isyani",-0.05),("kingdom_2",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),], [], 0x66023C),
  ("kingdom_7",  "Player Kingdom Custom Troops",  0, 0.9, [("player_faction",1.00),("koylu_isyani",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xE479DA),
 
 ("kingdom_6",  "Ayyubid Dynasty",  0, 0.9, [("koylu_isyani",-0.05),("kingdom_15",-0.05),("kingdom_1",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),], [], 0xDDDD33),
   ("kingdom_8",  "Khwarezmid Empire",  0, 0.9, [("koylu_isyani",-0.05),("kingdom_3",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x000000),
   ("kingdom_9",  "Abbasid Caliphate",  0, 0.9, [("koylu_isyani",-0.05),("kingdom_13",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),], [], 0x7BA174),
  ("kingdom_10",  "Kipchak Khanate",  0, 0.9, [("koylu_isyani",-0.05),("kingdom_14",-0.05),("kingdom_16",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x9d61ce),
  ("kingdom_12",  "Empire of Trebizond",  0, 0.9, [("koylu_isyani",-0.05),("kingdom_2",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC6633),
  ("kingdom_13",  "Kingdom of Cyprus",  0, 0.9, [("koylu_isyani",-0.05),("kingdom_9",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x006699),
  ("kingdom_14",  "Kingdom of Georgia",  0, 0.9, [("koylu_isyani",-0.05),("kingdom_10",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x993333),
  ("kingdom_15",  "Papal States",  0, 0.9, [("koylu_isyani",-0.05),("kingdom_6",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xFFCC00),
  ("kingdom_16",  "Bulgarian Empire",  0, 0.9, [("koylu_isyani",-0.05),("kingdom_10",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x999900),

##  ("kingdom_1_rebels",  "Swadian rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Vaegir rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_3_rebels",  "Khergit rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Nord rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Rhodok rebels",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),
  ("wild_animals","Wild Animals",0, 0.1,[("player_faction",-0.15)], [],0xFFFFFF),
  #isyankar koyluler
  ("koylu_isyani","Asi Koyluler", 0, 0.5,[("commoners",-0.2),("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1),("kingdom_1",-0.02),("kingdom_2",-0.02),("kingdom_3",-0.02),("kingdom_4",-0.02),("kingdom_5",-0.02),("kingdom_6",-0.02)], [], 0xFF0000),
  #("kipcak","Kipchaks", 0, 0.5,[("koylu_isyani",-0.05),("outlaws",-0.05),("peasant_rebels", -0.1),("desert_bandits", -0.02),("sea_raiders", -0.02),("steppe_bandits", -0.02),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("kingdom_1",-0.02)], [], 0x952AB0),
  ("parti_1", "{!}parti_1", 0, 0.0, [("kingdom_5",-0.05),("parti_1", 0.1)], []),

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("koylu_isyani",-0.05),], []),
  ("pechenegs","Pechenegs", 0, 0.5,[("outlaws",-0.6),("koylu_isyani",-0.05),("kingdom_16",-0.05),("kingdom_5",-0.05),], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0xFF7878),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x0404FF),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0xF18221),
  ("desert_bandits","Deserts Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0xDFDC0F),
  ("sea_raiders","Sea Raiders", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x83D3F5),
  ("steppe_bandits","Steppe Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0xA093F9),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
  ## ZZ Custom Kingdom Troops begin
  ("troop_name_temp_1",  "{!}", 0, 0.9, [], []),
  ("troop_name_temp_2",  "{!}", 0, 0.9, [], []),
  ("troop_name_temp_3",  "{!}", 0, 0.9, [], []),
  ("troop_name_temp_4",  "{!}", 0, 0.9, [], []),
  ("troop_name_temp_5",  "{!}", 0, 0.9, [], []),
  ("troop_name_temp_6",  "{!}", 0, 0.9, [], []),
  ("troop_name_temp_7",  "{!}", 0, 0.9, [], []),
  ("troop_name_temp_8",  "{!}", 0, 0.9, [], []),
  ("troop_name_temp_9",  "{!}", 0, 0.9, [], []),
  ("troop_name_temp_10",  "{!}", 0, 0.9, [], []),
## ZZ Custom Kingdom Troops end
]
# modmerger_start version=201 type=4
try:
    component_name = "factions"
    var_set = { "factions":factions,"default_kingdom_relations":default_kingdom_relations, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
