# ENG PHYS TEXT  ADVENTURE
# Mitchell Lemieux, Tyler Kashak, and Brendan Fallon
# Overhauled to CX_Freeze on Oct 27,2019 by Brendan Fallon:

"""
This is the file used with CX_Freeze to make the game into an EXE.
All you need to know is two things:
1. Have ALL file in the main directory (setup.py, the icon, readme, and changelog)
2. Open command prompt and navigate to the main directory.
3. Run "python setup.py bdist_msi" to make the installer OR "python setup.py build" to make JUST the EXE. 

As for the code:
Bassically CX_Freeze and py2exe are just running a portalable python interpruter and the launcher is an EXE.
So nothing is actually being compilied but I like to call it compiling just because it's condensing into one usable source.
A lot of this is utalizing dist_utils and MSI which I don't understand so sorry for the lack of comments.
I tried to give sources where possible but a lot of it is just google searching "CX_Freeze X".
The variable names should be fairely easy to understands

Sources:
How to include files - https://stackoverflow.com/questions/2553886/how-can-i-bundle-other-files-when-using-cx-freeze
How to make a desktop/start menu shortchut with the icon -
https://stackoverflow.com/questions/15734703/use-cx-freeze-to-create-an-msi-that-adds-a-shortcut-to-the-desktop
https://bitbucket.org/anthony_tuininga/cx_freeze/issues/48/documentation-of-how-to-create-desktop-or

Thank you to Anythony Tuininga for this awesome module and all the work!
"""


# THIS SCRIPT SHOULD BE CALLED SETUP.PY

# I like keeping this import here instead of 'from cx_Freeze import *' so I can know what's coming from cx_Freeze and what's not
import cx_Freeze  

#This list includes files and folders. Path must be relative to the compile program
includefiles = ["Readme How to Run the game.txt","Patch Notes for Release.txt", "settings.ini", "MediaAssets"]
includes = []
excludes = []
#packages = ["pygame"]  #This list includes the names important packages/modules that need to be included
packages = ["cPickle"]

#This governs the shortcut
cx_Freeze.shortcut_table = [
    ("DesktopShortcut",         # Shortcut
     "DesktopFolder",           # Directory_
     "EngPhysTextAdventure",                   # Name
     "TARGETDIR",               # Component_
     "[TARGETDIR]EngPhysTextAdventure.exe",    # Target
     None,                      # Arguments
     "THE GREAT ENG PHYS TEXT ADVENTURE! Filled with mystery and adventure for all!",  # Description
     None,                      # Hotkey
     None,                      # Icon
     None,                      # IconIndex
     None,                      # ShowCmd
     'TARGETDIR'                # WkDir
     )
    # WHAT this makes it so the game starts with this, don't have this for general installer
##    ,("StartupShortcut",         # Shortcut
##     "StartupFolder",           # Directory_
##     "EngPhysTextAdventure",    # Name
##     "TARGETDIR",               # Component_
##     "[TARGETDIR]EngPhysTextAdventure.exe",   # Target
##     None,                      # Arguments
##     None,                      # Description
##     None,                      # Hotkey
##     None,                      # Icon
##     None,                      # IconIndex
##     None,                      # ShowCmd
##     'TARGETDIR'                # WkDir
##   )

    ]

msi_data = {"Shortcut": cx_Freeze.shortcut_table}
bdist_msi_options = {'data': msi_data}

#executables = [cx_Freeze.Executable("EBTA.py")]

#This governs the artributes of the EXE being made
#All these commented ones are either not supported anymore or I don't know how to use them
target = cx_Freeze.Executable(
    script="EngPhysAdventure Alpha v0.30.py",  # Name of the main script
    #base="Win64GUI",
    #targetDir = r"dist",
    targetName = "EngPhysTextAdventure.exe",
    #compress=False,
    #copyDependentFiles=True,
    #appendScriptToExe=True,
    #appendScriptToLibrary=False,
    icon="newicon_Hbg_icon.ico",  # Icon Name
    #Don't use these because the MSI build actually references the installed EXE with that working directory 
    #This one runs an instance on the deskop with that as the working director so it CRASHES and makes a cache folder on the desktop which is bad
    #shortcutName = "EPTA",  
    #shortcutDir = "DesktopFolder",  # Where shortcut is placed, other option is StartupFolder I think
    
    )


#This is general info for the build and compilier
cx_Freeze.setup( 
        name = "Eng Phys Text Adventure",
        version = "0.30.01",
        description = "THE GREAT ENG PHYS TEXT ADVENTURE!",
        author = "13 Hollywood Productions",
        options = {"bdist_msi": bdist_msi_options, "build_exe": {"packages":packages,'include_files':includefiles}},
        executables = [target]
        )

print("420"*69)

# Printing out reminders for release
includefilesprint = ""
for i in includefiles:
    includefilesprint += i + "\n"
reminder = ["~~REMINDERS BEFORE FINAL RELEASE~~\n",
            "~SETUP & CODE~",
            "In setup Make sure to disable the writing to the startup folder and check the version number",
            "Make sure settings.ini file has all atributes set to 0",
            "MAKE SURE NOT IN DEV MODE",
            "Make sure the CSV files are disabled!",
            "Have all your code commented, documented, and readable! Also Patch Notes",
            "Check all the TODOs in the game",
            # Include but not limited to: Game Opening, Error catching, printT timing
            "Check that the opnning is enabled and all dev items aren't spawning",
            "Do a short playthrough of the game as Tyler Kashak focusing on new features\n"
            "Run playthrough logs to make sure"
            "Do final documentation of latest update",
            "Make sure the patch notes are updated but redacted",
            "Update the readme and patch notes release files",
            "Copy this setup and icon to parent folder befor running",
            "Make sure all the version names are updated in code or otherwise\n",
            "~Build and Release~",
            "Copy these files to the working directory: \nsetup.py\n" + includefilesprint,
            "Run This cx_Freeze setup",
            "Rename and Zip build folders, readme, and patchnotes as zip SFX .exe file",
            "Upload that the zip and installer to release folder",
            "Update release on GITHUB with tags? Make a post?"]


for i in reminder:
    print(str(reminder.index(i)) + ". " + i)



### Use this to run a build folder
#python setup.py build
### Use this to make an installer in dist folder
#python setup.py bdist_msi

