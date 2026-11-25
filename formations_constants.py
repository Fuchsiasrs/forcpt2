# Formations AI by Motomataru
# rel. 08/31/2012

#Formation modes
formation_none      = 0
formation_default   = 1
formation_ranks     = 2
formation_shield    = 3
formation_wedge     = 4
formation_square    = 5

#Formation tweaks
formation_minimum_spacing	= 67	#historical shieldwall was spaced about 47cm, the width of a man's shoulders. Here we loosen for ease of troop movement.
formation_minimum_spacing_horse_length	= 300
formation_minimum_spacing_horse_width	= 200
formation_start_spread_out	= 2	#extra 50cm spacings for ease of movement for new formations
formation_min_foot_troops	= 12	#minimum to make foot formation
formation_min_cavalry_troops	= 5	#minimum to make cavalry wedge
formation_native_ai_use_formation = 1
formation_delay_for_spawn	= .4	#used for M&B 1.011 implementation
formation_reequip	= 1	#allow troops in formations to switch weapons
formation_reform_interval	= 2 #seconds
formation_rethink_for_formations_only	= 0

#Other constants (not tweaks)
Third_Max_Weapon_Length = 250 / 3
Km_Per_Hour_To_Cm = formation_reform_interval * 100000 / 3600
Reform_Trigger_Modulus = formation_reform_interval * 2	#trigger is half-second
Top_Speed	= 13
Far_Away	= 1000000

###################################################################################
# AutoLoot: Modified Constants
# Most of these are slot definitions, make sure they do not clash with your mod's other slot usage
###################################################################################
# This is an item slot
# slot_item_difficulty = 5

# # Autoloot improved by rubik begin
# slot_item_weight                  = 6

# slot_item_cant_on_horseback       = 10
# slot_item_type_not_for_sell       = 11
# slot_item_modifier_multiplier     = 12

slot_item_needs_two_hands_f   = 41
slot_item_length_f            = 42
slot_item_speed_f             = 43
slot_item_thrust_damage_f     = 44
slot_item_swing_damage_f      = 45
slot_item_alternate_f         = 46	#table between swing/noswing versions of same weapon

slot_item_head_armor_f        = slot_item_needs_two_hands_f
slot_item_body_armor_f        = slot_item_thrust_damage_f
slot_item_leg_armor_f         = slot_item_swing_damage_f

slot_item_horse_speed_f       = slot_item_needs_two_hands_f
slot_item_horse_armor_f       = slot_item_thrust_damage_f
slot_item_horse_charge_f      = slot_item_swing_damage_f
# # Autoloot end

#positions used through formations and AI triggers
Current_Pos     = 34	#pos34
Speed_Pos       = 36	#pos36
Target_Pos      = 37	#pos37
Enemy_Team_Pos  = 38	#pos38
Temp_Pos        = 39	#pos39

#keys used for old M&B
from header_triggers import *
key_for_ranks       = key_j
key_for_shieldwall  = key_k
key_for_wedge       = key_l
key_for_square      = key_semicolon
key_for_undo        = key_u

#Team Slots
slot_team_faction                       = 1
slot_team_starting_x                    = 2
slot_team_starting_y                    = 3
slot_team_reinforcement_stage           = 4

#Reset with every call of Store_Battlegroup_Data
slot_team_size                          = 5
slot_team_adj_size                      = 6 #cavalry double counted for AI considerations
slot_team_num_infantry                  = 7	#class counts
slot_team_num_archers                   = 8
slot_team_num_cavalry                   = 9
slot_team_level                         = 10
slot_team_avg_zrot                      = 11
slot_team_avg_x                         = 12
slot_team_avg_y                         = 13
#Team Slots end

#Battlegroup slots (1 for each of 9 divisions)
slot_team_d0_size                       = 14
slot_team_d0_percent_ranged             = 23
slot_team_d0_percent_throwers           = 32
slot_team_d0_low_ammo                   = 41
slot_team_d0_level                      = 50
slot_team_d0_armor                      = 59
slot_team_d0_weapon_length              = 68
slot_team_d0_swung_weapon_length        = 77
slot_team_d0_front_weapon_length        = 86
slot_team_d0_front_agents               = 95	#for calculating slot_team_d0_front_weapon_length
slot_team_d0_is_fighting                = 104
slot_team_d0_enemy_supporting_melee     = 113
slot_team_d0_closest_enemy              = 122
slot_team_d0_closest_enemy_dist         = 131	#for calculating slot_team_d0_closest_enemy
slot_team_d0_closest_enemy_special      = 140	#tracks non-cavalry for AI infantry division, infantry for AI archer division
slot_team_d0_closest_enemy_special_dist = 149	#for calculating slot_team_d0_closest_enemy_special
slot_team_d0_avg_x                      = 158
slot_team_d0_avg_y                      = 167
slot_team_d0_avg_zrot                   = 176
#End Reset Group

slot_team_d0_type                       = 185	#sdt_* (see below)
slot_team_d0_formation                  = 194	#formation_* (see above)
slot_team_d0_formation_space            = 203	#number of extra 50cm spaces currently in use
slot_team_d0_move_order                 = 212	#now used only for player divisions
slot_team_d0_fclock                     = 221	#now used only for player divisions
slot_team_d0_first_member               = 230	#-1 if division not in formation
slot_team_d0_prev_first_member          = 239
slot_team_d0_speed_limit                = 248
slot_team_d0_percent_in_place           = 257
slot_team_d0_destination_x              = 266
slot_team_d0_destination_y              = 275
slot_team_d0_destination_zrot           = 284
slot_team_d0_target_team                = 293	#targeted battlegroup (team ID)
slot_team_d0_target_division            = 302	#targeted battlegroup (division ID)
#NEXT                                   = 311
#Battlegroup slots end

reset_team_stats_begin = slot_team_size  
reset_team_stats_end   = slot_team_d0_type

scratch_team = 7

#Slot Division Type definitions
sdt_infantry   = 0
sdt_archer     = 1
sdt_cavalry    = 2
sdt_polearm    = 3
sdt_skirmisher = 4
sdt_harcher    = 5
sdt_support    = 6
sdt_bodyguard  = 7
sdt_unknown    = -1

#Other slots
#use faction slots to remember information between battles
slot_faction_d0_mem_formation           = 200
slot_faction_d0_mem_formation_space     = 209
slot_faction_d0_mem_relative_x_flag     = 218
slot_faction_d0_mem_relative_y          = 227
#NEXT                                   = 236

#the following applied only to infantry in formation
slot_agent_in_first_rank       = 27
slot_agent_inside_formation    = 28
slot_agent_nearest_enemy_agent = 29
slot_agent_new_division        = 30

from module_constants import slot_town_arena_melee_mission_tpl
slot_party_cabadrin_order_d0 = slot_town_arena_melee_mission_tpl #78
# slot_party_gk_order          = slot_town_rebellion_readiness #77	#MOTO just use a global for this


