#This is the To-do list
appearently labeling TODO is the convention to mark things in code

Write to a file and encrypt it after finishing
https://www.guru99.com/reading-and-writing-files-in-python.html
https://www.youtube.com/watch?v=xSGnLPTjaXo
https://docs.python.org/2/tutorial/inputoutput.html - save structured data

--fixes--
Dr. Haugen still walking around after he dies (remove him)
BIg hits doesn't kill anyone
Fix the map (doesn't show layout right as bsb is bellow JHE)


--current update features--
safe files for infinite laptop loop
	will it just be at locations 
	or be able to save whenever you want with a command?
encrypt safe file/logfile
document
release 0.27

have that speed run time, steps, and other data saved to a stat file [encrypted] to be sent in and put on the leaderboard
	date, Name input, computer name?, steps, time played, game version,
	[this will later be the save file but] location, enemies killed, inventory, stats, quest status
	Key logging save file doesn't work for rng featues like bighits, Brendan fallon, etc but can be used for debugging (so can have a logloader) 
Add leaderboard in the QT

add try and except that if there is a bug it exits safely with a display and saves your file
restart or exit command once the gain ends (or keep playing if done the story)
	maybe using saves?
Have the text scroll by first time? And Also auto limit text display to roll over at 72 characters (no need to \n it).
	Also can we change it from 72 characters? Why is it that length? Why not 80? 100? Custom?
	Command prompt will rollover text automatically if too long
1 crazy idea feature
Creative Mode

--stretch features--
Music and sound effects
keeping an online synced leaderboard (website, raspberry pi server)
stats kept
starting screen
	GUI using pygame text based one?
interriors
Comment all the code and add documentation

--0.27 Update
Added 2nd floor hatch
diaolog for Dan Fitz
Updated the 2nd floors so you can walk between them
Fixed the Time display program (was broken for hours)
Tryed to start making a load from log file but made infinite loops
save and load files as a developer
fixed the key errors which broke the game and made it uplayable
Changed name of map class Remove to removeItem to be more clear and fit camelcase
Commented a lot of code
Made a Creative mode function for creative mode functions (this should be changed)
