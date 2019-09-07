# THIS SCRIPT SHOULD BE CALLED SETUP.PY
import cx_Freeze 

executables = [cx_Freeze.Executable("EBTA.py")]

cx_Freeze.setup( 
        name = "Eng Phys Text Adventure",
        version = "0.30",
        description = "THE GREAT ENG PHYS TEXT ADVENTURE!",
        options = {"build_exe": {"packages":["pygame"]}},
        executables = executables)


#python setup.py build
#python setup.py bdist_msi


#after main file
##display_width = 800
##display_height = 600
##
##gameDisplay = pygame.display.set_mode((display_width,display_height))
##
##audiopath = os.path.join(os.getcwd(), "MediaAssets","","ErikBeepBoxSong.mp3")
##pygame.mixer.music.load(audiopath)
##pygame.mixer.music.play(-1)
###fire_sound = pygame.mixer.Sound("boom.wav")
###pygame.mixer.Sound.play(fire_sound)
