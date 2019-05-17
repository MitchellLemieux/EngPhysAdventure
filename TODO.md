#This is the To-do list
appearently labeling TODO is the convention to mark things in code

Bugs
Peanut butter Kills anyone
Sound effect for dropping something even though it's not dropped?

Write to a file and encrypt it after finishing
https://www.guru99.com/reading-and-writing-files-in-python.html
https://www.youtube.com/watch?v=xSGnLPTjaXo
https://docs.python.org/2/tutorial/inputoutput.html - save structured data

--fixes--
Fix the map (doesn't show layout right as bsb is bellow JHE)
Hooded man doesn't have death Diologe
Too broken when you play as Tyler?
Dr. Novog doesn't death quest
can kill dr. cassidy after you kill mcamster and still give you the same dialog
still a problem with layers, saving and loading, hope it works for 0.27 release
talk to hooded man after he disapears
droesn't drop iron ring after you kill cassidy
add savegame info to the sign
Save files in the wrong location? Where is Doug?
Can't play as tyler Kashak after you stop

--current update features--
Test winning in the nested file
document
	The Game run loop diagrams



0.29
Music that works with the compilier via mixer or something jank
Updating all the people and places
time mechanic
Name everything and attack dialougs (use x to do y)
Save file update
	Encrypt the save and log files
	When you load allow you to select 
	Allow you to save as/copy, and delete files
Make the names actually do something and matter
Make EpiPen able to save you
Add leaderboard in the QT
	keeping an online synced leaderboard (website, raspberry pi server)?
add try and except that if there is a bug it exits safely with a display and saves your file
Have the text scroll by first time? And Also auto limit text display to roll over at 72 characters (no need to \n it).
	could try to overload the print function
	Also can we change it from 72 characters? Why is it that length? Why not 80? 100? Custom?
	Command prompt will rollover text automatically if too long but doesn't look nice
1 crazy idea feature
Make save files reconsile simple additions automatically
Creative Mode
Comment all the code and add documentation


	https://pythonbasics.org/python-play-sound/
Start hollywood expansion
stats kept, acheivements
starting screen
	GUI using pygame text based one? But all in Ascii
0.30
interriors

0.31 - want a balance update and full feature update, maybe DLC
Beyond
DLC
Make it something that you want to play with some sort of grinding leading to some character progression (Runescape)
Making it a web game


0.29 Updated
Made a new string pareser mod that is adaptable, checks for overages, and can control delay called printT (see documentation or examples)
Made items, people, interactables, and places all have different symbols around them
	[People], ~Places~, <Things>, /Interactables/
Made a display map for where you've traveled, and where you are
	Made it in the orientation of front but could be changed
	For each map object added a mapped attribute so you can explore
		(which in object definition is default to 0 to save changing the startup file)
	Each spot will be - until it has been in your explore site radius, even though you haven't visted it
	Want to fix sight based on height but for some reason bugs out the game
Code Conventions to Follow
	Made a good convention that if the function is over 40 lines, definetly by 50 then move it to it's own file
	Also following the PP8 convention style guide for some but need to redo the game at one point
		camel case for variables ex) dogNose
		lowercase with _ for functions ex) nose_colour
		Pascal case (letter of first words capatalized) for classes and objects 
	Try to comit one commit all day, or when a major stuff is done



https://dzone.com/articles/python-thread-part-1
https://www.python-course.eu/python3_inheritance.php

