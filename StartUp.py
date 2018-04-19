#The Great Engineering Text Based Adventure
#Authors: Mitchell Lemieux, Tyler Kashak
#Music: Brian, Erik
#Start Date: April 14th 2018
#Library of Items and Locations

from GameClasses import *

XRANGE = 7
YRANGE = 9
ZRANGE = 3

MAPS = [[[None for y in range(ZRANGE)] for y in range(YRANGE)] for x in range(XRANGE)]#0-5,0-7,0-2

#Locations: Place.name = "Name" - Place.coords = (X,Y,Z) - Place.info = "location information" - Place.lore = "lore"
#Example: Start = Map("Start",(0,0,0),"You start here")
LOCATIONS=[
Map("Starting Location",(2,3,1),"FRONT OF JHE:\nBSB is to your right. Hatch to your left.\nJHE field is to your rear.","You see the Iron Ring out front of JHE shining in the morning sun. The campus is bustling with student life.\nThere are people in all directions with the remnants of Kipling pranks still scattered about JHE.",()),
Map("Inside JHE",(2,4,1),"JHE LOBBY:\nTo your right you can exit towards BSB. To your left you can head into Hatch.\nForward is the Nuclear Research building. Behind you is the exit of JHE.","JHE lobby is alive. Students rushing in all directions as the smell of\nburnt coffee and sorrow tickles your nose. You scan the faces around\nyou but see no one familiar. There is an confused air about this place\nas Kipling was just last night. Many engineers happy. Many more still\nsuffering.",()),
Map("Nuclear Research Building",(2,5,1),"NUCLEAR RESEARCH BUILDING:\nTo your left lies the JHE-Annex. The Reactor is in front of you.\nThe Police Station is to your right. JHE lobby is behind you.","You have barely ever been in here other than to suffer through\n3 hours of waiting for a water-level PID controller to reach steady state.\nYou wonder how any one could get away with a floor plan this confusing.\nPerhaps that's why no terrorists have blown up the reactor because they are\nall still lost in here...",()),
Map("Inside Hatch",(1,4,1),"INSIDE HATCH:\nIn front of you lies JHE-Annex. To your right is the JHE lobby. To your rear you can exit Hatch.\nTo your left is an alley way.","The new Hatch building. That 'fresh building' smell still lingers.\nYou see many members of the various clubs rushing from room to room.\nThe Kipling clock ticks away... only 365 more...\nWho is this Gerald Hatch anyway?",()),
Map("In Front of Hatch",(1,3,1),"OUTSIDE HATCH:\nETB to your left. The entrance to Hatch in front of you.\nThe McMaster Map to your rear. JHE Entrance is to your right.","As you stare at the newly completed building you get shoved by a\ndehydrated engineer. The sun still shines and you are\nirritated by the constant sound of Hamilton sirens which you have yet\nto grow acustomed to...",()),
Map("Map of McMaster",(1,2,1),"MCMASTER MAP:\nIn front of you lies the Hatch Building. To your right, JHE Field.\nTo your rear lies the Health Sci Library. T-13 is to your left.","Has anyone even used this thing?\nA lost freshman asks you for directions even though the map is clearly\nnext to you.\nAfter sending them in the wrong direction you plan your next move.",()),
Map("Health Sciences Library",(1,1,1),"HEALTH SCIENCES LIBRARY:\nIn front of you is the McMaster Map. To your right is the bus stop.\nMDCL is behind you. The Hospital West wing is to your left.","You are constantly asked to be quiet\neven though you have yet to make a sound.\nAfter scanning the tables and see no one you recognize you take a seat\nin an arm chair and stare out towards the centre of campus daydreaming\nof a life where these study rooms weren't constantly full.",()),
Map("The Bus Stop",(2,1,1),"BUS STOP:\nHealth Sciences Library to your left. JHE field in front of you.\nThe Chapel is behind you. Art Museum to your right.","Students gather around to catch the next bus. You get pushed and shoved\nas they desperately clammer on-board. You overhear an arguement\nbetween a student and the Bus Driver when suddenly the altercation\nturns to blows and pours onto the sidewalk.",()),
Map("The Chapel",(2,0,1),"MCMASTER CHAPEL:\nThe Bus Stop is in front of you back out the door. There is a set of stairs going up.\nAn old stairway leads downward.","The low drone of the organ draws you in. The pews are relatively empty\nand the lighting quite dim. You think it would be in you best interest\nto pray especially with exam season just around the corner...\nIt can't hurt, right? It'd probably work better than those healing stones\non your desk.",("r",'l','b')),
Map("Out front of the Art Museum",(3,1,1),"OUTSIDE ART MUSEUM:\nYou can enter the museum to your rear. Bus Stop is to your left.\nWilly-dog stand to your right. BSB field lies in front of you.","Standing out front of the art museum you feel you are already being\ncritiqued. After narrowly escaping a conversation with an arts student\nabout their installation piece of a dirty coffee table...\nYou plan your next move.",()),
Map("Inside the Art Museum",(3,0,1),"ART MUSEUM:\nThe exit lies in front of you.","Who knew McMaster had such a beautiful gallery. You tilt your\nhead endlessly until the art sort of makes sense. After telling\nyourself you could totally make every piece in the place had you been given\na chance you tilt your nose up, put your pinky out, and contemplate your next move.",('r','l','b')),
Map("The Willy Dog stand",(4,1,1),"WILLY DOG STAND:\nThe turning circle lies in front of you. Mills library at your rear.\nThe Archway to your right. The Art Museum is to your left.","Oh that sweet sweet aroma. Many drunken nights flash through your head.\nThat Willy dog cart is more of a staple to McMaster students than the\nArchway next to it. Was it named Willy Dog after Sir William McMaster?\nYou'll never know...",()),
Map("Mills Library",(4,0,1),"MILLS LIBRARY:\nThe Willy Dog Stand is in front of you. MUSC is to your right.","This is definitely not Thode. You wonder if anything gets done in this\nlibrary. All of the debauchery taking place on the 6th floor sends a\nchill down your spine as you gather your wits.",('l','b')),
Map("Statue of Sir William McMaster",(5,2,1),"WILLIAM MCMASTER STATUE:\nHamilton Hall is in front of you. The Archway is behind you.\nTurning Circle is to your left.","Do you think you'll ever do something worth a statue of yourself\nchilling on a bench? What if Sir Willy McMaster was actually in that statue\nHan Solo style? After a quick selfie with Willy you plan your next move.",('r')),
Map("BSB Field",(3,2,1),"BSB FIELD:\nThe turning circle is to your right. JHE field is to your left.\nEntrance to BSB to your front. The Art Museum is to your rear.","You look up to see the flags flapping happily in the morning breeze.\nThat sun dial at their feet ticking to the tune of celestial magic.\nAfter swatting Neil Degrasse quotes from your thoughts and a quick smell of the flowerbed...\nYou consider what to do next.",()),
Map("JHE Field",(2,2,1),"JHE FIELD:\nBSB Field is to your right. McMaster map to your left. The Bus Stop is at your rear.\nThe entrance to JHE is in front of you.","The morning sun warms your face as you scoff at a hipster slack-lining.\nStudents lie in the grass around the field even though everyone knows\nnothing gets done studying outside.\nAfter narrowly dodging a frisbee you plan what to do.",()),
Map("McMaster Student Centre",(5,0,1),"MUSC:\nMills is to your left. The Archway is in front of you.\nA custodial closet is down the stairs.","The Student Centre is alive. After counting the number of jean jackets\nin the Starbucks line like the Count from Sesame Street you snap back into reality.\n(Oops there goes gravity).\nThe bustling atmosphere disorients you and it becomes difficult to think straight...",('r','b')),
Map("The McMaster Archway",(5,1,1),"ARCHWAY:\nMUSC at your rear. Statue of Willy in front of you.\nEntrance to University Hall is to your right. Willy Dog to your left.","Probably the most beautiful structure at Mac.\nThose Western kids have that Big Ben lookalike but this takes the cake.\nYou snap a quick selfie in front of the Archway for the 'gram.",()),
Map("Inside University Hall",(6,1,1),"UNIVERSITY HALL:\nThe Archway is to your left.","The glares from portraits of old white founding fathers intimidate you.\nThe memories of failing midterms in their presence sends you into an almost trance-like state.\nYou notice that the portrait of Keyes totally looks like Stephen Fry.\nAfter talking yourself out of stealing a piece of Mac history you plan your next move.",('r','b','f')),
Map("The Phoenix",(5,4,1),"THE PHOENIX:\nGeneral Sciences Building is to your left.\nHamilton Hall is to your rear. The trail to Bates is in front of you.\nYou can also go down the stairs to Bridges Cafe.","Upon entering, a rush of memories from last night enter your mind.\People's faces are a blur but you somewhat recall '16 tequila shots' as something you said.\nYou see a mysterious Hooded Man as he beckons you to come speak with him.",('r')),
Map("BSB",(3,3,1),"BSB:\nBSB field is at your rear. Exit BSB to your right.\nThe entrance to JHE is to your left. The Quantum Tunnel is down the stairs.","You were told JHE would be your home but after picking Eng Phys\nyou didn't realize how wrong you were.\nAt least the cafe is better than JHE's.\nA chill runs down your spine as you draw nearer to the electronics labs.\nWiping a cold sweat from your brow you plan ahead.",()),
Map("Between JHE and BSB",(3,4,1),"JHE/BSB JUNCTION:\nEnter JHE to your left. BSB is behind you.\nThe Police station is in front of you.","You look up and see the McMaster coat of arms engraved into the side of BSB.\nThis little pathway has been well worn and you wonder why they don't connect JHE and BSB anyway.\nAn underground (quantum) tunnel would save some hardship on a rainy day... After ignoring a shady e-textbook salesman you consider what to do next.",()),
Map("Police Station",(3,5,1),"POLICE STATION:\nThe path between JHE & BSB behind you. The GO station lies ahead of you.\nThe Nuclear Research Building is to your left. The tandem accelerator is to your right.","Thoughts of getting kicked out of res parties fill your head.\nThose special constables are punks.\nYou mutter the lyrics of a certain N.W.A hit. After avoiding a campus P.D cruiser\nscreaming around the blind corner you gather your surroundings.",()),
Map("Keyes",(4,6,1),"MARY KEYES:\nYou can head to the the bridge if you go forward. The GO station is to your left.\nThe tandem accelerator is at your rear. Bates is to your right.","Damn, Our oWN hip res and snack station thats open 'til midnight.\nWhat a life saver indeed.\nYou quickly thank the engineering gods for Mary Keyes and fight yourself\nfrom ordering a chicken fingers & fries super combo...",()),
Map("Nuclear Reactor",(2,6,1),"NUCLEAR REACTOR:\nGo down to enter. Right is the GO station.\nLeft is ABB.","As you approach you wonder if that steam is really radioactive?\nIt can't be.\nThe ominous stucture draws you closer as you consider what it would be\nlike to swim in that sweet blue pool...",()),
Map("ABB",(1,6,1),"ABB:\nYou can go upstairs. Thode is in front of you.\nJHE Annex is behind you. The Nuclear Reactor is to your right.\nLOT I is to your left.","As you scan the display cases of old lab apparatus and wonder if you would\never be able to create something like this even with 20 years of study.\nMost of them look like they could serve a purpose in the dark arts...\nYou stare at the electron microscope structure and wonder if it could even see your GPA...\nA tear rolls down your cheek. You collect yourself and plan what to do next.",()),
Map("Thode",(1,7,1),"THODE:\nABB is at your rear. The campus exit is to your right.\nCootes Dr. is to your left.","Oh the Reactor Cafe,\nYou think of the good old days when you could actually see the reactor from the Reactor Cafe...\nAfter overhearing someone ask whether keV is bigger than MeV you first contemplate your existence,\nthen contemplate your next move...",('f')),
Map("JHE Annex",(1,5,1),"JHE ANNEX:\nThe Eng Phys Office is up the stairs.\nThe entrance to Hatch is to your rear.\nABB in front of you. ITB is to your left.","They made a big engineering building, got money, then added more.\nYou wonder why Eng Phys classes get pushed into the rooms in this side of JHE...\nHmm...",()),
Map("DANGER",(2,7,1),"CAMPUS EXIT:\nHead to Thode by going left. Head down Cootes trail if you go right.","A faint glow can be seen in the distance but is impossible to make out.\nWarning signs litter the trail as you squint to get a better look.\nA chill is sent down your spine as you see the flickering stretched shadows of\nfighting dance on the road ahead.\nYou cannot go straight... yet.",('f')),
Map("ETB",(0,3,1),"ETB:\nTo your right is the Hatch Building. An alley way is in front of you.\nT-13 is behind you. You can also go upstairs.","The memories of actually doing something in first year flood your mind.\nGear trains. Python. 3D printing.\nEngineering had such a different meaning in your first year...\nYou snap out of your day dream and plan your next move.",('l')),
Map("Lot M",(5,7,1),"LOT M:\nTo your left is the bridge. Bates is behind you.","After 3 days of hiking you arrive at Lot M.\nAfter 2 more days of looking for your car you give up and contemplate what to do next.",('f','r')),
Map("Bates",(5,6,1),"BATES:\nLOT M lies in front of you. Keyes is to your left.\nThe trail to the Phoenix is behind you.","Memories of ridiculous res parties fill your mind.\nYou also recall the landfill of a room that was more of a circus attraction\nthan a living space.\nOh how distant first year seems...",('r')),
Map("Trail",(5,5,1),"TRAIL TO PHOENIX:\nBates lies in front of you. The Phoenix at your rear.\nThe Tandem Accelerator is to your left.","Longboarding down this trail going mach 16 was a blast and a half.\nDodging deer and first year like it's some sort of messed up cube runner.\Nice.",('r')),
Map("Hamilton Hall",(5,3,1),"HAMILTON HALL:\nThe Phoenix is in front of you. The road is to your left.\nThe Willy McMaster Statue is to your rear.","You think about helping out some first years in the Math help centre.\nThen you dont.\nThey should learn to suffer if they're going to make it through the\nnext 4 years.",('r')),
Map("Turning Circle",(4,2,1),"TURNING CIRCLE:\nWilly Dog stand is to your rear. BSB-field is to your left.\The Willy McMaster Statue is to your right. Head down the road if you go forward.","The circle thing with the two trees in it is looking pretty nice\nin the morning sun.\nStudents rush all around as a class has ended.\nThe aroma from the Willy Dog stand is making you pretty hungry...",()),
Map("Campus Road",(4,3,1),"A ROAD:\nEnter BSB to your left. Hamilton Hall to your right.\nThe turning circle is behind you. General Sciences building in front of you.","A lost parent of a first year drives by in a mini-van\nclearly ignoring the 'no access' sign.\nYou thank your astrology sign for making sure they looked up and saw you.",()),
Map("General Sciences",(4,4,1),"GENERAL SCIENCES BUILDING:\nThe Phoenix is to your right. The road is behind you.\nThe junction between JHE and BSB is to your left. Tandem Accelerator is in front of you.","Have you ever been in here?\nI haven't.\nYou see a group of people huddled around a pentagram wearing goat heads.\nI seriously don't know what goes on in there.",()),
Map("Tandem Accelerator",(4,5,1),"TANDEM ACCELERATOR:\nThe General Sciences Building is behind you. The Police station is to your left.\nA trail is to your right. Keyes is in front of you.","Turns out the Tandem Accelerator is NOT a rad place to ride a 2-person bike...\nBummed out you remind yourself you graduated and consider what to do next.",()),
Map("The Bridge",(4,7,1),"THE BRIDGE:\nLot M is to your right. Keyes is at your rear.\nHead down the Cootes trail if you go left.","Snapping out of a day-dream you jump out of the way of a GO bus\npick yourself up and brush yourself off.\nThen plan your next move.",('f')),
Map("Cootes Trail",(3,7,1),"COOTES TRAIL:\nCampus exit is to your left. GO station to your rear.\nThe Bridge to Lot M is to your right.","The flickering light through the trees dances off of the trail ahead of you.\nYou smile as you see a squirrel gathering nuts,\nprobably for his little squirrel family.\nWith this new positive outlook on life you plan your next move.",('f')),
Map("GO Station",(3,6,1),"GO STATION:\nThe Reactor is to your left. Keyes is to your right.\nCootes Trail is in front of you. The Police Station is behind you.","The rush of people and buses around you is disorienting.\nYou nearly get hit by 3 buses and 2 MAC Cop cars as\nyou play a strange game of real-life frogger.\nReaching a bench you sit down, catch your breath, and plan what to do next.",()),
Map("Cootes Dr.",(0,7,1),"COOTES DR.:\nThode is to your right. Lot I is behind you.","You see a student get pulled over in his dad's BMW.\nAfter taunting them and taking a pic for your snap story\nyou put your non-existent phone away and consider what to do.",('f','l')),
Map("Lot I",(0,6,1,),"LOT I:\nABB is to your right. Cootes Dr. is in front of you.\nITB is to your rear.","Nope, your car isn't here. Maybe you parked in Lot M?\nAfter scoffing at all of the prof cars that are way too nice...\nYou plan ahead.",('l')),
Map("ITB",(0,5,1),"ITB:\nJHE-Annex is to your right. Lot I is in front of you.\nAn alley is behind you.","McMaster, back at it again with the horrible floor plan.\nAfter getting lost for 5 hours you finally reach the lobby\nand gather your surroundings.",('l')),
Map("Alley",(0,4,1),"ALLEY:\nITB is in front of you. ETB is behind you.\nYou can enter Hatch to your right.","You reject a strange looking person's offer for a counterfeit student card.\nAfter thinking the picture on the card was of you,\nyou put it to the back of your mind and think of what to do next.",('l')),
Map("T-13",(0,2,1),"T-13:\nETB is in front of you. The McMaster Map is to your right.\nThe West Wing of the Hospital is behind you.","How many bad invidulators does it take to screw in a light bulb?\nI'm not sure but they took my damn Casio FX-911+C...",('l')),
Map("West Hospital",(0,1,1),"HOSPITAL WEST WING:\nIn front of your is T-13. To your right is the Health Sci Library.\nThe East Wing of the Hospital is behind you.","Doctors and Nurses rush around you.\nYou remember why you didn't want to become a doctor as you\nnearly faint looking at a patient's paper cut in the waiting room.\nAfter a drink from the water fountain you plan what to do.",('l')),
Map("East Hospital",(0,0,1),"HOSPITAL EAST WING:\nIn front of you is the West Wing. MDCL is to your right.\nThe Parking Garage is below you.","You smile as you overhear a conversation between a doctor\nand a family.\nTurns out their child is going to make a full recover.\nThanks science.",('l','b')),
Map("MDCL",(1,0,1),"MDCL:\nThe East Wing of the Hospital is to your left. Health Sci library is forward.","After a nice 5 minute meditation in the reflection area.\nYou make your next decision feeling refreshed.",('b','r')),
#Basement Level (X,Y,0)
Map("The Quantum Tunne",(3,3,0),"QUANTUM TUNNEL:\nGo up to return to the main floor of BSB","What other faculty spends thousands of dollars on furniture for a\nliteral custodial closet in the BSB basement?\nYou guessed it...\nEng Phys. Gotta love em'",('f','b','l','r','d')),
Map("Inside the Reactor",(2,6,0),"INSIDE THE REACTOR:\nGo up to head outside.","The hum of air conditioning drowns your thoughts.\nYou lose yourself staring into the faint blue glow of the pool as you slowly approach its edge.",('f','b','l','r','d')),
Map("Club Thode Basement",(1,7,0),"THODE BASEMENT:\nGo up to head outside.","You feel the laser glares burning into the back of your neck as\nyou hastily walk amongst the rows of desks.\nIs it possible to book a study room down here without finding a fallic object drawn on the white board?\nYou'll never know.",('f','b','l','r','d')),
Map("Bridges",(5,4,0),"BRIDGES CAFE:\nYou can only go back up to the Phoenix.","You feel guility walking in here after you performed a\nbeat down on a double big mac in a drunken stupor only hours eariler.\nYou scan the menu to try and find the most non-vegan vegan thing on the menu.\nYou settle with sweet potato fries.",('f','b','l','r','d')),
Map("Secret Trapdoor!",(4,6,0),"SECRET ROOM!:\nGo up to climb out.","A dark room which you can barely see 2 feet in front of you...\nThere are stacks of failed midterms all around you.\nA suit of armor and a chainmail flag with a skull on it are barely visible.\nWho made this place anyway?",('f','b','l','r','d')),
Map("Custodial Closet",(5,0,0),"CUSTODIAL CLOSET:\nYou can only go up to go back to MUSC.","You enter the custodial closet and a formidable stench fills your nostrils...\nEw.",('f','b','l','r','d')),
Map("NRB Basement",(2,5,0),"BASEMENT OF NRB:\nYou can only go back up to the main floor.","You head down the stairs to the basement...\nThe forgotten dreams of PhD students linger in the air.\nYou recall lost hours in 3L labs waiting to reach steady state...\nYou snap out of memoreies of boredom and gather your thoughts.",('f','b','l','r','d')),
Map("Chapel Undercroft",(2,0,0),"CHAPEL UNDERCROFT:\nYou can only go back up to the main floor.","You struggle down the dimly lit stair way into the undercroft.\nThe distinct smell of mould enters your nose as you travel further into the cold musty basement.\nThe faint glow of candles cause the shadows of ancient statues to flicker on the walls of the room...\nAfter a chill goes down your spine you plan your next move.",('f','b','l','r','d')),
Map("ITB Basement",(0,5,0),"ITB BASEMENT:\nYou can only go back up to the main floor.","As if the upstairs floor plan wasn't bad enough...\nAfter another 3 hours wandering around you are back where you started\nand don't feel like you learned anything...",('f','b','l','r','d')),
Map("ABB Basement",(1,6,0),"ABB BASEMENT:\nYou can only go back up to the main floor.","The Laser lab is pretty darn cool.\nWalking around here you notice a number of PhD students looking\nrather down.\nHmmm...\nYou wonder why that is.",('f','b','l','r','d')),
Map("Parking Garage",(0,0,0),"PARKING GARAGE:\nYou can only go back up to the Hospital.","The smooth floor down here makes an excellent skate surfrace.\nRad.\nIf only you learned how to kickflip.",('f','b','l','r','d')),
Map("Mills Basement",(4,0,0),"MILLS BASEMENT:\nYou can only go back up to Mills.","Jeez has anyone ever been down here?\nThe rows of bookshelves seem to go on forever...\nIf only you could possess all of the knowledge they hold.",('f','b','l','r','d')),
#Upper Level (X,Y,2)
Map("2nd Floor ABB",(1,6,2),"2ND FLOOR ABB:\nYou can only go back down the stairs.","You were told JHE would be your home.\nNope.\nInstead you recall countless hours of Haugen lectures on the 2nd floor\nas you drifted in and out of daydreams staring out the 2nd floor windows...",('f','b','l','r','u')),
Map("2nd Floor JHE",(2,4,2),"2ND FLOOR JHE:\nYou can only go back down the stairs.","You spend 20 minutes staring at the 1970 graduating class wondering if you could ever pull off a moustache like that...\nAfter realizing the cool lecture halls were only given to first years...\nYou shake your fist and plan your next move",('f','b','l','r','u')),
Map("2nd Floor ETB",(0,3,2),"2ND FLOOR ETB:\nYou can only go back down the stairs.","You realize you really have never come up here.\nYou see 4th year Eng Phys students hurry out of a long-winded lecture they dont care about.\nAfter picking a booger.\nYou plan your next move.",('f','b','l','r','u')),
Map("Eng Phys Office",(1,5,2),"ENG PHYS OFFICE:\nYou can only go back down the stairs.","The portrait of Novog makes you jealous as you realize you could\nnever pull off a hair style like that.\nYou scan the display case of past Eng Phys projects.\nThey display these as trophies...\nTrophies which only tell a story of suffering you think to yourself...",('f','b','l','r','u')),
Map("The Pheonix Loft",(5,4,2),"PHOENIX LOFT:\nYou can only go back down the stairs.","The history up here is incredible. So many relics from a time long past.\nFrom old play constumes to furniture.\nAfter a quick Shakespearean sonnet you think of what to do next.",('f','b','l','r','u')),
Map("Upstairs Chapel",(2,0,2),"2ND FLOOR CHAPEL:\nYou can only go back down the stairs.","The combination of ringing bells and echoes from the organ is deafening.\nYou can barely collect your thoughts.\nThe cobwebs and dust give you the impression this place been ill-travelled\nand long forgotten.",('f','b','l','r','u')),
Map("2nd Floor Thode",(1,7,2),"2ND FLOOR THODE:\nYou can only go back down the stairs.","As you enter Club Thode the smell of feet enters your nostrils.\nWho goes barefoot in a library? C'mon.\nThe countless hours spent slamming together a report made of nonsense, hopes,\ncaffeine, and dreams send you into a state of shock.\nComing to your senses... You plan your next move.",('f','b','l','r','u'))]

