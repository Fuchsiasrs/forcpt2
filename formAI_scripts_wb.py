# Formations AI by Motomataru
# rel. 08/31/2012

from header_common import *
from header_operations import *
from module_constants import *
from header_mission_templates import *
from header_items import *

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

formAI_scripts = [
# # AI with Formations Scripts
  # script_calculate_decision_numbers by motomataru
  # Input: AI team, size relative to battle in %
  # Output: reg0 - battle presence plus level bump, reg1 - level bump (team avg level / 3)
  ("calculate_decision_numbers", [
	(store_script_param, ":team_no", 1),
	(store_script_param, ":battle_presence", 2),
	(try_begin),
		(team_get_slot, reg0, ":team_no", slot_team_level),
		(store_div, reg1, reg0, 3),
		(store_add, reg0, ":battle_presence", reg1),	#decision w.r.t. all enemy teams
	(try_end)
	]),
	

  # script_team_field_ranged_tactics by motomataru
  # Input: AI team, size relative to largest team in %, size relative to battle in %
  # Output: none
  ("team_field_ranged_tactics", [
	(store_script_param, ":team_no", 1),
	(store_script_param, ":rel_army_size", 2),
	(store_script_param, ":battle_presence", 3),
	(assign, ":division", grc_archers), #Pre-Many Divisions
	(assign, ":bg_pos", Archers_Pos), #Pre-Many Divisions

	(try_begin),
		(store_add, ":slot", slot_team_d0_size, ":division"),
		(team_slot_eq, ":team_no", ":slot", 0),
		(try_begin),	#undo reversion to BP_Jockey (see below)
			(lt, "$battle_phase", BP_Fight),
			(call_script, "script_cf_any_fighting"),
			(call_script, "script_cf_count_casualties"),
			(assign, "$battle_phase", BP_Fight),
		(try_end),
	(else_try),
		(call_script, "script_battlegroup_get_position", ":bg_pos", ":team_no", ":division"),
		(call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, ":team_no", grc_everyone),
		(call_script, "script_point_y_toward_position", ":bg_pos", Enemy_Team_Pos),
		
		(store_add, ":slot", slot_team_d0_closest_enemy_special_dist, ":division"),	#distance to nearest enemy infantry agent
		(team_get_slot, ":distance_to_enemy", ":team_no", ":slot"),
		(try_begin),
			(eq, ":distance_to_enemy", 0),
			(call_script, "script_get_nearest_enemy_battlegroup_location", Nearest_Enemy_Battlegroup_Pos, ":team_no", ":bg_pos"),
			(assign, ":distance_to_enemy", reg0),
		(try_end),
		
		(try_begin),	#avoid being provoked from defensive position
			(ge, "$battle_phase", BP_Fight),
			(neg|call_script, "script_cf_any_fighting"),
			(assign, "$battle_phase", BP_Jockey),
			(assign, "$clock_reset", 0),
		(try_end),
		
		(store_add, ":slot", slot_team_d0_is_fighting, ":division"),
		(team_get_slot, ":is_firing", ":team_no", ":slot"),
		(store_add, ":slot", slot_team_d0_size, grc_infantry),
		(team_get_slot, ":num_infantry", ":team_no", ":slot"),
		
		(call_script, "script_calculate_decision_numbers", ":team_no", ":battle_presence"),
		(assign, ":decision_index", reg0),
		(assign, ":level_bump", reg1),
		(try_begin),
			(gt, ":decision_index", 86),	#outpower enemies more than 6:1?
			(team_get_movement_order, reg0, ":team_no", ":division"),
			(try_begin),
				(neq, reg0, mordr_charge),
				(team_give_order, ":team_no", ":division", mordr_charge),
			(try_end),
			
		(else_try),
			(lt, ":decision_index", 14),	#outpowered more than 6:1?
			(eq, ":num_infantry", 0),	#no infantry to delay enemy?
			(team_get_movement_order, reg0, ":team_no", ":division"),
			(try_begin),
				(neq, reg0, mordr_retreat),
				(team_give_order, ":team_no", ":division", mordr_retreat),
			(try_end),
			
		(else_try),
			(ge, "$battle_phase", BP_Jockey),
			(store_add, ":slot", slot_team_d0_low_ammo, ":division"),
			(team_slot_ge, ":team_no", ":slot", 1),	#running out of ammo?
			(team_get_movement_order, reg0, ":team_no", ":division"),
			(try_begin),
				(neq, reg0, mordr_charge),
				(team_give_order, ":team_no", ":division", mordr_charge),
			(try_end),
			
		(else_try),
			(ge, "$battle_phase", BP_Fight),
			(eq, ":is_firing", 0),
			(gt, ":decision_index", Advance_More_Point),
			(le, ":distance_to_enemy", AI_long_range),	#closer than reposition?
			(team_give_order, ":team_no", ":division", mordr_advance),

		#hold somewhere
		(else_try),
			(store_add, ":decision_index", ":rel_army_size", ":level_bump"),	#decision w.r.t. largest enemy team
			(assign, ":move_archers", 0),
			
			(init_position, Team_Starting_Point),
			(team_get_slot, reg0, ":team_no", slot_team_starting_x),
			(position_set_x, Team_Starting_Point, reg0),
			(team_get_slot, reg0, ":team_no", slot_team_starting_y),
			(position_set_y, Team_Starting_Point, reg0),
			(position_set_z_to_ground_level, Team_Starting_Point),
			
			(try_begin),
				(eq, "$battle_phase", BP_Setup),
				(assign, ":move_archers", 1),
			(else_try),
				(ge, "$battle_phase", BP_Fight),
				(try_begin),
					(neg|is_between, ":distance_to_enemy", AI_charge_distance, AI_long_range),
					(assign, ":move_archers", 1),
				(else_try),
					(lt, ":decision_index", Hold_Point),	#probably coming from a defensive position (see below)
					(eq, "$formation_AI_no_defense", 0),	#player hasn't set disallow defense option?
					(eq, ":is_firing", 0),	#probably because player team has retreated
					(assign, ":move_archers", 1),
				(try_end),
			(else_try),	#jockey phase
				(this_or_next|gt, "$formation_AI_no_defense", 0),	#player has set disallow defense option OR
				(ge, ":decision_index", Hold_Point),	#not starting in a defensive position (see below)
				(try_begin),
					(gt, ":distance_to_enemy", AI_long_range),	#enemy very far off
					(assign, ":move_archers", 1),
				(else_try),
					(call_script, "script_point_y_toward_position", Team_Starting_Point, ":bg_pos"),
					(position_get_rotation_around_z, reg0, Team_Starting_Point),
					(position_get_rotation_around_z, reg1, ":bg_pos"),
					(val_sub, reg0, reg1),
					(this_or_next|is_between, reg0, -45, 45),	#only move if within "cone of advancement" to prevent constant adjusting at border OR
					(eq, ":is_firing", 0),	#if not firing for some reason (hill in way?)
					
					(try_begin),
						(eq, ":num_infantry", 0),	#no infantry to wait for
						(assign, ":move_archers", 1),
					(else_try),
						(call_script, "script_battlegroup_get_position", Infantry_Pos, ":team_no", grc_infantry),
						(get_distance_between_positions, ":infantry_to_enemy", Infantry_Pos, Enemy_Team_Pos),
						(get_distance_between_positions, ":archers_to_enemy", ":bg_pos", Enemy_Team_Pos),
						(val_sub, ":infantry_to_enemy", ":archers_to_enemy"),
						(le, ":infantry_to_enemy", 1500),	#don't outstrip infantry when closing
						(assign, ":move_archers", 1),
					(try_end),
				(try_end),
			(try_end),
			
			(try_begin),
				(gt, ":move_archers", 0),
				(try_begin),
					(lt, ":decision_index", Hold_Point),	#outnumbered?
					(eq, "$formation_AI_no_defense", 0),	#player hasn't set disallow defense option?
					(lt, "$battle_phase", BP_Fight),
					(neq, ":team_no", 1),	#not attacker?
					(neq, ":team_no", 3),	#not ally of attacker?
					(store_div, ":distance_to_move", ":distance_to_enemy", 6),	#middle of rear third of battlefield
					(assign, ":hill_search_radius", ":distance_to_move"),

				(else_try),
					(try_begin),
						(ge, "$battle_phase", BP_Fight),
						(copy_position, ":bg_pos", Team_Starting_Point),
						(call_script, "script_point_y_toward_position", ":bg_pos", Enemy_Team_Pos),
						(try_begin),
							(gt, ":num_infantry", 0),
							(eq, "$formation_no_nearest_agent", 0),
							(store_add, ":slot", slot_team_d0_closest_enemy, grc_infantry),
							(team_get_slot, ":enemy_agent_nearest_infantry", ":team_no", ":slot"),
							(agent_get_team, ":target_team", ":enemy_agent_nearest_infantry"),
							(agent_get_division, ":target_division", ":enemy_agent_nearest_infantry"),
							(call_script, "script_battlegroup_get_position", Nearest_Enemy_Battlegroup_Pos, ":target_team", ":target_division"),
							(get_distance_between_positions, ":distance_to_enemy", ":bg_pos", Nearest_Enemy_Battlegroup_Pos),
						(else_try),
							(call_script, "script_get_nearest_enemy_battlegroup_location", Nearest_Enemy_Battlegroup_Pos, ":team_no", ":bg_pos"),
							(assign, ":distance_to_enemy", reg0),
						(try_end),
					(try_end),

					(try_begin),
						(eq, "$battle_phase", BP_Setup),
						(assign, ":shot_distance", AI_long_range),
					(else_try),
						(assign, ":shot_distance", AI_firing_distance),
						(store_sub, reg1, AI_firing_distance, AI_charge_distance),
						(val_sub, reg1, 200),	#subtract two meters to prevent automatically provoking melee from forward enemy infantry
						(store_add, ":slot", slot_team_d0_percent_throwers, ":division"),
						(team_get_slot, reg0, ":team_no", ":slot"),
						(val_mul, reg1, reg0),
						(val_div, reg1, 100),
						(val_sub, ":shot_distance", reg1),
					(try_end),

					(store_sub, ":distance_to_move", ":distance_to_enemy", ":shot_distance"),
					(store_div, ":hill_search_radius", ":shot_distance", 3),	#limit so as not to run into enemy
					(try_begin),
						(lt, "$battle_phase", BP_Fight),
						(try_begin),
							(this_or_next|eq, "$battle_phase", BP_Setup),
							(lt, ":battle_presence", Advance_More_Point),	#expect to meet halfway?
							(val_div, ":distance_to_move", 2),
						(try_end),
					(try_end),
				(try_end),

				(position_move_y, ":bg_pos", ":distance_to_move", 0),
				(try_begin),
					(lt, "$battle_phase", BP_Fight),
					(copy_position, pos1, ":bg_pos"),
					(store_div, reg0, ":hill_search_radius", 100),
					(call_script, "script_find_high_ground_around_pos1_corrected", ":bg_pos", reg0),
				(try_end),
			(try_end),

			(team_get_movement_order, reg0, ":team_no", ":division"),
			(try_begin),
				(neq, reg0, mordr_hold),
				(team_give_order, ":team_no", ":division", mordr_hold),
			(try_end),
			(team_set_order_position, ":team_no", ":division", ":bg_pos"),
		(try_end),
	(try_end)
	]),

	  
  # script_team_field_melee_tactics by motomataru #EDITED FOR SLOTS BY CABA...many divisions changes necessary
  # Input: AI team, size relative to largest team in %, size relative to battle in %
  # Output: none
  ("team_field_melee_tactics", [
	(store_script_param, ":team_no", 1),
#	(store_script_param, ":rel_army_size", 2),
	(store_script_param, ":battle_presence", 3),
	(call_script, "script_calculate_decision_numbers", ":team_no", ":battle_presence"),

	#mop up if outnumber enemies more than 6:1
	(try_begin),
		(gt, reg0, 86),
		(try_for_range, ":division", 0, 9),
			(store_add, ":slot", slot_team_d0_size, ":division"),
			(team_slot_ge, ":team_no", ":slot", 1),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(neg|team_slot_eq, ":team_no", ":slot", sdt_archer),
			(neg|team_slot_eq, ":team_no", ":slot", sdt_skirmisher),
			(call_script, "script_formation_end", ":team_no", ":division"),
			(team_get_movement_order, reg0, ":team_no", ":division"),
			(try_begin),
				(neq, reg0, mordr_charge),
				(team_give_order, ":team_no", ":division", mordr_charge),
			(try_end),
		(try_end),

	(else_try),		
		(assign, ":num_enemies", 0),
		(try_for_range, ":enemy_team_no", 0, 4),
			(teams_are_enemies, ":enemy_team_no", ":team_no"),
			(team_get_slot, ":value", ":enemy_team_no", slot_team_size),
			(val_add, ":num_enemies", ":value"),
		(try_end),
		
		(gt, ":num_enemies", 0),
		(call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, ":team_no", grc_everyone),
		
		(store_add, ":slot", slot_team_d0_size, grc_archers),
		(team_get_slot, ":num_archers", ":team_no", ":slot"),
		(try_begin),
			(eq, ":num_archers", 0),
			(assign, ":enemy_bg_nearest_archers_dist", Far_Away),
			(assign, ":archer_order", mordr_charge),
		(else_try),
			(call_script, "script_battlegroup_get_position", Archers_Pos, ":team_no", grc_archers),
			(call_script, "script_point_y_toward_position", Archers_Pos, Enemy_Team_Pos),
			(call_script, "script_get_nearest_enemy_battlegroup_location", pos0, ":team_no", Archers_Pos),
			(assign, ":enemy_bg_nearest_archers_dist", reg0),
			(team_get_movement_order, ":archer_order", ":team_no", grc_archers),
		(try_end),

		(store_add, ":slot", slot_team_d0_size, grc_infantry),
		(team_get_slot, ":num_infantry", ":team_no", ":slot"),
		(try_begin),
			(eq, ":num_infantry", 0),
			(assign, ":enemy_bg_nearest_infantry_dist", Far_Away),
			(assign, ":enemy_agent_nearest_infantry_dist", Far_Away),
		(else_try),
			(call_script, "script_battlegroup_get_position", Infantry_Pos, ":team_no", grc_infantry),
			(call_script, "script_get_nearest_enemy_battlegroup_location", pos0, ":team_no", Infantry_Pos),
			(assign, ":enemy_bg_nearest_infantry_dist", reg0),
			(store_add, ":slot", slot_team_d0_closest_enemy_dist, grc_infantry),
			(team_get_slot, ":enemy_agent_nearest_infantry_dist", ":team_no", ":slot"),
			(eq, ":enemy_agent_nearest_infantry_dist", 0),	#happens when player turns off closest agent mechanism (see mod options)
			(assign, ":enemy_agent_nearest_infantry_dist", ":enemy_bg_nearest_infantry_dist"),
		(try_end),

		(store_add, ":slot", slot_team_d0_size, grc_cavalry),
		(team_get_slot, ":num_cavalry", ":team_no", ":slot"),
		(try_begin),
			(eq, ":num_cavalry", 0),
			(assign, ":enemy_bg_nearest_cavalry_dist", Far_Away),
			(assign, ":enemy_agent_nearest_cavalry_dist", Far_Away),
		(else_try),
			(call_script, "script_battlegroup_get_position", Cavalry_Pos, ":team_no", grc_cavalry),
			(call_script, "script_get_nearest_enemy_battlegroup_location", pos0, ":team_no", Cavalry_Pos),
			(assign, ":enemy_bg_nearest_cavalry_dist", reg0),
			(store_add, ":slot", slot_team_d0_closest_enemy_dist, grc_cavalry),
			(team_get_slot, ":enemy_agent_nearest_cavalry_dist", ":team_no", ":slot"),
			(eq, ":enemy_agent_nearest_cavalry_dist", 0),	#happens when player turns off closest agent mechanism (see mod options)
			(assign, ":enemy_agent_nearest_cavalry_dist", ":enemy_bg_nearest_infantry_dist"),
		(try_end),

		(try_begin),
			(lt, "$battle_phase", BP_Fight),
			(this_or_next|le, ":enemy_bg_nearest_infantry_dist", AI_charge_distance),
			(this_or_next|le, ":enemy_bg_nearest_cavalry_dist", AI_charge_distance),
			(le, ":enemy_bg_nearest_archers_dist", AI_charge_distance),
			(assign, "$battle_phase", BP_Fight),
		(else_try),
			(lt, "$battle_phase", BP_Jockey),
			(this_or_next|le, ":enemy_agent_nearest_infantry_dist", AI_long_range),
			(le, ":enemy_agent_nearest_cavalry_dist", AI_long_range),
			(assign, "$battle_phase", BP_Jockey),
		(try_end),
		
		(team_get_leader, ":team_leader", ":team_no"),
		(assign, ":place_leader_by_infantry", 0),
		
		#infantry AI
		(try_begin),
			(le, ":num_infantry", 0),
			(assign, ":infantry_order", ":archer_order"),
			
			#deal with mounted heroes that team_give_order() treats as infantry   #CABA...could change their division?
			(team_get_movement_order, reg0, ":team_no", grc_infantry),
			(try_begin),
				(neq, reg0, ":infantry_order"),
				(team_give_order, ":team_no", grc_infantry, ":infantry_order"),
			(try_end),
			(try_begin),
				(gt, ":num_archers", 0),
				(copy_position, pos1, Archers_Pos),
				(position_move_y, pos1, 1000, 0),
				(team_set_order_position, ":team_no", grc_infantry, pos1),
			(else_try),
				(team_set_order_position, ":team_no", grc_infantry, Cavalry_Pos),
			(try_end),

		(else_try),
			(try_begin),
				(eq, "$formation_no_nearest_agent", 0),
				(store_add, ":slot", slot_team_d0_closest_enemy, grc_infantry),
				(team_get_slot, ":enemy_agent_nearest_infantry", ":team_no", ":slot"),
				
			(else_try),	#player has turned off closest agent mechanism (see mod options)
				(assign, ":enemy_agent_nearest_infantry", -1),
				(try_for_agents, ":enemy_agent"),
					(agent_is_alive, ":enemy_agent"),
					(agent_is_human, ":enemy_agent"),
					(agent_get_group, ":enemy_agent_nearest_infantry_team", ":enemy_agent"),
					(teams_are_enemies, ":enemy_agent_nearest_infantry_team", ":team_no"),
					(agent_slot_eq, ":enemy_agent", slot_agent_is_running_away, 0),
					
					(try_begin),
						(eq, ":enemy_agent_nearest_infantry", -1),
						(assign, ":enemy_agent_nearest_infantry", ":enemy_agent"),
					(else_try),
						(agent_get_position, pos0, ":enemy_agent"),
						(get_distance_between_positions, ":new_distance", pos0, Infantry_Pos),
						(agent_get_position, pos0, ":enemy_agent_nearest_infantry"),
						(get_distance_between_positions, ":old_distance", pos0, Infantry_Pos),
						(lt, ":new_distance", ":old_distance"),
						(assign, ":enemy_agent_nearest_infantry", ":enemy_agent"),
					(try_end),
				(try_end),
			(try_end),
			
			(agent_get_position, Nearest_Enemy_Troop_Pos, ":enemy_agent_nearest_infantry"),
			(agent_get_team, ":enemy_agent_nearest_infantry_team", ":enemy_agent_nearest_infantry"),
			(agent_get_division, ":enemy_agent_nearest_infantry_div", ":enemy_agent_nearest_infantry"),
			
			(assign, ":sum_level_enemy_infantry", 0),
			(try_for_range, ":enemy_team_no", 0, 4),
				(teams_are_enemies, ":enemy_team_no", ":team_no"),
				(try_for_range, ":enemy_division", 0, 9),
					(store_add, ":slot", slot_team_d0_type, ":enemy_division"),
					(team_get_slot, ":value", ":enemy_team_no", ":slot"),
					(this_or_next|eq, ":value", sdt_polearm),
					(eq, ":value", sdt_infantry),
					(store_add, ":slot", slot_team_d0_size, ":enemy_division"),
					(team_get_slot, ":value", ":enemy_team_no", ":slot"),
					(store_add, ":slot", slot_team_d0_level, ":enemy_division"),
					(team_get_slot, reg0, ":enemy_team_no", ":slot"),
					(val_mul, ":value", reg0),
					(val_add, ":sum_level_enemy_infantry", ":value"),
				(try_end),
			(try_end),
		
			(store_mul, ":percent_level_enemy_infantry", ":sum_level_enemy_infantry", 100),
			(val_div, ":percent_level_enemy_infantry", ":num_enemies"),
			(try_begin),
				(teams_are_enemies, ":team_no", "$fplayer_team_no"),
				(assign, ":combined_level", 0),
				(assign, ":combined_team_size", 0),
				(assign, ":combined_num_infantry", ":num_infantry"),
			(else_try),
				(store_add, ":slot", slot_team_d0_level, grc_infantry),
				(team_get_slot, ":combined_level", "$fplayer_team_no", ":slot"),
				(team_get_slot, ":combined_team_size", "$fplayer_team_no", slot_team_size),
				(store_add, ":slot", slot_team_d0_size, grc_infantry),
				(team_get_slot, ":combined_num_infantry", "$fplayer_team_no", ":slot"),
				(val_add, ":combined_num_infantry", ":num_infantry"),
			(try_end),
			(store_mul, ":percent_level_infantry", ":combined_num_infantry", 100),
			(store_add, ":slot", slot_team_d0_level, grc_infantry),
			(team_get_slot, ":level_infantry", ":team_no", ":slot"),
			(val_add, ":combined_level", ":level_infantry"),
			(val_mul, ":percent_level_infantry", ":combined_level"),
			(team_get_slot, reg0, ":team_no", slot_team_size),
			(val_add, ":combined_team_size", reg0),
			(val_div, ":percent_level_infantry", ":combined_team_size"),

			(assign, ":infantry_order", mordr_charge),
			(try_begin),	#enemy far away AND ranged not charging
				(gt, ":enemy_bg_nearest_archers_dist", AI_charge_distance),
				(gt, ":enemy_agent_nearest_infantry_dist", AI_charge_distance),
				(neq, ":archer_order", mordr_charge),
				(try_begin),	#fighting not started OR not enough infantry
					(this_or_next|le, "$battle_phase", BP_Jockey),
					(lt, ":percent_level_infantry", ":percent_level_enemy_infantry"),
					(assign, ":infantry_order", mordr_hold),
				(try_end),
			(try_end),

			# bum rush enemy archers?
			(try_begin),
				(le, ":level_infantry", AI_Poor_Troop_Level),
				(store_add, ":slot", slot_team_d0_type, ":enemy_agent_nearest_infantry_div"),
				(this_or_next|team_slot_eq, ":enemy_agent_nearest_infantry_team", ":enemy_agent_nearest_infantry_div", sdt_archer),
				(team_slot_eq, ":enemy_agent_nearest_infantry_team", ":enemy_agent_nearest_infantry_div", sdt_skirmisher),
				(get_distance_between_positions, reg0, Infantry_Pos, Nearest_Enemy_Troop_Pos),
				(le, reg0, AI_charge_distance),
				(call_script, "script_formation_end", ":team_no", grc_infantry),
				(team_get_movement_order, reg0, ":team_no", grc_infantry),
				(try_begin),
					(neq, reg0, mordr_charge),
					(team_give_order, ":team_no", grc_infantry, mordr_charge),
				(try_end),
				
			#else attempt to make formation somewhere
			(else_try),
				(store_add, ":slot", slot_team_d0_formation, grc_infantry),
				(team_get_slot, ":infantry_formation", ":team_no", ":slot"),
				(team_get_leader, ":enemy_leader", ":enemy_agent_nearest_infantry_team"),
				
				#consider new formation
				(try_begin),
					(store_add, ":slot", slot_team_d0_is_fighting, grc_infantry),
					(this_or_next|eq, ":infantry_formation", formation_none),
					(this_or_next|eq, ":infantry_formation", formation_default),
					(team_slot_eq, ":team_no", ":slot", 0),

					(call_script, "script_get_default_formation", ":team_no"),
					(assign, ":infantry_formation", reg0),
					(agent_get_class, ":enemy_nearest_troop_class", ":enemy_agent_nearest_infantry"), 
					
					(assign, ":num_enemy_cavalry", 0),
					(try_for_range, ":enemy_team_no", 0, 4),
						(teams_are_enemies, ":enemy_team_no", ":team_no"),
						(team_get_slot, ":value", ":enemy_team_no", slot_team_num_cavalry),
						(val_add, ":num_enemy_cavalry", ":value"),
					(try_end),					
					
					(store_mul, ":percent_enemy_cavalry", ":num_enemy_cavalry", 100),
					(val_div, ":percent_enemy_cavalry", ":num_enemies"),
					(try_begin),
						(neq, ":infantry_formation", formation_none),
						(try_begin),
							(gt, ":percent_enemy_cavalry", 66),
							(assign, ":infantry_formation", formation_square),
						(else_try),
							(neq, ":enemy_nearest_troop_class", grc_cavalry),
							(neq, ":enemy_nearest_troop_class", grc_archers),
							(neq, ":enemy_agent_nearest_infantry", ":enemy_leader"),
							(ge, ":num_infantry", 21),
							(store_add, ":slot", slot_team_d0_size, ":enemy_agent_nearest_infantry_div"),
							(team_get_slot, reg0, ":enemy_agent_nearest_infantry_team", ":slot"),
							(gt, reg0, ":num_infantry"),	#got fewer troops?
							(store_add, ":slot", slot_team_d0_armor, grc_infantry),
							(team_get_slot, ":average_armor", ":team_no", ":slot"),
							(store_add, ":slot", slot_team_d0_armor, ":enemy_agent_nearest_infantry_div"),
							(team_get_slot, reg0, ":enemy_agent_nearest_infantry_team", ":slot"),
							(gt, ":average_armor", reg0),	#got better armor?
							(assign, ":infantry_formation", formation_wedge),
						(else_try),
							(gt, ":num_infantry", AI_Max_Size_Oblong_Formations),
							(assign, ":infantry_formation", formation_square),
						(try_end),
					(try_end),
				(try_end),	#consider new formation
				
				(try_begin),
					(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_infantry, ":infantry_formation"),
					(store_add, ":slot", slot_team_d0_formation, grc_infantry),
					(team_set_slot, ":team_no", ":slot", ":infantry_formation"),
					
					#adjust spacing for long swung weapons
					(store_add, ":slot", slot_team_d0_swung_weapon_length, grc_infantry),
					(team_get_slot, ":spacing", ":team_no", ":slot"),
					(val_add, ":spacing", 25),	#rounding for 50cm
					(val_div, ":spacing", 50),
					(store_add, ":slot", slot_team_d0_formation_space, grc_infantry),
					(team_set_slot, ":team_no", ":slot", ":spacing"),

					(assign, ":place_leader_by_infantry", 1),
					
				(else_try),
					(call_script, "script_formation_end", ":team_no", grc_infantry),
					(team_get_movement_order, reg0, ":team_no", grc_infantry),
					(try_begin),
						(neq, reg0, ":infantry_order"),
						(team_give_order, ":team_no", grc_infantry, ":infantry_order"),
					(try_end),
					(eq, ":infantry_order", mordr_hold),
					(assign, ":place_leader_by_infantry", 1),
				(try_end),

				#hold near archers?
				(try_begin),
					(eq, ":infantry_order", mordr_hold),
					(gt, ":num_archers", 0),
					# (copy_position, pos1, Archers_Pos),
					(team_get_order_position, pos1, ":team_no", grc_archers),	#anticipate archers
					(position_move_x, pos1, -100, 0),
					(try_begin),
						(this_or_next|eq, ":enemy_agent_nearest_infantry_div", grc_cavalry),
						(gt, ":percent_level_infantry", ":percent_level_enemy_infantry"),
						(call_script, "script_battlegroup_dist_center_to_front", ":team_no", grc_infantry),	#make sure to clear archers
						(store_mul, ":distance_to_move", reg0, 2),
						(val_add, ":distance_to_move", 1000),
						(position_move_y, pos1, ":distance_to_move", 0),	#move ahead of archers in anticipation of charges
					(else_try),
						(position_move_y, pos1, -1000, 0),
					(try_end),

				#obtain destination
				(else_try),
					(assign, ":target_division", -1),
					(try_begin),
						(store_add, ":slot", slot_team_d0_is_fighting, grc_infantry),
						(team_slot_eq, ":team_no", ":slot", 0),	#not engaged?
						(gt, ":enemy_bg_nearest_archers_dist", AI_charge_distance),	#don't have to protect archers?
						# (lt, ":percent_enemy_cavalry", 100),	#non-cavalry exist? MOTO next command tests
						
						#prefer non-cavalry target (that infantry can catch)
						(store_add, ":slot", slot_team_d0_closest_enemy_special_dist, grc_infantry),
						(team_get_slot, ":distance_to_enemy_troop", ":team_no", ":slot"),
						(gt, ":distance_to_enemy_troop", 0),
						(store_add, ":slot", slot_team_d0_closest_enemy_special, grc_infantry),
						(team_get_slot, ":enemy_nearest_non_cav_agent", ":team_no", ":slot"),
						(agent_get_position, pos60, ":enemy_nearest_non_cav_agent"),
						(agent_get_team, ":enemy_non_cav_team", ":enemy_nearest_non_cav_agent"),
						(team_get_leader, reg0, ":enemy_non_cav_team"),
						(try_begin),
							(eq, ":enemy_nearest_non_cav_agent", reg0),	#team leader?
							(assign, ":distance_to_enemy_group", Far_Away),
						(else_try),
							(agent_get_division, ":target_division", ":enemy_nearest_non_cav_agent"),
							(store_add, ":slot", slot_team_d0_target_team, grc_infantry),
							(team_set_slot, ":team_no", ":slot", ":enemy_non_cav_team"),
							(store_add, ":slot", slot_team_d0_target_division, grc_infantry),
							(team_set_slot, ":team_no", ":slot", ":target_division"),
							(call_script, "script_battlegroup_get_attack_destination", pos1, ":team_no", grc_infantry, ":enemy_non_cav_team", ":target_division"),
							(call_script, "script_get_distance_to_battlegroup", ":enemy_non_cav_team", ":target_division", Infantry_Pos),
							(assign, ":distance_to_enemy_group", reg0),
						(try_end),
						
					#chase nearest target
					(else_try),
						(assign, ":distance_to_enemy_troop", ":enemy_agent_nearest_infantry_dist"),
						(copy_position, pos60, Nearest_Enemy_Troop_Pos),
						(try_begin),
							(eq, ":enemy_agent_nearest_infantry", ":enemy_leader"),
							(assign, ":distance_to_enemy_group", Far_Away),
						(else_try),
							(assign, ":target_division", ":enemy_agent_nearest_infantry_div"),
							(store_add, ":slot", slot_team_d0_target_team, grc_infantry),
							(team_set_slot, ":team_no", ":slot", ":enemy_agent_nearest_infantry_team"),
							(store_add, ":slot", slot_team_d0_target_division, grc_infantry),
							(team_set_slot, ":team_no", ":slot", ":target_division"),
							(call_script, "script_battlegroup_get_attack_destination", pos1, ":team_no", grc_infantry, ":enemy_agent_nearest_infantry_team", ":target_division"),
							(call_script, "script_get_distance_to_battlegroup", ":enemy_agent_nearest_infantry_team", ":target_division", Infantry_Pos),
							(assign, ":distance_to_enemy_group", reg0),
						(try_end),
					(try_end),
					
					#reassemble if too scattered
					(try_begin),
						(call_script, "script_get_distance_to_battlegroup", ":team_no", grc_infantry, pos60),	#we're using enemy troop as a reference
						(val_sub, reg0, ":distance_to_enemy_troop"),
						(gt, reg0, 1500),	#division center too far from where it should be (probably because of reinforcing troops)
						(position_copy_origin, pos1, Infantry_Pos),	#gather at average position
						(call_script, "script_battlegroup_dist_center_to_front", ":team_no", grc_infantry),
						(assign, ":distance_to_move", reg0),
						(store_mul, reg0, 350, formation_reform_interval),
						(val_add, ":distance_to_move", reg0),	#one interval movement
						(position_move_y, pos1, ":distance_to_move"),	#keep rear moving forward
						
					#attack leader if is closest troop
					(else_try),
						(eq, ":target_division", -1),
						(position_copy_origin, pos1, pos60),
						(call_script, "script_point_y_toward_position", Infantry_Pos, pos1),
						(position_copy_rotation, pos1, Infantry_Pos),
						
					#move no farther than nearest troop if its unit is far off
					(else_try),
						(call_script, "script_battlegroup_dist_center_to_front", ":team_no", grc_infantry),
						(val_add, ":distance_to_enemy_troop", reg0),	#distance to center of bg from nearest edge
						(store_sub, reg0, ":distance_to_enemy_group", ":distance_to_enemy_troop"),
						(gt, reg0, AI_charge_distance),
						(position_copy_origin, pos1, Infantry_Pos),
						(position_move_y, pos1, ":distance_to_enemy_troop"),
						
					#shift dead player troops right to clear allies when both attacking the same enemy battlegroup
					(else_try),
						(eq, ":team_no", "$fplayer_team_no"),
						(store_add, ":ally_team", "$fplayer_team_no", 2),
						(neg|teams_are_enemies, ":ally_team", "$fplayer_team_no"),
						(store_add, ":slot", slot_team_d0_size, grc_infantry),
						(team_slot_ge, ":ally_team", ":slot", 1),
						(store_add, ":slot", slot_team_d0_target_team, grc_infantry),
						(team_get_slot, ":target_team", "$fplayer_team_no", ":slot"),
						(team_slot_eq, ":ally_team", ":slot", ":target_team"),
						(store_add, ":slot", slot_team_d0_target_division, grc_infantry),
						(team_slot_eq, ":ally_team", ":slot", ":target_division"),
						(call_script, "script_battlegroup_get_position", pos0, ":ally_team", grc_infantry),
						(get_distance_between_positions, ":distance_to_ally", Infantry_Pos, pos0),
						(lt, ":distance_to_ally", ":distance_to_enemy_group"),	#shift only when not in melee to avoid rotation
						(call_script, "script_battlegroup_get_action_radius", ":ally_team", grc_infantry),	#move larger group less to maintain center
                        (val_div, reg0, 2),	#function returns length of bg
						(position_move_x, pos1, reg0),
					
					#shift allies left to clear dead player troops when both attacking the same enemy battlegroup
					(else_try),
						(main_hero_fallen),
						(eq, AI_Replace_Dead_Player, 1),
						(neq, ":team_no", "$fplayer_team_no"),
						(neg|teams_are_enemies, ":team_no", "$fplayer_team_no"),
						(store_add, ":slot", slot_team_d0_size, grc_infantry),
						(team_slot_ge, "$fplayer_team_no", ":slot", 1),
						(store_add, ":slot", slot_team_d0_target_team, grc_infantry),
						(team_get_slot, ":target_team", "$fplayer_team_no", ":slot"),
						(team_slot_eq, ":team_no", ":slot", ":target_team"),
						(store_add, ":slot", slot_team_d0_target_division, grc_infantry),
						(team_slot_eq, "$fplayer_team_no", ":slot", ":target_division"),
						(call_script, "script_battlegroup_get_position", pos0, "$fplayer_team_no", grc_infantry),
						(get_distance_between_positions, ":distance_to_ally", Infantry_Pos, pos0),
						(lt, ":distance_to_ally", ":distance_to_enemy_group"),	#shift only when not in melee to avoid rotation
						(call_script, "script_battlegroup_get_action_radius", "$fplayer_team_no", grc_infantry),	#move larger group less to maintain center
                        (val_div, reg0, -2),	#function returns length of bg
						(position_move_x, pos1, reg0),
					(try_end),
				(try_end),	#obtain destination
				
				(call_script, "script_set_formation_destination", ":team_no", grc_infantry, pos1),
				
				(try_begin),
					(store_add, ":slot", slot_team_d0_formation, grc_infantry),
					(neg|team_slot_eq, ":team_no", ":slot", formation_none),
					(call_script, "script_get_centering_amount", ":infantry_formation", ":num_infantry", ":spacing"),
					(position_move_x, pos1, reg0),
					(call_script, "script_form_infantry", ":team_no", grc_infantry, ":team_leader", ":spacing", 0, ":infantry_formation"),
				(try_end),
			(try_end),	#attempt to make formation somewhere
		(try_end),	
		
		#cavalry AI
		(try_begin),
			(gt, ":num_cavalry", 0),

			#get distance to nearest enemy battlegroup(s)
			(store_add, ":slot", slot_team_d0_armor, grc_cavalry),
			(team_get_slot, ":average_armor", ":team_no", ":slot"),
			(assign, ":nearest_threat_distance", Far_Away),
			(assign, ":nearest_target_distance", Far_Away),
			(assign, ":num_targets", 0),
			(try_for_range, ":enemy_team_no", 0, 4),
				(team_slot_ge, ":enemy_team_no", slot_team_size, 1),
				(teams_are_enemies, ":enemy_team_no", ":team_no"),
				(try_for_range, ":enemy_division", 0, 9),
					(store_add, ":slot", slot_team_d0_size, ":enemy_division"),
					(team_get_slot, ":size_enemy_battle_group", ":enemy_team_no", ":slot"),
					(gt, ":size_enemy_battle_group", 0),
					(call_script, "script_battlegroup_get_position", pos0, ":enemy_team_no", ":enemy_division"),
					(get_distance_between_positions, ":distance_of_enemy", Cavalry_Pos, pos0),
					(try_begin),	#threat or target?
						(store_add, ":slot", slot_team_d0_weapon_length, ":enemy_division"),
						(team_get_slot, reg0, ":enemy_team_no", ":slot"),
						(assign, ":decision_index", reg0),
						(store_add, ":slot", slot_team_d0_armor, ":enemy_division"),
						(team_get_slot, reg0, ":enemy_team_no", ":slot"),
						(val_mul, ":decision_index", reg0),
						(val_mul, ":decision_index", ":size_enemy_battle_group"),
						(val_div, ":decision_index", ":average_armor"),
						(val_div, ":decision_index", ":num_cavalry"),
						(try_begin),
							(neq, ":enemy_division", grc_cavalry),
							(val_div, ":decision_index", 2),	#double count cavalry vs. foot soldiers
						(try_end),
						(gt, ":decision_index", 100),
						(try_begin),
							(gt, ":nearest_threat_distance", ":distance_of_enemy"),
							(copy_position, Nearest_Threat_Pos, pos0),
							(assign, ":nearest_threat_distance", ":distance_of_enemy"),
						(try_end),
					(else_try),
						(val_add, ":num_targets", 1),
						(gt, ":nearest_target_distance", ":distance_of_enemy"),
						(copy_position, Nearest_Target_Pos, pos0),
						(assign, ":nearest_target_distance", ":distance_of_enemy"),
						(store_add, ":slot", slot_team_d0_target_team, grc_cavalry),
						(team_set_slot, ":team_no", ":slot", ":enemy_team_no"),
						(store_add, ":slot", slot_team_d0_target_division, grc_cavalry),
						(team_set_slot, ":team_no", ":slot", ":enemy_division"),
					(try_end),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":nearest_threat_distance", Far_Away),
				(assign, ":nearest_target_guarded", 0),
			(else_try),
				(eq, ":nearest_target_distance", Far_Away),
				(assign, ":nearest_target_guarded", 1),
			(else_try),
				(get_distance_between_positions, reg0, Nearest_Target_Pos, Nearest_Threat_Pos),
				(store_div, reg1, AI_charge_distance, 2),
				(try_begin),	#ignore target too close to threat
					(le, reg0, reg1),
					(assign, ":nearest_target_guarded", 1),
				(else_try),
					(assign, ":nearest_target_guarded", 0),
				(try_end),
			(try_end),

			(assign, ":cavalry_order", mordr_charge), ##CABA HERE
			(try_begin),
				(teams_are_enemies, ":team_no", 0),
				(neg|team_slot_ge, 1, slot_team_reinforcement_stage, AI_Max_Reinforcements),
				(neg|team_slot_eq, 1, slot_team_reinforcement_stage, "$attacker_reinforcement_stage"),
				(assign, ":cavalry_order", mordr_hold),
			(else_try),
				(teams_are_enemies, ":team_no", 1),
				(neg|team_slot_ge, 0, slot_team_reinforcement_stage, AI_Max_Reinforcements),
				(neg|team_slot_eq, 0, slot_team_reinforcement_stage, "$defender_reinforcement_stage"),
				(assign, ":cavalry_order", mordr_hold),
			(else_try),
				(neq, ":infantry_order", mordr_charge),
				(try_begin),
					(le, "$battle_phase", BP_Jockey),
					(assign, ":cavalry_order", mordr_hold),
				(else_try),
					(eq, ":nearest_target_distance", Far_Away),
					(try_begin),
						(eq, ":num_archers", 0),
						(assign, ":distance_to_archers", 0),
					(else_try),
						(get_distance_between_positions, ":distance_to_archers", Cavalry_Pos, Archers_Pos),
					(try_end),
					(try_begin),
						(this_or_next|gt, ":enemy_agent_nearest_cavalry_dist", AI_charge_distance),
						(gt, ":distance_to_archers", AI_charge_distance),
						(assign, ":cavalry_order", mordr_hold),
					(try_end),
				(try_end),
			(try_end),

			(try_begin),
				(eq, ":team_no", 0),
				(assign, ":cav_destination", Team0_Cavalry_Destination),
			(else_try),
				(eq, ":team_no", 1),
				(assign, ":cav_destination", Team1_Cavalry_Destination),
			(else_try),
				(eq, ":team_no", 2),
				(assign, ":cav_destination", Team2_Cavalry_Destination),
			(else_try),
				(eq, ":team_no", 3),
				(assign, ":cav_destination", Team3_Cavalry_Destination),
			(try_end),
			(store_add, ":slot", slot_team_d0_percent_ranged, grc_cavalry),
			(team_get_slot, reg0, ":team_no", ":slot"),
			
			#horse archers don't use wedge
			(try_begin),
				(ge, reg0, 50),
				(call_script, "script_formation_end", ":team_no", grc_cavalry),
				(try_begin),
					(eq, ":num_archers", 0),
					(team_get_movement_order, reg0, ":team_no", grc_cavalry),
					(try_begin),
						(neq, reg0, mordr_charge),
						(team_give_order, ":team_no", grc_cavalry, mordr_charge),
					(try_end),
				(else_try),
					(team_get_movement_order, reg0, ":team_no", grc_cavalry),
					(try_begin),
						(neq, reg0, ":cavalry_order"),
						(team_give_order, ":team_no", grc_cavalry, ":cavalry_order"),
					(try_end),
					(copy_position, ":cav_destination", Archers_Pos),
					(position_move_y, ":cav_destination", -500, 0),
					(team_set_order_position, ":team_no", grc_cavalry, ":cav_destination"),
				(try_end),
				
			#close in with no unguarded target farther off, free fight
			(else_try),
				(eq, ":cavalry_order", mordr_charge),
				(this_or_next|eq, ":num_archers", 0),
				(le, ":enemy_agent_nearest_cavalry_dist", AI_charge_distance),
				(try_begin),
					(eq, ":num_targets", 1),
					(eq, ":nearest_target_guarded", 0),
					(gt, ":nearest_target_distance", ":nearest_threat_distance"),
					(assign, reg0, 0),
				(else_try),
					(ge, ":num_targets", 2),
					(eq, ":nearest_target_guarded", 1),
					(assign, reg0, 0),
				(else_try),
					(assign, reg0, 1),
				(try_end),
				(eq, reg0, 1),
				(call_script, "script_formation_end", ":team_no", grc_cavalry),
				(team_get_movement_order, reg0, ":team_no", grc_cavalry),
				(try_begin),
					(neq, reg0, mordr_charge),
					(team_give_order, ":team_no", grc_cavalry, mordr_charge),
				(try_end),

			#grand charge if target closer than threat AND not guarded
			(else_try),
				(lt, ":nearest_target_distance", ":nearest_threat_distance"),
				(eq, ":nearest_target_guarded", 0),
				(call_script, "script_formation_end", ":team_no", grc_cavalry),
				(team_get_movement_order, reg0, ":team_no", grc_cavalry),
				(try_begin),
					(neq, reg0, mordr_hold),
					(team_give_order, ":team_no", grc_cavalry, mordr_hold),
				(try_end),
				
				#lead archers up to firing point
				(try_begin),
					(gt, ":nearest_target_distance", AI_firing_distance),
					(eq, ":cavalry_order", mordr_hold),
					(try_begin),
						(eq, ":num_archers", 0),
						(copy_position, ":cav_destination", Cavalry_Pos),	#must be reinforcements, so gather at average position
					(else_try),						
						(copy_position, ":cav_destination", Archers_Pos),
						(position_move_y, ":cav_destination", AI_charge_distance, 0),
					(try_end),
					
				#then CHARRRRGE!
				(else_try),
					(copy_position, ":cav_destination", Cavalry_Pos),
					(call_script, "script_point_y_toward_position", ":cav_destination", Nearest_Target_Pos),
					(position_move_y, ":cav_destination", ":nearest_target_distance", 0),
				(try_end),
				(team_set_order_position, ":team_no", grc_cavalry, ":cav_destination"),
				
			#make a wedge somewhere
			(else_try),
				(try_begin),
					(eq, ":cavalry_order", mordr_charge),
					(neq, ":nearest_target_distance", Far_Away),
					(copy_position, ":cav_destination", Cavalry_Pos),
					(call_script, "script_point_y_toward_position", ":cav_destination", Nearest_Target_Pos),
					(position_move_y, ":cav_destination", ":nearest_target_distance", 0),
					(position_move_y, ":cav_destination", AI_charge_distance, 0),	#charge on through to the other side
				(else_try),
					(neq, ":cavalry_order", mordr_charge),
					(eq, ":num_archers", 0),
					(copy_position, ":cav_destination", Cavalry_Pos),	#must be reinforcements, so gather at average position
				(else_try),
					(copy_position, ":cav_destination", Archers_Pos),	#hold near archers
					(position_move_x, ":cav_destination", 500, 0),
					(position_move_y, ":cav_destination", -1000, 0),
				(try_end),
				
				#move around threat in the way to destination
				(try_begin),
					(neq, ":nearest_threat_distance", Far_Away),
					(call_script, "script_point_y_toward_position", Cavalry_Pos, Nearest_Threat_Pos),
					(call_script, "script_point_y_toward_position", Nearest_Threat_Pos, ":cav_destination"),
					(position_get_rotation_around_z, reg0, Cavalry_Pos),
					(position_get_rotation_around_z, reg1, Nearest_Threat_Pos),
					(store_sub, ":rotation_diff", reg0, reg1),
					(try_begin),
						(lt, ":rotation_diff", -180),
						(val_add, ":rotation_diff", 360),
					(else_try),
						(gt, ":rotation_diff", 180),
						(val_sub, ":rotation_diff", 360),
					(try_end),
					
					(try_begin),
						(is_between, ":rotation_diff", -135, 136),
						(copy_position, ":cav_destination", Cavalry_Pos),
						(assign, ":distance_to_move", AI_firing_distance),
						(try_begin),	#target is left of threat
							(is_between, ":rotation_diff", -135, 0),
							(val_mul, ":distance_to_move", -1),
						(try_end),
						(position_move_x, ":cav_destination", ":distance_to_move", 0),
						(store_sub, ":distance_to_move", ":nearest_threat_distance", AI_firing_distance),
						(position_move_y, ":cav_destination", ":distance_to_move", 0),
						(call_script, "script_point_y_toward_position", ":cav_destination", Cavalry_Pos),
						(position_rotate_z, ":cav_destination", 180),
					(try_end),
				(try_end),
				(get_scene_boundaries, pos0, pos1),
				(position_get_x, reg0, ":cav_destination"),
				(position_get_x, reg1, pos0),
				(val_max, reg0, reg1),
				(position_get_x, reg1, pos1),
				(val_min, reg0, reg1),
				(position_set_x, ":cav_destination", reg0),
				(position_get_y, reg0, ":cav_destination"),
				(position_get_y, reg1, pos0),
				(val_max, reg0, reg1),
				(position_get_y, reg1, pos1),
				(val_min, reg0, reg1),
				(position_set_y, ":cav_destination", reg0),
				(position_set_z_to_ground_level, ":cav_destination"),
				
				(try_begin),
					(call_script, "script_cf_battlegroup_valid_formation", ":team_no", grc_cavalry, formation_wedge),
					(copy_position, pos1, ":cav_destination"),
					(call_script, "script_form_cavalry", ":team_no", grc_cavalry, ":team_leader", 0, 0),
					(store_add, ":slot", slot_team_d0_formation, grc_cavalry),
					(team_set_slot, ":team_no", ":slot", formation_wedge),
					# (team_give_order, ":team_no", grc_cavalry, mordr_hold),
				(else_try),
					(call_script, "script_formation_end", ":team_no", grc_cavalry),
					(team_get_movement_order, reg0, ":team_no", grc_cavalry),
					(try_begin),
						(neq, reg0, ":cavalry_order"),
						(team_give_order, ":team_no", grc_cavalry, ":cavalry_order"),
					(try_end),
				(try_end),
				(call_script, "script_set_formation_destination", ":team_no", grc_cavalry, ":cav_destination"),
			(try_end),
		(try_end),

		#place leader
		(try_begin),
			(ge, ":team_leader", 0),
			(agent_is_alive, ":team_leader"),
			(agent_slot_eq, ":team_leader", slot_agent_is_running_away, 0),
			(try_begin),
				(le, ":num_infantry", 0),
				(try_begin),
					(this_or_next|le, ":num_archers", 0),
					(eq, ":archer_order", mordr_retreat),
					
					(assign, ":more_reinforcements", 1),
					(try_begin),
						(teams_are_enemies, ":team_no", 0),
						(team_slot_ge, 1, slot_team_reinforcement_stage, AI_Max_Reinforcements),
						(assign, ":more_reinforcements", 0),
					(else_try),
						(teams_are_enemies, ":team_no", 1),
						(team_slot_ge, 0, slot_team_reinforcement_stage, AI_Max_Reinforcements),
						(assign, ":more_reinforcements", 0),
					(try_end),
					(eq, ":more_reinforcements", 0),
					
					(agent_clear_scripted_mode, ":team_leader"),
					(agent_start_running_away, ":team_leader"),
					(agent_set_slot, ":team_leader",  slot_agent_is_running_away, 1),
				(else_try),
					(eq, ":archer_order", mordr_charge),
					(agent_clear_scripted_mode, ":team_leader"),
				(else_try),
					(copy_position, pos1, Archers_Pos),
					(position_move_y, pos1, -1000, 0),
					(agent_set_scripted_destination, ":team_leader", pos1, 1),
				(try_end),
			(else_try),
				(neq, ":place_leader_by_infantry", 0),
				(call_script, "script_battlegroup_get_position", pos1, ":team_no", grc_infantry),
				(team_get_order_position, pos0, ":team_no", grc_infantry),
				(call_script, "script_point_y_toward_position", pos1, pos0),
				(call_script, "script_battlegroup_get_action_radius", ":team_no", grc_infantry),
				(val_div, reg0, 2),	#bring to edge of battlegroup
				(position_move_x, pos1, reg0, 0),
				(position_move_x, pos1, 100, 0),
				(agent_set_scripted_destination, ":team_leader", pos1, 1),
			(else_try),
				(agent_clear_scripted_mode, ":team_leader"),
			(try_end),
		(try_end),
	(try_end)
	]),
	  
  # script_field_tactics by motomataru
  # Input: flag 1 to include ranged
  # Output: none
  ("field_tactics", [
	(store_script_param, ":include_ranged", 1),
	
	(assign, ":largest_team_size", 0),
	(assign, ":battle_size", 0),
	(try_for_range, ":ai_team", 0, 4),
		(team_get_slot, ":team_size", ":ai_team", slot_team_size),
		(gt, ":team_size", 0),
		(team_get_slot, ":team_cav_size", ":ai_team", slot_team_num_cavalry),
		(store_add, ":team_adj_size", ":team_size", ":team_cav_size"),	#double count cavalry to capture effect on battlefield
		(val_add, ":battle_size", ":team_adj_size"),
		
		(try_begin),
			(neq, ":ai_team", "$fplayer_team_no"),
			(neg|teams_are_enemies, ":ai_team", "$fplayer_team_no"),
			(team_get_slot, ":player_team_adj_size", "$fplayer_team_no", slot_team_adj_size),
			(val_add, ":team_adj_size", ":player_team_adj_size"),	#ally team takes player team into account
			(team_set_slot, "$fplayer_team_no", slot_team_adj_size, ":team_adj_size"),	#and vice versa
		(try_end),
		(team_set_slot, ":ai_team", slot_team_adj_size, ":team_adj_size"),
		
		(lt, ":largest_team_size", ":team_adj_size"),
		(assign, ":largest_team_size", ":team_adj_size"),
	(try_end),

	#apply tactics to every AI team
    (set_show_messages, 0),
	(try_for_range, ":ai_team", 0, 4),
		(team_get_slot, ":ai_team_size", ":ai_team", slot_team_adj_size),
		(gt, ":ai_team_size", 0),
		
		(assign, ":do_it", 0),
		(try_begin),
			(neq, ":ai_team", "$fplayer_team_no"),
			(assign, ":do_it", 1),
		(else_try),
			(main_hero_fallen),    #have AI take over for mods with post-player battle action
			(eq, AI_Replace_Dead_Player, 1),
			(assign, ":do_it", 1),
		(try_end),
		(eq, ":do_it", 1),
		
		(team_get_slot, ":ai_faction", ":ai_team", slot_team_faction),
		(try_begin),
			(this_or_next|eq, AI_for_kingdoms_only, 0),
			(this_or_next|eq, ":ai_faction", fac_deserters),	#deserters have military training
			(is_between, ":ai_faction", kingdoms_begin, kingdoms_end),
			(val_mul, ":ai_team_size", 100),
			(store_div, ":team_percentage", ":ai_team_size", ":largest_team_size"),
			(store_div, ":team_battle_presence", ":ai_team_size", ":battle_size"),
			(try_begin),
				(eq, ":include_ranged", 1),
				(try_begin),
					(store_mod, ":team_phase", ":ai_team", 2),
					(eq, ":team_phase", 0),
					(assign, ":time_slice", 0),
				(else_try),
					(store_div, ":time_slice", Reform_Trigger_Modulus, 2),
				(try_end),

				(store_mod, reg0, "$ranged_clock", Reform_Trigger_Modulus),
				(this_or_next|eq, reg0, ":time_slice"),
				(eq, "$battle_phase", BP_Setup),
				(call_script, "script_team_field_ranged_tactics", ":ai_team", ":team_percentage", ":team_battle_presence"),
			(try_end),
				
			(try_begin),
				(neg|main_hero_fallen),
				(store_add, ":slot", slot_team_d0_target_team, grc_infantry),
				(team_slot_eq, ":ai_team", ":slot", "$fplayer_team_no"),
				(store_add, ":slot", slot_team_d0_target_division, grc_infantry),
				(team_get_slot, ":enemy_division", ":ai_team", ":slot"),
				(store_add, ":slot", slot_team_d0_size, ":enemy_division"),
				(team_slot_ge, "$fplayer_team_no", ":slot", 1),
				(store_add, ":slot", slot_team_d0_fclock, ":enemy_division"),
				(team_get_slot, ":fclock", "$fplayer_team_no", ":slot"),
				(store_mod, reg0, ":fclock", Reform_Trigger_Modulus),
				(store_div, ":time_slice", Reform_Trigger_Modulus, 2),
			(else_try),
				(store_mod, reg0, "$ranged_clock", Reform_Trigger_Modulus),
				(store_mod, ":team_phase", ":ai_team", 2),
				(eq, ":team_phase", 0),
				(assign, ":time_slice", 0),
			(else_try),
				(store_div, ":time_slice", Reform_Trigger_Modulus, 2),
			(try_end),

			(eq, reg0, ":time_slice"),
			(call_script, "script_team_field_melee_tactics", ":ai_team", ":team_percentage", ":team_battle_presence"),
		(try_end),
	(try_end),
	(set_show_messages, 1),
	]),

	
