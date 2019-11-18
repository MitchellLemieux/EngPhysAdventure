"""
This function is just to keep track of colours from colorama and any other stylization
These also have the variables that set the colours
"""

import colorama  # Colour module, no bolding on windows :(
from colorama import Fore, Back, Style




colorama.init()
# Text Colour definitions (foreground)

# Text colours (foreground)
CLEARSCREEN = '\033[2J'  # This is the clearscreen variable
black = Fore.BLACK  #
blue = Fore.BLUE   # a dark blue
cyan = Fore.CYAN   # this is light blue
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
red = Fore.RED      # a dark red
textreset = Fore.RESET
white = Fore.WHITE
yellow = '\u001b[33m'
yellow = Fore.YELLOW   # This is actually green

colournamelist = ["black","blue","cyan","green","lightblack","lightblue",
              "lightcyan","lightgreen","lightmagenta","lightred","lightred",
              "lightewhite","lightyellow","magenta","red","white","yellow"]
colourlist = [black,blue,cyan,green,lightblack,lightblue,lightcyan,lightgreen,
              lightmagenta,lightred,lightwhite,lightyellow,magenta,red,white,yellow]

# Styles for text or background
stylebright = Style.BRIGHT
styledim = Style.DIM   # this doesn't seem to work
stylenormal = Style.NORMAL
stylereset = Style.RESET_ALL

# Background colours (background)
backblack = Back.BLACK
backblue = Back.BLUE

# Game Text Colours
textcolour = lightgreen
backcolour = black
wincolour = lightyellow
losecolour = red
indicatecolour = lightwhite

#Game Background Colours
backgroundcolour = backblack
weirdback = backblue


# Object Text Colours
mapcolour = lightwhite
itemcolour = lightcyan
interactcolour = lightyellow
#offinteractcolour = cyan
personcolour = lightmagenta
deadpersoncolour = red
#offpersoncolour = magenta

coloursusedlist = [lightwhite,lightcyan,lightyellow,lightmagenta,red]


#Defaults
# textcolour = lightgreen
# mapcolour = lightwhite
# itemcolour = lightcyan
# interactcolour = lightyellow
# personcolour = lightmagenta