#Items: Equipment.name = "Name" - Equipment.location = tuple of location - Equipment.image = .jpg of item
#       Equipment.info = "info" - Equipment.worn = 'head','hand','body',or 'off-hand' - Equipment.stats = (Atk,Def,Spd)
#Example: Gun = Equipment("Gun",(0,0,0),"Gun.jpg","It shoots people.","hand",(100,0,100))
#Head Items
ITEMS = [
Equipment("Fireball Hat",(2,2,1),"EngHat.jpg","Kind of like the hat you bought in first year and thought you'd wear it forever...","head",(0,3,1)),
Equipment("Pope Hat",(2,0,2),"PopeHat.jpg","Does the Pope where a silly hat? Now you do.","head",(0,3,2)),
Equipment("Goggles",(3,2,1),"Goggles.jpg","Got PPE?","head",(2,0,2)),
Equipment("Wendy's Bag",(0,6,1),"WendyBag.jpg","Fully equipped with grease stains.","head",(1,0,-5)),
Equipment("Empty Bucket",(5,0,0),"Bucket.jpg","The smell of cheap soap still lingers.","head",(-5,10,1)),
Equipment("Gas Mask",(3,5,1),"GasMask.jpg","No one cared who I was till I put on the mask.","head",(5,10,5)),
Equipment("Hard Hat",(4,2,1),"HardHat.jpg","You don't really want to look like a Civil kid. But at least it protects your head.","head",(1,15,5)),
Equipment("Laser Safety Glasses",(1,6,0),"LSGlasses.jpg","Protection from the UV, my dude.","head",(0,3,5)),
Equipment("Raybans",(5,5,1),"Raybans.jpg","GQ Teen says Raybans, Board Shorts, Vans, and a Muscle Tee.","head",(0,1,3)),
Equipment("Bike Helmet",(3,7,1),"BikeHelmet.jpg","One of those fast Tour de France ones.","head",(0,8,10)),
Equipment("Surgical Mask",(0,1,1),"SurgicalMask.jpg","Don't touch me I'm sterile!","head",(0,2,3)),
Equipment("Phils Braces",(2,5,0),"PhilBraces.jpg","Bark AND the bite.","head",(3,2,1)),
Equipment("Santa Hat",(0,0,1),"SantaHat.jpg","Happy Holidays!","head",(0,3,2)),
Equipment("Party Hat",(4,3,1),"PartyHat.jpg","Found in a Chirstmas Cracker","head",(0,5,3)),
#Body Items
Equipment("Eng Phys Shirt",(3,3,0),"EngPhysShirt.jpg","Rolling Rock baby! Premium Stream my ass... More like premium pain...","body",(0,10,5)),
Equipment("Big Hits Shirt",(6,1,1),"BigHits.jpg","The Shirt of the Hero of Kyvach!","body",(25,30,20)),
Equipment("Okons Chainmail",(4,6,0),"OkonMail.jpg","The sacred chainmail forged by the legend himself","body",(25,50,25)),
Equipment("Hazmat Suit",(2,5,1),"Hazmat.jpg","Protection from all sorts of McCrindle farts...","body",(0,10,10)),
Equipment("McMaster map",(1,2,1),"MACMap.jpg","A map of McMaster you can... wear? I guess?","body",(1,5,5)),
Equipment("Priest Gown",(2,0,2),"Gown.jpg","Wearing this gives people the impression you are a holy person...","body",(1,5,3)),
Equipment("Pizza Box",(0,6,1),"PizzaBox.jpg","Fully equipped with crusted cheese.","body",(1,5,1)),
Equipment("Starbucks Apron",(5,0,1),"Apron.jpg","If you put this on do you immediately know how to make a frappe?","body",(1,5,5)),
Equipment("Maroon Jumpsuit",(5,1,1),"MaroonSuit.jpg","Overalls of the Maroons","body",(1,10,5)),
Equipment("Redsuit",(2,4,2),"Redsuit.jpg","Overalls of drunks... I mean engineers","body",(5,10,5)),
Equipment("High Vis Vest",(2,6,1),"HighVis.jpg","Safety first, folks.","body",(0,5,3)),
Equipment("Toilet Seat",(5,0,0),"Toilet.jpg","How do you even wear this?","body",(0,3,2)),
Equipment("Blazer",(5,6,1),"Blazer.jpg","Styyyyyylishhhhhh","body",(0,4,1)),
#Hand Items
Equipment("MSP430",(2,3,1),"MSP430.jpg","A literal piece of garbage.","hand",(-5,0,-5)),
Equipment("Old Headphones",(1,7,1),"OldHeadphones.jpg","Old frayed apple headphones. Good for whipping.","hand",(5,0,5)),
Equipment("Empty Bottle",(4,1,1),"EmptyBottle.jpg","Dasani, more like Dishonest! Amirite?!","hand",(1,0,1)),
Equipment("Banana Wires",(3,3,1),"BanWires.jpg","Alligator clips added for extra whippage.","hand",(8,0,8)),
Equipment("Wrench",(1,3,1),"Wrench.jpg","It's a wrench. 22mm.","hand",(10,0,0)),
Equipment("Pencil",(2,4,1),"Pencil.jpg","HB2. Sharpened.","hand",(2,0,5)),
Equipment("Squash Racket",(5,0,1),"Racket.jpg","Dr.Buijs' Racket? Voltage Divider!","hand",(5,0,10)),
Equipment("Willy Dog",(4,1,1),"Hotdog.jpg","Definitely not vegan","hand",(1,0,2)),
Equipment("Needa Pita",(4,6,1),"Pita.jpg","Better have gotten black olives on that","hand",(2,0,1)),
Equipment("Dirty Needle",(0,1,1),"Needle.jpg","This isn't clean. Somone find me a SharpXchange!",'hand',(10,0,5)),
Equipment("Used Plunger",(5,0,0),"Plunger.jpg","Used. Lovely...","hand",(10,0,10)),
Equipment("Broken Wine Bottle",(4,3,1),"WineBottle.jpg","A broken wine bottle from 1996, good year.","hand",(15,0,5)),
Equipment("Plastic Bag",(2,1,1),"Condom.jpg","The audacity of some people to leave their filth around.","hand",(10,0,-10)),
Equipment("Eng Phys Pen",(3,3,0),"PhysPen.jpg","It would be amazing if this thing actually worked. Plug it in and find all of 2P04.","hand",(5,0,5)),
Equipment("Butter Knife",(4,6,1),"ButterKnife.jpg","Meant for spreading, not stabbing...","hand",(4,0,5)),
Equipment("Pee Bottle",(2,1,1),"PeeBottle.jpg","It is literally a bottle of urine.","hand",(10,0,0)),
Equipment("Tofu",(5,4,0),"Carrot.jpg","Vegan's delight.","hand",(1,0,5)),
Equipment("Space Pop",(1,7,2),"SpacePop.jgp","Get ready to go to space pop city.","hand",(4,0,15)),
Equipment("Banana",(1,7,1),"Banana.jpg","High in potassium.","hand",(5,0,5)),
Equipment("PVC Pipe",(3,7,1),"PVCPipe.jpg","Probably part of a PID project...","hand",(9,2,10)),
Equipment("Car Keys",(0,6,1),"CarKeys.jpg","Fun for babies. Not for batman","hand",(7,0,15)),
Equipment("Ukelele",(4,4,1),"Ukelele.jpg","Wasting away again in Margarrittaville...","hand",(6,0,5)),
Equipment("Lamp",(0,5,1),"Lamp.jpg","I love lamp.","hand",(8,0,4)),
Equipment("Mop",(0,0,1),"Mop.jpg","I'm going to clean up this town.","hand",(6,0,4)),
Equipment("Skateboard",(0,0,0),"Skateboard.jpg","Cowabunga, dude.","hand",(9,0,10)),
Equipment("RCA TV",(5,6,1),"RCATV.jpg","They still make these?","hand",(15,0,-999)),
Equipment("Candlestick",(4,0,0),"Candlestick.jpg","Lumiere is up to no good.","hand",(10,0,5)),
Equipment("Tire Iron",(5,7,1),"TireIron.jpg","Is this even a real tool? Or just a murder weapon...","hand",(11,0,3)),
#Off-Hand Items
Equipment("Coffee",(2,4,1),"Coffee.jpg","The fuel of thinkers.","off-hand",(10,0,10)),
Equipment("Griffiths Electrodynamics",(2,4,2),"Griffiths.jpg","The holy scriptures which govern the fabric of our being","off-hand",(0,25,5)),
Equipment("Ice-Cold Pint",(4,3,1),"Pint.jpg","Ale of the Gods.","off-hand",(3,0,-5)),
Equipment("Diary of the Fallen",(4,6,0),"Diary.jpg","The personal notes of an ancient Hero.","off-hand",(45,45,45)),
Equipment("Wood Shield",(5,4,2),"Shield.jpg","An old wooden shield used in a play, you think...","off-hand",(5,40,-5)),
Equipment("Casio",(2,2,1),"Casio.jpg","This one can do integrals. That's illegal.","off-hand",(5,5,30)),
Equipment("Paint Brush",(3,0,1),"Brush.jpg","You can feel the emotions of a failed arts student coursing through this thing.","off-hand",(5,0,20)),
Equipment("Lenovo Laptop",(1,5,2),"Lenovo.jpg","This heap of computing majesty could block bullets... I think...","off-hand",(5,20,-5)),
Equipment("Priceless Painting",(3,0,1),"Painting.jpg","This painting is supposed to be worth millions...","off-hand",(1,20,5)),
Equipment("Brendan Fallons Lunchbox",(3,3,0),"Lunchbox.jpg","The Lunch Box of an Ancient Hero. Full of samosas","off-hand",(5,10,15)),
Equipment("Jar of Peanut Butter",(4,0,1),"Peanut.jpg","Death paste to those who are allergic... Could prove effective...","off-hand",(0,5,5)),
Equipment("Adderall",(4,0,1),"Adderall.jpg","Speed up, my dude!","off-hand",(0,0,50)),
Equipment("Drumstick",(5,4,2),"Drumstick.jpg","'Property of E-Smooth'","off-hand",(0,10,15)),
Equipment("Bottle Opener",(3,7,1),"BottleOpener.jpg","I wish I had a bottle of wine right about now...","off-hand",(0,10,15)),
Equipment("Jar of Mayo",(0,2,1),"Mayo.jpg","Is mayonaise an instrument?","off-hand",(3,0,5)),
Equipment("Jar of Horse Radish",(4,5,1),"HRaddish.jpg","Apparently not an instrument...","off-hand",(2,0,4)),
Equipment("Tarzan VHS",(0,2,1),"Tarzan.jpg","If only I had a VCR...","off-hand",(0,2,6)),
Equipment("Couch Cushion",(1,7,1),"CCushion.jpg","I hope I find I pillow fight.","off-hand",(0,10,1)),
Equipment("VH Sauce",(1,4,1),"VHSauce.jpg","Sweet and sour. Nice.","off-hand",(1,2,1)),
Equipment("Franks Red Hot",(0,4,1),"FranksRed.jpg","I put that...","off-hand",(3,0,2)),
Equipment("Old Candle",(2,0,0),"OldCandle.jpg","Seems like it's had some use.","off-hand",(0,2,2)),
#Special/Dropped Items
Equipment("Iron Ring",(None),"IronRing.jpg","The One Ring to Rule them ALL.","hand",(1000,1000,1000)),
Equipment("Femtosecond Laser",(None),"Laser.jpg","Haugen's personal femtosecond laser.","hand",(125,0,999)),
Equipment("Minnicks Glasses",(None),"MinnickGlasses.jpg","The Spectacles of an ancient wizard.","head",(60,50,50)),
Equipment("Kenricks Oscilloscope",(None),"Oscilloscope.jpg","The window into the electronics world...","off-hand",(0,150,50)),
Equipment("Joint of Destiny",(None),"Joint.jpg","A tighly rolled spliff filled with Devil's lettuce... for real.","off-hand",(420,420,420)),
Equipment("PID control system",(None),"PID.jpg","A PID control system. Kp = 69, my dude.","head",(45,0,10)),
Equipment("LED of Power",(None),"LED.jpg","An LED with the power output of a neutron star, ok maybe not.","hand",(100,0,75)),
Equipment("Horrible Assignment",(None),"BadAss.jpg","A barely legible report on Fourier analysis.","off-hand",(3,0,0)),
Equipment("Cold Beer",(None),"ColdBeer.jpg","A freshly brewed pint from Andy Knights himself.","off-hand",(15,0,20)),
Equipment("Green Bang Bong",(None),"GBB.jpg","The sacred glass flute providing righteous tokes since '69.","off-hand",(420,420,420)),
Equipment("3W Textbook",(None),"3WText.jpg","Text book that probably has useful information if you could read it. Too bad it has never been in the QT","off-hand",(5,5,10)),
Equipment("Fake Gun",(None),"FakeGun.jpg","Is this seriously what at the MAC cops carry...","hand",(5,0,5)),
Equipment("Eriks Frosted Tips",(None),"FrostedTips.jpg","Ever wanted to look rad as hell? Now you can!","head",(0,3,20)),
Equipment("Engineering Mug",(None),"EngMug.jpg","Do people even have these anymore?","hand",(1,0,2)),
Equipment("Crucifix",(None),"Crucifix.jpg","The Power of Chirst compels you!","hand",(10,0,10)),
Equipment("Huge Shirt",(None),"HugeShirt.jpg","This shirt is WAY too big","body",(0,5,5)),
Equipment("Puke",(None),"Puke.jpg","Ew, literally a pool of vomit","body",(1,0,-10)),
Equipment("Guitar",(None),"Guitar.jpg","Monster Mash.","hand",(5,0,10)),
Equipment("Phone",(None),"Phone.jpg","This thing has been dropped Graham's number times.","off-hand",(5,6,9)),
Equipment("Meow Mix",(None),"MeowMix.jpg","I love chicken, I love liver...","off-hand",(5,0,5)),
Equipment("Visor Glasses",(None),"FastGlasses.jpg","Damn, you are now travelling waaaay to fast. Slow down dude!","head",(3,4,30)),
Equipment("ColdSteel Katana",(None),"katana.jpg","This could probably kill a buffalo fish...","hand",(20,10,10)),
Equipment("Vomit",(None),"Vomit.jpg","Literally spew.","off-hand",(0,0,1)),
Equipment("Stylish Watch",(None),"watch.jpg","If only you learned how to tell time on an analog clock...","off-hand",(0,15,20)),
Equipment("Ancient Incantation",(None),"Incantation.jpg","An old tattered scroll with an incantation written in Latin.","off-hand",(1,1,1))]

