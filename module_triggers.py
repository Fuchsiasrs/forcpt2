from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *

from module_constants import *
from header_terrain_types import *
from header_game_menus import *

####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################

# Some constants for use below
merchant_inventory_space = 30
num_merchandise_goods = 36



triggers = [
# Tutorial:

#(1, 0, 24.0, [],
#[    (assign, "$temp", spai_accompanying_army),
#    (assign, "$temp_2", "p_main_party"),
#	 
#	(store_current_hours, ":hours"),
#	(party_set_slot, "pt_pechenegs", slot_party_following_orders_of_troop, "trp_kingdom_heroes_including_player_begin"),
#	(party_set_slot, "pt_pechenegs", slot_party_orders_type, "$temp"),
#	(party_set_slot, "pt_pechenegs", slot_party_orders_object, "$temp_2"),
#	(party_set_slot, "pt_pechenegs", slot_party_orders_time, ":hours"),
#	
# #(party_set_ai_behavior, "pt_pechenegs", ai_bhvr_attack_party),
# #    (party_set_ai_object,"pt_pechenegs", "p_town_28"),
# ]),

##player lord troops
#	  (0, 0, 24, [(store_faction_of_troop, ":lord_faction", active_npcs_begin, active_npcs_end),
#	(eq, ":lord_faction", "fac_player_supporters_faction"),], [
#	  
#	  (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
#	  (troop_set_slot, ":troop_no", slot_troop_original_faction, "fac_player_supporters_faction"), #player kingdom troops-custom troops
#	  (try_end),
#	]),
 
 #(call_script, "script_bayrak_ve_trooplar_degissin"),
 (0.1, 0, ti_once, [(faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),], [(jump_to_menu,"mnu_krallik_asker")]),
 #(0.1, 0, ti_once, [(eq, "$ana_gorev_baslasin", 1)], [(jump_to_menu,"mnu_cihat5")]),
  (3.1, 0, ti_once, [], [(jump_to_menu,"mnu_mod_bilgiler"),]),
  (1, 0, 1, [(eq, "$cocuk_isim_degistir_aktif", 1)], [(jump_to_menu,"mnu_cocuk_isim_degistir"),]),
  #(3.1, 0, 4, [], [(assign, "$trabzon_sabotaj_gorevi", 1),]),
 # (3.1, 0, 4, [], [(assign, "$kaffaya_git", 1),]),
  (0.3, 0, ti_once, [(eq, "$kaffaya_git", 1),], [(dialog_box,"str_kaffaya_git"),]),
  (0.1, 0, ti_once, [(eq, "$kaffaya_git", 1),], [(dialog_box,"str_oyunu_kaydet"),]),
  (5, 0, ti_once, [(eq, "$kaffaya_git", 1),], [(jump_to_menu,"mnu_kaffa_deniz_savasi"),]),
  (24, 0, ti_once, [(eq, "$sultan_haber_gelir", 1),], [(jump_to_menu,"mnu_sultan_haber_gelir"),]),
  #paralli asker kamp yagma sifirlansin
  (5, 0, 5, [(eq, "$asker_kamp_yagmalandi", 1),], [(assign, "$asker_kamp_yagmalandi", 0),]),
  (24, 0, 24, [(eq, "$su_zehirlendi", 1),], [(assign, "$su_zehirlendi",0),]),
  
  (24, 0, ti_once, [(eq, "$keykubat_cagiri", 1)], [(jump_to_menu,"mnu_keykubat_cagirir"),]),
  (23, 0, ti_once, [(eq, "$keykubat_cagiri", 1)], [(call_script,"script_diplomacy_start_war_between_kingdoms", "fac_kingdom_1", "fac_kingdom_2",1),(call_script,"script_diplomacy_start_war_between_kingdoms", "fac_kingdom_5", "fac_kingdom_2",1),
  (call_script,"script_diplomacy_start_war_between_kingdoms", "fac_kingdom_12", "fac_kingdom_2",1),]),
  

(6, 0, 240.0, 
  [
    (store_num_parties_of_template, reg3, "pt_mongol_war_party"),    
    (lt, reg3, 12),(faction_slot_eq, "fac_kingdom_3", slot_faction_state, sfs_active),
  ],
  [
    (set_spawn_radius, 5),
    (spawn_around_party, "p_castle_30", "pt_mongol_war_party"),
    (spawn_around_party, "p_town_18", "pt_mongol_war_party"),
    (spawn_around_party, "p_town_24", "pt_mongol_war_party"),
    (spawn_around_party, "p_town_23", "pt_mongol_war_party"),
    (spawn_around_party, "p_castle_35", "pt_mongol_war_party"),
    (spawn_around_party, "p_town_12", "pt_mongol_war_party"),
    (spawn_around_party, "p_town_9", "pt_mongol_war_party"),
    (spawn_around_party, "p_town_20", "pt_mongol_war_party"),
    (spawn_around_party, "p_town_32", "pt_mongol_war_party"),
    (spawn_around_party, "p_village_134", "pt_mongol_war_party"),
	(display_message, "@Mongolian invading armies formed!!!", 0xFF0000),
  ]),
  (5.7, 0, 240.0, 
  [
    (store_num_parties_of_template, reg3, "pt_pechenegs_army"),    
    (lt, reg3, 4),#(faction_slot_eq, "fac_kingdom_3", slot_faction_state, sfs_active),
  ],
  [
   # (set_spawn_radius, 2),
   # (spawn_around_party, "p_pecenek_yeri", "pt_pechenegs_army"),
   # (assign, ":spawned_party", reg0),  
	(set_spawn_radius, 2),
(spawn_around_party, "p_pecenek_yeri", "pt_pechenegs_army"),
(spawn_around_party, "p_pecenek_yeri", "pt_pechenegs_army"),
(spawn_around_party, "p_pecenek_yeri", "pt_pechenegs_army"),
(spawn_around_party, "p_pecenek_yeri", "pt_pechenegs_army"),
(assign, ":spawned_party", reg0),
#(party_get_position, pos0, "p_town_5"),
(call_script, "script_party_set_ai_state", ":spawned_party", spai_patrolling_around_center, "p_town_5"),
(party_set_slot, ":spawned_party", slot_party_ai_object, "p_town_5"),
(party_set_slot, ":spawned_party", slot_party_ai_state, spai_patrolling_around_center),
(party_set_ai_behavior, ":spawned_party", ai_bhvr_patrol_party),
(party_set_ai_object, ":spawned_party", "p_town_5"),
#(party_set_ai_target_position, ":spawned_party", pos0),

 
#(party_set_ai_behavior, ":spawned_party", ai_bhvr_patrol_location),
#(party_set_ai_object, ":spawned_party", "p_town_5"),
#(party_set_ai_patrol_radius, ":spawned_party", 3),
#(call_script, "script_party_set_ai_state", ":spawned_party", spai_patrolling_around_center, "p_town_5"),	
   #(party_set_ai_behavior,":spawned_party",ai_bhvr_patrol_location),
   #                                   (party_get_position, pos1, "p_town_5"),
   #                                   (party_set_ai_target_position,":spawned_party",pos1),
   # (party_get_position, pos0, "p_town_5"),    
   # (party_set_ai_behavior, ":spawned_party_id", ai_bhvr_patrol_location),
   # (party_set_ai_patrol_radius, ":spawned_party_id", 3),
   # (party_set_ai_target_position, ":spawned_party_id", pos0),
  ]),
  (5.7, 0, 840.0, 
  [
    (store_num_parties_of_template, reg3, "pt_crusade_army"),    
    (lt, reg3, 2),
	(faction_slot_eq, "fac_kingdom_15", slot_faction_state, sfs_active),
#(store_faction_of_party, ":center_faction", "p_town_6"),
#(eq, ":center_faction", "fac_kingdom_6"),
  ],
  [
  
	(set_spawn_radius, 2),
(spawn_around_party, "p_town_34", "pt_crusade_army"),
(display_message,"@A Crusade army formed around Rome!!Target is Jerusalem.", 0xE633FF), 
(assign, ":spawned_party", reg0),
(try_begin),
(store_faction_of_party, ":center_faction", "p_town_6"),
(eq, ":center_faction", "fac_kingdom_1"),
(call_script, "script_party_set_ai_state", ":spawned_party", spai_patrolling_around_center, "p_town_6"),
(party_set_slot, ":spawned_party", slot_party_ai_object, "p_town_6"),
(party_set_slot, ":spawned_party", slot_party_ai_state, spai_patrolling_around_center),
(party_set_ai_behavior, ":spawned_party", ai_bhvr_patrol_location),
(party_set_ai_object, ":spawned_party", "p_town_6"),
(else_try),
(call_script, "script_party_set_ai_state", ":spawned_party", spai_patrolling_around_center, "p_town_6"),
(party_set_slot, ":spawned_party", slot_party_ai_object, "p_town_6"),
(party_set_slot, ":spawned_party", slot_party_ai_state, spai_patrolling_around_center),
(party_set_ai_behavior, ":spawned_party", ai_bhvr_attack_party),
(party_set_ai_object, ":spawned_party", "p_town_6"),
(try_end),

  ]),
   (120, 0, 1800, 
  [(store_faction_of_party, ":center_faction", "p_town_13"),
(eq, ":center_faction", "fac_kingdom_2"),
(faction_slot_eq, "fac_kingdom_4", slot_faction_state, sfs_active),
  ],
  [
  
	(set_spawn_radius, 2),
(spawn_around_party, "p_castle_10", "pt_hashasi_tebriz_ordusu"),
(display_message,"@A Assassins army formed around Elamut!!Target is Tebriz.", 0xE633FF), 

(assign, ":spawned_party", reg0),
(call_script, "script_party_set_ai_state", ":spawned_party", spai_patrolling_around_center, "p_town_13"),
(party_set_slot, ":spawned_party", slot_party_ai_object, "p_town_13"),
(party_set_slot, ":spawned_party", slot_party_ai_state, spai_patrolling_around_center),
(party_set_ai_behavior, ":spawned_party", ai_bhvr_attack_party),
(party_set_ai_object, ":spawned_party", "p_town_13"),
(call_script,"script_diplomacy_start_war_between_kingdoms", "fac_kingdom_4", "fac_kingdom_2",1),

  ]),
  
  
  (5.7, 0, 0.0, 
  [
    (store_num_parties_of_template, reg5, "pt_kipcak_women"),    
    (lt, reg5, 5),(faction_slot_eq, "fac_kingdom_10", slot_faction_state, sfs_active),
  ],
  [
    (set_spawn_radius, 5),
    (spawn_around_party, "p_town_27", "pt_kipcak_women"),
    (spawn_around_party, "p_town_28", "pt_kipcak_women"),
    (spawn_around_party, "p_village_134", "pt_kipcak_women"),
    (spawn_around_party, "p_village_130", "pt_kipcak_women"),
    (spawn_around_party, "p_village_131", "pt_kipcak_women"),
    
  ]),

  
  #(10, 0, ti_once, [], [(jump_to_menu,"mnu_istanbul_yendin")]),  #sonra kaldir

# (0.1, 0, 0, [], [(call_script, "script_randomly_start_war_peace_new", 1),]),
 #Kelle avcisi toplama
  (0.0, 0, 72.0, [], [(assign, "$asker_1", 1),(assign, "$asker_2", 1),(assign, "$asker_3", 1),(assign, "$asker_4", 1),]),
  (240.0, 0, 840.0, [(neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_empieza_asedio", 1),
(neq, "$g_player_icon_state", pis_ship),
(neq, "$g_player_is_captive", 1),], [(jump_to_menu,"mnu_kaybolmus_kiz"),(finish_mission),]),
  (24.0, 0, 24.0, [(eq,"$irz_dusman",3),(neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_empieza_asedio", 1),
(neq, "$g_player_icon_state", pis_ship),
(neq, "$g_player_is_captive", 1),], [(jump_to_menu,"mnu_ofkeli_kalabalik"),]),#(eq,"$irz_dusman",2)
  (24.0, 0, 260.0, [(store_num_parties_of_template,":parti_sayisi","pt_rastgele_koy"),(ge,":parti_sayisi", 10),], [(try_begin),(try_for_range, ":oyuncu_koyleri", villages_begin, villages_end),
	   (party_slot_eq, ":oyuncu_koyleri", slot_town_lord, "trp_player"),(jump_to_menu, "mnu_rastgele_koy_sayi_10"),(try_end)]),
  (24.0, 0, 260.0, [(store_num_parties_of_template,":parti_sayisi_2","pt_rastgele_fort"),(ge,":parti_sayisi_2", 10),], [(try_begin),(try_for_range, ":oyuncu_koyleri_2", towns_begin, towns_end),
	   (party_slot_eq, ":oyuncu_koyleri_2", slot_town_lord, "trp_player"),(jump_to_menu, "mnu_rastgele_fort_sayi_10"),(try_end)]),
  
  (24.0, 0, 900.0, [(eq,"$hisar_koy_ciksin", 1),(store_num_parties_of_template,":parti_sayisi_sabit","pt_rastgele_koy"),(lt,":parti_sayisi_sabit", 12),], [
(store_random_in_range, ":rastgele_koy", towns_begin, villages_end),(set_spawn_radius, 10),
    (spawn_around_party, ":rastgele_koy", "pt_rastgele_koy"),
	(store_random_in_range, ":rastgele_fort", castles_begin, castles_end),(set_spawn_radius, 10),
	(display_message,"@Desert soldiers build a fort.", 0xE633FF), 
    (spawn_around_party, ":rastgele_fort", "pt_rastgele_fort"),]),#(eq,"$irz_dusman",2)
##gunluk resetlenecek degerler
  (24.0, 0, 24.0, [], [(assign, "$han_konusma_1",1),(assign, "$han_konusma_2",1),(assign, "$han_konusma_3",1),(assign,"$duello_yapildi",1),(assign, "$lorda_kufur_edildi",1),
  (assign, "$parali_asker_alinabilir_1", 1),(assign, "$parali_asker_alinabilir_2", 1),(assign, "$parali_asker_alinabilir_3", 1),(assign, "$erzak_ordu_alindi",0),]),#(eq,"$irz_dusman",2)
  
  
  (6, 0, ti_once, [(eq,"$yil_gecsin",1)], [(jump_to_menu, "mnu_cocuk_buyudu"),(finish_mission)]),#(eq,"$irz_dusman",2)
  (72.0, 0, 72.0, [(eq, "$cocuk_erzak_al", 1),
(neq, "$g_player_is_captive", 1),], [(jump_to_menu, "mnu_cocuk_erzak_aldi"),(party_force_add_members, "p_main_party", "trp_cocuk_1",1),]),
  (72.0, 0, 72.0, [(eq, "$cocuk_asker_topla_gonderildi", 1),

(neq, "$g_player_is_captive", 1),], [(jump_to_menu, "mnu_cocuk_asker_topla"),(finish_mission)]),
#2 hafta
(336.0, 0, 840.0, [(neq, "$freelancer_state", 1),
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_empieza_asedio", 1),
(neq, "$g_player_icon_state", pis_ship),
(neq, "$g_player_is_captive", 1),(eq, "$player_has_homage", 1),], [(store_random_in_range, ":rastgele_olay", 0,2),(try_begin),(eq, ":rastgele_olay", 0),(jump_to_menu, "mnu_lord_oldun"),(try_end),]),

(336.0, 0, 840.0, [(neq, "$freelancer_state", 1),(eq, "$esirler_satilabilir",1),
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_empieza_asedio", 1),
(neq, "$g_player_icon_state", pis_ship),
(neq, "$g_player_is_captive", 1),], [(store_random_in_range, ":rastgele_olay", 0,2),(try_begin),(eq, ":rastgele_olay", 0),(jump_to_menu, "mnu_kole_avcilari_geldi"),(try_end),]),


(5, 0, 5, [(call_script, "script_get_troop_item_amount", "trp_player", "itm_byzantine_emperor_head1"),(assign, ":adet", reg0),(ge, ":adet", 1),(eq, "$esya_var", 0),
		], [
		(troop_raise_skill, "trp_player", "skl_leadership", 1),
		(display_message, "@Your leadership increased +1",0x06DEF6),(assign, "$esya_var", 1),
		]),
(5, 0, 5, [
         (call_script, "script_get_troop_item_amount", "trp_player", "itm_byzantine_emperor_head1"),(assign, ":adet", reg0),(lt, ":adet", 1),(eq, "$esya_var", 1),], [(troop_raise_skill, "trp_player", "skl_leadership", -1),
		 		(display_message, "@Your leadership decreased -1",0x06DEF6),(assign, "$esya_var", 0),
		 ]),
(5, 0, 5, [(call_script, "script_get_troop_item_amount", "trp_player", "itm_seljuk_sultan_circlet"),(assign, ":adet", reg0),(ge, ":adet", 1),(eq, "$esya_var_2", 0),
		], [
		(troop_raise_skill, "trp_player", "skl_leadership", 1),
		(display_message, "@Your leadership increased +1",0x06DEF6),(assign, "$esya_var_2", 1),
		]),
(5, 0, 5, [
         (call_script, "script_get_troop_item_amount", "trp_player", "itm_seljuk_sultan_circlet"),(assign, ":adet", reg0),(lt, ":adet", 1),(eq, "$esya_var_2", 1),], [(troop_raise_skill, "trp_player", "skl_leadership", -1),
		 		(display_message, "@Your leadership decreased -1",0x06DEF6),(assign, "$esya_var_2", 0),
		 ]),		 


  


# (0, 0, 1, [
#  (store_num_parties_destroyed_by_player,":avlanan_hayvan","pt_deer_herd"),
#  (gt, ":avlanan_hayvan", "$avlanan_hayvanlar1"),
#  ], 
#[(val_add,"$avlanan_hayvanlar1",1),
#]),
# (0, 0, 1, [
#  (store_num_parties_destroyed_by_player,":avlanan_hayvan","pt_deer_herd2"),
#  (gt, ":avlanan_hayvan", "$avlanan_hayvanlar2"),
#  ], 
#[(val_add,"$avlanan_hayvanlar2",1),
#]),
# (0, 0, 1, [
#  (store_num_parties_destroyed_by_player,":avlanan_hayvan","pt_boar_herd2"),
#  (gt, ":avlanan_hayvan", "$avlanan_hayvanlar3"),
#  ], 
#[(val_add,"$avlanan_hayvanlar3",1),
#]),
# (0, 0, 1, [
#  (store_num_parties_destroyed_by_player,":avlanan_hayvan","pt_boar_herd3"),
#  (gt, ":avlanan_hayvan", "$avlanan_hayvanlar4"),
#  ], 
#[(val_add,"$avlanan_hayvanlar4",1),
#]),
#(0, 0, 1, [
#  (store_num_parties_destroyed_by_player,":avlanan_hayvan","pt_sheep_herd"),
#  (gt, ":avlanan_hayvan", "$avlanan_hayvanlar5"),
#
#  ], 
#[(val_add,"$avlanan_hayvanlar5",1),]),
#(0, 0, 1, [
#  (val_add, reg5, "$avlanan_hayvanlar1"),
#(val_add, reg5, "$avlanan_hayvanlar2"),
#(val_add, reg5, "$avlanan_hayvanlar3"),
#(val_add, reg5, "$avlanan_hayvanlar4"),
#(val_add, reg5, "$avlanan_hayvanlar5"),
#(store_sub, reg1, reg5, "$ucunkatlari"),
#(eq, reg1, 1),
#(val_add,"$ucunkatlari",1),
#(jump_to_menu,"mnu_hayvan_avi"),
#  ], 
#[]),
  
  
  
  (72.0, 0, 0.0, [(party_get_slot, reg12, "$current_town", slot_center_has_academy),         (lt, reg12, 2), #this value is used later
], [(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),#add town garrisons
	 
         (store_random_in_range, ":added_troops", 4, 8),
         #(val_add, ":cur_troops", ":added_troops"),
         #(val_min, ":cur_troops", ":prosperity"),
         (party_set_slot, ":center_no", slot_center_has_academy, ":added_troops"),
      (try_end),(assign, "$oba_yagmalandi", 1),]),

	
 (0.1, 0, ti_once, [], [(try_for_range, ":npc", 0, active_npcs_end),
	    (this_or_next|eq, ":npc", "trp_player"),
		(is_between, ":npc", active_npcs_begin, active_npcs_end),
		
		(troop_set_slot, ":npc", slot_troop_guardian, -1),
		(troop_set_slot, ":npc", slot_troop_spouse, -1),
		(troop_set_slot, ":npc", slot_troop_betrothed, -1),
        (troop_set_slot, ":npc", slot_troop_prisoner_of_party, -1),		
        (troop_set_slot, ":npc", slot_lady_last_suitor, -1),		
        (troop_set_slot, ":npc", slot_troop_stance_on_faction_issue, -1),		
		
		(store_random_in_range, ":decision_seed", 0, 10000),
        (troop_set_slot, ":npc", slot_troop_set_decision_seed, ":decision_seed"),	#currently not used
        (troop_set_slot, ":npc", slot_troop_temp_decision_seed, ":decision_seed"),	#currently not used, holds for at least 24 hours			
	  (try_end),]),

  #(0.1, 0, ti_once, [(map_free,0)], [(dialog_box,"str_tutorial_map1")]),
    #(0.1, 0, 0, [(eq, "$culture_2",1),], [(call_script,"script_culture_2")]),
	    #(74, 0, 0, [], [(call_script,"script_player_faction_troops")]),
		
	#player lord troops
#	  (0, 0, 24, [], [
#	  #(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
#         
#           # (assign, ":faction", "$players_kingdom"),
#	  #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
#	#(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
#	#(troop_slot_eq, "$g_talk_troop", slot_troop_kingsupport_state, 0),
#	#(store_faction_of_troop, ":lord_faction", active_npcs_begin, active_npcs_end),
#	#(eq, ":troop_no", "fac_player_supporters_faction"),
#	(try_for_range, ":troop_no", heroes_begin, heroes_end),
#           (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
#           (store_troop_faction, ":troop_faction_no", ":troop_no"),
#		   (this_or_next|eq, "$players_kingdom", ":troop_faction_no"),
#           (eq, "fac_player_supporters_faction", ":troop_faction_no"),
#	(troop_set_slot, ":troop_no", slot_troop_original_faction, "fac_kingdom_11"), #player kingdom troops-custom troops
#	]),
	     (1, 0, 1, [(eq,"$ability",2)], [

                 (val_sub,"$iron","$ironnew"),
                 (val_sub,"$strike","$strikenew"),
                 (val_sub,"$draw","$drawnew"),
                 (val_sub,"$throw","$thrownew"),             

                 (troop_raise_skill,"trp_player","skl_ironflesh","$iron"),
                 (troop_raise_skill,"trp_player","skl_power_strike","$strike"),
                 (troop_raise_skill,"trp_player","skl_power_draw","$draw"),
                 (troop_raise_skill,"trp_player","skl_power_throw","$throw"),

#                 (troop_raise_attribute,"trp_player",0,-20),
                 (troop_raise_attribute,"trp_player",1,-5),                    

                 (display_message,"@Your rage dies down...",0x6495ed),
                 (call_script, "script_rage_exp_penalty"),       

                 (assign, "$ability", 1),

         ]),
		
(1, 0, 1, [(eq,"$ability",3)], [

                 (val_sub,"$athletics","$athleticsnew"),

                 (troop_raise_skill,"trp_player","skl_athletics","$athletics"),

                 (troop_raise_attribute,"trp_player",1,-15),                    

                 (display_message,"@You are out of breath... ",0x6495ed),
                 (call_script, "script_sprint_exp_penalty"),       

                 (assign, "$ability", 1),
         ]),      

      (1, 0, 1, [(eq,"$ability",4)], [

                 (val_mul,"$bonus",-1),

                (troop_raise_proficiency_linear,"trp_player",0,"$bonus"),
                (troop_raise_proficiency_linear,"trp_player",1,"$bonus"),
                (troop_raise_proficiency_linear,"trp_player",2,"$bonus"),
                (troop_raise_proficiency_linear,"trp_player",3,"$bonus"),
                (troop_raise_proficiency_linear,"trp_player",4,"$bonus"),
                (troop_raise_proficiency_linear,"trp_player",5,"$bonus"),           

                 (troop_raise_attribute,"trp_player",1,-5),                    

                 (display_message,"@Your lose your focus... ",0x6495ed),
                 (call_script, "script_focus_exp_penalty"),       

                 (assign, "$ability", 1),
         ]),      		 

	(0.1, 0, 0.0, [],
[(try_for_parties, ":cur_party"),
   (party_get_current_terrain, ":terrain", "p_main_party"),

   (eq, ":terrain", rt_bridge),
  (party_get_template_id, ":cur_party", "p_main_party"),
(eq, ":cur_party", "p_main_party"),	
    (assign, "$g_player_icon_state", pis_ship),
    (party_set_icon, ":cur_party", "icon_ship"),
 (try_end),
]),
(0.1, 0, 0.0, [],
[(try_for_parties, ":cur_party"),
   (party_get_current_terrain, ":terrain", "p_main_party"),
   (this_or_next|eq, ":terrain", rt_steppe),
   (this_or_next|eq, ":terrain", rt_plain),
   (this_or_next|eq, ":terrain", rt_snow),
   (this_or_next|eq, ":terrain", rt_desert),
   (this_or_next|eq, ":terrain", rt_steppe_forest),
     (this_or_next|eq, ":terrain", rt_forest),
   (this_or_next|eq, ":terrain", rt_snow_forest),
   (eq, ":terrain", rt_desert_forest),
  (party_get_template_id, ":cur_party", "p_main_party"),
(eq, ":cur_party", "p_main_party"),
 (try_begin),
  (troop_get_inventory_slot, ":cur_horse", "trp_player", 8),
 (try_begin),
 (assign,"$g_camp_mode", 1),
           (assign, "$g_infinite_camping", 0),
           (assign, "$g_player_icon_state", pis_camping),
		   (else_try),
  (ge, ":cur_horse", 0),
  (assign, "$g_player_icon_state", pis_normal),
  (party_set_icon, ":cur_party", "icon_player_horseman"), 
  (else_try),
  (assign, "$g_player_icon_state", pis_normal),
  (party_set_icon, ":cur_party", "icon_player"),
 (try_end),
]),

(0.1, 0, 0.0, [],
[(try_for_parties, ":cur_party"),
   (party_get_current_terrain, ":terrain", ":cur_party"),
   (eq, ":terrain", rt_bridge),
  (party_get_template_id, ":cur_template", ":cur_party"),
 (this_or_next|eq, ":cur_template", "pt_kingdom_hero_party"),
 (this_or_next|eq, ":cur_template", "pt_kingdom_caravan_party"),
 (this_or_next|eq, ":cur_template", "pt_manhunters"),
 (this_or_next|eq, ":cur_template", "pt_village_farmers"),
 (this_or_next|eq, ":cur_template", "pt_deserters"),
 (this_or_next|eq, ":cur_template", "pt_looters"),
 (this_or_next|eq, ":cur_template", "pt_forest_bandits"),
 (this_or_next|eq, ":cur_template", "pt_steppe_bandits"),
 (this_or_next|eq, ":cur_template", "pt_mountain_bandits"),
 (this_or_next|eq, ":cur_template", "pt_patrol_party"),
 (this_or_next|eq, ":cur_template", "pt_kipcak_gocebe"),
 (this_or_next|eq, ":cur_template", "pt_pechenegs"),
 (this_or_next|eq, ":cur_template", "pt_kayi_devriye"),
 (this_or_next|eq, ":cur_template", "pt_kayi_devriye_2"),
 (this_or_next|eq, ":cur_template", "pt_kirim_gocebe"),
 (this_or_next|eq, ":cur_template", "pt_turkmen_gocebe"),
 (this_or_next|eq, ":cur_template", "pt_koylu_isyani"),
 (this_or_next|eq, ":cur_template", "pt_desert_bandits"),
 (this_or_next|eq, ":cur_template", "pt_crusade_army"),
 (this_or_next|eq, ":cur_template", "pt_mongol_war_party"),
 (this_or_next|eq, ":cur_template", "pt_kipcak_women"),
 (this_or_next|eq, ":cur_template", "pt_pechenegs_army"),
 (eq, ":cur_template", "pt_sea_raiders"),
   (party_set_icon, ":cur_party", "icon_ship"),
 (try_end),
]),

#(0.1, 0, 0.0, [],
#[(try_for_parties, ":cur_party"),
#   (party_get_current_terrain, ":terrain", ":cur_party"),
#   (this_or_next|eq, ":terrain", rt_steppe),
#   (this_or_next|eq, ":terrain", rt_plain),
#   (this_or_next|eq, ":terrain", rt_snow),
#   (this_or_next|eq, ":terrain", rt_desert),
#   (this_or_next|eq, ":terrain", rt_steppe_forest),
#   (this_or_next|eq, ":terrain", rt_forest),
#   (this_or_next|eq, ":terrain", rt_snow_forest),
#   (eq, ":terrain", rt_desert_forest),
#  (party_get_template_id, ":cur_template", ":cur_party"),
#(eq, ":cur_template", "pt_patrol_party"),	
#   #(party_set_icon, ":cur_party", "icon_flagbearer_a"),
#   #(call_script, "script_patrol"),
# (try_end),
#]),
#
#(0.1, 0, 0.0, [],
#[(try_for_parties, ":cur_party"),
#   (party_get_current_terrain, ":terrain", ":cur_party"),
#   (this_or_next|eq, ":terrain", rt_steppe),
#   (this_or_next|eq, ":terrain", rt_plain),
#   (this_or_next|eq, ":terrain", rt_snow),
#   (this_or_next|eq, ":terrain", rt_desert),
#   (this_or_next|eq, ":terrain", rt_steppe_forest),
#   (this_or_next|eq, ":terrain", rt_forest),
#   (this_or_next|eq, ":terrain", rt_snow_forest),
#   (eq, ":terrain", rt_desert_forest),
#  (party_get_template_id, ":cur_template", ":cur_party"),
#(eq, ":cur_template", "pt_kingdom_hero_party"),	
#   #(party_set_icon, ":cur_party", "icon_flagbearer_a"),
#   #(call_script, "script_draw_icons"),
# (try_end),
#]),

#(0.1, 0, 0.0, [],
#[(try_for_parties, ":cur_party"),
#   (party_get_current_terrain, ":terrain", ":cur_party"),
#   (this_or_next|eq, ":terrain", rt_steppe),
#   (this_or_next|eq, ":terrain", rt_plain),
#   (this_or_next|eq, ":terrain", rt_snow),
#   (this_or_next|eq, ":terrain", rt_desert),
#   (this_or_next|eq, ":terrain", rt_steppe_forest),
#   (this_or_next|eq, ":terrain", rt_forest),
#   (this_or_next|eq, ":terrain", rt_snow_forest),
#   (eq, ":terrain", rt_desert_forest),
#  (party_get_template_id, ":cur_template", ":cur_party"),
#
#(eq, ":cur_template", "pt_kingdom_caravan_party"),	
#   (party_set_icon, ":cur_party", "icon_icon_kervan"),
# (try_end),
#]),

#(0.1, 0, 0.0, [],
#[(try_for_parties, ":cur_party"),
#   (party_get_current_terrain, ":terrain", ":cur_party"),
#   (this_or_next|eq, ":terrain", rt_steppe),
#   (this_or_next|eq, ":terrain", rt_plain),
#   (this_or_next|eq, ":terrain", rt_snow),
#   (this_or_next|eq, ":terrain", rt_desert),
#   (this_or_next|eq, ":terrain", rt_steppe_forest),
#   (this_or_next|eq, ":terrain", rt_forest),
#   (this_or_next|eq, ":terrain", rt_snow_forest),
#   (eq, ":terrain", rt_desert_forest),
#  (party_get_template_id, ":cur_template", ":cur_party"),
#(eq, ":cur_template", "pt_manhunters"),	
#   (party_set_icon, ":cur_party", "icon_gray_knight"),
# (try_end),
#]),

#(0.1, 0, 0.0, [],
#[(try_for_parties, ":cur_party"),
#   (party_get_current_terrain, ":terrain", ":cur_party"),
#   (this_or_next|eq, ":terrain", rt_steppe),
#   (this_or_next|eq, ":terrain", rt_plain),
#   (this_or_next|eq, ":terrain", rt_snow),
#   (this_or_next|eq, ":terrain", rt_desert),
#   (this_or_next|eq, ":terrain", rt_steppe_forest),
#   (this_or_next|eq, ":terrain", rt_forest),
#   (this_or_next|eq, ":terrain", rt_snow_forest),
#   (eq, ":terrain", rt_desert_forest),
#  (party_get_template_id, ":cur_template", ":cur_party"),
#  (this_or_next|eq, ":cur_template", "pt_kipcak_gocebe"),	
#  (this_or_next|eq, ":cur_template", "pt_kirim_gocebe"),	
#  (this_or_next|eq, ":cur_template", "pt_pechenegs"),	
#  (this_or_next|eq, ":cur_template", "pt_kayi_devriye"),	
#  (this_or_next|eq, ":cur_template", "pt_kayi_devriye_2"),	
#(eq, ":cur_template", "pt_turkmen_gocebe"),	
#   (party_set_icon, ":cur_party", "icon_icon_turk_patrol"),
# (try_end),
#]),

#(0.1, 0, 0.0, [],
#[(try_for_parties, ":cur_party"),
#   (party_get_current_terrain, ":terrain", ":cur_party"),
#   (this_or_next|eq, ":terrain", rt_steppe),
#   (this_or_next|eq, ":terrain", rt_plain),
#   (this_or_next|eq, ":terrain", rt_snow),
#   (this_or_next|eq, ":terrain", rt_desert),
#   (this_or_next|eq, ":terrain", rt_steppe_forest),
#   (this_or_next|eq, ":terrain", rt_forest),
#   (this_or_next|eq, ":terrain", rt_snow_forest),
#   (eq, ":terrain", rt_desert_forest),
#  (party_get_template_id, ":cur_template", ":cur_party"),
#    (this_or_next|eq, ":cur_template", "pt_koylu_isyani"),	
#
#(eq, ":cur_template", "pt_village_farmers"),	
#   (party_set_icon, ":cur_party", "icon_peasant"),
# (try_end),
#]),

(0.1, 0, 0.0, [],
[(try_for_parties, ":cur_party"),
   (party_get_current_terrain, ":terrain", ":cur_party"),
   (this_or_next|eq, ":terrain", rt_steppe),
   (this_or_next|eq, ":terrain", rt_plain),
   (this_or_next|eq, ":terrain", rt_snow),
   (this_or_next|eq, ":terrain", rt_desert),
   (this_or_next|eq, ":terrain", rt_steppe_forest),
   (this_or_next|eq, ":terrain", rt_forest),
   (this_or_next|eq, ":terrain", rt_snow_forest),
   (eq, ":terrain", rt_desert_forest),
  (party_get_template_id, ":cur_template", ":cur_party"),
  (try_begin),
(eq, ":cur_template", "pt_deserters"),	
   (party_set_icon, ":cur_party", "icon_vaegir_knight"),
   (try_end),
   (try_begin),
    (this_or_next|eq, ":cur_template", "pt_mongol_war_party"),	
    (this_or_next|eq, ":cur_template", "pt_kipcak_women"),	
   (eq, ":cur_template", "pt_pechenegs_army"),	
   (party_set_icon, ":cur_party", "icon_icon_mongol_patrol"),
   (try_end),
   (try_begin),
    (this_or_next|eq, ":cur_template", "pt_hacli_ordu"),	
   (eq, ":cur_template", "pt_crusade_army"),	
   (party_set_icon, ":cur_party", "icon_icon_crusader_patrol"),
   (try_end),
   
   (try_begin),
   (eq, ":cur_template", "pt_kingdom_caravan_party"),	
   (party_set_icon, ":cur_party", "icon_icon_kervan"),
   (try_end),
   (try_begin),
   (eq, ":cur_template", "pt_desert_bandits"),	
   (party_set_icon, ":cur_party", "icon_icon_desertbandit"),
   (try_end),
   (try_begin),
   (eq, ":cur_template", "pt_manhunters"),	
   (party_set_icon, ":cur_party", "icon_gray_knight"),
   (try_end),
   (try_begin),
   (this_or_next|eq, ":cur_template", "pt_kipcak_gocebe"),	
  (this_or_next|eq, ":cur_template", "pt_kirim_gocebe"),	
  (this_or_next|eq, ":cur_template", "pt_pechenegs"),	
  (this_or_next|eq, ":cur_template", "pt_kayi_devriye"),	
  (this_or_next|eq, ":cur_template", "pt_kayi_devriye_2"),	
(eq, ":cur_template", "pt_turkmen_gocebe"),	
   (party_set_icon, ":cur_party", "icon_icon_turk_patrol"),
   (try_end),
   (try_begin),
(this_or_next|eq, ":cur_template", "pt_koylu_isyani"),	
(eq, ":cur_template", "pt_village_farmers"),
(party_set_icon, ":cur_party", "icon_peasant"),
   (try_end),
   (try_begin),
   (eq, ":cur_template", "pt_looters"),	
   (party_set_icon, ":cur_party", "icon_icon_bandit"),
   (try_end),
   (try_begin),
   (eq, ":cur_template", "pt_steppe_bandits"),	
   (party_set_icon, ":cur_party", "icon_steppe_bandit"),
   (try_end),
   (try_begin),
(this_or_next|eq, ":cur_template", "pt_sea_raiders"),	
(this_or_next|eq, ":cur_template", "pt_forest_bandits"),	
(eq, ":cur_template", "pt_mountain_bandits"),   (party_set_icon, ":cur_party", "icon_axeman"),
   (try_end),
   
 (try_end),
]),

#(0.1, 0, 0.0, [],
#[(try_for_parties, ":cur_party"),
#   (party_get_current_terrain, ":terrain", ":cur_party"),
#   (this_or_next|eq, ":terrain", rt_steppe),
#   (this_or_next|eq, ":terrain", rt_plain),
#   (this_or_next|eq, ":terrain", rt_snow),
#   (this_or_next|eq, ":terrain", rt_desert),
#   (this_or_next|eq, ":terrain", rt_steppe_forest),
#   (this_or_next|eq, ":terrain", rt_forest),
#   (this_or_next|eq, ":terrain", rt_snow_forest),
#   (eq, ":terrain", rt_desert_forest),
#  (party_get_template_id, ":cur_template", ":cur_party"),
#(eq, ":cur_template", "pt_looters"),	
#   (party_set_icon, ":cur_party", "icon_icon_bandit"),
# (try_end),
#]),
#
#
#
#(0.1, 0, 0.0, [],
#[(try_for_parties, ":cur_party"),
#   (party_get_current_terrain, ":terrain", ":cur_party"),
#   (this_or_next|eq, ":terrain", rt_steppe),
#   (this_or_next|eq, ":terrain", rt_plain),
#   (this_or_next|eq, ":terrain", rt_snow),
#   (this_or_next|eq, ":terrain", rt_desert),
#   (this_or_next|eq, ":terrain", rt_steppe_forest),
#   (this_or_next|eq, ":terrain", rt_forest),
#   (this_or_next|eq, ":terrain", rt_snow_forest),
#   (eq, ":terrain", rt_desert_forest),
#  (party_get_template_id, ":cur_template", ":cur_party"),
#(eq, ":cur_template", "pt_steppe_bandits"),	
#   (party_set_icon, ":cur_party", "icon_steppe_bandit"),
# (try_end),
#]),
#
#(0.1, 0, 0.0, [],
#[(try_for_parties, ":cur_party"),
#   (party_get_current_terrain, ":terrain", ":cur_party"),
#   (this_or_next|eq, ":terrain", rt_steppe),
#   (this_or_next|eq, ":terrain", rt_plain),
#   (this_or_next|eq, ":terrain", rt_snow),
#   (this_or_next|eq, ":terrain", rt_desert),
#   (this_or_next|eq, ":terrain", rt_steppe_forest),
#   (this_or_next|eq, ":terrain", rt_forest),
#   (this_or_next|eq, ":terrain", rt_snow_forest),
#   (eq, ":terrain", rt_desert_forest),
#  (party_get_template_id, ":cur_template", ":cur_party"),
#(this_or_next|eq, ":cur_template", "pt_sea_raiders"),	
#(this_or_next|eq, ":cur_template", "pt_forest_bandits"),	
#(eq, ":cur_template", "pt_mountain_bandits"),	
#   (party_set_icon, ":cur_party", "icon_axeman"),
# (try_end),
#]),


	
	
	
	
	
	
	
	
	
	
	
	


  #Haritada rastgele gerceklesen olaylar
  #(480, 0, 480, [], [(jump_to_menu,"mnu_olay_1"),(assign, "$olay_basladi", 1)]),
  #(240, 0, 480, [(eq, "$olay_basladi", 1)], [(jump_to_menu,"mnu_olay_2"),(assign, "$olay_basladi2", 1)]),
  #(360, 0, 480, [(eq, "$olay_basladi2", 1)], [(jump_to_menu,"mnu_olay_3")]),
  #Koylu isyani icin  
  #(store_num_parties_destroyed_by_player,":koylu_isyani","pt_koylu_isyani"),(ge, ":koylu_isyani", 1)
  (0, 0, 1, [(store_num_parties_destroyed_by_player,":koylu_isyani","pt_koylu_isyani"),(ge, ":koylu_isyani", "$son_asi")], [
	  (display_message,"@You destroyed 1 rebel villager party!!",0x3AD00D),(troop_add_gold,"trp_player",2000),(val_add,"$son_asi",1),
      ]),
	  
	  (0, 0, ti_once, [], [
	  (troop_remove_gold,"trp_player",2000),
      ]),
  (1200, 0, 1200, [
      (store_num_parties_of_template, reg2, "pt_koylu_isyani"),    
    (lt, reg2, 25)
    ], [(jump_to_menu,"mnu_koylu_isyani"),
        
        (set_spawn_radius, 1),
        (spawn_around_party, "p_town_1", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_2", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_3", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_4", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_5", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_6", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_7", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_8", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_9", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_10", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_11", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_12", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_13", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_14", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_15", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_16", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_17", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_19", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_20", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_21", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_22", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_23", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_24", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_25", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_26", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_27", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_28", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_29", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_30", "pt_koylu_isyani"),
		(set_spawn_radius, 1),
        (spawn_around_party, "p_town_31", "pt_koylu_isyani"),
		
    ]),
  
  #Han,altin madeni,bugday tarlasi kira geliri  (dialog_box,"str_tutorial_map1")
  (168.0, 0, 168.0, [(eq, "$han_alindi", 1),], [(troop_add_gold,"trp_player",1500),(display_message,"@You collected tavern rents!!!",0x3AD00D),]),
  (672.0, 0, 1200.0, [(eq, "$han_alindi", 1),], [(store_random_in_range, ":rastgele_olay", 0,2),(try_begin),(eq, ":rastgele_olay", 1),(dialog_box,"str_han_icin_sarap_lazim"),(assign, "$han_alindi", 0),(assign, "$han_icin_sarap", 1),(try_end),]),
  (24.0, 0, 24.0, [(eq, "$han_icin_sarap", 1),], [(display_message,"@Caravanserai Innkeeper wanted 5 barrel of wines from you!",0x3AD00D),]),
  (168.0, 0, 168.0, [(eq, "$at_ciftligi_alindi", 1),], [(troop_add_gold,"trp_player",750),(troop_add_item, "trp_player","itm_courser",imod_spirited),(display_message,"@Horse farm yields have collected and a horse has breeded!!",0x3AD00D),]),
  (672.0, 0, 1200.0, [(eq, "$at_ciftligi_alindi", 1),], [(store_random_in_range, ":rastgele_olay", 0,2),(try_begin),(eq, ":rastgele_olay", 1),(jump_to_menu,"mnu_at_ciftlig_sorun"),(try_end),]),

  (168.0, 0, 168.0, [(eq, "$altin_madeni_alindi", 1),], [(troop_add_gold,"trp_player",2500),(troop_add_item, "trp_player","itm_silver_item"),(display_message,"@Gold mine yields have collected and your men have exchanged gold to ingot!",0x3AD00D),]),
  (672.0, 0, 672.0, [(eq, "$altin_madeni_alindi", 1),], [(store_random_in_range, ":rastgele_olay", 0,2),(try_begin),(eq, ":rastgele_olay", 1),(dialog_box,"str_maden_icin_alet"),(assign, "$altin_madeni_alindi", 0),(assign, "$maden_icin_aletler", 1),(try_end),]),
  (24.0, 0, 24.0, [(eq, "$maden_icin_aletler", 1),], [(display_message,"@For mine camp 5 tools necessary!",0x3AD00D),]),
  (168.0, 0, 168.0, [(eq, "$bugday_tarlasi_alindi", 1),], [(troop_add_gold,"trp_player",1300),(troop_add_items, "trp_player","itm_grain",5),(display_message,"@Wheat field yields and crops have collected!!!",0x3AD00D),]),
  (672.0, 0, 1200.0, [(eq, "$bugday_tarlasi_alindi", 1),], [(store_random_in_range, ":rastgele_olay", 0,2),(try_begin),(eq, ":rastgele_olay", 1),(dialog_box,"str_tarla_boga_lazim"),(assign, "$bugday_tarlasi_alindi", 0),(assign, "$tarla_boga_lazim", 1),(try_end),]),
  (24.0, 0, 24.0, [(eq, "$tarla_boga_lazim", 1),], [(display_message,"@You must take away a bull to caravanserai which nears in Ankara to plough ti farm!",0x3AD00D),]),

# Refresh Merchants
  (0, 0, 24.0, [],
  [    
    (call_script, "script_refresh_center_inventories"),(party_set_ai_behavior, "pt_kayi_devriye", ai_bhvr_patrol_location),
        (party_set_ai_object,"pt_kayi_devriye", "p_kayi_obasi"),(party_set_ai_behavior, "pt_kayi_devriye_2", ai_bhvr_patrol_location),
        (party_set_ai_object,"pt_kayi_devriye_2", "p_kayi_obasi"),
  ]),
# (0, 0, 0, [],
# [    
# (party_set_slot, "pt_kayi_devriye", slot_party_type, spt_patrol),
#            (try_for_parties, ":party"),
#            (party_slot_eq, ":party", slot_party_type, spt_patrol),
#            (call_script, "script_party_set_ai_state", ":party", spai_besieging_center, "p_town_5"),
#            (call_script, "script_party_set_ai_state", "pt_kayi_devriye", spai_accompanying_army, ":party"),
#            (try_end),
# 
#   
# ]),

# Refresh Armor sellers
  (0.0, 0, 168.0, [],
  [    
    (call_script, "script_refresh_center_armories"),
	(call_script, "script_cf_kervan_ticaret"),
  ]),

# Refresh Weapon sellers
  (0.0, 0, 168.0, [],
  [
    (call_script, "script_refresh_center_weaponsmiths"),
	(call_script, "script_tuccar"),
	(call_script, "script_cf_kasap"),
	(call_script, "script_cf_erzakci"),
	(call_script, "script_cf_kumasci"),
	(call_script, "script_cf_baharatci"),
	
	
  ]),

# Refresh Horse sellers
  (0.0, 0, 168.0, [],
  [
    (call_script, "script_refresh_center_stables"),
	(call_script, "script_refresh_booksellers"),
	(call_script, "script_refresh_yayci"),
	(call_script, "script_refresh_migferci"),
	(call_script, "script_refresh_eldivenci"),
	(call_script, "script_refresh_arbeletci"),
  ]),
  

#############

#Captivity:

#  (1.0, 0, 0.0, [],
#   [
#       (ge,"$captivity_mode",1),
#       (store_current_hours,reg(1)),
#       (val_sub,reg(1),"$captivity_end_time"),
#       (ge,reg(1),0),
#       (display_message,"str_nobleman_reached_destination"),
#       (jump_to_menu,"$captivity_end_menu"),
#    ]),


  (5.7, 0, 0.0, 
  [
    (store_num_parties_of_template, reg2, "pt_manhunters"),    
    (lt, reg2, 4)
  ],
  [
    (set_spawn_radius, 1),
    (store_add, ":p_town_22_plus_one", "p_town_22", 1),
    (store_random_in_range, ":selected_town", "p_town_1", ":p_town_22_plus_one"),
    (spawn_around_party, ":selected_town", "pt_manhunters"),
  ]),



  (1.0, 0.0, 0.0, [
  (check_quest_active, "qst_track_down_bandits"),
  (neg|check_quest_failed, "qst_track_down_bandits"),
  (neg|check_quest_succeeded, "qst_track_down_bandits"),
  
  ],
   [
    (quest_get_slot, ":bandit_party", "qst_track_down_bandits", slot_quest_target_party),
	(try_begin),
		(party_is_active, ":bandit_party"),
		(store_faction_of_party, ":bandit_party_faction", ":bandit_party"),
		(neg|is_between, ":bandit_party_faction", kingdoms_begin, kingdoms_end), #ie, the party has not respawned as a non-bandit
		
		
		(assign, ":spot_range", 8),
		(try_begin),
			(is_currently_night),
			(assign, ":spot_range", 5),
		(try_end),
		
		(try_for_parties, ":party"),
			(gt, ":party", "p_spawn_points_end"),
			
			(store_faction_of_party, ":faction", ":party"),
			(is_between, ":faction", kingdoms_begin, kingdoms_end),
			
			
			(store_distance_to_party_from_party, ":distance", ":party", ":bandit_party"),
			(lt, ":distance", ":spot_range"),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_party_name, s4, ":party"),
				(display_message, "@{!}DEBUG -- Wanted bandits spotted by {s4}"),
			(try_end),
			
			(call_script, "script_get_closest_center", ":bandit_party"),
			(assign, ":nearest_center", reg0),
#			(try_begin),
#				(get_party_ai_current_behavior, ":behavior", ":party"),
#				(eq, ":behavior", ai_bhvr_attack_party),
#				(call_script, "script_add_log_entry",  logent_party_chases_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
#				(eq, ":behavior", ai_bhvr_avoid_party),
#				(call_script, "script_add_log_entry",  logent_party_runs_from_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
			(call_script, "script_add_log_entry",  logent_party_spots_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(try_end),
		(try_end),
	(else_try), #Party not found
		(display_message, "str_bandits_eliminated_by_another"),
        (call_script, "script_abort_quest", "qst_track_down_bandits", 0),
	(try_end),
   ]),


#Tax Collectors
# Prisoner Trains
#  (4.1, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_prisoner_train"),
#                         (assign, "$pin_limit", peak_prisoner_trains),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),
#
#  (4.1, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_prisoner_train"),
#                         (assign, "$pin_limit", peak_prisoner_trains),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_prisoner_train_party"),
               (party_is_in_any_town,reg(2)),
               ],
              [(store_faction_of_party, ":faction_no", reg(2)),
               (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
               (party_set_ai_object,reg(2),reg0),
               (party_set_flags, reg(2), pf_default_behavior, 0),
            ]),

##Caravans
#  (4.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_caravan"),
#                         (assign, "$pin_limit", peak_kingdom_caravans),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

#  (4.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_caravan"),
#                         (assign, "$pin_limit", peak_kingdom_caravans),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

##  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_kingdom_caravan_party"),
##               (party_is_in_any_town,reg(2)),
##               ],
##              [(store_faction_of_party, ":faction_no", reg(2)),
##               (call_script,"script_cf_select_random_town_with_faction", ":faction_no"),
##               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
##               (party_set_ai_object,reg(2),reg0),
##               (party_set_flags, reg(2), pf_default_behavior, 0),
##            ]),
  
  (4.0, 0, 0.0,
   [
     (eq, "$caravan_escort_state", 1), #cancel caravan_escort_state if caravan leaves the destination
     (assign, ":continue", 0),
     (try_begin),
       (neg|party_is_active, "$caravan_escort_party_id"),
       (assign, ":continue", 1),
     (else_try),
       (get_party_ai_object, ":ai_object", "$caravan_escort_party_id"),
       (neq, ":ai_object", "$caravan_escort_destination_town"),
       (assign, ":continue", 1),
     (try_end),
     (eq, ":continue", 1),
     ],
   [
     (assign, "$caravan_escort_state", 0),
     ]),

#Messengers
#  (4.2, 0, 0.0, [],
#   [(assign, "$pin_faction", "fac_swadians"),
#    (assign, "$pin_party_template", "pt_swadian_messenger"),
#    (assign, "$pin_limit", peak_kingdom_messengers),
#    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#    (party_set_ai_object,"$pout_party","$pout_town"),
#    ]),

#  (4.2, 0, 0.0, [],
#   [(assign, "$pin_faction", "fac_vaegirs"),
#    (assign, "$pin_party_template", "pt_vaegir_messenger"),
#    (assign, "$pin_limit", peak_kingdom_caravans),
#    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#    (party_set_ai_object,"$pout_party","$pout_town"),
#    ]),

  (1.5, 0, 0, [(store_random_party_of_template, reg(2), "pt_messenger_party"),
               (party_is_in_any_town,reg(2)),
               ],
   [(store_faction_of_party, ":faction_no", reg(2)),
    (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
    (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
    (party_set_ai_object,reg(2),reg0),
    (party_set_flags, reg(2), pf_default_behavior, 0),
    ]),
  
  

#Deserters

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_deserters"),
#                         (assign, "$pin_limit", 4),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),
  
#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_deserters"),
#                         (assign, "$pin_limit", 4),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#Kingdom Parties
  (1.0, 0, 0.0, [],
   [(try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
##      (neq, ":cur_kingdom", "fac_player_supporters_faction"),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_forager),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_scout),
##      (try_end),
      (try_begin),
       (store_random_in_range, ":random_no", 0, 100),
      (lt, ":random_no", 10),
       (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_patrol),
     (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_messenger),
##      (try_end),
      (try_begin),
        (store_random_in_range, ":random_no", 0, 100),
        (lt, ":random_no", 10),
        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_kingdom_caravan),
      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_prisoner_train),
##      (try_end),
    (try_end),
    ]),


#Swadians
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_foragers",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_scouts",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_harassers",3)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_war_parties",2)]),


