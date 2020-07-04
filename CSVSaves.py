# First Draft on June 26,2019:
"""This is a development file used to easier develop all content in the game.
It's used to export all objects and attributes to a CSV file which is much easier to write in Excel than on an IDE.
This will also give a nice visual display to see issues, spelling/format mistakes, and map layout.
After writing it can be imported back on runtime or converted back into object declaration code which can be copied
into the startup file.

Side note on Why using Pickler and CSVs: If a pickler saving/loading to file is already in the game why not
use one or the other? Ideally all data is saved in CSVs and then encrypted/de-encrypted. But for now the workflow is
to develop using the CSVs and excel then copy the code back into startup for compilation.
This makes it easier to develop but a bit more of a pain to pass back and forth and debug.
Also, why not do the CSV -> python conversion in Excel? You would have to understand Python and VBA
which some developers do but should be expected in order to change this code.
Also saving different classes to different files because it makes it easier to read.
TODO add encryption of these files so a pickler isn't needed
"""

import csv
import os  # Used for file navigation
from StartUp import XRANGE, YRANGE, ZRANGE, DRANGE  # Importing the map bound variables from StartUp to be used in the load



csvPath = os.path.join(os.getcwd(), "Dev", "")  # Gives the base path so the CSVs can be put in the dev folder


