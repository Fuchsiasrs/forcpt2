from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small
pf_rastgele = pf_is_static|pf_hide_defenders|pf_label_medium|pf_always_visible

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(-17, -52.5),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################  
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18,-60),[]),

  ("town_1","Urgench",  icon_icon_mongol_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(165.6, 126.7),[], 170),
  ("town_2","Athina",     icon_icon_izmir|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.4, 38.5),[], 80),
  ("town_3","Smyrna",   icon_icon_izmir|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.4, 52.5),[], 80),
  ("town_4","Iskenderun",     icon_icon_konya|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40, 27.4),[], 180),
  ("town_5","Constantinople",  icon_icon_constantinople|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.6, 84.74),[], 270),
  ("town_6","Jerusalem",   icon_icon_ierusalem|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44, -37.4),[], 1),
  ("town_7","Acre",   icon_icon_acre|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43, -18.5),[], 0),

  ("town_8","Icconium", icon_icon_konya|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-71.44, 53.3),[], 175),
  ("town_9","Baghdad",   icon_icon_bagdat|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24, -14.2),[], 90),
  ("town_10","Samarqand",   icon_icon_mongol_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(207.5, 79),[], 180),
  ("town_11","Trapezus",   icon_icon_konya|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12, 79.5),[], 150),
  ("town_12","Amid", icon_icon_konya|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.2, 47.9),[], 0),
  ("town_13","Tebriz",icon_icon_konya|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30, 37),[],260),
  ("town_14","Kashgar",  icon_icon_mongol_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(246.5, 88),[], 180),

  ("town_15","Thessaloniki",  icon_icon_izmir|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-163.8, 82.3),[], 45),
  ("town_16","Tarablus",  icon_icon_konya|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.82, 2.89),[], 0),
  ("town_17","Asqabat",  icon_icon_mongol_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(139.8, 46.6),[], 90),
  ("town_18","Ghazni",  icon_icon_mongol_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(181, -7.5),[], 135),

  ("town_19","Alexandria", icon_icon_iaffa|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-97.51, -46.48),[], 215),
  ("town_20","Damascus", icon_icon_damascus|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16, 1.1),[], 180),
  ("town_21","Cairo", icon_icon_konya|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.5, -76.5),[], 330),
  ("town_22","Amman", icon_icon_konya|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21, -23.7),[], 180),
  ("town_23","Isfahan", icon_icon_konya|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70, -22.7),[], 180),
  ("town_24","Zerenc", icon_icon_konya|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(148, -34.7),[], 180),
  ("town_25","Hurmuz", icon_icon_iaffa|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(166, -103.7),[], 355),
  ("town_26","Kufe", icon_icon_konya|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13, -39.7),[], 175),
    ("town_27","Itil",   icon_icon_mongol_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.5, 126),[], 180),
    ("town_28","Kaffa",   icon_icon_mongol_city|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.5, 132),[], 180),
  ("town_29","Alashia",  icon_icon_acre|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60, 10),[], 135),
  ("town_30","Cerasus",  icon_icon_acre|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25, 80),[], 230),
  ("town_31","Celenderis",  icon_icon_acre|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65, 28),[], 130),
  ("town_32","Tbilisi",  icon_icon_konya|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35, 90),[], 65),
  ("town_33","Kutaisi",  icon_icon_konya|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7, 99),[], 135),
  ("town_34","Rome",  icon_icon_acre|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-248, 90),[], 45),
  ("town_35","Rimini",  icon_icon_acre|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-243, 117),[], 200),
  ("town_36","Tarnova",  icon_icon_izmir|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132, 117),[], 135),
  ("town_37","Harsova",  icon_icon_izmir|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-103, 135),[], 135),