#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_foragers"),
#                         (assign, "$pin_limit", "$peak_swadian_foragers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_scouts"),
#                         (assign, "$pin_limit", "$peak_swadian_scouts"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_patrol"),
#                         (assign, "$pin_limit", "$peak_swadian_harassers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_war_party"),
#                         (assign, "$pin_limit", "$peak_swadian_war_parties"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),
#Vaegirs
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_foragers",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_scouts",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_harassers",3)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_war_parties",2)]),
  

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_foragers"),
#                         (assign, "$pin_limit", "$peak_vaegir_foragers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_scouts"),
#                         (assign, "$pin_limit", "$peak_vaegir_scouts"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_patrol"),
#                         (assign, "$pin_limit", "$peak_vaegir_harassers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_war_party"),
#                         (assign, "$pin_limit", "$peak_vaegir_war_parties"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#Villains etc.
#  (14.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_sea_raiders"),
#                         (assign, "$pin_party_template", "pt_sea_raiders"),
#                         (assign, "$pin_limit", 5),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),


#
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_refugees"),
##                         (assign, "$pin_limit", 5),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),
##
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_farmers"),
##                         (assign, "$pin_limit", 6),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),

#  [1.0, 96.0, ti_once, [], [[assign,"$peak_dark_hunters",3]]],
  
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_dark_hunters"),
##                         (assign, "$pin_limit", "$peak_dark_hunters"),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),

