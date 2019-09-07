#This is the To-do list
* appearently labeling TODO is the convention to mark things in code
* Style Guide: https://guides.github.com/features/mastering-markdown/
* Cheat Sheet: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

Write to a file and encrypt it after finishing
https://www.guru99.com/reading-and-writing-files-in-python.html
https://www.youtube.com/watch?v=xSGnLPTjaXo
https://docs.python.org/2/tutorial/inputoutput.html - save structured data

# **Bugs**
- [ ] Peanut butter Kills anyone
- [ ] Sound effect for dropping something even though it's not dropped?
- [ ] Hooded man doesn't have death Diologe
- [ ] Dr. Novog doesn't death quest
- [ ] can kill dr. cassidy after you kill mcamster and still give you the same dialog
- [ ] still a problem with layers, saving and loading, hope it works for 0.27 release
- [ ] Can talk to hooded man after he disapears
- [ ] droesn't drop iron ring after you kill cassidy
- [ ] add savegame info to the sign
- [ ] Save files in the wrong location? Where is Doug?
- [ ] Can't play as tyler Kashak after you stop
- [ ] When you exit from the start screen or otherwise the error catcher catches you
- [ ] Map loading is maybe weird?
- [ ] Lot I was broken?
- [ ] Check to make sure nest game, correct times, and everything add up
- [ ] Many more

# **Fixed Bugs**
**Includes Date, bug, and bug fix**
- [x] Pre0.30 - When you load game music doesn't start for a minute
    - In Setup() return if loadgame had to set GAMEINFO['musicOn'] to 0 so music would know it's the beginning
    - Also set GAMEINFO['timestart'] so the local time variable hopefully adds correctly

        

# 0.31 TOTAL Rebuild, realease to BETA
- [ ] Redo so no more global variables
- [ ] Make all things entities and inherited classes
    - [ ] Different item classes with abilities and sound effects
- [ ] Map out and find a good way to do code execution flowchart for loading/quests
- [ ] Rename code files and put things in proper modules so they make sense
- [ ] MAP tuple overhall:
    - [ ] Get rid of dumb map tuple dictionary calling in a way that makes searching easier?
    * Basically the constructor is nice but don't want to reference coordinates and don't want to have to loop through
     full x,y,z ranges if are is not filled not all those buildings exist  
        - [ ] Entity name with linked list?
        - [ ] Faster search algorithm?
        - [ ] Does the looping even matter?
    - [ ] Incorporate building interior into map coordinate
- [ ] Make PP8 Style using Pycharm
    * https://docs.python.org/2/tutorial/classes.html

# 0.31+
- [ ] New Combat Mechanic
- [ ] Pygame with Music and GUI that works with compiler

- [ ] Music that works with the compilier via mixer or something jank
- [ ] GUI for custom text
- [ ] Updating all the people and places with dropped text
- [ ] time mechanic
- [ ] Name everything and attack dialougs (use x to do y)
- [ ] Save file update
- [ ] Encrypt the save and log files
  - [ ] When you load allow you to select 
  - [ ] Allow you to save as/copy, and delete files
- [ ] Make the names actually do something and matter
- [ ] Make EpiPen able to save you
- [ ] Add leaderboard in the QT
  - [ ] keeping an online synced leaderboard (website, raspberry pi server)?
- [ ] add try and except that if there is a bug it exits safely with a display and saves your file
- [x] Have the text scroll by first time? And Also auto limit text display to roll over at 72 characters (no need to \n it).
  - [x] could try to overload the print function
  - [x] Also can we change it from 72 characters? Why is it that length? Why not 80? 100? Custom?
  - [x] Command prompt will rollover text automatically if too long but doesn't look nice
- [ ] Make save files reconsile simple additions automatically
- [ ] Creative Mode
- [ ] CSV entity importer and code writer
- [ ] Comment all the code and add documentation


	https://pythonbasics.org/python-play-sound/
Start hollywood expansion
stats kept, acheivements
starting screen
	GUI using pygame text based one? But all in Ascii


# Beyond
* want a balance update and full feature update, maybe DLC
* DLC
* Make it something that you want to play with some sort of grinding leading to some character progression (Runescape)
* Simple web interaction
* heavy web interaction
* Making it a web game
* Big Lez show intercut 00:38:40, 00:49:00




# 0.30 NEXT will be kipling
- [x] Make game load, setting save, and dev mode
- [ ] Interiors
    - [x] Add one dimension to everythong
    - [x] Make links work 
    - [ ] Make walking within interiors work (or just add walls to everything and check)
        * Yeah do they even need a size? They do for maps but that's about it
    - [x] Dictionary of interriors with name so it can call up the name at start
    - [ ] Make BSB interior by adding link in on surrounding squares and link out at doorways
    - [ ] Capstone Room
