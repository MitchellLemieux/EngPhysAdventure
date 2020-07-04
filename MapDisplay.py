"""
This function is used for outputting/displaying the maps of the game

"""
from GameFunctions import *  # importing the global dictionaries/values
from StartUp import XRANGE, YRANGE, ZRANGE, DRANGE

centreX, centreY, centreZ, centreDim = STARTLOCATION  # The centre of the map, used to define the ground level starting position


# TODO make this proper pass by value instead of global variable bs
# TODO make show interiors


def mini():
    """
    This function prints a discovery mini-map which shows areas discovered, not discovered, and where the player is.
    This makes the player explore areas and see places to go WITHOUT showing any secrets.
    Developers should be careful of variables like xplayer which is the player location vs x which is the iterating one.
    """

    # Importing global variables
    # noinspection PyGlobalUndefined
    global PLAYER
    # noinspection PyGlobalUndefined
    global MAPS
    global centreZ

    # This grabs the current position of the character and stores for later use
    xplayer = PLAYER.location[0]
    yplayer = PLAYER.location[1]
    zplayer = PLAYER.location[2]
    dimplayer = PLAYER.location[3]

    # As a reminder the coordinates are setup like a graph with y being the vertical, x being horizontal, and 0,0 in the
    #   bottom left corner. I know graphics start in the other orientation but for now I'll start with this.

    # r is the radius of nodes around you discover. Gets bigger the higher up you are.
    r = zplayer - centreZ + 1  # On ground level r should be 1, in basement 0, 2nd floor 2, etc

    MAPS[xplayer][yplayer][zplayer][dimplayer].mapped = 1  # maps the spot you move to every time

    # Map Discovery Loop:
    # Discovers locations around you by flipping the mapped flag in a square radius r around you.
    for z in [1, 2]:  # Only Maps the ground floor and second floor radius so you don't discover secrets.
        for y in range(yplayer - r, yplayer + r + 1, 1):  # a square of radius r around the player
            for x in range(xplayer - r, xplayer + r + 1, 1):  # a square of radius r around the player
                try:  # Error catching to see if the map location exists before mapping it so do not get range error.
                    # I feel like there is a better way to do this but here it is
                    if MAPS[x][y][z][dimplayer]:  # if desired discovery location exist
                        MAPS[x][y][z][dimplayer].mapped = 1  # flips discovery flag
                except:
                    1 + 1  # does nothing, used to finish the error catching patch

    # Map Display Loop:
    if dimplayer != 0:
        print(DIMENSIONS[dimplayer])  # Prints the interior name if they're not in the overworld
    # Creates a row printout string and then prints each line from top to bottom. Z is constant for level player is on.
    for y in range(YRANGE - 1, 0 - 1, -1):  # prints out the map from top to bottom to match player orientation
        # TODO make map rotatable for cardinal coordinates
        maprow = ""  # string accumulator for printing a whole row. Resets after each row is printed
        for x in range(XRANGE):
            if MAPS[x][y][zplayer][dimplayer]:  # checks if the map exists
                # BE CAREFUL of the order of these if statements. Map only displays in desired view if in this order

                if not MAPS[x][y][zplayer][dimplayer].mapped:  # If undiscovered/unmapped flag then shows up as null
                    maprow += "-  "
                # if it's in the basement or above the second floor AND unexplored AND exists, it doesn't display.
                #   Will display once you explore it
                elif ((zplayer > (centreZ + 1)) or (zplayer < centreZ)) and MAPS[x][y][zplayer][dimplayer].travelled:
                    maprow += "-  "
                elif (x == xplayer) and (y == yplayer):  # The marker for the current player location
                    maprow += "x  "
                elif MAPS[x][y][zplayer][dimplayer]:  # If the player has discovered it then will show if it has been traveled to
                    maprow += str(MAPS[x][y][zplayer][dimplayer].travelled) + "  "
            else:  # Used to catch if the location doesn't exist will display as null
                maprow += "-  "
        print(maprow)


def macro_map():
    print("I am not done yet!")
    # This is a map style exported to csv which can be very transferable to this big map

    return

# TODO Make it so the map gets bigger as you discover it. Use these ranges in the code which expand out

# Could use these for map resizing but I don't think I want to do that yet
# this defines the expanding map, these need to be outside the function so they don't re-initialize
# posXrange = centreX+1  #positive X Range, starts on centre
# negXrange = centreX-1 #neagitve X Range, starts on centre
# posYrange = centreY+1 #positive Y range, starts on centre
# negYrange = centreY-1 #negative Y range, starts on centre
#
# #these define the ranges the player can see,
# #   if they go out of the range it expands in that direction,
# #   if they go upstairs to a new place increments what they can see
# #   only shows basements and floors above 2 if they've been there
#
# #if you move outside the corner it expands the range in the corresponding direction
# if x > posXrange: posXrange += 1
# elif x < negXrange: negXrange -= 1
# elif y > posYrange: posYrange += 1
# elif y < negYrange: negYrange -= 1
