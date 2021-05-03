# EngPhysAdventure
- Game Release: https://engphystextadventure.wordpress.com/downloads/


Simple Feedback: https://goo.gl/forms/OEMQCupWvEtibd0E3

Bug Reporting: 


-For Developers:-

This is the main file for the Eng Phys Text Adventure (EPTA). This game utilizes some poorly done OOP (sorry Mitch), it has it's strengths though! 
The comments, organization, and optimization. In general try to keep this structure and put any other long ascii display or mode into another file:

AsciiArt.py = Where all of the ascii art display files are

EngPhysAdventure ____ = Run this to run the game. The setup, main loop, and ending. Setup includes opening, main loop has parser, and ending is convoluted in there. 

GameFunctions.py = All front end and backend mechanics of the game and global variables. All non-class functions. May one day split this up.

GameClasses.py = Class definitions and their coresponding functions.

Opening.py = Starting screen, opening, and closing text display

Quests.py = Quests of the game

Startup.py = All the map locations, items, npcs (called enemies), and interactables. Also creates the dictionaries of them.

Setup.py = Py2exe file used to compile into an exe. Run using "python setup.py py2exe" in command prompt.




-Important Links for Developers-

Simple Poll Feedback:https://goo.gl/forms/OEMQCupWvEtibd0E3

Advanced Poll Feedback: https://docs.google.com/spreadsheets/d/1qr7xi4gWhKWCpJCsHvnHTmldAFwFBFbI4btk_TM7hg8/edit?usp=sharing

Developer TODO: https://docs.google.com/document/d/18hpMp26rm4UZgvYt8rPuDq-okjhxGOF3mwWPm8BZAXw/edit



Feeedback: https://goo.gl/forms/OEMQCupWvEtibd0E3
Advanced Feedback: https://goo.gl/forms/LbLxflbmLF61YvmD2
