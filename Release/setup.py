# THIS SCRIPT SHOULD BE CALLED SETUP.PY
import cx_Freeze 

#This list includes files and folders. Path must be relatie to the compile program
includefiles = ["Readme How to Run the game.txt","Patch Notes for Release.txt", "MediaAssets"]
includes = []
excludes = []
packages = ["pygame"]  #This list includes important packages/modules!

#executables = [cx_Freeze.Executable("EBTA.py")]

target = cx_Freeze.Executable(
    script="EngPhysAdventure Alpha v0.30.py",
    #base="Win64GUI",
    #targetDir = r"dist",
    targetName = "EngPhys Text Adventure.exe",
    #compress=False,
    #copyDependentFiles=True,
    #appendScriptToExe=True,
    #appendScriptToLibrary=False,
    icon="newicon_Hbg_icon.ico",
    shortcutName = "EPTA",
    shortcutDir = "DesktopFolder",
    
    )

cx_Freeze.setup( 
        name = "Eng Phys Text Adventure",
        version = "0.30",
        description = "THE GREAT ENG PHYS TEXT ADVENTURE!",
        author = "13 Hollywood Productions",
        options = {"build_exe": {"packages":packages,'include_files':includefiles}},
        executables = [target]
        )


print "Make sure the CSV files are disabled!"

### Use this to run a build folder
#python setup.py build
### Use this to make an installer in dist folder
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