- [ ] People & Items
- [ ] Make high pitch willhelm screen when women die
- [ ] Capstone Minigames
- [x] Pack-a-punch 
    - [ ] With sounds when it starts and ends
    - [ ] Bell dongs every hour
- [ ] More sound effects
- [ ] Accept more directions and movements and fix move past walls bug with overwriting direction or changing to translation
- [ ] Change dev-mode name to doug before release

add verb accepts for 2 words and 1 word for
remove
speak
look
move, go, run, jog, bike, scate, drive, head
	add cardinal directions to those directions

- [ ] Fix Bugs
- [x] Make Dev mode go right into game with " " name, speedrun, etc
- [ ] Turn into BETA

# Done so Far
* CHANGE Music to 4 min Bboy version
* ADDED some dev files for ending tests
    - [x] Light, tash, legit
    - [ ] Dark,
    - [x] Tkashak, 
    - [x] Full Legit, 
    - [ ] Secrets
* ADDED Ability to load from load screen
    * Took a long time, stuff with loading and game path always takes a long time to develope, maybe consider re-doing
    execution flowchart (try mapping it out) for big rebuild
    * Basically displays the savegame file and lets you select one
* ADDED Settings ini file save to parent folder for starting a new game
* ADDED Dev mode that disables error catching, startup blip, Startscreen, and name input
* ADDED more random character dialogs: _ eating too much Lava Pizza, checking their atomic clock, 
contemplating how much Mayo is too much, bathing in Mayonnaise, in a sushi coma, 
phasing in and out of this dimension, eating an XLarge Pho with too much spice, reading a book under a tree, 
wondering how you can read their thoughts, playing 4D chess, pondering necromancy, 
unsuccessfully painting their WarHammer figure with Mili, Synthesizing Gold Nanoparticles, creating an AI Dog, petting a cat,
carrying a soccer ball, playing football by themself, balancing a tennis racket on their nose,
building a tower in Minecraft, Catching a shiny Pikachu, checking their Hearthstone Bot,
solving time traveling, computing the eigenvalue of the inverse Mobius strip, watching Gilmore Girls, 
watching Little House on the Prairie, getting shot by an auto-turret in Rust, trying to think of a capstone idea, being watched
* ADDED more random death descriptors
* CHANGED Mapped attribute in map class to default to 1 in dictionary not argument
* CHANGED Deleted Hooded lore file because it wasn't being used
* ADDED Restructured the quests/story to separate functions and added an events function
* ADDED 3rd floor JHE, 3rd floor BSB, Squid Hat, and COD WAW PS3 Disk Case
* CHANGED Inspecting an intractable now triggers the quest flag if there is no item needed
    * Made this so an inspectable with a blank need is an interface for quests
    * I.E. it can inspecting something blank can trigger something like. PAP machine interface
    * Will do this for items as well. 
    * Another way to do this could be do add a script attribute so when it's inspected it runs a specified script
    * Also want to add a sound effects attribute so it plays a sound when you talk or interact
* ADDED PAP Event and TenThirty Event
    * PAP is a new upgradeable weapon thing, TenThirty is you can't wear a shirt
    * PAP has whole interface and triggers
    * PAP will drop an upgraded weapon of the upgraded weapon but will cost a sacrifice
    * IF sum of stats of Sacrifice is 1/10 or larger the upgrade weapon stats will double
    * Else the stats of the upgrade will be the sum of the upgrade and sacrifice stats
    * PAP will happen at 4:20 or if game is beaten fully
    * 10:30 happens at 10:30 and your shirt always drops
* CHANGED Map attribute Coords to location to be more consistant
* ADDED INTERIORS 
    * New dimension to all objects at end of all locations called dimension or building #
    * ex) JHE located in (2,4,1,0) where 0 is the Overworld
    * Link attribute which moves/teliports a player to a location if they move off a space in the specified direction
    * Says when you go into an interior and leave it, also so interior name on map
    
Insanity Update
ADDED Your dad and Super crocs that show secrets
Alex Jones 
Rhomes around
Brings you down to 1 health unless you have a tin foil hat

Super Male Vitality
-5, -5, -5, -5
has been used by Alex Jones in order to maximize vitality when working up to 12 hours a day or more in the fight for freedom.


Patriot Blend Medium Roast
-5,-5,15, 5
Start your day off right with our gourmet, 100% organic coffee and help us Wake Up America!

Jesse Ventura

I'm a peaceful warrior
I HUNTED PREDITORS IN QUATAMALA.
I DON"T HAVE TO DO ANYTHING. WHAT ARE YOU MY COMMANDING OFFICER

More/changing voice dialoges for people
ability for people to play audio when you talk to them

# Things to Read
* https://dzone.com/articles/python-thread-part-1
* https://www.python-course.eu/python3_inheritance.php

