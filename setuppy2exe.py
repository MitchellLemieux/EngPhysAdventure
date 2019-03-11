#run this using "python setup.py py2exe" in command prompt
from distutils.core import setup
import py2exe

setup( console= [
        {

            "script": "EngPhysAdventure Alpha v0.27.py",
            "icon_resources": [(0, "newicon_Hbg_icon.ico")]
        }
     ]
)

#TODO make the icon apear automatically, moving the media files, and make an installer
reminder = ["\n\nDon't forget to:\n",
            "1.Check all the TODOs in the game\n",
            "2.Check that the openning is enabled and all dev items aren't spawning\n",
            "3.Do documentation of latest update\n",
            "4.Copy Media Assets folder to dist\n",
            "5.Replace the icon with resource hacker\n",
            "6.Make sure all the version names are updated\n",
            "7.Update the readme and patch notes release files\n",
            "8.Make sure the patch notes are updated but redacted\n",
            "9.Zip folders, readme, and patchnotes as zip SFX .exe file\n",
            "10.Upload that .exe to release folder"]
for i in reminder:
    print i



#use iexpress or one of these to make the installer
    #https://helpdeskgeek.com/free-tools-review/4-tools-to-create-windows-installer-packages/
    