#   Aztaq_Castle       
#  Malabadi_Castle
  ("castle_1","Varna",icon_icon_bzt_castle3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.3, 113),[],50),
  ("castle_2","Tous",icon_icon_mongol_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(149.5, 33.2),[],75),
  ("castle_3","Amisus",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.86, 88.4),[], 170),
  ("castle_4"," Erzingan",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.5, 64.8),[],180),
  ("castle_5","Barseh",icon_icon_alamut|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.8, 18.7),[],90),
  ("castle_6","Gazze",icon_icon_crusader_castle_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.6, -26.1),[],55),
  ("castle_7","Nukus",icon_icon_mongol_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(133.5, 130.5),[],45),
  ("castle_8","Ankara",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.2, 71),[],30),
  ("castle_9","Mora",icon_icon_bzt_castle3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-167.8, 27.5),[], 110),
  ("castle_10","Elamut",icon_icon_alamut|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.2, 5),[],110),
  ("castle_11","Lambesar",icon_icon_alamut|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(60.50, 12.46),[],75),
  ("castle_12","Rudhan",icon_icon_alamut|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.75, 18.5),[],95),
  ("castle_13","Tyre",icon_icon_crusader_castle_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42, -12.5),[], 180),
  ("castle_14","Serez",icon_icon_bzt_castle3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-148.4, 86.1),[],90),
  ("castle_15","Edirne",icon_icon_bzt_castle3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-117.4, 83.5),[], 80),
  ("castle_16","Sofia",icon_icon_bzt_castle3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-163.6, 112.6),[],45),
  ("castle_17","Hotan",icon_icon_mongol_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(237.3, 69.8),[],15),
  ("castle_18","Miryakefalon",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.4, 56.1),[],300),
  ("castle_19","Baku",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.5, 71.6),[],280),
  ("castle_20","Ayintap",icon_icon_crusader_castle_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27, 33.5),[], 100),
  ("castle_21","Filibe",icon_icon_bzt_castle3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.3, 105.8),[],15),
  ("castle_22","Otrar",icon_icon_mongol_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(222, 130),[],260),
  ("castle_23","Samaxi",icon_icon_crusader_castle_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.8, 72.3),[],80),
  ("castle_24","Antioch",icon_icon_crusader_castle_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.9, 22.6),[],260),
  ("castle_25","Beyrut",icon_icon_crusader_castle_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40, -2.6),[],260),
  ("castle_26","Adana",icon_icon_crusader_castle_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.2, 35),[],30),
  ("castle_27","Hama",icon_icon_crusader_castle_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.3, 14),[],260),
  ("castle_28","Bursa",icon_icon_bzt_castle3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.4, 68.3),[],260),

  ("castle_29","Malatya",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.5, 47.8),[], 170),
  ("castle_30","Ray",icon_icon_mongol_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(95, 22),[],260),
  ("castle_31","Trablus",icon_icon_crusader_castle_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.7, 8.5),[],260),
  ("castle_32","Talaqan",icon_icon_alamut|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68, -10.1),[],260),
  ("castle_33","Milas",icon_icon_bzt_castle3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.4, 38.1),[],80),
  ("castle_34","Manjil",icon_icon_alamut|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.5, 7.6),[],260),
  ("castle_35","Caesarea",icon_icon_crusader_castle_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44, 53.2),[], 90),
  ("castle_36","Elan",icon_icon_alamut|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.3, -2.2),[],260),
  ("castle_37","Basra",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.3, -45),[],260),
  ("castle_38","Herat",icon_icon_mongol_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(162.7, 5.3),[],260),
  ("castle_39","Mosul",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.8, 7.5),[],280),
  ("castle_40","Bukhara",icon_icon_mongol_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(183.9, 83),[],260),

  ("castle_41","Damietta",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.3, -42.1),[],260),
  ("castle_42","Bilbeis",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-78.3, -64.1),[],260),
  ("castle_43","Aqaba",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.3, -84.1),[],260),
  ("castle_44","Ismailia",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.3, -58.1),[],260),
  ("castle_45","Damanhur",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-88.3, -53.1),[],260),
  ("castle_46","Suez",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-58.3, -68.1),[],260),
  ("castle_47","Darum",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.3, -40.1),[],260),
  ("castle_48","Be'er Sheva",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.3, -39.1),[],180),
   ("castle_49","Siraz",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.3, -42.1),[],180),
   ("castle_50","Bandar Abbas",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.3, -82.1),[],180),
   ("castle_51","Kerman",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.3, -31.1),[],180),
   ("castle_52","Zahedan",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(146.3, -49.1),[],180),
   ("castle_53","Hyderabad",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(189.3, -89.1),[],180),
   ("castle_54","Khairpur",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(196.3, -80.1),[],180),
   ("castle_55","Bahawalpur",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(211.3, -62.1),[],180),

   ("castle_56","El-Kadiriye",icon_icon_saracen_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.3, -27.1),[],180),
      
	  ("castle_57","Azov",icon_icon_mongol_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.3, 159.1),[],180),
      ("castle_58","Sarai Berke",icon_icon_mongol_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.3, 184.1),[],180),
      ("castle_59","Sarai Batu",icon_icon_mongol_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.3, 130.1),[],180),