def entities_to_CSV(PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS, GAMEINFO, GAMESETTINGS):
    """This function exports all the main dictionaries/entities in memory to csv files with some special formatting.
    This is called in CreativeMode when you save the game.
    For Developers: The code blocks are very similar aside from the particulars of each class so only the item class
    writing and special map creation is commented properly.
    """  # these are docstrings for function, which come up on idle

    # Player to CSV
    # Will add only when multiple players in the game

    # Items to CSV file
    # This is the top of the CSV file which describes the attribute and can be filtered
    iheader = ['Name', 'Description', 'Image Name', 'x', 'y', 'z', 'dim', 'Attack', 'Defense', 'Speed', 'Health', 'Where Worn']
    with open(csvPath + "ITEMS.csv", "wb") as f:
        writer = csv.writer(f, delimiter=',')  # defining the writer object based on the open file
        # writer.writerow(list) writes a whole line with each element in the list being a separate cell
        writer.writerow(iheader)  # write the header list to the file.
        # Write the actual content line by line
        for item in ITEMS:  # looping through all the entries in the dictionary
            i = ITEMS[item]  # accessing the object the dictionary and storing it to a temporary variable
            # writing all the attributes of the object to the CSV files
            writer.writerow([i.name, i.info, i.image, i.location[0], i.location[1], i.location[2], i.location[3],
                             i.stats[0], i.stats[1], i.stats[2], i.health, i.worn])
        writer.writerow(["DELETE ME BEFORE SORTING: To see everything in Excel select columns then and double click "
                         "border to make it autofit. Then do same to rows."])  # last line Excel format message
    f.close()

    # Map to CSV
    mheader = ['Name', 'Description', 'x', 'y', 'z','dim', 'Item Inventory', 'Enemy Inventory',
               'Place Description (will leave soon)', 'Inside', 'Wall locations', 'Interior Size', 'Travelled Flag',
               'Mapped Flag']
    with open(csvPath + "MAPS.csv", "wb") as f:
        writer = csv.writer(f, delimiter=',')  # defining the writer object
        writer.writerow(mheader)  # write the header list
        # This big guy loops through the map locations using the dumb index notation, hopefully that will go away soon
        for x in range(XRANGE):
            for y in range(YRANGE):
                for z in range(ZRANGE):
                    for dim in range(DRANGE):
                        # There are different objects in 1 vs the other so need to replace object with the new one
                        if MAPS[x][y][z][dim]:
                            # accessing the object inter he dictionary and storing it to a temporary variable
                            m = MAPS[x][y][z][dim]
                            writer.writerow([m.name, m.info, m.location[0], m.location[1], m.location[2], m.location[3],
                                             m.items, m.ENEMY,m.lore, m.inside, m.walls, m.size, m.travelled, m.mapped])
        writer.writerow(["DELETE ME BEFORE SORTING: To see everything in Excel select columns then and double click "
                         "border to make it autofit. Then do same to rows."])  # last line Excel format message
    f.close()

    # Special Dev Map:
    # This is a printout of the current map with names and walls to a nicely format-able Excel file
    with open(csvPath + "SpecialMap.csv", "wb") as f:
        writer = csv.writer(f, delimiter=',')  # defining the writer object
        # Since the printout will be much larger than the number of map spaces the space needs to be defined first
        XSize = XRANGE * 2 + 3  # size of the border formed by the range in each direction based on the map size
        YSize = YRANGE * 2 + 3

        # Special Map Writer Loop
        for Z in range(ZRANGE):  # Each cross-section is a Z level
            writer.writerow(["This map is for display purposes only, editing will not do anything"])
            # Map prinout Constructor:
            # This makes a 2 dimensional list of each item which will be filled with data later
            crossSection = []  # map writer accumulator
            for X in range(XSize):  # makes the first set in X
                crossSection.append([])
                for Y in range(YSize):  # makes the second set in y
                    crossSection[X].append([])
            # z = 0 [x][y]
            # crossSection[0][0] is bottom left

            # Filling in the border
            # Corners
            crossSection[0][0] = "Z = " + str(Z)  # bottom left corner marker indicated Z Level
            crossSection[XSize - 1][YSize - 1] = "Z = " + str(Z)  # top left corner marker indicated Z Level
            crossSection[0][YSize - 1] = "Y"  # Top right corner marker showing the Y direction
            crossSection[XSize - 1][0] = "X"  # Bottom right corner marker showing the X direction
            # Border Creator
            # Filling in the Y border, Starting from the first index at 2 to the size, skipping ever 2
            border = 0  # The border indicator which increments
            for Y in range(2, YSize - 1, 2):
                crossSection[0][Y] = border  # Labelling the left side
                crossSection[XSize - 1][Y] = border  # Labelling the right side
                border += 1  # Incrementing the border incrementer

            # Filling in the X border, same comments as the Y border but just for X indicies
            border = 0
            for X in range(2, XSize - 1, 2):
                crossSection[X][0] = border
                crossSection[X][YSize - 1] = border
                border += 1

            # Filling in Names and Walls  TODO Interior Mapping
            for X in range(2, YSize - 1, 2):  # Creating row print first with X being the map variable
                for Y in range(2, YSize - 1, 2):
                    # Error catching for if a map spot doesn't exist. If there is a better way please do it
                    try:
                        # Goes to each map spot and fills in walls around it
                        #   Using (X - 2) / 2 to convert from CSV space to game map space and loop through all spaces
                        if MAPS[(X - 2) / 2][(Y - 2) / 2][Z][0]:  # checks if the map exists at the reference location
                            printname = ""  # Cell accumulator string for the mapname
                            walls = MAPS[(X - 2) / 2][(Y - 2) / 2][Z][0].walls  # Storing the wall variable temporarily
                            if walls:  # if the map has walls
                                # does all the cases to adds the side walls to the cell around the map name
                                if 'f' in walls: crossSection[X][Y + 1] = "-------------------------------"
                                if 'b' in walls: crossSection[X][Y - 1] = "-------------------------------"
                                if 'r' in walls: crossSection[X + 1][Y] = "|\n|"
                                if 'l' in walls: crossSection[X - 1][Y] = "|\n|"
                                # If a wall is above or below it it adds these indicators to the name
                                if 'u' in walls: printname = printname + "^^^ "
                                if 'd' in walls: printname = printname + "vvv "
                            # Adding the full map name to the element
                            crossSection[X][Y] = printname + MAPS[(X - 2) / 2][(Y - 2) / 2][Z][0].name
                    except:
                        crossSection[x][y] = "-"  # if no map location put a null
            # Printout/CSV Writer
            # Puts the elements of the map writer into a printer which can print the row
            printer = []  # printer accumulator
            for Y in range(YSize - 1, -1, -1):  # makes the second set in y
                for X in range(XSize):  # counts in the x direction
                    printer.append(crossSection[X][Y])  # reads in a row into the printer string
                # removes empty lists for printout because all elements will have a list
                for i in printer:
                    if i == []:
                        printer[printer.index([])] = ""
                writer.writerow(printer)  # writes the print output to the row
                printer = []  # resets the printer accumulator for the next row
            # Row Seperator between Z levels
            writer.writerow([""])
            writer.writerow([""])
            writer.writerow([""])
        writer.writerow(["DELETE ME BEFORE SORTING: To see everything in Excel select columns then and double click "
                         "border to make it autofit. Then do same to rows."])  # last line Excel format message
    f.close()

    # Quest, GameInfo, & Game Settings will be added as needed. For now not big enough to need Excel.

    # Enemies to CSV
    eheader = ['Name', 'Talk Text', 'x', 'y', 'z','dim', 'Attack', 'Defense', 'Speed', 'health', 'drop', 'need',
               'Special/Quest Text', 'Death Text']
    with open(csvPath + "ENEMIES.csv", "wb") as f:
        writer = csv.writer(f, delimiter=',')  # defining the writer object
        writer.writerow(eheader)  # write the header list
        for enemy in ENEMIES:  # looping through all the entries in the dictionary
            e = ENEMIES[enemy]  # accessing the object inter he dictionary and storing it to a temporary variable
            writer.writerow([e.name, e.info, e.location[0], e.location[1], e.location[2], e.location[3], e.stats[0],
                             e.stats[1], e.stats[2], e.health, e.drop, e.need, e.Sinfo, e.Dinfo])
        writer.writerow(["DELETE ME BEFORE SORTING: To see everything in Excel select columns then and double click "
                         "border to make it autofit. Then do same to rows."])  # last line Excel format message
    f.close()

    # Intractable to CSV
    intheader = ['Name', 'Description', 'x', 'y', 'z', 'dim','Special/Quest Info', 'Quest Item', 'Given Item']
    with open(csvPath + "INTERACT.csv", "wb") as f:
        writer = csv.writer(f, delimiter=',')  # defining the writer object
        writer.writerow(intheader)  # write the header list
        for inter in INTERACT:  # looping through all the entries in the dictionary
            inter = INTERACT[inter]  # accessing the object inter he dictionary and storing it to a temporary variable
            writer.writerow(
                [inter.name, inter.info, inter.location[0], inter.location[1], inter.location[2], inter.location[3],
                 inter.Sinfo, inter.need, inter.drop])
        writer.writerow(["DELETE ME BEFORE SORTING: To see everything in Excel select columns then and double click "
                         "border to make it autofit. Then do same to rows."])  # last line Excel format message
    f.close()

    # Quest, GameInfo, & Game Settings will be added as needed. For now not big enough to need Excel.
    return


