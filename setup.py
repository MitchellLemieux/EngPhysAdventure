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
    