#yeni kaleler     
	 ("castle_60","Rhizaum",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.3, 83.1),[],180),
      ("castle_61","Comana",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.3, 69.1),[],180),
      ("castle_62","Soli",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.73, 29.19),[],225),
      ("castle_63","Selinus",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.3, 30.1),[],180),
      ("castle_64","Gori",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.3, 95.1),[],180),
      ("castle_65","Batumi",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.3, 88.1),[],180),
      ("castle_66","Gandza",icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.3, 81.1),[],180),
      ("castle_67","Fermo",icon_icon_bzt_castle3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-232.3, 105.1),[],180),
      ("castle_68","Comacchin",icon_icon_bzt_castle3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-247.3, 125.1),[],180),
      ("castle_69","Bologna",icon_icon_bzt_castle3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-260.3, 123.1),[],180),
      ("castle_70","Nikopol",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-141.3, 125.1),[],180),
      ("castle_71","Silistra",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-116.3, 129.1),[],180),
      ("castle_72","Targovishte",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-141.3, 140.1),[],180),


#     Rinimad      
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
  ####Svadyalilar
  ("village_1", "Tarsus",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53, 35.5),[], 100),
  ("village_2", "Misis",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43, 34.5),[], 100),
  ("village_3", "Kilis",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24, 29.5),[], 100),
  ("village_4", "Yafa",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40, -7.5),[],260),
  ("village_5", "Halep",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23, 23.5),[], 100),
  ("village_6", "Arca",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33, 10.5),[], 100),
  ("village_7", "Krak",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31, 15.5),[], 100),
  ("village_8", "Bsharri",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33, 1.5),[], 100),
  ("village_9", "Jubayl",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41, -4.5),[], 100),
  ("village_10","Ba'labak",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30, -7.5),[], 100),
  ("village_11","Zahlah",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35, -3.5),[], 100),
  ("village_12","Sidon",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42, -9.5),[], 100),
  ("village_13","An Nabatiyah",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38, -12.5),[], 100),
  ("village_14","Haifa",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46, -29.5),[], 100),
  ("village_15","Homs",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30, 5.5),[], 100),
  
  #####Vaegirliler
  ("village_16","Eskisehir",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70, 69.8),[], 170),
  ("village_17","Aksaray",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47, 49.8),[], 170),
  ("village_18","Sinop",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.5, 92.3),[],100),
  ("village_19","Kars",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12, 79.8),[], 170),
  ("village_20","Van",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19, 56.8),[], 170),
  ("village_21","Harran",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.7, 39.4),[],280),
  ("village_22","Bayburt",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6, 67.8),[], 170),
  ("village_23","Erzurum",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.72, 76.8),[], 170),
  ("village_24","Bitlis",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6, 46.8),[], 170),
  ("village_25","Mus",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4, 49.8),[], 170),
  ("village_26","Malazgirt",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11, 64.8),[], 170),
  ("village_27","Harput",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21, 53.8),[], 170),
  ("village_28","Aksehir",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-78, 58.8),[], 170),
  ("village_29","Kutahya",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82, 60.8),[], 170),
  ("village_30","Antalya",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83, 38.8),[], 170),
  
  #####Mongol
  ("village_31","Merv",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(131, 42),[], 100),
  ("village_32","Nishapur",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107, 31),[], 100),
  ("village_33","Kabul",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(188, -3),[], 100),
  ("village_34","Yarkand",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(237, 78),[], 100),
  ("village_35","Xiva",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(166, 118),[], 100),
  ("village_36","Dasoguz",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(156, 130),[], 100),
  ("village_37","Navoiy",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(193, 89),[], 100),
  ("village_38","Qarshi",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(193, 66),[], 100),
  ("village_39","Termiz",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(210, 54),[], 100),
  ("village_40","Kunduz",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(220, 51),[], 100),
  ("village_41","Gorgan",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103, 26),[], 100),
  ("village_42","Kandahar",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(180, -21),[], 100),
  ("village_43","Farah",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(161, -12),[], 100),
  ("village_44","Anar Dara",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(156, -7),[], 100),
  ("village_45","Aktobe",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(227, 122),[], 100),
  
  ##Bizans
  ("village_46","Erythrai",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118.8, 52.5),[], 110),
  ("village_47","Aydin",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-101.8, 45.5),[], 110),
  ("village_48","Gelibolu",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-111.8, 73.5),[], 110),
  ("village_49","Iznik",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-90.8, 73.5),[], 110),
  ("village_50","Izmit",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.8, 77.5),[], 110),
  ("village_51","Manisa",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.8, 58.5),[], 110),
  ("village_52","Gebze",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-88.8, 80.5),[], 110),
  ("village_53","Corlu",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.8, 87.5),[], 110),
  ("village_54","Avlonya",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-187.8, 56.5),[], 110),
  ("village_55","Berat",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-183.8, 71.5),[], 110),
  ("village_56","Ohri",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-178.8, 76.5),[], 110),
  ("village_57","Kirklareli",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.8, 94.5),[], 110),
  ("village_58","Ihilman",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-155.8, 101.5),[], 110),
  ("village_59","Yenisehir",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-167.8, 53.5),[], 110),
  ("village_60","Yanya",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-180.5, 60.6),[],100),

  ####Hashasiler
  ("village_61","Navisar Shah",  icon_icon_assasin_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.8, 4.65),[], 100),
  ("village_62","Shahrak",  icon_icon_assasin_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.8, 1.65),[], 100),
  ("village_63","Lamasar",  icon_icon_assasin_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.8, 9.65),[], 100),
  ("village_64","Kulej",  icon_icon_assasin_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.8, -6.65),[], 100),
  ("village_65","Narah",  icon_icon_assasin_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.8, 14.65),[], 100),
  ("village_66","Atan",  icon_icon_assasin_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.8, 2.65),[], 100),
  ("village_67","Lat",  icon_icon_assasin_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.8, 23.65),[], 100),
  
  ###Selcuklu koyleeri
  ("village_68","Sahand",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.8, 31.65),[], 100),
  ("village_69","Agsu",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.8, 69.65),[], 100),
  ("village_70","Pirqulu",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.8, 78.65),[], 100),

  ("village_71","Sumqayit",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(54.2, 73.22),[], 100),
  ("village_72","Naxcivan",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.8, 63.65),[], 100),
  
  ##Mongol extra koyler
  ("village_73","Loyish",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(203.8, 86.65),[], 100),
  ("village_74","Jizzax",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(222.8, 88.65),[], 100),
  #gazli sahnesine sahip koyler
  ("village_75","Alat",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(166.8, 70.65),[], 100),
  ("village_76","Gazli",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(158.8, 91.65),[], 100),
  ("village_77","Forish",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(213.8, 101.65),[], 100),
  ("village_78","Bulakbashi",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(199.8, 96.65),[], 100),
  ("village_79","Karokh",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(185.8, 21.65),[], 100),
  ("village_80","Nuqra",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(157.8, 7.65),[], 100),