#Enemies: Enemy.name = "Name" - Enemy.info = "Description" - Enemy.location = (X,Y,Z) - Enemy.stats = (ATK, DEF, SPD) - Enemy.health = [integer]
#Enemies: Enemy.drop = Item dropped on death or given - Enemy.need = special item they want - Enemy.Sinfo = "Special comment they have if you bring them 'need' item"
#Example: Man = Enemy("Man","A Man",(1,1,1),drop,need,Sinfo,Dinfo)
#Bosses
ENEMIES = [
Enemy("Dr.Minnick","I'm jealous of people who are stupid, they have more opportunities to learn!",(3,3,1),(500,500,500),200,"minnicks glasses",None,"",""),
Enemy("Dr.Novog","Whats up folks.",(2,6,0),(420,420,420),200,"iron ring",None,"Smoke up folks! You've earned your Iron Ring!",""),
Enemy("Dr.Haugen","Pedrotti Cubed!",(1,6,0),(250,100,999),200,"femtosecond laser",None,"Oh my! You've earned the right to use my laser!",""),
Enemy("Kenrick","The oscilloscope is the window into the electronic world.",(3,4,1),(200,100,200),100,"kenricks oscilloscope",None,"Here, take this. It is the windor into the electronics world!",""),
Enemy("Dr.Kitai","It's just a midterm. Don't kill youself.",(0,3,2),(150,50,50),150,"led of power",None,"I've beeen looking all over for this! Where did you find it? Take this!",""),
Enemy("Dr.Knights","Whoever took the 3W text book... Shall feel my eternal wrath",(1,6,2),(200,100,50),300,"cold beer","3w textbook","I've been looking all over for that! Have cold one on me.",""),
#Special
Enemy("Brendan Fallon","What's up dude? I'm here to bless up your shit",None,(9999,9999,9999),999,"green bang bong",None,"THANKS! TOKE UP MY DUDES!",""),
#General
Enemy("Father Frobenius","You need prayer. Recharge at the altar.",(2,0,1),(10,10,10),25,"crucifix",None,"","I am slain!"),
Enemy("Steven the first year","Have you got the LONCAPA Python code?",(3,6,1),(5,1,10),15,"engineering mug",None,"","I'm a failure at home and at school!"),
Enemy("Phil the drunk","MHhmgh, Soouh whatu we getta druuuunk",(5,5,1),(10,5,1),15,"vomit",None,"","mhmh spooky ghost urggh ectoplasm noooooo"),
Enemy("Jana the vegan","Did I mention I'm vegan?",(5,4,0),(15,1,5),10,"3w textbook",None,"","I was going to bring it back I swear!"),
Enemy("Larry the bus driver","Is that even your bus pass?",(2,1,1),(10,10,5),40,"huge shirt",None,"","That was definitely not your bus pass!"),
Enemy("Brian the hipster","Man, you were a RIOT at the Phoenix last night!",(2,2,1),(5,2,10),10,"guitar",None,"","That's not vegan."),
Enemy("Mitch the TA","Hey, I saw your picture on instagram!\nThey let you get away with doing that to the\nWilly McMaster statue?",(0,3,1),(10,5,10),25,"phone",None,"","There's my phone."),
Enemy("Erik the Sk8r","Check out this trey flip. It's pretty tight, eh?",(0,0,0),(15,15,40),20,"eriks frosted tips",None,"","Man, that's dumb!"),
Enemy("Megan the Bartender","Hey kid, want some beer?",(5,4,1),(15,20,10),20,"meow mix",None,"","Nuuuuuuuuuuuu"),
Enemy("Bill the MAC Cop","Give me your student card!",(3,5,1),(50,25,10),50,"fake gun",None,"","We aren't able to arrest you anyway!"),
Enemy("Andreas the Nerd","Full send, dude",(3,2,1),(10,15,5),50,"visor glasses",None,"","Dude, that was definitely a full send"),
Enemy("Eric the Baller","Huge talking to people play.",(0,5,0),(20,15,20),50,"coldsteel katana",None,"","This is sub-optimal."),
Enemy("Mario the Mixologist","Yo check out my meme page. You ever heard coco jay?",(1,4,1),(15,10,20),50,"stylish watch",None,"","si ya saben como consigo, por que me invitan?"),
Enemy("Undead Grad Student","Mussst eeaaat funnnndingg... Er, I mean braaaains.",(2,0,0),(20,10,1),20,"horrible assignment",None,"","My 12 year post-grad was for nothiiiiiingggggg!"),
Enemy("Hooded Man","I've been looking for you. Especially after what you did last night.\nI recommend you seak out the profs of Eng Phys if you are to find your ring...\nOnly they can right the wrongs you have done.",(5,4,1),(999,999,999),999,"",None,"","")]
 
