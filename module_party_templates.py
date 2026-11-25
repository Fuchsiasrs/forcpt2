from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *
from module_parties import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,8,12)]),
  #Koylu isyani
  ("koylu_isyani","Rebellious Peasants",icon_peasant,0,fac_koylu_isyani,bandit_personality,[(trp_rebel_peasent,50,100),(trp_rebel_peasent_woman,25,50)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Looters",icon_icon_bandit|carries_goods(8),0,fac_outlaws,army_personality,[(trp_brigand_leader,1,5),(trp_bandit,5,15),(trp_looter,35,70)]),
# Ryan END
  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_slaver_chief,1,1),(trp_slave_crusher,7,20),(trp_slave_hunter,8,20),(trp_slave_driver,9,20),(trp_manhunter,10,20),]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ("steppe_bandits","Steppe Bandits",icon_steppe_bandit|carries_goods(2),0,fac_steppe_bandits,army_personality,[(trp_steppe_horseman,10,20),(trp_steppe_horse_archery,10,20),(trp_steppe_bandit,20,40),]),
  ("taiga_bandits","Cavlaki's Sect",icon_axeman|carries_goods(2),0,fac_outlaws,army_personality,[(trp_taiga_bandit,20,88)]),
  ("desert_bandits","Desert Bandits",icon_icon_desertbandit|carries_goods(2),0,fac_desert_bandits,army_personality,[(trp_desert_lion,1,5),(trp_bedevi,4,12),(trp_veteran_desert_bandit,4,12),(trp_desert_horse_archer,4,12),(trp_desert_bandit,20,40)]),
  ("forest_bandits","Forest Bandits",icon_axeman|carries_goods(2),0,fac_forest_bandits,army_personality,[(trp_veteran_forest_bandit,5,15),(trp_veteran_forest_archer,5,15),(trp_forest_bandit,10,52),]),
  ("mountain_bandits","Mountain Bandits",icon_axeman|carries_goods(2),0,fac_mountain_bandits,army_personality,[(trp_veteran_mountain_bandit,5,15),(trp_mountain_crossbowman,5,15),(trp_mountain_bandit,10,60),]),
  ("sea_raiders","Sea Raiders",icon_axeman|carries_goods(2),0,fac_sea_raiders,army_personality,[(trp_sea_raider_liderr,1,2),(trp_sea_raider_veteran,5,15),(trp_sea_raider,15,70)]),

  ("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
    
  ("merchant_caravan","Merchant Caravan",icon_icon_kervan|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("wagon_train","Wagon Train",icon_icon_kervan|carries_goods(20)|pf_show_faction,0,fac_player_faction,escorted_merchant_personality,[(trp_wagon_master,1,1),(trp_caravan_guard,1,1)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,army_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,army_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,12,20),(trp_peasant_woman,8,18)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_icon_kervan|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_mercenary_cavalry,15,20),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_recruit,15,25),(trp_swadian_footman,15,25)]),
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_crusader_cavalary,8,13),(trp_swadian_infantry,8,13),(trp_swadian_crossbowman,7,12),(trp_hired_blade,7,12)]),
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,5,9),(trp_jerusalem_knight,5,8),(trp_knight_of_hospitaller,5,8),(trp_crusader_guard,5,8),(trp_swadian_knight,5,9),(trp_mercenary_cavalry,5,8)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)

  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_recruit,6,10),(trp_alp,6,10),(trp_seljuk_horseman1,6,10),(trp_gazi,6,10),(trp_turkmen,6,10)]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_seljuk_infantry1,5,9),(trp_seljuk_archer_frozen,5,9),(trp_turkmen_horse_archer,5,8),(trp_turkmen_piyada,5,8),(trp_seljuk_infantry2,5,8),(trp_kurdish_mercenary_soldier,5,8)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_seljuk_horseman2,5,9),(trp_seljuk_crossbowman,5,8),(trp_seljuk_horseman4,5,8),(trp_seljuk_infantry2,5,8),(trp_vaegir_knight,5,9),(trp_seljuk_subasi,5,8),]),

  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_tribesman,8,13),(trp_mongol_militia,8,13),(trp_khergit_skirmisher,7,12),(trp_kirim_tatar,7,12)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,5,9),(trp_mongol_infantry,5,9),(trp_mongol_veteran_archer,5,8),(trp_mongol_archer,5,8),(trp_khergit_horse_archer,5,8),(trp_tatar,5,8)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_mercenary_fire_man,5,8),(trp_khergit_veteran_horse_archer,5,9),(trp_elite_mangudai,5,8),(trp_royal_mongol_archer,5,8),(trp_royal_keshik,5,8),(trp_keshik,5,9)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_footman,15,25),(trp_nord_recruit,15,25)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_footmana,10,17),(trp_nord_footmana,10,17),(trp_nord_footman,10,16)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_warrior,5,9),(trp_alamut_fedayen,5,8),(trp_masyaf_archer,5,8),(trp_bas_dai_komutani,5,8),(trp_mercenary_fire_man,5,8),(trp_bas_dai,5,9)]),
  #hashasi kaleler icin ekstra askerler
  ("kingdom_4_reinforcements_b_2", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_footmana,80,82),(trp_nord_footmana,80,122),(trp_nord_footman,60,62)]),

  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_tribesman,15,25),(trp_rhodok_spearman,15,25)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,6,10),(trp_rum,6,10),(trp_rhodok_sharpshooter,6,10),(trp_rhodok_trained_crossbowman,6,10),(trp_rhodok_sharpshooter,6,10)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,8,13),(trp_elite_varangian_guard,8,13),(trp_rhodok_veteran_crossbowman,7,12),(trp_fire_man,7,12)]), 
  ("kingdom_5_reinforcements_b_2", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,60,80),(trp_rum,40,60),(trp_rhodok_sharpshooter,20,40),(trp_rhodok_trained_crossbowman,20,40),(trp_rhodok_sharpshooter,40,120)]),

  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sarranid_recruit,15,25),(trp_sarranid_footman,15,25)]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarranid_skirmisher,8,13),(trp_bedevi,8,13),(trp_sarranid_veteran_footman,7,12),(trp_sarranid_footman,7,12)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_guard,6,10),(trp_royal_abna,6,10),(trp_mercenary_fire_man,6,10),(trp_royal_mamluk_2,6,10),(trp_royal_mamluk,6,10)]),

  ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_kingdom_crossbowman,30,50)]),
  ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_kingdom_sharpshooter,30,50)]),
  ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_kingdom_knight,30,50)]),
  
  ("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_harzem1,10,17),(trp_harzem2,10,17),(trp_turkmen,10,16)]),
  ("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_harzem3,5,9),(trp_harzem4,5,9),(trp_harzem5,5,8),(trp_harzem7,5,8),(trp_turkmen_piyada,5,8),(trp_turkmen_horse_archer,5,8)]),
  ("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_harzem6,10,17),(trp_mercenary_fire_man,10,17),(trp_harzem8,10,16)]),
  
  ("kingdom_9_reinforcements_a", "{!}kingdom_9_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_abbasi1,10,17),(trp_abbasi2,10,17),(trp_abbasi3,10,16)]),
  ("kingdom_9_reinforcements_b", "{!}kingdom_9_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_abbasi3,5,9),(trp_abbasi4,5,9),(trp_abbasi5,5,8),(trp_abbasi6,5,8),(trp_abbasi2,5,8),(trp_abbasi7,5,8)]),
  ("kingdom_9_reinforcements_c", "{!}kingdom_9_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_abbasi7,5,9),(trp_mercenary_fire_man,5,8),(trp_royal_aswaran,5,8),(trp_savaran,5,8),(trp_savaran_archer,5,8),(trp_abbasi8,5,9)]),
  
  ("kingdom_10_reinforcements_a", "{!}kingdom_10_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_kipchak_tribesman,10,17),(trp_kipchak_archer,10,17),(trp_kipcak_warrior,10,16)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_10_reinforcements_b", "{!}kingdom_10_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_kipcak_warrior,8,13),(trp_kipchak_archer,8,13),(trp_kipcak_khan_guard,7,12),(trp_kipcak_suvari,7,12)]),
  ("kingdom_10_reinforcements_c", "{!}kingdom_10_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_kipchak_cavalary,5,9),(trp_elite_kipchak_women,5,9),(trp_royal_kipchak_women,5,8),(trp_mercenary_fire_man,5,8),(trp_kipchak_noble,5,8),(trp_kipchak_women,5,8)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  #trabzon
  ("kingdom_12_reinforcements_a", "{!}kingdom_12_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_trebizond_recruit,10,17),(trp_trebizond_skirmisher,10,17),(trp_trebizond_archers,10,16)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_12_reinforcements_b", "{!}kingdom_12_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_trebizond_militia_spearman,10,17),(trp_scoutatoi_spearman,10,17),(trp_kavallarioi,10,16)]),
  ("kingdom_12_reinforcements_c", "{!}kingdom_12_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_royal_trebizond_knight,5,9),(trp_heavy_scoutatoi_spearman,5,9),(trp_trebizond_pronoiaroi,5,8),(trp_mercenary_fire_man,5,8),(trp_trebizond_knight,5,8),(trp_trebizond_guard_archers,5,8)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  #kibris
  ("kingdom_13_reinforcements_a", "{!}kingdom_13_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_cyprus_recruit,10,17),(trp_cyprus_skirmisher,10,17),(trp_cyprus_footman,10,16)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_13_reinforcements_b", "{!}kingdom_13_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_cyprus_crossbowman,10,17),(trp_cyprus_axeman,10,17),(trp_cyprus_marksman,10,16)]),
  ("kingdom_13_reinforcements_c", "{!}kingdom_13_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_cyprus_cavalary,5,9),(trp_cyprus_axeman_2,5,9),(trp_cyprus_knight,5,8),(trp_swadian_knight,5,8),(trp_mercenary_cavalry,5,8),(trp_mercenary_fire_man,5,8)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  #gurci
  ("kingdom_14_reinforcements_a", "{!}kingdom_14_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_georgian_recruit,10,17),(trp_svanian_archer,10,17),(trp_kartlian_spearman,10,16)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_14_reinforcements_b", "{!}kingdom_14_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_metsikhovne_archer,10,17),(trp_georgian_horse_archer,10,17),(trp_khevsur_warrior,10,16)]),
  ("kingdom_14_reinforcements_c", "{!}kingdom_14_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_monaspa_archer,5,9),(trp_prince_royal_monaspa,5,9),(trp_elite_khevsur_warrior,5,8),(trp_monaspa_heavy_horse_archer,5,8),(trp_royal_monaspa,5,8),(trp_mercenary_fire_man,5,8)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  #papalik
  ("kingdom_15_reinforcements_a", "{!}kingdom_15_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_papal_recruit,10,17),(trp_italian_spear_militia,10,17),(trp_peasant_crossbowman,10,16)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_15_reinforcements_b", "{!}kingdom_15_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_papal_crossbowman,10,17),(trp_papal_mounted_crossbowman,10,17),(trp_veteran_italian_spear_militia,10,16)]),
  ("kingdom_15_reinforcements_c", "{!}kingdom_15_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_royal_papal_guard,5,9),(trp_papal_cavalary,5,9),(trp_veteran_italian_spear_militia,5,8),(trp_mercenary_fire_man,5,8),(trp_papal_guard,5,8),(trp_papal_knight,5,8)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  #bulgar
  ("kingdom_16_reinforcements_a", "{!}kingdom_16_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bulgarian_recruit,10,17),(trp_bulgarian_swordsman,10,17),(trp_bulgarian_peasant_archer,10,16)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_16_reinforcements_b", "{!}kingdom_16_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_bulgarian_heavy_swordsman,10,17),(trp_bulgarian_archer,10,17),(trp_bulgarian_peasant_archer,10,16)]),
  ("kingdom_16_reinforcements_c", "{!}kingdom_16_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_elite_bulgarian_swordsman,5,9),(trp_royal_bolyar,5,9),(trp_bulgarian_elite_archer,5,8),(trp_bulgarian_proniar,5,8),(trp_bolyar,5,8),(trp_mercenary_fire_man,5,8)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)



##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,7),(trp_swadian_skirmisher,5,10),(trp_swadian_militia,11,26)]),
##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,5,10),(trp_swadian_infantry,5,10),(trp_swadian_crossbowman,3,8)]),
##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight,2,6),(trp_swadian_sergeant,2,5),(trp_swadian_sharpshooter,2,5)]),
##
##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,3,7),(trp_vaegir_skirmisher,5,10),(trp_vaegir_footman,11,26)]),
##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,4,9),(trp_vaegir_infantry,5,10),(trp_vaegir_archer,3,8)]),
##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_knight,3,7),(trp_vaegir_guard,2,5),(trp_vaegir_marksman,2,5)]),
##
##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,3,7),(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,11,26)]),
##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer,4,9),(trp_khergit_horse_archer,5,10),(trp_khergit_horseman,3,8)]),
##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,3,7),(trp_khergit_veteran_horse_archer,2,5),(trp_khergit_horse_archer,2,5)]),
##
##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_nord_footman,5,10),(trp_nord_recruit,11,26)]),
##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_veteran,4,9),(trp_nord_warrior,5,10),(trp_nord_footman,3,8)]),
##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,3),(trp_nord_veteran,2,5),(trp_nord_warrior,2,5)]),
##
##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,3,7),(trp_rhodok_crossbowman,5,10),(trp_rhodok_tribesman,11,26)]),
##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,9),(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,3,8)]),
##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,7),(trp_rhodok_veteran_spearman,2,5),(trp_rhodok_veteran_crossbowman,2,5)]),



  ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_icon_haydutkamp2|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,100)]),
  ("taiga_bandit_lair","Cavlaki's Followers Lair",icon_icon_haydutkamp|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,100)]),
  ("desert_bandit_lair" ,"Desert Bandit Lair",icon_icon_haydutkamp2|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,100)]),
  ("forest_bandit_lair" ,"Forest Bandit Camp",icon_icon_haydutkamp|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,100)]),
  ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_icon_haydutkamp|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,100)]),
  ("sea_raider_lair","Sea Raider Landing",icon_icon_haydutkamp|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,100)]),
  ("looter_lair","Kidnappers' Hideout",icon_icon_haydutkamp|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,100)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,100)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),
  #Hunting
  ("deer_herd","Deer Herd",icon_deer_icon|carries_goods(30),0,fac_wild_animals,merchant_personality,[(trp_deer,3,9)]),
  ("deer_herd2","Deer Herd",icon_deer_icon|carries_goods(30),0,fac_wild_animals,merchant_personality,[(trp_deer,6,9)]),
  ("boar_herd2","Boar Herd",icon_boar_icon|carries_goods(30),0,fac_wild_animals,merchant_personality,[(trp_boar,5,8)]),
  ("boar_herd3","Boar Herd",icon_boar_icon|carries_goods(30),0,fac_wild_animals,merchant_personality,[(trp_boar,5,8)]),
  ("sheep_herd","Sheep Herd",icon_sheep_mod_a_icon|carries_goods(30),0,fac_wild_animals,merchant_personality,[(trp_sheep,5,8)]),

  ("boar_herd","Boar Herd",icon_boar_icon|carries_goods(30),0,fac_wild_animals,merchant_personality,[(trp_boar,5,8)]),
  #Hunting
    ("kipcak_gocebe","Kipchaks",icon_icon_turk_patrol,0,fac_kingdom_3,soldier_personality,[(trp_kipcak_suvari,9,20),(trp_kipcak_okcu,9,10),(trp_kipcak_warrior,9,10)]),
    ("kirim_gocebe","Crimea Tatars",icon_icon_turk_patrol,0,fac_kingdom_3,soldier_personality,[(trp_tatar,9,20),(trp_kirim_tatar,9,10),(trp_kirim_tatar,9,10)]),
    ("turkmen_gocebe","Turkmens",icon_icon_turk_patrol,0,fac_kingdom_2,soldier_personality,[(trp_turkmen,9,20),(trp_turkmen_piyada,9,10),(trp_turkmen_horse_archer,9,10)]),
    
	("player_camp","Camp",icon_camp|pf_always_visible|pf_limit_members,0,fac_player_faction,courage_15,[]),
("rigale_treasure_spot","An X marks the spot",icon_bandit_lair|pf_is_static,0, fac_neutral,merchant_personality,[]), 
  ("pechenegs","Pechenegs",icon_icon_mongol_patrol,0,fac_pechenegs,soldier_personality,[(trp_pecheneg_noble,1,1),(trp_veteran_pecheneg_warrior,5,7),(trp_pecheneg_warrior,7,9),(trp_pecheneg_chief,9,10),(trp_pecheneg,10,15),]),
  ("pechenegs_army","Pechenegs Army",icon_icon_mongol_patrol,0,fac_pechenegs,army_personality,[(trp_pecheneg_noble,5,10),(trp_veteran_pecheneg_warrior,12,15),(trp_pecheneg_warrior,10,15),(trp_pecheneg_chief,12,18),(trp_pecheneg,10,15),]),
  ("vergi_muhafizlari","Taxpayers",icon_icon_mongol_patrol,0,fac_manhunters,soldier_personality,[(trp_vergi_muhafiz,10,15),]),
  ("kayi_devriye","Kayig Patrol",icon_icon_mongol_patrol,0,fac_kingdom_2,soldier_personality,[(trp_alp_cavalary_2,1,3),(trp_alp_cavalary,5,10),(trp_alp,5,15),(trp_alp_archer,10,12),]),
  ("kayi_devriye_2","Suleyman Shah",icon_icon_mongol_patrol,0,fac_kingdom_2,soldier_personality,[(trp_suleyman_sah,1,1),(trp_dundar,1,1),(trp_ertugrul,1,1),(trp_alp_cavalary_2,20,30),(trp_alp_cavalary,25,35),(trp_alp,30,50),]),

  ("rastgele_koy","Village",icon_village_burnt_a|carries_goods(2)|pf_rastgele|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,100)]),
  ("rastgele_fort","Fort",icon_castle_c|carries_goods(2)|pf_rastgele|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,100)]),
  #("parti_1","Mercenary Cavalary",icon_gray_knight|pf_quest_party, 0, fac_parti_1, escorted_merchant_personality,[(trp_mercenary_cavalry,140,185)]),
   
  ("hacli_ordu","Crusaders",icon_icon_crusader_patrol|carries_goods(2),0,fac_kingdom_1,soldier_personality,[(trp_swadian_knight,10,15),(trp_jerusalem_knight,10,15),(trp_swadian_man_at_arms,10,15),(trp_crusader_cavalary,20,35),]),
  ("crusade_army","Crusader Army",icon_icon_crusader_patrol|carries_goods(20),0,fac_kingdom_1,army_personality,[(trp_holy_crusader,1,1),(trp_royal_knight_of_hospitaller,5,7),(trp_swadian_knight,15,20),(trp_swadian_crossbowman,30,50),(trp_swadian_footman,50,100),(trp_swadian_recruit,100,150),]),
  ("mongol_war_party","Mongol Invaders",icon_icon_mongol_patrol|carries_goods(2),0,fac_kingdom_3,army_personality,[(trp_royal_keshik,1,5),(trp_keshik,10,15),(trp_khergit_lancer,10,15),(trp_khergit_veteran_horse_archer,10,15),(trp_mongol_infantry,40,80),(trp_mongol_veteran_archer,15,35),]),
  ("kipcak_women","Kipchak Women Warriors",icon_icon_mongol_patrol|carries_goods(2),0,fac_kingdom_10,army_personality,[(trp_royal_kipchak_women,1,3),(trp_elite_kipchak_women,5,9),(trp_kipchak_women,25,30),(trp_kipchak_women_2,25,30),]),
  ("acemi_birlik","Mercenary Troops",icon_icon_mongol|carries_goods(2),0,fac_neutral,soldier_personality,[(trp_townsman,1,2),(trp_turkmen_piyada,1,3),(trp_turkmen_horse_archer,1,2),(trp_kirim_tatar,1,3),(trp_watchman,5,7),(trp_caravan_guard,5,7),]),
  ("kidemli_birlik","Mercenary Troops",icon_icon_mongol|carries_goods(2),0,fac_neutral,soldier_personality,[(trp_watchman,1,2),(trp_turk_cavalary,2,3),(trp_turkmen,2,3),(trp_mercenary_swordsman,4,5),(trp_mercenary_horseman,4,5),(trp_rum,4,5),]),
  ("elit_birlik","Mercenary Troops",icon_icon_mongol|carries_goods(2),0,fac_neutral,soldier_personality,[(trp_hired_blade,2,3),(trp_rum,2,3),(trp_gazi,2,3),(trp_kurdish_mercenary_soldier,4,5),(trp_mercenary_crossbowman,4,5),(trp_mercenary_cavalry,4,5),]),
  ("hashasi_tebriz_ordusu","Assassins Army",icon_gray_knight|carries_goods(20),0,fac_kingdom_4,soldier_personality,[(trp_bas_dai_komutani,30,50),(trp_alamut_fedayen,100,150),(trp_masyaf_archer,111,200),(trp_nord_footman,250,300),]),


	
]
# modmerger_start version=201 type=2
try:
    component_name = "party_templates"
    var_set = { "party_templates" : party_templates }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end