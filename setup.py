from distutils.core import setup
import py2exe

setup( console= [
        {
            "script": "EngPhysAdventure.py",
            "icon_resources": [(0, "newicon_Hbg_icon.ico")]
        }
     ]
)
    