#Stationary Objects to interact with
#Interact(name,location,info,Sinfo,need,drop)
INTERACT = [
Interact("Garbage Can",(2,3,1),"It's a garbage can.","You throw the MSP430... Yes, you have chosen wisely.","msp430","puke"),
Interact("Ancient Mirror",(4,0,0),"It's an old mirror from a time long past.","You mutter the incantation... Suddenly, you see the reflection of (PERSON) himself standing behind you!\n'You have come a long way. The way of the physicist is strong with you.'\n'Here, take this.'","ancient incantation","")]

def WorldMap():
    global MAPS
    global LOCATIONS
    global ENEMIES
    global ITEMS
    for i in LOCATIONS:
        position = i.coords
        x = position[0]
        y = position[1]
        z = position[2]
        MAPS[x][y][z] = i
    for i in ENEMIES:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            MAPS[x][y][z].placeEnemy(i)
    for i in ITEMS:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            MAPS[x][y][z].placeItem(i)
    for i in INTERACT:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            MAPS[x][y][z].placeItem(i)
    return tuple(MAPS)

def ItemDictionary():
    global ITEMS
    ItemDictionary = {}
    for item in ITEMS:
        name = item.name.lower()
        ItemDictionary.update({name:item})
    return ItemDictionary

def EnemyDictionary():
    global ENEMIES
    EnemyDictionary = {}
    for enemy in ENEMIES:
        name = enemy.name.lower()
        EnemyDictionary.update({name:enemy})
    return EnemyDictionary

def InteractDictionary():
    global INTERACT
    InteractDictionary = {}
    for interact in INTERACT:
        name = interact.name.lower()
        InteractDictionary.update({name:interact})
    return InteractDictionary
