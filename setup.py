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


reminder = ["\n\nDon't forget to:\n",
            "1. Check all the TODOs in the game\n",
            "2. Check that the openning is enabled and all dev items (iron ring) aren't spawning\n",
            "3.Replace the icon with resource hacker\n",
            "4.Make sure all the version names are updated\n",
            "5.Update the readme and patch notes release files\n",
            "6.Make sure the patch notes are updated but redacted\n",
            "7.Zip folders, readme, and patchnotes as zip SFX .exe file\n",
            "8.Upload that .exe to release folder"]
for i in reminder:
    print i