##Sarranidler
  ("village_81","El-Hamam",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.6, -51.3),[], 20),
  ("village_82","Disuq",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.6, -49.3),[], 20),
  ("village_83","Rashid",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.6, -41.3),[], 20),
  ("village_84","Banha",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-78.6, -70.3),[], 20),
  ("village_85","El-Thamad",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.6, -74.3),[], 20),
  ("village_86","Shirbin",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.6, -48.3),[], 20),
  
  ##Vaegir ek koyler
  ("village_87","Nasiriye",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.6, -41.3),[], 20),
  ("village_88","Erbil",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(23.6, 5.3),[], 20),
  ("village_89","Hilla",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.6, -25.3),[], 20),
  ("village_90","Samarra",  icon_icon_turk_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.6, -6.3),[], 20),
 ##Sarranid
  ("village_91","Helwan",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.6, -82.3),[], 20),
  ("village_92","Al Qababt",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.6, -88.3),[], 20),
  ("village_93","Sintimay",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.6, -56.3),[], 20),
  ("village_94","Abu Zenima",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.6, -73.3),[], 20),
  ("village_95","Hebron",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.6, -35.3),[], 20),
  ("village_96","Rafah",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.6, -37.3),[], 20),
  ("village_97","Madaba",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.6, -32.3),[], 20),
  ("village_98","Karak",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.6, -39.3),[], 20),
  ("village_99","Sahab",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.6, -26.3),[], 20),
  ("village_100","Dumayr",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.6, 4.3),[], 20),

  ("village_101","Qatan",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.6, -3.3),[], 20),
  ("village_102","Al Zumayra",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.6, -35.3),[], 20),
  ("village_103","Al Hassa",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.6, -39.3),[], 20),
  ("village_104","Bethlehem",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.6, -35.3),[], 20),
  ("village_105","Gadres",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.6, -45.3),[], 20),
  ("village_106","Semova",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.6, -42.3),[], 20),
  ("village_107","Abila",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18.6, 4.3),[], 20),
  ("village_108","Sevlon",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.6, -20.3),[], 20),
  ("village_109","Beni Suef",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.6, -96.3),[], 20),
  ("village_110","Faiyum",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.6, -92.3),[], 20),
    ("village_111","Kazerun",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.6, -42.3),[], 20),
  ("village_112","Shahrekord",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.6, -30.3),[], 20),
  ("village_113","Shahreza",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.6, -30.3),[], 20),
  ("village_114","Minab",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.6, -88.3),[], 20),
  ("village_115","Mahan",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.6, -35.3),[], 20),
  ("village_116","MirJaveh",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(151.6, -55.3),[], 20),
  ("village_117","Mirpur Khas",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(205.6, -85.3),[], 20),
  ("village_118","Rasoolpur",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(201.6, -63.3),[], 20),
  ("village_119","Gaddani",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(147.6, -104.3),[], 20),
  ("village_120","HaJi Sheedi",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(185.6, -102.3),[], 20),
  ("village_121","Shileh",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(145.6, -41.3),[], 20),
  ("village_122","Nosrat Abad",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(131.6, -39.3),[], 20),

    ("village_123","Shamiyah",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.6, -44.3),[], 20),
  ("village_124","Samawah",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.6, -40.3),[], 20),
  ("village_125","Al-Fallujah",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.6, -16.3),[], 20),
  ("village_126","Madain",  icon_icon_arab_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.6, -19.3),[], 20),
  #Kipcak koyler
    ("village_127","Kerch",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.6, 134.3),[], 20),
	  ("village_128","Bataysk",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.6, 158.3),[], 20),
  ("village_129","Shakhty",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.6, 180.3),[], 20),
  ("village_130","Basy",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.6, 123.3),[], 20),
  ("village_131","Lagan",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.6, 115.3),[], 20),
    ("village_132","Narimanov",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.6, 142.3),[], 20),
  ("village_133","Sudak",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.6, 127.3),[], 20),
  ("village_134","Elista",  icon_icon_mongol_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.6, 138.3),[], 20),
  
  #abbasi koyler
  
    ("village_135","Salamis",  icon_icon_crusader_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57, 15.5),[], 100),
    #papal
	("village_136","Sutri",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-251, 93.5),[], 100),
    ("village_137","Nursia",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-238, 91.5),[], 100),
    ("village_138","Pesaro",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-240, 113.5),[], 100),
    ("village_139","Ancona",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-234, 110.5),[], 100),
    ("village_140","Ravenna",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-246, 121.5),[], 100),
    ("village_141","Faenza",  icon_icon_bzt_village|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-252, 121.5),[], 100),
	#bulgar
    ("village_142","Vchina",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-91, 146.5),[], 100),
    ("village_143","Severin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-163, 142.5),[], 100),
    ("village_144","Lom",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-160, 133.5),[], 100),
    ("village_145","Lovoch",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-143, 119.5),[], 100),
    ("village_146","Cherven",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125, 123.5),[], 100),
	#kibris
    ("village_147","Anamur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67, 27.5),[], 100),
    ("village_148","Gulnar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65, 31.5),[], 100),
    ("village_149","Ghazipasha",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-75, 32.5),[], 100),
	#trabzon
    ("village_150","Turhal",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31, 70.5),[], 100),
    ("village_151","Surmene",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7, 82.5),[], 100),
    ("village_152","Tirebolu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19, 80.5),[], 100),
    ("village_153","Macka",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14, 75.5),[], 100),
    #gurci
	("village_154","Koboleti",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4, 90.5),[], 100),
    ("village_155","Samtredia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9, 93.5),[], 100),
    ("village_156","Kaspi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27, 91.5),[], 100),
    ("village_157","Rustavi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38, 87.5),[], 100),
    ("village_158","Tovuz",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42, 85.5),[], 100),
    #bizans ek
	("village_159","Dobrich",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105, 116.5),[], 100),
    ("village_160","Haskova",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-127, 103.5),[], 100),




  ("salt_mine","Salt_Mine",icon_icon_arab_village|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.2, 31),[]),
  ("four_ways_inn","Four_Ways_Inn",icon_icon_arab_village|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.8, 39.6),[]),
  ("test_scene","test_scene",icon_icon_arab_village|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.8, 19.6),[]),
  ("test_scene","test_scene",icon_icon_arab_village|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.8, 19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_icon_arab_village|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.8, 16.6),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50,58),[]),

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(192, 83),[]),

  ("training_ground_1", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110.4, -50.8),[], 100),
  ("training_ground_2", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.8, 0),[], 100),
  ("training_ground_3", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-153.5, 76.0),[], 100),
  ("training_ground_4", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.5, -8.2),[], 100),
  
  ("training_ground_5", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.8, 58.5),[], 100),
 # ("training_ground_6", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-253.5, 107.2),[], 100),
 # ("training_ground_7", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-130.5, 129.2),[], 100),
 # ("training_ground_8", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.5, 128.2),[], 100),
 # ("training_ground_9", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.5, 96.2),[], 100),
 # ("training_ground_10", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.5, 74.2),[], 100),
 # ("training_ground_11", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.5, 14.2),[], 100),
 # ("training_ground_12", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.5, -24.2),[], 100),
 # ("training_ground_13", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.5, -60.2),[], 100),
 # ("training_ground_14", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(181.5, 91.2),[], 100),


