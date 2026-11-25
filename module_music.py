from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
##  ("losing_battle", "alosingbattle.mp3", sit_calm|sit_action),
##  ("reluctant_hero", "reluctanthero.mp3", sit_action),
##  ("the_great_hall", "thegreathall.mp3", sit_calm),
##  ("requiem", "requiem.mp3", sit_calm),
##  ("silent_intruder", "silentintruder.mp3", sit_calm|sit_action),
##  ("the_pilgrimage", "thepilgrimage.mp3", sit_calm),
##  ("ambushed", "ambushed.mp3", sit_action),
##  ("triumph", "triumph.mp3", sit_action),

##  ("losing_battle", "alosingbattle.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("reluctant_hero", "reluctanthero.mp3", mtf_sit_attack),
##  ("the_great_hall", "thegreathall.mp3", mtf_sit_map_travel),
##  ("requiem", "requiem.mp3", mtf_sit_map_travel),
##  ("silent_intruder", "silentintruder.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("the_pilgrimage", "thepilgrimage.mp3", mtf_sit_map_travel),
##  ("ambushed", "ambushed.mp3", mtf_sit_attack),
##  ("triumph", "triumph.mp3", mtf_sit_attack),
  ("bolu_beyi_main", "bolu_beyi.mp3", mtf_start_immediately|mtf_sit_main_title, 0),
  ("Orden_der_Tempelritter", "Orden_der_Tempelritter.mp3", mtf_start_immediately|mtf_sit_main_title, 0),
  ("harry_gregson-williams_-_ibelin", "harry_gregson-williams_-_ibelin.mp3", mtf_start_immediately|mtf_sit_main_title, 0),
  ("harry_gregson-williams_-_to_jerusalem", "harry_gregson-williams_-_to_jerusalem.mp3", mtf_start_immediately|mtf_sit_main_title, 0),
  ("Sacrifice", "Sacrifice.mp3", mtf_sit_ambushed, mtf_sit_fight),
  ("Solace_-_Sword_Dance_Routine", "Solace_-_Sword_Dance_Routine.mp3", mtf_sit_ambushed, mtf_culture_1|mtf_culture_2|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_fight),
  ("Swordsman", "Swordsman.mp3", mtf_culture_4|mtf_sit_ambushed, mtf_culture_1|mtf_culture_2|mtf_culture_5|mtf_culture_6|mtf_sit_fight),
  ("castlejam", "castlejam.mp3", mtf_culture_4|mtf_sit_fight, mtf_culture_1|mtf_culture_2|mtf_culture_5|mtf_culture_6|mtf_sit_fight),
  ("Quan_vei_la_lauzeta_mover", "Quan_vei_la_lauzeta_mover.mp3", mtf_culture_4|mtf_sit_fight, mtf_culture_1|mtf_culture_2|mtf_culture_5|mtf_culture_6|mtf_sit_fight),
  ("Riders_Of_The_Night", "Riders_Of_The_Night.mp3", mtf_culture_5|mtf_sit_ambushed, mtf_culture_1|mtf_culture_2|mtf_culture_4|mtf_culture_6|mtf_sit_fight),
  ("Wings_Of_Glory", "Wings_Of_Glory.mp3", mtf_culture_1|mtf_sit_ambushed, mtf_culture_2|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_fight),
  ("Seafights", "Seafights.mp3", mtf_culture_2|mtf_sit_ambushed, mtf_culture_1|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_fight),
  ("Solace_-_Beledi", "Solace_-_Beledi.mp3", mtf_culture_6|mtf_sit_ambushed, mtf_culture_1|mtf_culture_2|mtf_culture_4|mtf_culture_5|mtf_sit_fight),
 #arena
  ("seigneurs", "seigneurs.mp3", mtf_sit_arena, 0),
  ("arena_2", "Aegean_Sailor.mp3", mtf_sit_arena, 0),
  ("arena_3", "ambushed_by_khergit.mp3", mtf_sit_arena, 0),
  ("arena_4", "east_meets_east.mp3", mtf_sit_arena, 0),
  ("arena_5", "enter_the_warrior.mp3", mtf_sit_arena, 0),
  
  #tavern
  ("tavern_1", "Tavern_music.mp3", mtf_sit_tavern,mtf_sit_tavern),
  ("tavern_2", "turkish_folk.mp3", mtf_culture_2|mtf_sit_tavern,mtf_sit_travel, 0),#selcuk taverna, travel,
  ("tavern_3", "old_turkish_ciftetelli.mp3", mtf_culture_2|mtf_sit_tavern,mtf_sit_travel, 0),#selcuk taverna ve travel
  
  #mongol
  ("travel_khergit", "travel_khergit.mp3", mtf_culture_3|mtf_culture_10|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_all),
  ("chinggis_khaanii_magtaal_batzorig_vaanchig", "chinggis_khaanii_magtaal_batzorig_vaanchig.mp3", mtf_culture_3|mtf_culture_10|mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night|mtf_culture_3|mtf_culture_10),
  ("infiltration_khergit", "infiltration_khergit.mp3", mtf_culture_3|mtf_culture_10|mtf_sit_town_infiltrate, mtf_culture_all),
  ("ambushed_by_khergit", "ambushed_by_khergit.mp3", mtf_culture_3|mtf_culture_10|mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_culture_all),
  ("mongol_1", "mongol_1.mp3", mtf_culture_3|mtf_culture_10|mtf_sit_siege|mtf_sit_travel|mtf_sit_fight, 0),
  
  #seljuk
  ("seljuk_1", "old_ottoman.mp3", mtf_culture_2|mtf_sit_siege|mtf_sit_travel|mtf_sit_fight|mtf_sit_town, mtf_culture_2|mtf_sit_siege|mtf_sit_travel|mtf_sit_fight),
  ("seljuk_2", "olad_ottoman_cemil_bey.mp3", mtf_culture_2|mtf_sit_travel|mtf_sit_town, mtf_culture_2|mtf_sit_travel), #travel sadece
  ("bolu_beyi", "bolu_beyi.mp3", mtf_culture_2|mtf_sit_travel|mtf_sit_town, mtf_culture_2|mtf_sit_travel), #travel sadece
  ("kuzgun", "kuzgun.mp3", mtf_culture_all|mtf_sit_ambushed, 0), #travel sadece


  
  
  ("Rapsodia", "Rapsodia.mp3", mtf_culture_1|mtf_start_immediately|mtf_sit_night, mtf_sit_town),
  ("O_quanta_qualia", "O_quanta_qualia.mp3", mtf_culture_2|mtf_start_immediately|mtf_sit_night, mtf_sit_town),
  ("Sancta_Maria_(Mascagni)", "Sancta_Maria_(Mascagni).mp3", mtf_culture_4|mtf_start_immediately|mtf_sit_night, mtf_sit_town),
  ("Two_medieval_melodies", "Two_medieval_melodies.mp3", mtf_culture_5|mtf_start_immediately|mtf_sit_night, mtf_sit_town),
  ("capture", "capture.mp3", mtf_persist_until_finished, 0),
  ("coronation", "capture.mp3", mtf_persist_until_finished, 0),
  ("Rast_Medhal", "Rast_Medhal.mp3", mtf_culture_6|mtf_persist_until_finished, 0),
  ("captured", "Rast_Medhal.mp3", mtf_culture_6|mtf_persist_until_finished, 0),
  ("escape", "escape.mp3", mtf_persist_until_finished, 0),
  ("empty_village", "escape.mp3", mtf_persist_until_finished, 0),
  ("enter_the_warrior", "enter_the_warrior.mp3", mtf_culture_6|mtf_sit_fight|mtf_sit_ambushed, 0),
  ("ambushed_by_rhodok", "enter_the_warrior.mp3", mtf_culture_6|mtf_sit_fight|mtf_sit_ambushed, 0),
  ("east_meets_east", "east_meets_east.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed, 0),
  ("Aegean_Sailor", "Aegean_Sailor.mp3", mtf_sit_fight|mtf_sit_ambushed, 0),
  ("Main_Theme_-_Score", "Main_Theme_-_Score.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed, 0),
  ("Crusade", "Crusade.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed, 0),
  ("Carl_Orff_-_Carmina_Burana", "Carl_Orff_-_Carmina_Burana.mp3", mtf_culture_all|mtf_sit_fight, 0),
  ("Lacrimosa", "Lacrimosa.mp3", mtf_culture_all|mtf_sit_fight|mtf_sit_ambushed, 0),
  ("Battle_Of_Knights", "Battle_Of_Knights.mp3", mtf_culture_all|mtf_sit_fight, 0),
  ("killed_by_neutral", "killed_by_neutral.mp3", mtf_culture_6|mtf_persist_until_finished|mtf_sit_killed, 0),
  ("fiasco", "fiasco.mp3", mtf_culture_1|mtf_persist_until_finished|mtf_sit_killed, 0),
  ("castlejam", "castlejam.mp3", mtf_culture_4, mtf_culture_1|mtf_culture_2|mtf_culture_5|mtf_culture_6|mtf_sit_tavern),
  ("harry_gregson-williams_-_ibelin", "harry_gregson-williams_-_ibelin.mp3", mtf_culture_all, mtf_start_immediately),
  ("unquest_grave", "unquest_grave.mp3", mtf_culture_2, mtf_start_immediately|mtf_sit_tavern),
  ("Quan_vei_la_lauzeta_mover", "Quan_vei_la_lauzeta_mover.mp3", mtf_culture_5|mtf_culture_6, mtf_start_immediately|mtf_sit_tavern),
  ("minstrell_hall", "minstrell_hall.mp3", mtf_culture_4|mtf_start_immediately|mtf_sit_town, 0),
  ("harry_gregson-williams_-_the_king", "harry_gregson-williams_-_the_king.mp3", mtf_culture_1|mtf_start_immediately|mtf_sit_town, 0),
  ("Dame_de_qui_toute_ma_joie_vient", "Dame_de_qui_toute_ma_joie_vient.mp3", mtf_culture_5|mtf_start_immediately|mtf_sit_town, 0),
  ("planxty_corcoran", "planxty_corcoran.mp3", mtf_culture_2|mtf_start_immediately|mtf_sit_town, 0),
  ("harry_gregson-williams_-_saladin", "harry_gregson-williams_-_saladin.mp3", mtf_culture_6|mtf_start_immediately|mtf_sit_town, 0),
  ("Maktub", "Maktub.mp3", mtf_sit_town_infiltrate|mtf_culture_6, 0),
  ("thechant", "thechant.mp3", mtf_sit_siege, mtf_sit_multiplayer_fight|mtf_sit_ambushed),
  ("Douce_dame_jolie", "Douce_dame_jolie.mp3", mtf_sit_multiplayer_fight|mtf_sit_siege, 0),
  ("final_battle", "final_battle.mp3", mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("Constantinopolis", "Constantinopolis.mp3", mtf_sit_town, 0),
  ("Entre_Av'e_Eva", "Entre_Av'e_Eva.mp3", mtf_culture_all|mtf_start_immediately|mtf_sit_town, 0),
  ("Dame_mon_cuer_en_vouis_remaint", "Dame_mon_cuer_en_vouis_remaint.mp3", mtf_culture_5|mtf_sit_town, mtf_culture_1|mtf_culture_2|mtf_culture_4|mtf_culture_6),
  ("allelujah", "allelujah.mp3", mtf_culture_1|mtf_sit_town, mtf_culture_2|mtf_culture_4|mtf_culture_5|mtf_culture_6|mtf_sit_night),
  ("harry_gregson-williams_-_sibylla", "harry_gregson-williams_-_sibylla.mp3", mtf_culture_all|mtf_start_immediately|mtf_sit_town|mtf_sit_night, 0),
  ("Scenes_of_Istanbul", "Scenes_of_Istanbul.mp3", mtf_sit_travel, 0),
  ("KINGHT_TEMPLAR-FRENCH_SONG_CHANT", "KINGHT_TEMPLAR-FRENCH_SONG_CHANT.mp3", mtf_culture_4|mtf_sit_travel, 0),
  ("harry_gregson-williams_-_burning_the_past", "harry_gregson-williams_-_burning_the_past.mp3", mtf_culture_5|mtf_sit_travel, 0),
  ("harry_gregson-williams_-_to_jerusalem", "harry_gregson-williams_-_to_jerusalem.mp3", mtf_culture_1|mtf_sit_travel, 0),
  ("unquest_grave", "unquest_grave.mp3", mtf_culture_2|mtf_sit_travel, 0),
  ("White_Summer", "White_Summer.mp3", mtf_culture_6|mtf_sit_travel, 0),
  ("Donna,_pos_vos_ay_chausida", "Donna,_pos_vos_ay_chausida.mp3", mtf_culture_5|mtf_culture_6|mtf_sit_travel, 0),
  ("victorious_evil", "victorious_evil.mp3", mtf_persist_until_finished, 0),
  ("Foy_porter", "Foy_porter.mp3", mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("appytimes", "appytimes.mp3", mtf_culture_1|mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("imperator_rex_graecorum", "imperator_rex_graecorum.mp3", mtf_culture_2|mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("I_Believe_I_Saw_an_Angel", "I_Believe_I_Saw_an_Angel.mp3", mtf_culture_4|mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("Gloria_a_te,_Cristo_Gesu", "Gloria_a_te,_Cristo_Gesu.mp3", mtf_culture_5|mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("Trophies_&_Memorials", "Trophies_&_Memorials.mp3", mtf_culture_5|mtf_culture_6|mtf_persist_until_finished|mtf_sit_victorious, 0),
  ("wedding", "wedding.mp3", mtf_persist_until_finished, 0),
  ("harry_gregson-williams_-_coronation", "harry_gregson-williams_-_coronation.mp3", mtf_persist_until_finished, 0),
  

  
]
# modmerger_start version=201 type=4
try:
    component_name = "music"
    var_set = { "tracks":tracks, }
    from modmerger import modmerge
    modmerge(var_set, component_name)
except:
    raise
# modmerger_end
