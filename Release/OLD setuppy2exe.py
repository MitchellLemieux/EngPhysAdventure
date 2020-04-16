# When this file is in the folder with "EngPhysAdventure" file run this using "python setup.py py2exe" in command prompt
from distutils.core import setup
import py2exe

setup( console= [
        {

            "script": "EngPhysAdventure Alpha v0.30.py",
            "icon_resources": [(0, "newicon_Hbg_icon.ico")]
        }
     ]
)



reminder = ["\n\nDon't forget to:\n",
            "Have all your code documented and ready to go!\n",
            "Check all the TODOs in the game\n",
            # Include but not limited to: Game Opening, Error catching, printT timing
            "Check that the opnning is enabled and all dev items aren't spawning\n",
            "Do a short playthrough of the game as Tyler Kashak focusing on new features\n"
            "Run playthrough logs to make sure"
            "Do final documentation of latest update\n",
            "Make sure the patch notes are updated but redacted\n",
            "Update the readme and patch notes release files\n",
            "Copy this setup and icon to parent folder befor running\n",
            "Run This Py2exe\n"
            "Delete the build folder\n",
            "Copy Media Assets folder to dist, Rename dist to EngPhysAdventure, and make sure you can run it\n",
            "Replace the icon with resource hacker\n",
            "Make sure all the version names are updated\n",
            "Zip folders, readme, and patchnotes as zip SFX .exe file\n",
            "Upload that .exe to release folder",
            "Update release on GITHUB with tags?"]

for i in reminder:
    print(str(reminder.index(i)) + ". " + i)



#use iexpress or one of these to make the installer
    #https://helpdeskgeek.com/free-tools-review/4-tools-to-create-windows-installer-packages/
    
