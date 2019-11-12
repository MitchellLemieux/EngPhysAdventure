#This is the Bugs/To-do/Done list
* appearently labeling TODO is the convention to mark things in code
* Style Guide: https://guides.github.com/features/mastering-markdown/
* Cheat Sheet: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

# **Bugs**
- [ ] If crashes then gave saves may break the game due to giving the object then brekaing on quest
- [ ] When game is loaded with mismatched items it will break in the middle of the loading loop causing many of the
    things to not be loaded even if they're fine. It needs a save reconsiler that removes the wrong object.
- [ ] still a problem with layers, saving and loading, hope it works for 0.27 release
- [ ] Save files in the wrong location? Where is Doug?
- [ ] Can't play as tyler Kashak after you stop
- [ ] When you exit from the start screen or otherwise the error catcher catches you
- [ ] Check to make sure nest game, correct times, and everything add up

# **Fixed Bugs**
**Includes Date, bug, and bug fix**
- [x] Pre0.30 - When you load game music doesn't start for a minute
    - In Setup() return if loadgame had to set GAMEINFO['musicOn'] to 0 so music would know it's the beginning
    - Also set GAMEINFO['timestart'] so the local time variable hopefully adds correctly
- [x] 0.30 - You can go through walls when not using shortcuts
    - Redid direction matching in GameFunctions.Move() so it will always recognize walls no matter what you type
- [x] 0.30 - Can talk to hooded man or anyone after they disapear
    - You can talk to enemy's still when removed because the GameFunction.Talk() only checks their location and when
    an enemy is removed the Enemy.location stays the same.
    - Changed CameClasses MAP.removeEnemy() method so that it also sets the enemy location to none
- [x] 0.30 - When you exit from ingame or start screen error catcher catches you and may overwrite your file
    - We could normally do an acception for a keyboard interrupt but since the game is in a loop it's broken at the
    wrong spot to be caught by the macro error catcher
    - Could implement inner loop error catching or within printT but for now having autosaver make the file have
    autosave on the end so it doesn't overwrite your main game data. Will filter out null outsaves later.
- [x] 0.30 - Can't talk or fight any of the characters with the name change
    - Bassically the location was set to none (so talk or other function wouldn't work) BECAUSE the ENEMY.location was
    set inside the local scope of the GameFunctions.namechange() function
    - Set it to return MAPS, ENEMIES to fix the scoping issue and update those dictionaries in the global scope

        

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



# 0.30.0 NEXT will be kipling
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

- [ ] Comment all the code and add documentation


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
    


# Things to Read
* https://dzone.com/articles/python-thread-part-1
* https://www.python-course.eu/python3_inheritance.php

