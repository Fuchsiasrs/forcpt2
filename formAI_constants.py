# Formations AI by Motomataru
# rel. 08/31/2012

#AI variables
AI_long_range	= 13000	#do not put over 130m if you want archers to always fire
AI_firing_distance	= AI_long_range / 2
AI_charge_distance	= 2000
AI_for_kingdoms_only	= 0
Percentage_Cav_For_New_Dest	= 40
Hold_Point	= 100	#archer hold if outnumbered
Advance_More_Point	= 100 - Hold_Point * 100 / (Hold_Point + 100)	#advance 'cause expect other side is holding
AI_Max_Reinforcements	= 2	#maximum number of reinforcement stages in a battle
AI_Replace_Dead_Player	= 1
AI_Poor_Troop_Level	= 12	#average level of troops under which a division may lose discipline
AI_Max_Size_Oblong_Formations	= 48	#size above which AI will make a (more maneuverable) square (typical Roman lines 40 w x 7.5 d; here 16 w x 3 d)

#Battle Phases
BP_Setup	= 1
BP_Jockey	= 2
BP_Fight	= 3

#positions used in a script, named for convenience
Nearest_Enemy_Troop_Pos	= 48	#pos48	used only by infantry AI
Nearest_Enemy_Battlegroup_Pos	= 50	#pos50	used only by ranged AI
Nearest_Threat_Pos	= Nearest_Enemy_Troop_Pos	#used only by cavalry AI
Nearest_Target_Pos	= Nearest_Enemy_Battlegroup_Pos	#used only by cavalry AI
Infantry_Pos	= 51	#pos51
Archers_Pos	= 53	#pos53
Cavalry_Pos	= 54	#pos54
Team_Starting_Point	= 55	#pos55

#positions used through battle
Team0_Cavalry_Destination	= 56	#pos56
Team1_Cavalry_Destination	= 57	#pos57
Team2_Cavalry_Destination	= 58	#pos58
Team3_Cavalry_Destination	= 59	#pos59
