@echo off
cd /d "%~dp0"

C:\Python27\python.exe process_init.py
C:\Python27\python.exe process_global_variables.py
C:\Python27\python.exe process_strings.py
C:\Python27\python.exe process_skills.py
C:\Python27\python.exe process_music.py
C:\Python27\python.exe process_animations.py
C:\Python27\python.exe process_meshes.py
C:\Python27\python.exe process_sounds.py
C:\Python27\python.exe process_skins.py
C:\Python27\python.exe process_map_icons.py
C:\Python27\python.exe process_factions.py
C:\Python27\python.exe process_items.py
C:\Python27\python.exe process_scenes.py
C:\Python27\python.exe process_troops.py
C:\Python27\python.exe process_particle_sys.py
C:\Python27\python.exe process_scene_props.py
C:\Python27\python.exe process_tableau_materials.py
C:\Python27\python.exe process_presentations.py
C:\Python27\python.exe process_party_tmps.py
C:\Python27\python.exe process_parties.py
C:\Python27\python.exe process_quests.py
C:\Python27\python.exe process_info_pages.py
C:\Python27\python.exe process_scripts.py
C:\Python27\python.exe process_mission_tmps.py
C:\Python27\python.exe process_game_menus.py
C:\Python27\python.exe process_simple_triggers.py
C:\Python27\python.exe process_dialogs.py
C:\Python27\python.exe process_global_variables_unused.py
C:\Python27\python.exe process_postfx.py

@del *.pyc
echo.
echo ______________________________
echo.
echo Script processing has ended.
echo Press any key to exit. . .
pause>nul
