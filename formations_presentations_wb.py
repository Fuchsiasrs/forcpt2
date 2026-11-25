# Formations AI by Motomataru
# rel. 08/31/2012

from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
from xgm_mod_options_header import *
import string

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

formations_presentations = [
("order_display", prsntf_read_only,0,[
	  (ti_on_presentation_load,
	   [(set_fixed_point_multiplier, 1000),

		(try_for_range, ":i", 0, 9),
			(store_add, ":slot", ":i", slot_party_cabadrin_order_d0),
			(party_set_slot, "p_main_party_backup", ":slot", -1),
		(try_end),
		
		(assign, ":y_position", 564),
		(try_begin), #Figure out which orders to display, set strings
			(eq, "$gk_order", 0),
			(str_store_string, s1, "@F4 - Additional formation types"),
			(assign, ":num_orders", 1),
			(assign, ":y_position", 474),	#564 - 3 * 30
		(else_try),
			(eq, "$gk_order", gk_order_2),
			(str_store_string, s1, "@F7 - Memorize div. placement"),
			(str_store_string, s2, "@F8 - Default division placement"),
			(assign, ":num_orders", 2),
			(assign, ":y_position", 384),	#564 - 6 * 30
		(else_try),
			(eq, "$gk_order", gk_order_4),
			(str_store_string, s1, "@F4 - Ranks"),
			(str_store_string, s2, "@F5 - Shieldwall"),
			(str_store_string, s3, "@F6 - Wedge"),
			(str_store_string, s4, "@F7 - Square"),
			(str_store_string, s5, "@F8 - No Formation"),
			(assign, ":num_orders", 5),
		(try_end),
		(assign, "$menu_by_gk_order", "$gk_order"),

		(try_for_range, ":i", 0, ":num_orders"),
			(try_begin),
				(eq, ":i", 0),
				(str_store_string_reg, s0, s1),
			(else_try),
				(eq, ":i", 1),
				(str_store_string_reg, s0, s2),
			(else_try),
				(eq, ":i", 2),
				(str_store_string_reg, s0, s3),
			(else_try),
				(eq, ":i", 3),
				(str_store_string_reg, s0, s4),
			(else_try),
				(eq, ":i", 4),
				(str_store_string_reg, s0, s5),
			(try_end),
			(create_text_overlay, ":overlay", s0),
			(overlay_set_color, ":overlay", 0xFFFFFF),
			(position_set_x, pos1, 1000),
			(position_set_y, pos1, 1000),
			(overlay_set_size, ":overlay", pos1),
			(position_set_x, pos1, 1),
			(position_set_y, pos1, ":y_position"),
			(overlay_set_position, ":overlay", pos1),
			
			(store_add, ":slot", ":i", slot_party_cabadrin_order_d0),
			(party_set_slot, "p_main_party_backup", ":slot", ":overlay"),
			
			(val_sub, ":y_position", 30),
		(try_end),
		(store_mul, ":add_back", 30, ":num_orders"),
		(val_add, ":y_position", ":add_back"),
		(val_sub, ":y_position", 4),
		(try_for_range, ":i", 0, ":num_orders"),
			(create_mesh_overlay, ":overlay", "mesh_order_frame"),
			(position_set_x, pos1, 700),
			(position_set_y, pos1, 700),
			(overlay_set_size, ":overlay", pos1),

			(position_set_x, pos1, 0),
			(position_set_y, pos1, ":y_position"),
			(overlay_set_position, ":overlay", pos1),

			(val_sub, ":y_position", 30),
		(try_end),
		
		(try_begin),
			(neq, "$gk_order", 0),
			(neq, "$gk_order", gk_order_2),
			(create_mesh_overlay, ":overlay", "mesh_white_plane"),
			(overlay_set_color, ":overlay", 0),
			(overlay_set_alpha, ":overlay", 0x10),
			(position_set_x, pos1, 14000),
			(position_set_y, pos1, 4500),
			(overlay_set_size, ":overlay", pos1),
			
			(position_set_x, pos1, 0),
			(position_set_y, pos1, 498),
			(overlay_set_position, ":overlay", pos1),
		(try_end),    
		
		(presentation_set_duration, 999999),
	   ]),
	(ti_on_presentation_run,
	   [(store_trigger_param_1, ":cur_time"),
		(gt, ":cur_time", 250), #0.25 Second after Pres. Start
		(try_begin),
		  (this_or_next|game_key_clicked, gk_order_1),
		  (this_or_next|game_key_clicked, gk_order_2),
		  (this_or_next|game_key_clicked, gk_order_3), #Order Keys not used by Expanded Orders
		  (this_or_next|game_key_clicked, gk_view_orders),
		  (this_or_next|game_key_clicked, gk_group0_hear),
		  (this_or_next|game_key_clicked, gk_group1_hear),
		  (this_or_next|game_key_clicked, gk_group2_hear),
		  (this_or_next|game_key_clicked, gk_group3_hear),
		  (this_or_next|game_key_clicked, gk_group4_hear),
		  (this_or_next|game_key_clicked, gk_group5_hear),
		  (this_or_next|game_key_clicked, gk_group6_hear),
		  (this_or_next|game_key_clicked, gk_group7_hear),
		  (this_or_next|game_key_clicked, gk_group8_hear),
		  (this_or_next|game_key_clicked, gk_everyone_hear),
		  (this_or_next|game_key_clicked, gk_reverse_order_group), 
		  (game_key_clicked, gk_everyone_around_hear), 
		  (presentation_set_duration, 0),
		(try_end),
		(try_begin),
			(assign, ":key", -1),
			(try_begin),
				(game_key_clicked, gk_order_4),
				(assign, ":key", 4),
			(else_try),
				(game_key_clicked, gk_order_5),
				(assign, ":key", 5),
			(else_try),
				(game_key_clicked, gk_order_6),
				(assign, ":key", 6),
			(else_try),
				(key_clicked, key_f7),
				(assign, ":key", 7),
			(else_try),
				(key_clicked, key_f8),
				(assign, ":key", 8),
			(try_end),
			(neq, ":key", -1),
			(try_begin),
				(eq, "$menu_by_gk_order", 0),
				(presentation_set_duration, 0),
			(else_try),
				(eq, "$menu_by_gk_order", gk_order_4),
				(assign, ":min_key", 4),
				(assign, ":max_key", 8),

				(store_sub, ":num_orders", ":max_key", ":min_key"),
				(val_add, ":num_orders", 1),
				(store_sub, ":key_pressed", ":key", ":min_key"),
				(is_between, ":key_pressed", 0, ":num_orders"),
				(try_for_range, ":i", 0, ":num_orders"),
					(store_add, ":slot", ":i", slot_party_cabadrin_order_d0),
					(party_get_slot, ":overlay", "p_main_party_backup", ":slot"), 
					(try_begin),
						(neq, ":i", ":key_pressed"),
						(overlay_animate_to_alpha, ":overlay", 400, 0x00),
						(val_add, ":overlay", ":num_orders"),
						(overlay_animate_to_alpha, ":overlay", 400, 0x00),
					(else_try),				
						(overlay_animate_to_alpha, ":overlay", 1100, 0x00),
						(val_add, ":overlay", ":num_orders"),
						(overlay_animate_to_alpha, ":overlay", 1100, 0x00),
					(try_end),
				(try_end),			
				(presentation_set_duration, 200), 
			(try_end),
		(try_end),
		]),
	]),	

#Formation mod option menu as generated by xgm by Sphere, adapted
("formation_mod_option", 0, mesh_load_window, [
	(ti_on_presentation_load, [
		(presentation_set_duration, 999999),
		(set_fixed_point_multiplier, 1000),
		
		(str_clear, s0),
		(assign, "$g_presentation_obj_1", 0), # forced initialization
		(create_text_overlay, "$g_presentation_obj_1", s0, tf_scrollable),
		(position_set_x, pos1, xgm_mod_options_pane_posx),
		(position_set_y, pos1, xgm_mod_options_pane_posy),
		(overlay_set_position, "$g_presentation_obj_1", pos1),
		(position_set_x, pos1, xgm_mod_options_pane_width),
		(position_set_y, pos1, xgm_mod_options_pane_height),
		(overlay_set_area_size, "$g_presentation_obj_1", pos1),
		(set_container_overlay, "$g_presentation_obj_1"),
		
		(position_set_x, pos1, xgm_mod_options_property_posx),
		(store_sub, ":cur_posy", xgm_mod_options_pane_height, xgm_mod_options_property_height/2),
		
		#Disable formations option
		(position_set_x, pos1, xgm_mod_options_property_label_posx),
		(create_text_overlay, reg0, "@Disable mod formations:", tf_vertical_align_center),
		(position_set_y, pos1, ":cur_posy"),
		(overlay_set_position, reg0, pos1),
		
		(assign, "$g_presentation_obj_2", 0), # forced initialization
		(position_set_x, pos1, xgm_mod_options_property_value_posx + xgm_ov_checkbox_offsetx),
		(create_check_box_overlay, "$g_presentation_obj_2", "mesh_checkbox_off", "mesh_checkbox_on"),
		(store_add, reg1, ":cur_posy", xgm_ov_checkbox_offsety),
		(position_set_y, pos1, reg1),
		(overlay_set_position, "$g_presentation_obj_2", pos1),
		
		(assign, reg1, "$formation_off"),		
		(overlay_set_val, "$g_presentation_obj_2", reg1),
		(position_set_x, pos1, xgm_ov_checkbox_scalex),
		(position_set_y, pos1, xgm_ov_checkbox_scaley),
		(overlay_set_size, "$g_presentation_obj_2", pos1),
		
		(val_sub, ":cur_posy", xgm_mod_options_property_height),
		
		#Player division assignment
		(position_set_x, pos1, xgm_mod_options_property_label_posx),
		(create_text_overlay, reg0, "@Put player in division:", tf_vertical_align_center),
		(position_set_y, pos1, ":cur_posy"),
		(overlay_set_position, reg0, pos1),
		
		(assign, "$g_presentation_obj_3", 0), # forced initialization
		(position_set_x, pos1, xgm_mod_options_property_value_posx + xgm_ov_numberbox_offsetx),
		(create_number_box_overlay, "$g_presentation_obj_3", 0, 10),
		(store_add, ":control_y", ":cur_posy", xgm_ov_numberbox_offsety),
		(position_set_y, pos1, ":control_y"),
		(overlay_set_position, "$g_presentation_obj_3", pos1),
		(position_set_x, pos1, xgm_ov_numberbox_scalex),
		(position_set_y, pos1, xgm_ov_numberbox_scaley),
		(overlay_set_size, "$g_presentation_obj_3", pos1),
		
		(assign, reg1, "$formation_player_in_division"),
		(overlay_set_val, "$g_presentation_obj_3", reg1),
		
		(val_sub, ":cur_posy", xgm_mod_options_property_height),
		
		#Autorotate formations option
		(position_set_x, pos1, xgm_mod_options_property_label_posx),
		(create_text_overlay, reg0, "@Formations rotate to face enemy center:", tf_vertical_align_center),
		(position_set_y, pos1, ":cur_posy"),
		(overlay_set_position, reg0, pos1),
		
		(assign, "$g_presentation_obj_4", 0), # forced initialization
		(position_set_x, pos1, xgm_mod_options_property_value_posx + xgm_ov_checkbox_offsetx),
		(create_check_box_overlay, "$g_presentation_obj_4", "mesh_checkbox_off", "mesh_checkbox_on"),
		(store_add, reg1, ":cur_posy", xgm_ov_checkbox_offsety),
		(position_set_y, pos1, reg1),
		(overlay_set_position, "$g_presentation_obj_4", pos1),
		
		(assign, reg1, "$formation_autorotate"),
		(overlay_set_val, "$g_presentation_obj_4", reg1),
		(position_set_x, pos1, xgm_ov_checkbox_scalex),
		(position_set_y, pos1, xgm_ov_checkbox_scaley),
		(overlay_set_size, "$g_presentation_obj_4", pos1),
		
		(val_sub, ":cur_posy", xgm_mod_options_property_height),
		
		#Drop nearest agent loop option (stops stuttering for larger than normal battles)
		(position_set_x, pos1, xgm_mod_options_property_label_posx),
		(create_text_overlay, reg0, "@Make large battles smoother, AI dumber:", tf_vertical_align_center),
		(position_set_y, pos1, ":cur_posy"),
		(overlay_set_position, reg0, pos1),
		
		(assign, "$g_presentation_obj_6", 0), # forced initialization
		(position_set_x, pos1, xgm_mod_options_property_value_posx + xgm_ov_checkbox_offsetx),
		(create_check_box_overlay, "$g_presentation_obj_6", "mesh_checkbox_off", "mesh_checkbox_on"),
		(store_add, reg1, ":cur_posy", xgm_ov_checkbox_offsety),
		(position_set_y, pos1, reg1),
		(overlay_set_position, "$g_presentation_obj_6", pos1),
		
		(assign, reg1, "$formation_no_nearest_agent"),
		(overlay_set_val, "$g_presentation_obj_6", reg1),
		(position_set_x, pos1, xgm_ov_checkbox_scalex),
		(position_set_y, pos1, xgm_ov_checkbox_scaley),
		(overlay_set_size, "$g_presentation_obj_6", pos1),
		
		(val_sub, ":cur_posy", xgm_mod_options_property_height),
		
		#Prevent AI from taking defensive
		(position_set_x, pos1, xgm_mod_options_property_label_posx),
		(create_text_overlay, reg0, "@Prevent AI from taking defensive:", tf_vertical_align_center),
		(position_set_y, pos1, ":cur_posy"),
		(overlay_set_position, reg0, pos1),
		
		(assign, "$g_presentation_obj_7", 0), # forced initialization
		(position_set_x, pos1, xgm_mod_options_property_value_posx + xgm_ov_checkbox_offsetx),
		(create_check_box_overlay, "$g_presentation_obj_7", "mesh_checkbox_off", "mesh_checkbox_on"),
		(store_add, reg1, ":cur_posy", xgm_ov_checkbox_offsety),
		(position_set_y, pos1, reg1),
		(overlay_set_position, "$g_presentation_obj_7", pos1),
		
		(assign, reg1, "$formation_AI_no_defense"),
		(overlay_set_val, "$g_presentation_obj_7", reg1),
		(position_set_x, pos1, xgm_ov_checkbox_scalex),
		(position_set_y, pos1, xgm_ov_checkbox_scaley),
		(overlay_set_size, "$g_presentation_obj_7", pos1),
		
		(val_sub, ":cur_posy", xgm_mod_options_property_height),
		
		# Finish with options
		(set_container_overlay, -1),

		# This is for Done button
		(assign, "$g_presentation_obj_5", 0), # forced initialization
		(create_game_button_overlay, "$g_presentation_obj_5", "@Done"),
		(position_set_x, pos1, 900),
		(position_set_y, pos1, 25),
		(overlay_set_position, "$g_presentation_obj_5", pos1),
		]),
	   
	(ti_on_presentation_event_state_change, [
		(store_trigger_param_1, ":object"),
		(store_trigger_param_2, ":value"),

		(try_begin),                
			(eq, ":object", "$g_presentation_obj_2"),
			(assign, "$formation_off", ":value"),
		(else_try),                
			(eq, ":object", "$g_presentation_obj_3"),
			(assign, "$formation_player_in_division", ":value"),
		(else_try),                
			(eq, ":object", "$g_presentation_obj_4"),
			(assign, "$formation_autorotate", ":value"),
		(else_try),                
			(eq, ":object", "$g_presentation_obj_6"),
			(assign, "$formation_no_nearest_agent", ":value"),
		(else_try),                
			(eq, ":object", "$g_presentation_obj_7"),
			(assign, "$formation_AI_no_defense", ":value"),
		(else_try),
			(eq, ":object", "$g_presentation_obj_5"),
			(presentation_set_duration, 0),
		(try_end),
		]),
	]),
] # presentations