# def csv_to_entities(PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS, GAMEINFO, GAMESETTINGS):
#     """This function loads in data from CSVs and puts those enemies into memory
#     """
#     # This would load at the start of the game to read it in. To do save files would have to save all info
#     # TODO Load fram CSV File
#     return


def csv_to_code():  # this file tries to autoatically update the save file
    # TODO Compile code based off of saved CSV file, add an update to verbs
    """This function takes in data from CSV files and writes to code that can be copied into startup
    """
    # read from one file and write to another at the same time each line (this basically works as an independent script

    with open(csvPath + "STARTUPcode.csv", "wb") as STARTUP:
        writer = csv.writer(STARTUP, delimiter=',')  # defining the writer object
        writer.writerow(['ITEMS1 = ['])
        # looping through all the items to try to reproduct the startup code
        with open(csvPath + "ITEMS.csv", 'rb') as csvitems:
            reader = csv.reader(csvitems, delimiter=',')  # reads in the entire document into the reader object

            next(reader)  # removing the header
            for row in reader:  # reads in a row of the CSV file as a list which each element is broken up to write
                code = 'Equipment("' + row[0] + '", ('
                if row[3] == "":  # if the item doesn't have a starting position sets it to none
                    code = code + "None"
                else:
                    code = code + row[3] + ',' + row[4] + ',' + row[5]
                code = code + '), "' + row[2] + '", "' + row[1] + '", "' + row[10] + '", (' + row[6] + ',' + row[7] \
                            + ',' + row[8] + '),'
                if row[9] == "":  # if items doesn't have health sets it to an empty string
                    code = code + '""),'
                else:
                    code = code + row[9] + '),'
                writer.writerow([code])  # Writing the Code row

            csvitems.close()
        writer.writerow([']  # DON"T FORGET TO REMOVE THE LAST COMA!'])
        # TODO Would put the rest of the CSVs to write to code here
        STARTUP.close()

    # Enemy("Connor the Biologist", "I would really like a cricket to continue my research...", (1, 7, 3), (10, 10, 10),
    #       15, None, "cricket", "Thanks!", "'I can't believe you've done this."),

    return

# This converts the CSV to code when you run this file
# csv_to_code()
