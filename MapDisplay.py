"""
This function is used for outputting/displaying the maps of the game

"""
from GameFunctions import * #importing the global dictionaries/values
from StartUp import XRANGE, YRANGE, ZRANGE #7, 9, 4



centreX, centreY, centreZ = STARTLOCATION #will need to import this later  x,y,z 2,3,1

#TODO make this proper pass by value instead of global variable bs
def mini():
    
    global PLAYER
    global MAPS
    global centreZ
    #global posXrange, negXrange, posYrange, negYrange, centreZ
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    Z = PLAYER.location[2] #captical Z, not lowercase


    r = Z-centreZ+1 #r is the radius of sight around you
    
    #exploring, maps a radius around
    #try not doing it top left spot already mapped
    MAPS[x][y][Z].mapped = 1 #maps the spot you're in
    #Todo try to fix and make the sightrange mechanic based on height work, maybe rewrite the things to debug
    #for Z in [1,2] #not sure why this messes it up the way it does but can follow

    for z in [1,2]: #itteration variable Z here is different than display Z, change this
        for Y in range(y-r,y+r+1,1):
            for X in range(x-r,x+r+1,1):
                try: #dumb way to do it but it works
                    if MAPS[X][Y][z]: #if it exists
                        MAPS[X][Y][z].mapped = 1
                except:
                    1+1

    
    for Y in range(YRANGE-1, 0-1,-1):
        #TODO make map rotatable 
        maprow = "" #accumulator for print a whole row, which is a row in y. Columns are in x
        for X in range(XRANGE):
            if MAPS[X][Y][Z]: #checks if the map exists
                #if unmapped flag then won't display
                if (not(MAPS[X][Y][Z].mapped)):
                    maprow += "-  "
                #if it's in the basement or above the second floor AND unexplored AND exists, it doesn't display.
                #   Will display once you explore it
                elif ( (Z > (centreZ +1) ) or (Z < centreZ) ) and MAPS[X][Y][Z].travelled:
                    maprow += "-  "
                elif (X==x) and (Y==y):
                    maprow += "X  "
                elif MAPS[X][Y][Z]:
                    maprow += str(MAPS[X][Y][Z].travelled) + "  "
            else:
                maprow += "-  "
        print maprow




#Could use these for map resizing but I don't think I want to do that yet
###TODO want to save these ranges
###this defines the starting map which will then expand, these need to be outside the function so they don't re-initialize 
##posXrange = centreX+1  #positive X Range, starts on centre
##negXrange = centreX-1 #neagitve X Range, starts on centre
##posYrange = centreY+1 #positive Y range, starts on centre
##negYrange = centreY-1 #negative Y range, starts on centre
##
###these define the ranges the player can see,
###   if they go out of the range it expands in that direction,
###   if they go upstairs to a new place increments what they can see
###   only shows basements and floors above 2 if they've been there
##
###if you move outside the corner it expands the range in the coresponding direction
##if x > posXrange: posXrange += 1
##elif x < negXrange: negXrange -= 1
##elif y > posYrange: posYrange += 1
##elif y < negYrange: negYrange -= 1
        