#  bridge_a
  ("Bridge_1","{!}1",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),
  ("Bridge_2","{!}2",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),
  ("Bridge_3","{!}3",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),
  ("Bridge_4","{!}4",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),
  ("Bridge_5","{!}5",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),
  ("Bridge_6","{!}6",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),
  ("Bridge_7","{!}7",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),
  ("Bridge_8","{!}8",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),
  ("Bridge_9","{!}9",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),
  ("Bridge_10","{!}10",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),
  ("Bridge_11","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),
  ("Bridge_12","{!}12",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),
  ("Bridge_13","{!}13",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),
  ("Bridge_14","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-307.37, -220.10),[], -44.8),

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-26, -77),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(197, 85),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(69, 0),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-132, 95),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(27, 58.8),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-110.5, 60),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-110.5, 60),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-9, -12),[(trp_looter,15,0)]),
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
    ("kervansaray","Caravanserai",icon_icon_kervansaray|pf_is_static|pf_always_visible|pf_label_large|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.75, -7.5),[],95),
   #altin madeni
   ("kervansaray2","Caravanserai",icon_icon_kervansaray|pf_is_static|pf_always_visible|pf_label_large|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.75, 14.5),[],95),
#at ciftligi
   ("kervansaray3","Caravanserai",icon_icon_kervansaray|pf_is_static|pf_always_visible|pf_label_large|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.75, 64.5),[],95),
	#bugday tarlasi
	("freelancer_party_backup","{!}",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
	("wagon_train","Wagon Train",pf_disabled|icon_gray_knight|carries_goods(20), no_menu, pt_none, fac_player_faction,0,escorted_merchant_personality,0,(5.23,-90.26),[(trp_wagon_master,1,0)]),
   ("pecenek_yeri","Pecheneg Village",icon_icon_mongol_village|pf_is_static|pf_always_visible|pf_label_large|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.75, 136.5),[],95),
   ("kayi_obasi","Kayig Clan",icon_icon_mongol_village|pf_is_static|pf_always_visible|pf_label_medium|pf_hide_defenders, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(-20.75, 27.5),[],95),
      ("oncu_birlik","Oncu Birlikler",icon_camp|pf_is_static|pf_always_visible|pf_label_medium|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.75, 35.5),[],95),
   ("parali_asker_kampi_1","Mercenary Camp",icon_camp|pf_is_static|pf_always_visible|pf_label_medium|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(116.75, -32.5),[],95),
   ("parali_asker_kampi_2","Mercenary Camp",icon_camp|pf_is_static|pf_always_visible|pf_label_medium|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.75, -5.5),[],95),
   ("parali_asker_kampi_3","Mercenary Camp",icon_camp|pf_is_static|pf_always_visible|pf_label_medium|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-104.75, 72.5),[],95),
   ("parali_asker_kampi_4","Mercenary Camp",icon_camp|pf_is_static|pf_always_visible|pf_label_medium|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.75, 97.5),[],95),
   ("parali_asker_kampi_5_test","Mercenary Camp",icon_camp|pf_is_static|pf_disabled|pf_label_medium|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.75, 27.5),[],95),


  ]
# modmerger_start version=201 type=2
try:
    component_name = "parties"
    var_set = { "parties" : parties }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