# the following code block is to be inserted into "battle" presentation's trigger for ti_on_presentation_event_state_change
# just before the line (call_script, "script_update_order_flags_on_map"),
code_block1=[
# formations by motomataru
		  (assign, ":fixed_point_multiplier", 1),
		  (convert_to_fixed_point, ":fixed_point_multiplier"),
		  (set_fixed_point_multiplier, 100),
		  (call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, "$fplayer_team_no", grc_everyone),
		  
		  (try_for_range, ":division", 0, 9),
			(assign, ":do_it", 0),
			(try_begin),
				(eq, ":division", 0),
				(eq, "$g_formation_group0_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 1),
				(eq, "$g_formation_group1_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 2),
				(eq, "$g_formation_group2_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 3),
				(eq, "$g_formation_group3_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 4),
				(eq, "$g_formation_group4_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 5),
				(eq, "$g_formation_group5_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 6),
				(eq, "$g_formation_group6_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 7),
				(eq, "$g_formation_group7_selected", 1),
				(assign, ":do_it", 1),
			(else_try),
				(eq, ":division", 8),
				(eq, "$g_formation_group8_selected", 1),
				(assign, ":do_it", 1),
			(try_end),
			(eq, ":do_it", 1),
			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(neq, ":formation", formation_none),
			(copy_position, pos1, pos3),
			(call_script, "script_point_y_toward_position", pos1, Enemy_Team_Pos),			
			(call_script, "script_set_formation_destination", "$fplayer_team_no", ":division", pos1),
			
			(store_add, ":slot", slot_team_d0_size, ":division"),
			(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
			
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":spacing", "$fplayer_team_no", ":slot"),
			
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(call_script, "script_get_centering_amount", formation_default, ":troop_count", ":spacing"),
				(val_mul, reg0, -1),
				(position_move_x, pos1, reg0),
				(call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":spacing", 0, ":formation"),
			(else_try),
				(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":spacing", 0),
			(else_try),
				(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":spacing"),
				(position_move_x, pos1, reg0),
				(call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":spacing", 0, ":formation"),
			(try_end),

			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", mordr_hold),	
		  (try_end),	#try_for_range ":division"
		  (set_fixed_point_multiplier, ":fixed_point_multiplier"),
# end formations
		  (call_script, "script_update_order_flags_on_map"),
]


from util_common import *
from util_wrappers import *
from util_presentations import *

def modmerge_formations_presentations(orig_presentations):
	add_objects(orig_presentations, formations_presentations, True)	#add_presentations doesn't work
	
	# inject code into battle presentation
	try:
		find_i = list_find_first_match_i( orig_presentations, "battle" )
		battlep = PresentationWrapper(orig_presentations[find_i])
		codeblock = battlep.FindTrigger(ti_on_presentation_event_state_change).GetOpBlock()
		pos = codeblock.FindLineMatching( (call_script, "script_update_order_flags_on_map") )
		codeblock.InsertBefore(pos, code_block1)			
	except:
		import sys
		print "Injecton 1 failed:", sys.exc_info()[1]
		raise
