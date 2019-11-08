"""
This function is just to keep track of colours from colorama and any other stylization
-- Default Colours ---
White is place
Blue objects
Yellow interacts
Green People
"""

import colorama  # Colour module, no bolding on windows :(
from colorama import Fore, Back, Style



colorama.init()
# Text Colour definitions (foreground)
 
CLEARSCREEN = '\033[2J'  # This is the clearscreen variable
black = Fore.BLACK
blue = Fore.BLUE
cyan = Fore.CYAN
green = Fore.GREEN
lightblack = Fore.LIGHTBLACK_EX
lightblue = Fore.LIGHTBLUE_EX
lightcyan = Fore.LIGHTCYAN_EX
lightgreen = Fore.LIGHTGREEN_EX
lightmagenta = Fore.LIGHTMAGENTA_EX
lightred = Fore.LIGHTRED_EX
lightwhite = Fore.LIGHTWHITE_EX
lightyellow = Fore.LIGHTYELLOW_EX
magenta = Fore.MAGENTA
red = Fore.RED
reset = Fore.RESET
white = Fore.WHITE
yellow = Fore.YELLOW

colournamelist = ["black","blue","cyan","green","lightblack","lightblue",
              "lightcyan","lightgreen","lightmagenta","lightred","lightred",
              "lightewhite","lightyellow","magenta","red","white","yellow"]
colourlist = [black,blue,cyan,green,lightblack,lightblue,lightcyan,lightgreen,
              lightmagenta,lightred,lightwhite,lightyellow,magenta,red,white,yellow]



# Object References
textcolour = lightgreen
mapcolour = lightwhite
objectcolour = lightcyan
interactcolour = lightyellow
personcolour = lightcyan



#this is printout
#print lightred + "WHATS UP"


