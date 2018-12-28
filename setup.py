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


print "\n\nDon't forget to:\n0.Check that the openning is enabled and all dev items (iron ring) aren't spawning\n1.Replace the icon with resource hacker\n2.Make sure all the version names are updated\n3.Update the readme and update callout file\n4.Make sure the patch notes are updated but redacted\n5.Zip folders, readme, and patchnotes as zip SFX .exe file\n6.Upload that .exe and update callout file to release folder"