#Companion quests

##  (0, 0, ti_once,
##   [
##       (entering_town,"p_town_1"),
##       (main_party_has_troop,"trp_borcha"),
##       (eq,"$borcha_freed",0)
##    ],
##   
##   [
##       (assign,"$borcha_arrive_sargoth_as_prisoner", 1),
##       (start_map_conversation, "trp_borcha", -1)
##    ]
##   ),
##
##  (1, 0, ti_once,
##   [
##      (map_free,0),
##      (eq,"$borcha_asked_for_freedom",0),
##      (main_party_has_troop,"trp_borcha")
##    ],
##   [
##       (start_map_conversation, "trp_borcha", -1)
##    ]
##   ),
##  
##  (2, 0, ti_once,
##   [
##      (map_free, 0),
##      (neq,"$borcha_asked_for_freedom",0),
##      (eq,"$borcha_freed",0),
##      (main_party_has_troop,"trp_borcha")
##    ],
##   [
##       (start_map_conversation, "trp_borcha", -1),
##    ]
##   ),

##### TODO: QUESTS COMMENT OUT BEGIN

###########################################################################
### Random Governer Quest triggers
###########################################################################

# Incriminate Loyal Advisor quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_incriminate_loyal_commander"),
       (neg|check_quest_concluded, "qst_incriminate_loyal_commander"),
       (quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_current_state, 2),
       (quest_get_slot, ":quest_target_center", "qst_incriminate_loyal_commander", slot_quest_target_center),
       (quest_get_slot, ":quest_target_party", "qst_incriminate_loyal_commander", slot_quest_target_party),
       (try_begin),
         (neg|party_is_active, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (call_script, "script_fail_quest", "qst_incriminate_loyal_commander"),
       (else_try),
         (party_is_in_town, ":quest_target_party", ":quest_target_center"),
         (remove_party, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (quest_get_slot, ":quest_object_troop", "qst_incriminate_loyal_commander", slot_quest_object_troop),
         (assign, ":num_available_factions", 0),
         (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
           (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
           (neq, ":faction_no", "fac_player_supporters_faction"),
           (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
           (val_add, ":num_available_factions", 1),
         (try_end),
         (try_begin),
           (gt, ":num_available_factions", 0),
           (store_random_in_range, ":random_faction", 0, ":num_available_factions"),
           (assign, ":target_faction", -1),
           (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
             (eq, ":target_faction", -1),
             (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
             (neq, ":faction_no", "fac_player_supporters_faction"),
             (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
             (val_sub, ":random_faction", 1),
             (lt, ":random_faction", 0),
             (assign, ":target_faction", ":faction_no"),
           (try_end),
         (try_end),
         (try_begin),
           (gt, ":target_faction", 0),
           (call_script, "script_change_troop_faction", ":quest_object_troop", ":target_faction"),
         (else_try),
           (call_script, "script_change_troop_faction", ":quest_object_troop", "fac_robber_knights"),
         (try_end),
         (call_script, "script_succeed_quest", "qst_incriminate_loyal_commander"),
       (try_end),
    ],
   []
   ),
# Runaway Peasants quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_bring_back_runaway_serfs"),
       (neg|check_quest_concluded, "qst_bring_back_runaway_serfs"),
       (quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
       (quest_get_slot, ":quest_target_center", "qst_bring_back_runaway_serfs", slot_quest_target_center),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_1"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_1"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_2"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_2"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_3"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_3"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
         (try_end),
       (try_end),
       (assign, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_returned"),
       (val_add, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_fleed"),
       (ge, ":sum_removed", 3),
       (try_begin),
         (ge, "$qst_bring_back_runaway_serfs_num_parties_returned", 3),
         (call_script, "script_succeed_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (eq, "$qst_bring_back_runaway_serfs_num_parties_returned", 0),
         (call_script, "script_fail_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (call_script, "script_conclude_quest", "qst_bring_back_runaway_serfs"),
       (try_end),
    ],
   []
   ),
### Defend Nobles Against Peasants quest
##  (0.2, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_defend_nobles_against_peasants"),
##       (neg|check_quest_succeeded, "qst_defend_nobles_against_peasants"),
##       (neg|check_quest_failed, "qst_defend_nobles_against_peasants"),
##       (quest_get_slot, ":quest_target_center", "qst_defend_nobles_against_peasants", slot_quest_target_center),
##       (assign, ":num_active_parties", 0),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_1", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_1", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_2", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_2", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_3", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_3", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_4", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_4", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_5", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_5", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_6", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_6", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_7", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_7", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_8", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_8", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (eq, ":num_active_parties", 0),
##       (try_begin),
##         (store_div, ":limit", "$qst_defend_nobles_against_peasants_num_nobles_to_save", 2),
##         (ge, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":limit"),
##         (call_script, "script_succeed_quest", "qst_defend_nobles_against_peasants"),
##       (else_try),
##         (call_script, "script_fail_quest", "qst_defend_nobles_against_peasants"),
##       (try_end),
##    ],
##   []
##   ),
### Capture Conspirators quest
##  (0.15, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_capture_conspirators"),
##       (neg|check_quest_succeeded, "qst_capture_conspirators"),
##       (neg|check_quest_failed, "qst_capture_conspirators"),
##       (quest_get_slot, ":quest_target_center", "qst_capture_conspirators", slot_quest_target_center),
##       (quest_get_slot, ":faction_no", "qst_capture_conspirators", slot_quest_target_faction),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_num_parties_to_spawn", "$qst_capture_conspirators_num_parties_spawned"),
##         (store_random_in_range, ":random_no", 0, 100),
##         (lt, ":random_no", 20),
##         (set_spawn_radius, 3),
##         (spawn_around_party,":quest_target_center","pt_conspirator"),
##         (val_add, "$qst_capture_conspirators_num_parties_spawned", 1),
##         (party_get_num_companions, ":num_companions", reg0),
##         (val_add, "$qst_capture_conspirators_num_troops_to_capture", ":num_companions"),
##         (party_set_ai_behavior, reg0, ai_bhvr_travel_to_party),
##         (party_set_ai_object, reg0, "$qst_capture_conspirators_party_1"),
##         (party_set_flags, reg0, pf_default_behavior, 0),
##         (try_begin),
##           (le, "$qst_capture_conspirators_party_2", 0),
##           (assign, "$qst_capture_conspirators_party_2", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_3", 0),
##           (assign, "$qst_capture_conspirators_party_3", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_4", 0),
##           (assign, "$qst_capture_conspirators_party_4", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_5", 0),
##           (assign, "$qst_capture_conspirators_party_5", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_6", 0),
##           (assign, "$qst_capture_conspirators_party_6", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_7", 0),
##           (assign, "$qst_capture_conspirators_party_7", reg0),
##         (try_end),
##       (try_end),
##
##       (assign, ":num_active_parties", 0),
##
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_1", 0),
##         (party_is_active, "$qst_capture_conspirators_party_1"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_1"),
##           (remove_party, "$qst_capture_conspirators_party_1"),
##         (else_try),
##           (party_get_num_attached_parties, ":num_attachments", "$qst_capture_conspirators_party_1"),
##           (gt, ":num_attachments", 0),
##           (assign, ":leave_meeting", 0),
##           (try_begin),
##             (store_sub, ":required_attachments", "$qst_capture_conspirators_num_parties_to_spawn", 1),
##             (eq, ":num_attachments", ":required_attachments"),
##             (val_add, "$qst_capture_conspirators_leave_meeting_counter", 1),
##             (ge, "$qst_capture_conspirators_leave_meeting_counter", 15),
##             (assign, ":leave_meeting", 1),
##           (try_end),
##           (try_begin),
##             (eq, "$qst_capture_conspirators_num_parties_to_spawn", "$qst_capture_conspirators_num_parties_spawned"),
##             (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_capture_conspirators_party_1"),
##             (assign, ":min_distance", 3),
##             (try_begin),
##               (is_currently_night),
##               (assign, ":min_distance", 2),
##             (try_end),
##             (lt, ":cur_distance", ":min_distance"),
##             (assign, "$qst_capture_conspirators_leave_meeting_counter", 15),
##             (assign, ":leave_meeting", 1),
##           (try_end),
##           (eq, ":leave_meeting", 1),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_1", ai_bhvr_travel_to_point),
##           (party_set_flags, "$qst_capture_conspirators_party_1", pf_default_behavior, 0),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_1"),
##           (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##           (party_set_ai_target_position, "$qst_capture_conspirators_party_1", pos2),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_2", 0),
##             (party_detach, "$qst_capture_conspirators_party_2"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_2", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_3", 0),
##             (party_detach, "$qst_capture_conspirators_party_3"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_3", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_4", 0),
##             (party_detach, "$qst_capture_conspirators_party_4"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_4", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_5", 0),
##             (party_detach, "$qst_capture_conspirators_party_5"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_5", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_6", 0),
##             (party_detach, "$qst_capture_conspirators_party_6"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_6", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_7", 0),
##             (party_detach, "$qst_capture_conspirators_party_7"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_7", pos2),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_1"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_1"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_1"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_1", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_1", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_1", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_1", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_2", 0),
##         (party_is_active, "$qst_capture_conspirators_party_2"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_2"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_2", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_2"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_2"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_hold),
##             (party_attach_to_party, "$qst_capture_conspirators_party_2", "$qst_capture_conspirators_party_1"),
##             (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_2"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_2"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_2"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_2", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_2", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_3", 0),
##         (party_is_active, "$qst_capture_conspirators_party_3"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_3"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_3", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_3"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_3"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_hold),
##             (party_attach_to_party, "$qst_capture_conspirators_party_3", "$qst_capture_conspirators_party_1"),
##             (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_3"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_3"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_3"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_3", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_3", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_4", 0),
##         (party_is_active, "$qst_capture_conspirators_party_4"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_4"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_4", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_4"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_4"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_4", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_4"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_4"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_4"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_4", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_4", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_5", 0),
##         (party_is_active, "$qst_capture_conspirators_party_5"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_5"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_5", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_5"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_5"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_5", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_5"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_5"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_5"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_5", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_5", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_6", 0),
##         (party_is_active, "$qst_capture_conspirators_party_6"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_6"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_6", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_6"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_6"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_6", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_6"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_6"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_6"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_6", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_6", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_7", 0),
##         (party_is_active, "$qst_capture_conspirators_party_7"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_7"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_7", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_7"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_7"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_7", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_7"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_7"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_7"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_7", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_7", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##
##       (eq, ":num_active_parties", 0),
##       (party_count_prisoners_of_type, ":count_captured_conspirators", "p_main_party", "trp_conspirator"),
##       (party_count_prisoners_of_type, ":count_captured_conspirator_leaders", "p_main_party", "trp_conspirator_leader"),
##       (val_add, ":count_captured_conspirators", ":count_captured_conspirator_leaders"),
##       (try_begin),
##         (store_div, ":limit", "$qst_capture_conspirators_num_troops_to_capture", 2),
##         (gt, ":count_captured_conspirators", ":limit"),
##         (call_script, "script_succeed_quest", "qst_capture_conspirators"),
##       (else_try),
##         (call_script, "script_fail_quest", "qst_capture_conspirators"),
##       (try_end),
##    ],
##   []
##   ),
# Follow Spy quest
  (0.5, 0.0, 0.0,
   [
       (check_quest_active, "qst_follow_spy"),
       (eq, "$qst_follow_spy_no_active_parties", 0),
       (quest_get_slot, ":quest_giver_center", "qst_follow_spy", slot_quest_giver_center),
       (quest_get_slot, ":quest_object_center", "qst_follow_spy", slot_quest_object_center),
       (assign, ":abort_meeting", 0),
       (try_begin),
         (this_or_next|ge, "$qst_follow_spy_run_away", 2),
         (this_or_next|neg|party_is_active, "$qst_follow_spy_spy_party"),
         (neg|party_is_active, "$qst_follow_spy_spy_partners_party"),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 0),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_party"),
         (try_begin),
           (assign, ":min_distance", 3),
           (try_begin),
             (is_currently_night),
             (assign, ":min_distance", 1),
           (try_end),
           (le, ":cur_distance", ":min_distance"),
           (store_distance_to_party_from_party, ":player_distance_to_quest_giver_center", "p_main_party", ":quest_giver_center"),
           (gt, ":player_distance_to_quest_giver_center", 1),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "$qst_follow_spy_spy_partners_party", "$qst_follow_spy_spy_party"),
           (le, ":cur_distance", 1),
           (party_attach_to_party, "$qst_follow_spy_spy_party", "$qst_follow_spy_spy_partners_party"),
           (assign, "$qst_follow_spy_meeting_state", 1),
           (assign, "$qst_follow_spy_meeting_counter", 0),
         (try_end),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 1),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_partners_party"),
         (try_begin),
           (le, ":cur_distance", 1),
           (party_detach, "$qst_follow_spy_spy_party"),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (val_add, "$qst_follow_spy_meeting_counter", 1),
           (gt, "$qst_follow_spy_meeting_counter", 4),
           (party_detach, "$qst_follow_spy_spy_party"),
           (assign, ":abort_meeting", 1),
           (assign, "$qst_follow_spy_meeting_state", 2),
         (try_end),
       (try_end),
       (try_begin),
         (eq, ":abort_meeting", 1),
         (party_set_ai_object, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         
         (party_set_ai_object, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         
         (party_set_ai_behavior, "$qst_follow_spy_spy_party", ai_bhvr_travel_to_party),
         (party_set_ai_behavior, "$qst_follow_spy_spy_partners_party", ai_bhvr_travel_to_party),
         (party_set_flags, "$qst_follow_spy_spy_party", pf_default_behavior, 0),
         (party_set_flags, "$qst_follow_spy_spy_partners_party", pf_default_behavior, 0),
       (try_end),
       (assign, ":num_active", 0),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         (remove_party, "$qst_follow_spy_spy_party"),
         (assign, "$qst_follow_spy_spy_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_partners_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         (remove_party, "$qst_follow_spy_spy_partners_party"),
         (assign, "$qst_follow_spy_partner_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (eq, "$qst_follow_spy_partner_back_in_town",1),
         (eq, "$qst_follow_spy_spy_back_in_town",1),
         (call_script, "script_fail_quest", "qst_follow_spy"),
       (try_end),
       (try_begin),
         (eq, ":num_active", 0),
         (assign, "$qst_follow_spy_no_active_parties", 1),
         (party_count_prisoners_of_type, ":num_spies", "p_main_party", "trp_spy"),
         (party_count_prisoners_of_type, ":num_spy_partners", "p_main_party", "trp_spy_partner"),
         (gt, ":num_spies", 0),
         (gt, ":num_spy_partners", 0),
         (call_script, "script_succeed_quest", "qst_follow_spy"),
       (try_end),
    ],
   []
   ),
### Raiders quest
##  (0.95, 0.0, 0.2,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##    ],
##   [
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
##    ]
##   ),
##
##  (0.7, 0, 0.2,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##    ],
##   [
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (party_set_ai_behavior,":quest_target_party",ai_bhvr_travel_to_party),
##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
##    ]
##   ),
##  
##  (0.1, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (neg|party_is_active, ":quest_target_party")
##    ],
##   [
##       (call_script, "script_succeed_quest", "qst_hunt_down_raiders"),
##    ]
##   ),
##  
##  (1.3, 0, 0.0,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (quest_get_slot, ":quest_target_center", "qst_hunt_down_raiders", slot_quest_target_center),
##       (party_is_in_town,":quest_target_party",":quest_target_center")
##    ],
##   [
##       (call_script, "script_fail_quest", "qst_hunt_down_raiders"),
##       (display_message, "str_raiders_reached_base"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (remove_party, ":quest_target_party"),
##    ]
##   ),

##### TODO: QUESTS COMMENT OUT END

#########################################################################
# Random MERCHANT quest triggers
####################################  
 # Apply interest to merchants guild debt  1% per week
  (24.0 * 7, 0.0, 0.0,
   [],
   [
       (val_mul,"$debt_to_merchants_guild",101),
       (val_div,"$debt_to_merchants_guild",100)
    ]
   ),
# Escort merchant caravan:
  (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_merchant_caravan"),
                   (eq, "$escort_merchant_caravan_mode", 1)
                   ],
                  [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                   (try_begin),
                     (party_is_active, ":quest_target_party"),
                     (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
                     (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                   (try_end),
                   ]),
  (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_merchant_caravan"),
                    (eq, "$escort_merchant_caravan_mode", 0),
                    ],
                   [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                    (try_begin),
                      (party_is_active, ":quest_target_party"),
                      (party_set_ai_behavior, ":quest_target_party", ai_bhvr_escort_party),
                      (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                      (party_set_ai_object, ":quest_target_party", "p_main_party"),
                    (try_end),
                    ]),

  (0.1, 0, 0.0, [(check_quest_active, "qst_escort_merchant_caravan"),
                 (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                 (neg|party_is_active,":quest_target_party"),
                 ],
                [(call_script, "script_abort_quest", "qst_escort_merchant_caravan", 2),
                 ]),

# Troublesome bandits
  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_failed, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (eq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(display_message, "str_bandits_eliminated_by_another"),
                   (call_script, "script_abort_quest", "qst_troublesome_bandits", 0),
                   ]),

  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_succeeded, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (neq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(call_script, "script_succeed_quest", "qst_troublesome_bandits"),]),
				  
# Kidnapped girl:
   (1, 0, 0,
   [(check_quest_active, "qst_kidnapped_girl"),
    (quest_get_slot, ":quest_target_party", "qst_kidnapped_girl", slot_quest_target_party),
    (party_is_active, ":quest_target_party"),
    (party_is_in_any_town, ":quest_target_party"),
    (remove_party, ":quest_target_party"),
    ],
   []
   ),


#Rebellion changes begin
#move 

  (0, 0, 24 * 14,
   [
        (try_for_range, ":pretender", pretenders_begin, pretenders_end),
          (troop_set_slot, ":pretender", slot_troop_cur_center, 0),
          (neq, ":pretender", "$supported_pretender"),
          (troop_get_slot, ":target_faction", ":pretender", slot_troop_original_faction),
          (faction_slot_eq, ":target_faction", slot_faction_state, sfs_active),
          (faction_slot_eq, ":target_faction", slot_faction_has_rebellion_chance, 1),
          (neg|troop_slot_eq, ":pretender", slot_troop_occupation, slto_kingdom_hero),

          (try_for_range, ":unused", 0, 30),
            (troop_slot_eq, ":pretender", slot_troop_cur_center, 0),
            (store_random_in_range, ":town", towns_begin, towns_end),
            (store_faction_of_party, ":town_faction", ":town"),
            (store_relation, ":relation", ":town_faction", ":target_faction"),
            (le, ":relation", 0), #fail if nothing qualifies
           
            (troop_set_slot, ":pretender", slot_troop_cur_center, ":town"),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, 4, ":pretender"),
              (str_store_party_name, 5, ":town"),
              (display_message, "@{!}{s4} is in {s5}"),
            (try_end),
          (try_end),

#        (try_for_range, ":rebel_faction", rebel_factions_begin, rebel_factions_end),
#            (faction_get_slot, ":rebellion_status", ":rebel_faction", slot_faction_state),
#            (eq, ":rebellion_status", sfs_inactive_rebellion),
#            (faction_get_slot, ":pretender", ":rebel_faction", slot_faction_leader),
#            (faction_get_slot, ":target_faction", ":rebel_faction", slot_faction_rebellion_target),#

#            (store_random_in_range, ":town", towns_begin, towns_end),
#            (store_faction_of_party, ":town_faction", ":town"),
#            (store_relation, ":relation", ":town_faction", ":target_faction"),
#            (le, ":relation", 0), #fail if nothing qualifies

 #           (faction_set_slot, ":rebel_faction", slot_faction_inactive_leader_location, ":town"),
        (try_end), 
       ],
[]
),
#Rebellion changes end

#NPC system changes begin
#Move unemployed NPCs around taverns
   (24 * 15 , 0, 0, 
   [
    (call_script, "script_update_companion_candidates_in_taverns"),
    ],
   []
   ),

#Process morale and determine personality clashes
  (0, 0, 24,
   [],
[

#Count NPCs in party and get the "grievance divisor", which determines how fast grievances go away
#Set their relation to the player
        (assign, ":npcs_in_party", 0),
        (assign, ":grievance_divisor", 100),
        (try_for_range, ":npc1", companions_begin, companions_end),
            (main_party_has_troop, ":npc1"),
            (val_add, ":npcs_in_party", 1),
        (try_end),
        (val_sub, ":grievance_divisor", ":npcs_in_party"),
        (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
        (val_add, ":grievance_divisor", ":persuasion_level"),
        (assign, reg7, ":grievance_divisor"),

#        (display_message, "@{!}Process NPC changes. GD: {reg7}"),



##Activate personality clash from 24 hours ago
        (try_begin), #scheduled personality clashes require at least 24hrs together
             (gt, "$personality_clash_after_24_hrs", 0),
             (eq, "$disable_npc_complaints", 0),
             (try_begin),
                  (troop_get_slot, ":other_npc", "$personality_clash_after_24_hrs", slot_troop_personalityclash_object),
                  (main_party_has_troop, "$personality_clash_after_24_hrs"),
                  (main_party_has_troop, ":other_npc"),
                  (assign, "$npc_with_personality_clash", "$personality_clash_after_24_hrs"),
             (try_end),
             (assign, "$personality_clash_after_24_hrs", 0),
        (try_end),
#

         
        (try_for_range, ":npc", companions_begin, companions_end),
###Reset meeting variables
            (troop_set_slot, ":npc", slot_troop_turned_down_twice, 0),
            (try_begin),
                (troop_slot_eq, ":npc", slot_troop_met, 1),
                (troop_set_slot, ":npc", slot_troop_met_previously, 1),
            (try_end),

###Check for coming out of retirement
            (troop_get_slot, ":occupation", ":npc", slot_troop_occupation),
            (try_begin),
                (eq, ":occupation", slto_retirement),
                (troop_get_slot, ":renown_min", ":npc", slot_troop_return_renown),

                (str_store_troop_name, s31, ":npc"),
                (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
                (assign, reg4, ":player_renown"),
                (assign, reg5, ":renown_min"),
#                (display_message, "@{!}Test {s31}  for retirement return {reg4}, {reg5}."),

                (gt, ":player_renown", ":renown_min"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_occupation, 0),
            (try_end),


#Check for political issues
			(try_begin), #does npc's opponent pipe up?
				(troop_slot_ge, ":npc", slot_troop_days_on_mission, 5),
				(troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_kingsupport),

				(troop_get_slot, ":other_npc", ":npc", slot_troop_kingsupport_opponent),
				(troop_slot_eq, ":other_npc", slot_troop_kingsupport_objection_state, 0),
				
				(troop_set_slot, ":other_npc", slot_troop_kingsupport_objection_state, 1),
				
				(str_store_troop_name, s3, ":npc"),
				(str_store_troop_name, s4, ":other_npc"),

				(try_begin),
					(eq, "$cheat_mode", 1),
					(display_message, "str_s4_ready_to_voice_objection_to_s3s_mission_if_in_party"),
				(try_end),
			(try_end),

			#Check for quitting
            (try_begin),
                (main_party_has_troop, ":npc"),
				
                (call_script, "script_npc_morale", ":npc"),
                (assign, ":npc_morale", reg0),

                (try_begin),
                    (lt, ":npc_morale", 20),
                    (store_random_in_range, ":random", 0, 100),
                    (val_add, ":npc_morale", ":random"),
                    (lt, ":npc_morale", 20),
                    (assign, "$npc_is_quitting", ":npc"),
                (try_end),

				#Reduce grievance over time (or augment, if party is overcrowded
                (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),

                (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),


				#Change personality grievance levels
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash_state),
                (try_end),
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash2_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash2_object),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash2_state),
                (try_end),
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalitymatch_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalitymatch_object),
                    (main_party_has_troop, ":object"),
                    (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                    (val_mul, ":grievance", 9),
                    (val_div, ":grievance", 10),
                    (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),
                (try_end),


				
#Check for new personality clashes

				#Active personality clash 1 if at least 24 hours have passed
                (try_begin),
                    (eq, "$disable_npc_complaints", 0),
                    (eq, "$npc_with_personality_clash", 0),
                    (eq, "$npc_with_personality_clash_2", 0),
                    (eq, "$personality_clash_after_24_hrs", 0),
                    (troop_slot_eq, ":npc", slot_troop_personalityclash_state, 0),
                    (troop_get_slot, ":other_npc", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":other_npc"),
                    (assign, "$personality_clash_after_24_hrs", ":npc"),
                (try_end),

				#Personality clash 2 and personality match is triggered by battles
				(try_begin),
					(eq, "$npc_with_political_grievance", 0),
				
					(troop_slot_eq, ":npc", slot_troop_kingsupport_objection_state, 1),
					(assign, "$npc_with_political_grievance", ":npc"),
				(try_end),

			#main party does not have troop, and the troop is a companion
			(else_try), 
				(neg|main_party_has_troop, ":npc"),
				(eq, ":occupation", slto_player_companion),

				
				(troop_get_slot, ":days_on_mission", ":npc", slot_troop_days_on_mission),
				(try_begin),
					(gt, ":days_on_mission", 0),
					(val_sub, ":days_on_mission", 1),
					(troop_set_slot, ":npc", slot_troop_days_on_mission, ":days_on_mission"),
				(else_try), 
					(troop_slot_ge, ":npc", slot_troop_current_mission, 1),
					
					#If the hero can join
					(this_or_next|neg|troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_rejoin_when_possible),
						(hero_can_join, ":npc"),
						
					(assign, "$npc_to_rejoin_party", ":npc"),
				(try_end),
            (try_end),
        (try_end),
    ]),


#NPC system changes end

# Lady of the lake achievement
   (1, 0, 0,
   [
     (troop_get_type, ":is_female", "trp_player"),
     (eq, ":is_female", 1),       
     (try_for_range, ":companion", companions_begin, companions_end),
       (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),

       (troop_get_inventory_capacity, ":inv_cap", ":companion"),
       (try_for_range, ":i_slot", 0, ":inv_cap"),
         (troop_get_inventory_slot, ":item_id", ":companion", ":i_slot"),

		 (ge, ":item_id", 0),

	 	 (this_or_next|eq, ":item_id", "itm_great_sword"),
	 	 (this_or_next|eq, ":item_id", "itm_sword_two_handed_a"),
		 (eq, ":item_id", "itm_strange_great_sword"),
		 		 
		 (unlock_achievement, ACHIEVEMENT_LADY_OF_THE_LAKE),
		 (assign, ":inv_cap", 0),
	   (try_end),
	 (try_end),
    ],
   []
   ),


#+freelancer start

#  CHECKS IF "$enlisted_party" IS DEFEATED

    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
        (gt, "$enlisted_party", 0),
        (neg|party_is_active, "$enlisted_party"),
    ],
    [
        (assign, "$freelancer_state", 0),
        (call_script, "script_freelancer_detach_party"),
		
		#to prevent companions from being lost forever
		(call_script, "script_party_restore"), 
		(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
        (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
			(party_stack_get_troop_id, ":return_troop", "p_main_party", ":cur_stack"),
			(neg|troop_is_hero, ":return_troop"),
			(party_stack_get_size, ":stack_size", "p_main_party", ":cur_stack"),
			(party_remove_members, "p_main_party", ":return_troop", ":stack_size"),
		(try_end),

        #removes faction relation given at enlist
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
            (neq, ":commander_faction", ":cur_faction"),
			(faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
            (call_script, "script_set_player_relation_with_faction", ":cur_faction", 0),
        (try_end),

		(assign, "$g_encountered_party", "$g_enemy_party"),
		(jump_to_menu, "mnu_captivity_start_wilderness"),
    ]),

 #  CHECKS IF "$enlisted_party" HAS JOINED BATTLE

    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
		
		#collected nearby enemies->detach (post-battle)
		(try_begin), 
			(party_slot_ge, "p_freelancer_party_backup", slot_party_last_in_combat, 1),
			(map_free),
			(party_set_slot, "p_freelancer_party_backup", slot_party_last_in_combat, 0),
			(party_get_num_attached_parties, ":num_attached", "p_main_party"),
			(try_for_range_backwards, ":i", 0, ":num_attached"),
				(party_get_attached_party_with_rank, ":party", "p_main_party", ":i"),
				(party_detach, ":party"),
			(try_end),
		(try_end),
		
		#Is currently in battle
        (party_get_battle_opponent, ":commander_enemy", "$enlisted_party"),
        (gt, ":commander_enemy", 0),
		
		#checks that the player's health is high enough to join battle
        (store_troop_health, ":player_health", "trp_player"),
        (ge, ":player_health", 50),
    ],
    [
        (jump_to_menu, "mnu_world_map_soldier"),
    ]),

#  CHECKS IF PLAYER WON THE REVOLT

    (1.0, 0, 0, [
        (eq, "$freelancer_state", 0),
        (gt, "$enlisted_party", 0),
        (neg|party_is_active, "$enlisted_party"),

		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":commander_faction"),
        (lt, ":relation", 0),

        (party_get_attached_party_with_rank, ":attached_party", "p_main_party", 0),
        (eq, "p_temp_party_2", ":attached_party"),
    ],
    [
        (assign, "$enlisted_party", -1),
        (party_detach, "p_temp_party_2"),
        (store_skill_level, ":cur_leadership", "skl_leadership", "trp_player"),
        (store_skill_level, ":cur_persuasion", "skl_persuasion", "trp_player"),
        (store_add, ":chance", ":cur_persuasion", ":cur_leadership"),
        (val_add, ":chance", 10),
        (store_random_in_range, ":prisoner_state", 0, ":chance"),

        (try_begin),
            (is_between, ":prisoner_state", 0, 5),
            (call_script, "script_party_calculate_strength", "p_main_party", 0),
            (assign, ":main_strength", reg0),
            (call_script, "script_party_calculate_strength", "p_temp_party_2", 0),
            (assign, ":temp_strength", reg0),
            (ge, ":temp_strength", ":main_strength"),

            (party_get_num_prisoner_stacks, ":num_stacks", "p_temp_party_2"),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (party_prisoner_stack_get_troop_id, ":cur_troops", "p_temp_party_2", ":cur_stack"),
                (party_prisoner_stack_get_size, ":cur_size", "p_temp_party_2", ":cur_stack"),
                (party_remove_prisoners, "p_temp_party_2", ":cur_troops", ":cur_size"),
            (try_end),

            (tutorial_box, "@The released prisoners were not be trusted and they are preparing to attack you!", "@Warning!"),
            (start_encounter, "p_temp_party_2"),
            (change_screen_map),
        (else_try),
            (is_between, ":prisoner_state", 5, 10),
            (tutorial_box, "@The released prisoners scattered as soon as the battle finished. You will not be seeing them again.", "@Notice!"),
            (party_clear, "p_temp_party_2"),
        (else_try),
            (tutorial_box, "@The released prisoners have remained loyal and will join your party", "@Notice!"),
            (party_get_num_companion_stacks, ":num_stacks", "p_temp_party_2"),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":cur_troops", "p_temp_party_2", ":cur_stack"),
                (party_stack_get_size, ":cur_size", "p_temp_party_2", ":cur_stack"),
                (party_add_members, "p_main_party", ":cur_troops", ":cur_size"),
            (try_end),
            (party_clear, "p_temp_party_2"),
        (try_end),
    ]),

# IF LEFT MOUSE CLICK GO TO SOLDIER'S MENU

    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
        (key_clicked, key_left_mouse_button),

        (set_fixed_point_multiplier, 1000),
        (mouse_get_position, pos0),
        (position_get_y, ":y", pos0),
        (gt, ":y", 50), #allows the camp, reports, quests, etc. buttons to be clicked
    ],
    [
        (jump_to_menu, "mnu_world_map_soldier"),
        (rest_for_hours_interactive, 9999, 4, 0),
    ]),

(24.0, 0, 0, [
        (eq, "$freelancer_state", 2),
    ],
    [
		(troop_get_slot, ":days_left", "trp_player", slot_troop_days_on_mission),
		(try_begin),
		  (gt, ":days_left", 5),
		  (val_sub, ":days_left", 1),
		  (troop_set_slot, "trp_player", slot_troop_days_on_mission, ":days_left"),
		(else_try),		  
		  (is_between, ":days_left", 1, 5),
		  (assign, reg0, ":days_left"),
		  (display_message, "@You have {reg0} days left till you are declared as a deserter!"),
		  (val_sub, ":days_left", 1),
		  (troop_set_slot, "trp_player", slot_troop_days_on_mission, ":days_left"),
		(else_try), #declare deserter
		  (eq, ":days_left", 0),
		  (call_script, "script_event_player_deserts"),
          (display_message, "@You have now been declared as a deserter!"),
		(try_end),  
    ]),


#+freelancer end


 
]
# modmerger_start version=201 type=2
try:
    component_name = "triggers"
    var_set = { "triggers" : triggers }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