# # Utilities used by AI by motomataru

  # script_find_high_ground_around_pos1_corrected by motomataru
  # Input:	arg1: destination position
  #			arg2: search_radius (in meters)
  #			pos1 should hold center_position_no
  # Output:	destination contains highest ground within a <search_radius> meter square around pos1
  # Also uses position registers: pos0
  ("find_high_ground_around_pos1_corrected", [
	(store_script_param, ":destination_pos", 1),
	(store_script_param, ":search_radius", 2),
	(assign, ":fixed_point_multiplier", 1),
	(convert_to_fixed_point, ":fixed_point_multiplier"),
	(set_fixed_point_multiplier, 1),

	(position_get_x, ":o_x", pos1),
	(position_get_y, ":o_y", pos1),
	(store_sub, ":min_x", ":o_x", ":search_radius"),
	(store_sub, ":min_y", ":o_y", ":search_radius"),
	(store_add, ":max_x", ":o_x", ":search_radius"),
	(store_add, ":max_y", ":o_y", ":search_radius"),

	(get_scene_boundaries, ":destination_pos", pos0),
	(position_get_x, ":scene_min_x", ":destination_pos"),
	(position_get_x, ":scene_max_x", pos0),
	(position_get_y, ":scene_min_y", ":destination_pos"),
	(position_get_y, ":scene_max_y", pos0),
	(val_max, ":min_x", ":scene_min_x"),
	(val_max, ":min_y", ":scene_min_y"),
	(val_min, ":max_x", ":scene_max_x"),
	(val_min, ":max_y", ":scene_max_y"),

	(assign, ":highest_pos_z", -100),
	(copy_position, ":destination_pos", pos1),
	(init_position, pos0),

	(try_for_range, ":i_x", ":min_x", ":max_x"),
		(try_for_range, ":i_y", ":min_y", ":max_y"),
			(position_set_x, pos0, ":i_x"),
			(position_set_y, pos0, ":i_y"),
			(position_set_z_to_ground_level, pos0),
			(position_get_z, ":cur_pos_z", pos0),
			(try_begin),
				(gt, ":cur_pos_z", ":highest_pos_z"),
				(copy_position, ":destination_pos", pos0),
				(assign, ":highest_pos_z", ":cur_pos_z"),
			(try_end),
		(try_end),
	(try_end),

	(set_fixed_point_multiplier, ":fixed_point_multiplier"),
  ]),
  
  
  # script_cf_count_casualties by motomataru
  # Input: none
  # Output: evalates T/F, reg0 num casualties
  ("cf_count_casualties", [
	(assign, ":num_casualties", 0),
	(try_for_agents,":cur_agent"),
		(try_begin),
			(this_or_next|agent_is_wounded, ":cur_agent"),
			(this_or_next|agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 1),
			(neg|agent_is_alive, ":cur_agent"),
			(val_add, ":num_casualties", 1),
		(try_end),
	(try_end),
	(assign, reg0, ":num_casualties"),
	(gt, ":num_casualties", 0)
	]),
	
	
  # script_cf_any_fighting by motomataru
  # Input: none
  # Output: evalates T/F
  ("cf_any_fighting", [
	(assign, ":any_fighting", 0),
	(try_for_range, ":team", 0, 4),
		(team_slot_ge, ":team", slot_team_size, 1),
		(eq, ":any_fighting", 0),
		(assign, ":num_divs", 9),
		(try_for_range, ":division", 0, ":num_divs"),
			(store_add, ":slot", slot_team_d0_is_fighting, ":division"),
			(team_slot_ge, ":team", ":slot", 1),
			(assign, ":any_fighting", 1),
			(assign, ":num_divs", 0),
		(try_end),
	(try_end),
	
	#lag this check to be sure
	(store_mission_timer_c, ":time_stamp"),
	(try_begin),	#time lag
		(gt, ":any_fighting", 0),
		(assign, "$teams_last_fighting", ":time_stamp"),
	(try_end),
	(assign, ":fighting_finished", formation_reform_interval),
	(val_max, ":fighting_finished", 5),
	(val_add, ":fighting_finished", "$teams_last_fighting"),
	(gt, ":fighting_finished", ":time_stamp"),
	]),
	
	
  # script_get_nearest_enemy_battlegroup_location by motomataru
  # Input: destination position, fron team, from position
  # Output:	destination position, reg0 with distance
  # Run script_store_battlegroup_data before calling!
  ("get_nearest_enemy_battlegroup_location", [
	(store_script_param, ":bgposition", 1),
	(store_script_param, ":team_no", 2),
	(store_script_param, ":from_pos", 3),
	(assign, ":distance_to_nearest_enemy_battlegoup", Far_Away),
	(try_for_range, ":enemy_team_no", 0, 4),
		(team_slot_ge, ":enemy_team_no", slot_team_size, 1),
		(teams_are_enemies, ":enemy_team_no", ":team_no"),
		(try_for_range, ":enemy_division", 0, 9),
			(store_add, ":slot", slot_team_d0_size, ":enemy_division"),
			(team_slot_ge, ":enemy_team_no", ":slot", 1),
			(call_script, "script_battlegroup_get_position", pos0, ":enemy_team_no", ":enemy_division"),
			(get_distance_between_positions, reg0, pos0, ":from_pos"),
			(try_begin),
				(gt, ":distance_to_nearest_enemy_battlegoup", reg0),
				(assign, ":distance_to_nearest_enemy_battlegoup", reg0),
				(copy_position, ":bgposition", pos0),
			(try_end),
		(try_end),
	(try_end),
	(assign, reg0, ":distance_to_nearest_enemy_battlegoup")
  ]),
]


from util_scripts import *
from util_wrappers import *

scripts_directives = [
	[SD_OP_BLOCK_INSERT, "decide_run_away_or_not", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (agent_start_running_away, ":cur_agent"), 0, [
		(agent_clear_scripted_mode, ":cur_agent"),	#handle scripted mode troops - motomataru
	]],
	[SD_OP_BLOCK_INSERT, "decide_run_away_or_not", D_SEARCH_FROM_BOTTOM | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (agent_start_running_away, ":cur_agent"), 0, [
		(agent_clear_scripted_mode, ":cur_agent"),	#handle scripted mode troops - motomataru
	]],
] # scripts_rename

def modmerge_formAI_scripts(orig_scripts):
	process_script_directives(orig_scripts, scripts_directives)
	add_scripts(orig_scripts, formAI_scripts, True)