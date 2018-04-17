#The Great Engineering Text Based Adventure
#Authors: Mitchell Lemieux, Tyler Kashak
#Music: Brian, Erik
#Start Date: April 14th 2018
#Library of Items and Locations

from GameClasses import *

XRANGE = 6
YRANGE = 8
ZRANGE = 3

MAPS = [[[None for y in range(ZRANGE)] for y in range(YRANGE)] for x in range(XRANGE)]#0-5,0-7,0-2

Start = Map("Starting Location",(2,3,1),"You are out front of JHE. BSB is to your right and Hatch to your left. JHE field is to your rear.","You awake disoriented. Looking up you see the Iron Ring shining in the morning sun.\nYou quickly collect yourself and gather your surroundings. The campus is bustling\nwith student life. There are people in all directions with the remnants of Kipling\npranks still scattered about JHE. You check your hand and realize your Iron Ring is\nmissing! Where could it have gone?",())
InJHE = Map("Inside JHE",(2,4,1),"You enter the JHE lobby. To your right you can exit towards BSB. To your left you can head into Hatch.","JHE lobby is alive. Students rushing in all directions as the smell of\nburnt coffee and sorrow tickles your nose. You scan the faces around\nyou but see no one familiar. There is an confused air about this place\nas Kipling was just last night. Many engineers happy. Many more still\nsuffering.",())
NukeRS = Map("Nuclear Research Building",(2,5,1),"You enter the Nuclear Research Building. To your left lies the JHE-Annex. The Reactor is in front of you. The Police Station is to your right. JHE lobby is behind you.","NRB. You have barely ever been in here other than to suffer through\n3 hours of waiting for a water-level PID controller to reach steady state.\nYou wonder how any one could get away with a floor plan this confusing.\nPerhaps that's why no terrorists have blown up the reactor because they are\nall still lost in here...",())
InHatch = Map("Inside Hatch",(1,4,1),"You enter the Hatch lobby. In front of you lies JHE-Annex. To your right is the JHE lobby. To your rear you can exit Hatch.","The new Hatch building. That 'fresh building' smell still lingers.\nYou see many members of the various clubs rushing from room to room.\nThe Kipling clock ticks away... only 365 more...\nWho is this Gerald Hatch anyway?",())
FrntHatch = Map("In Front of Hatch",(1,3,1),"You are out front of Hatch. ETB to your left. The entrance to Hatch in front of you. The McMaster Map to your rear. Starting Location to your right.","As you stare at the newly completed building you get shoved by a\ndehydrated engineer. What a punce. The sun still shines and you are\nirritated by the constant sound of Hamilton sirens which you have yet\nto grown acustomed to...",())
MACMap = Map("Map of McMaster",(1,2,1),"You see the Map of McMaster. In front of you lies the Hatch Building. To your right, JHE Field. To your rear lies the Health Sciences Library.","The map of McMaster. Has anyone even used this thing?\nA lost freshman asks you for directions even though the map is clearly\nnext to you.\nAfter sending them in the wrong direction you plan your next move.",())
HLTHSci = Map("Health Sciences Library",(1,1,1),"You enter the Health Sciences Library. In front of you is the McMaster Map. To your right is the bus stop.","Health Sci Library. You are constantly asked to be quiet\neven though you have yet to make a sound.\nAfter scanning the tables and see no one you recognize you take a seat\nin an arm chair and stare out towards the centre of campus daydreaming\nof a life where these study rooms weren't constantly full.",())
BusStop = Map("The Bus Stop",(2,1,1),"You are at the Bus Stop. Health Sciences Library to your left. JHE field in front of you. The Chapel behind you. Art Museum to your right.","Students gather around to catch the next bus. You get pushed and shoved\nas they desperately clammer on-board. You faintly overhear an arguement\nbetween a student and the bus driver when suddenly the altercation\nturns to blows and pours onto the sidewalk.",())
InChapel = Map("The Chapel",(2,0,1),"You enter the McMaster Chapel. The Bus Stop is in front of you back out the door.","The low drone of the organ draws you in. The pews are relatively empty\nand the lighting quite dim. You think it would be in you best interest\nto pray especially with exam season just around the corner...\nIt can't hurt, right? It'd probably work better than those healing stones\non your desk.",("r"))
ArtMus = Map("Out front of the Art Museum",(3,1,1),"You can enter the museum to your rear. Bus Stop is to your left. Willy-dog stand to your right. BSB field lies in front of you.","Standing out front of the art museum you feel you are already being\ncritiqued. After narrowly escaping a conversation with an arts student\nabout their installation piece of a dirty coffee table...\nYou plan your next move.",())
InArtMus = Map("Inside the Art Museum",(3,0,1),"You are inside the art museum. The exit lies in front of you.","Who knew McMaster had such a beautiful gallery. You tilt your\nhead endlessly until the art sort of makes sense. After telling\nyourself you could totally make every piece in the place had you been given\na chance you tilt your nose up, put your pinky out, and contemplate your next move.",('r','l'))
WillyDog = Map("The Willy Dog stand",(4,1,1),"You are at the Willy Dog Stand. Statue of Sir McMaster lies in front of you. Mills at your rear. The Archway to your right. The Art Museum is to your left.","Oh that sweet sweet aroma. Many drunken nights flash through your head.\nThat Willy dog cart is more of a staple to McMaster students than the\nArchway next to it. Was it named Willy Dog after Sir William McMaster?\nYou'll never know...",())
Mills = Map("Mills Library",(4,0,1),"You are inside Mills Library. The Willy Dog Stand is in front of you. MUSC is to your right.","This is definitely not Thode. You wonder if anything gets done in this\nlibrary. All of the debauchery taking place on the 6th floor sends a\nchill down your spine as you gather your wits.",("l"))
Statue = Map("Statue of Sir William McMaster",(4,2,1),"The Statue of Sir William McMaster. The Phoenix is in front of you. Entrance to University Hall is to your right. BSB field is to your left.","Do you think you'll ever do something worth a statue of yourself\nchilling on a bench? What if Sir Willy McMaster was actually in that statue\nHan Solo style? After a quick selfie with Willy you plan your next move.",())
BSBField = Map("BSB Field",(3,2,1),"You are in BSB Field. The Statue of Willy McMaster is to your right. JHE field to your left. Entrance to BSB to your front.","You look up to see the flags flapping happily in the morning breeze.\nThat sun dial at their feet ticking to the tune of celestial magic.\nAfter swatting Neil Degrasse quotes from your thoughts and a quick smell of the flowerbed...\nYou consider what to do next.",())
JHEField = Map("JHE Field",(2,2,1),"You are in JHE Field. BSB Field is to your right. McMaster map to your left. The Bus Stop is at your rear. The Starting location is in front of you.","The morning sun warms your face as you scoff at a hipster slack-lining.\nStudents lie in the grass around the field even though everyone knows\nnothing gets done studying outside.\nAfter narrowly dodging a frisbee you plan what to do.",())
MUSC = Map("McMaster Student Centre",(5,0,1),"You are in the Student Centre. Mills is to your left. The Archway is in front of you. A custodial closet downstairs.","The Student Centre is alive. After counting the number of jean jackets\nin the Starbucks line like the Count from Sesame Street you snap back into reality.\n(Oops there goes gravity).\nThe bustling atmosphere disorients you and it becomes difficult to think straight...",())
Archway = Map("The McMaster Archway",(5,1,1),"You are under the Archway. The Willy Dog Stand is to your left. MUSC at your rear. Enterance to University Hall in front of you.","Probably the most beautiful structure at Mac.\nThose Western kids have that Big Ben lookalike but this takes the cake.\nYou snap a quick selfie in front of the Archway for the 'gram.",("u"))
UniHall = Map("Inside University Hall",(5,2,1),"You enter University Hall. The Archway is at your rear. The Statue of Willy McMaster is to your left.","The glares from portraits of old white founding fathers intimidate you.\nThe memories of failing midterms in their presence sends you into an almost trance-like state.\nYou notice that the portrait of Keyes totally looks like Stephen Fry.\nAfter talking yourself out of stealing a piece of Mac history you plan your next move.",("b"))
Phoenix = Map("The Phoenix",(4,3,1),"YoU are in the camPus watering hole. BSB is to your left. The Statue of Willy McMaster is to your rear. You can go down to Bridges Cafe.","At last, the Phoenix. A little drinky-poo wouldn't hurt anyone.\nThe clinking of glassing and the hopsy aroma makes you salivate.\nMemories of drunken karaoke flood your head and smile comes across your face.\nAfter scanning the multiple coats of arms you think of what to do next.",())
BSB = Map("BSB",(3,3,1),"You are in BSB. BSB field is at your rear. The Phoenix to your right. Starting Location is to your left.","You were told JHE would be your home but after picking Eng Phys\nyou didn't realize how wrong you were.\nAt least the cafe is better than JHE's.\nA chill runs down your spine as you draw nearer to the electronics labs.\nWiping a cold sweat from your brow you plan ahead.",())
JHEBSB = Map("Between JHE and BSB",(3,4,1),"You are between JHE and BSB. Enter JHE to your left. BSB to your right. Trek to Mary Keyes if you go forward.","You look up and see the McMaster coat of arms engraved into the side of BSB.\nThis little pathway has been well worn and you wonder why they don't connect JHE and BSB anyway.\nAn underground (quantum) tunnel would save some hardship on a rainy day... After ignoring a shady e-textbook salesman you consider what to do next.",())
Police = Map("Police Station",(3,5,1),"You see the Police Station. Between JHE & BSB behind you. Mary Keyes lies ahead of you.","You didn't realize there was a Police station on campus\nThoughts of getting kicked out of res parties fill your head.\nThose special constables are punks.\nYou mutter the lyrics of a certain N.W.A hit. After avoiding a campus P.D cruiser\nscreaming around the blind corner you gather your surroundings.",())
Keyes = Map("Keyes",(3,6,1),"You are in Keyes. You can head to the Campus exit if you go forward. The Nuclear Reactor is to your left. JHE-BSB connection at your rear.","Damn, Our oWN hip res and snack station thats open 'til midnight.\nWhat a life saver indeed.\nYou quickly bless the engineering gods for Mary Keyes and fight yourself\nfrom ordering a chicken fingers & fries super combo...",())
Reactor = Map("Nuclear Reactor",(2,6,1),"You are at the McMaster Nuclear Reactor. Go down to enter. Right is Mary Keyes. Left is ABB.","As you approach you wonder if that steam is really radioactive?\nIt can't be.\nThe ominous stucture draws you closer as you consider what it would be\nlike to swim in that sweet blue pool...",())
ABB = Map("ABB",(1,6,1),"You are in ABB. You can go upstairs. Thode is in front of you. JHE Annex behind you. The Nuclear Reactor is to your right.","You scan the display cases of old lab apparatus and wonder if you would\never be able to create something like even with 20 years of study.\nMost of them look like they could serve a pupose in the dark arts...\nYou stare at the strucure covering the electron microscope and wonder if it could even see your GPA...\nA tear rolls down your cheek. You collect yourself and plan what to do next.",())
Thode = Map("Club Thode",(1,7,1),"You are in Thode Library. ABB is at your rear. You can head to the campus exit by going forward.","As you enter Club Thode the smell of feet enters your nostrils.\nWho goes barefoot in a library? C'mon.\nThe countless hours spent slamming together a report made of nonsense, hopes,\ncaffeine, and dreams send you into a state of shock.\nYou plan your next move.",())
JHEAnnex = Map("JHE Annex",(1,5,1),"You enter the JHE Annex. The Entrance to Hatch is to your rear. ABB in front of you.","They made a big engineering building, got money, then added more.\nYou wonder why Eng Phys classes get pushed into the rooms in this side of JHE...\nHmm...",())
OFFCampus = Map("DANGER",(2,7,1),"You approach the exit of campus. Sanders Blvd lies ahead. Head to club Thode by going left. Head to Mary Keyes if you go right.","A faint glow can be seen in the distance but is impossible to make out.\nWarning signs litter the trail as you squint to get a better look.\nA chill is sent down your spine as you faintly see the flickering stretched shadows of\nfighting dance on the road ahead.\nYou cannot go straight... yet.",())
ETB = Map("ETB",(0,3,1),"You arrive at ETB. To your right is the Hatch Building.","The memories of actually doing something in first year flood your mind.\nGear trains. Python. 3D printing.\nEngineering had such a different meaning in your first year...\nYou snap out of your day dream and plan your next move.",())

#Basement Level (X,Y,-Z)
QuantumTunnel = Map("The Quantum Tunne",(3,3,0),"You are at the Quantum Tunnel. Go up to return to the main floor of BSB","What other faculty spends thousands of dollars on furniture for a\nliteral custodial closet in the BSB basement?\nYou guessed it...\nEng Phys. Gotta love em'",('f','b','l','r'))
InsideReactor = Map("Inside the Reactor",(2,6,0),"You are inside the Nuclear Reactor. Go up to head outside.","The hum of air conditioning drowns your thoughts.\nYou lose yourself staring into the faint blue glow of the pool as you slowly approach its edge.",('f','b','l','r'))
ThodeBasement = Map("Club Thode Basement",(1,7,0),"SHHHH you are in the Quiet Study. Go up to head outside.","You feel the laser glares burning into the back of your neck as\nyou hastily walk amongst the rows of desks.\nIs it possible to book a study room down here without finding a fallic object drawn on the white board?\nYou'll never know.",('f','b','l','r'))
Bridges = Map("Bridges",(4,3,0),"Bridges Cafe. You can only go back up to the Phoenix.","You feel guility walking in here after you performed a\nbeat down on a double big mac in a drunken stupor only hours eariler.\nYou scan the menu to try and find the most non-vegan vegan thing on the menu.\nYou settle with sweet potato fries.",('f','b','l','r'))
KeyesSecret = Map("Secret Trapdoor!",(3,6,0),"You fell into a Secret Room! Go up to climb out.","A dark room which you can barely see 2 feet in front of you...\nThere are stacks of failed midterms all around you.\nA suit of armor and a chainmail flag with a skull on it are barely visible.\nWho made this place anyway?",('f','b','l','r'))
CustodialCloset = Map("Custodial Closet",(5,0,0),"You are in a custodial closet. You can only go up to go back to MUSC.","You enter the custodial closet and a formidable stench fills your nostrils...\nEw.",('f','b','l','r'))

#Upper Level (X,Y,+Z)
ABBUpstairs = Map("2nd Floor ABB",(1,6,2),"The 2nd floor of ABB. You can only go back down the stairs.","You were told JHE would be your home.\nNope.\nInstead you recall countless hours of Haugen lectures on the 2nd floor\nas you drifted in and out of daydreams staring out the 2nd floor windows...",('f','b','l','r'))
JHEUpstairs = Map("2nd Floor JHE",(2,4,2),"The 2nd floor of JHE. You can only go back down the stairs.","You spend 20 minutes staring at the 1970 graduating class wondering if you could ever pull off a moustache like that...\nAfter realizing the cool lecture halls were only given to first years...\nYou shake your fist and plan your next move",('f','b','l','r'))
ETBUpstairs = Map("2nd Floor ETB",(0,3,2),"The 2nd floor of ETB. You can only go back down the stairs.","You realize you really have never come up here.\nYou see 4th year Eng Phys students hurry out of a long-winded lecture they dont care about.\nAfter picking a booger.\nYou plan your next move.",('f','b','l','r'))
JHEAUpstairs = Map("Eng Phys Office",(1,5,2),"The Eng Phys Office. You can only go back down the stairs.","The portrait of Novog makes you jealous as you realize you could\nnever pull off a hair style like that.\nYou scan the display case of past Eng Phys projects.\nThey display these as trophies...\nTrophies which only tell a story of suffering you think to yourself...",('f','b','l','r'))
PhoenixLoft = Map("The Pheonix Loft",(4,3,2),"The Phoenix Loft. You can only go back down the stairs.","The history up here is incredible. So many relics from a time long past.\nFrom old play constumes to furniture.\nAfter a quick Shakespearean sonnet you think of what to do next.",('f','b','l','r'))
ChapelUpstairs = Map("Upstairs Chapel",(2,0,2),"Upstairs in the Chapel. You can only go back down stairs.","The combination of ringing bells and echoes from the organ is deafening.\nYou can barely collect your thoughts.\nThe cobwebs and dust give you the impression this place been ill-travelled and long forgotten.",('f','b','l','r'))

#List of ALL Location names.

    
#Items: Equipment.name = "Name" - Equipment.location = tuple of location - Equipment.image = .jpg of item
#       Equipment.info = "info" - Equipment.worn = 'head','hand','body',or 'off-hand' - Equipment.stats = (Atk,Def,Spd)
#Example: Gun = Equipment("Gun",(0,0,0),"Gun.jpg","It shoots people.","hand",(100,0,100))
#Head Items
EngHat = Equipment("Fireball Hat",(-2,-1,0),"EngHat.jpg","Kind of like the hat you bought in first year and thought you'd wear it forever...","head",(0,3,1))
PopeHat = Equipment("Pope Hat",(0,-3,0),"PopeHat.jpg","Does the Pope where a silly hat? Now you do.","head",(0,3,2))
Goggles = Equipment("Goggles",(0,-2,0),"Goggles.jpg","Got PPE?","head",(2,0,2))
WendysBag = Equipment("Wendy's Bag",(1,1,0),"WendyBag.jpg","Fully equipped with grease stains.","head",(1,0,-5))
Bucket = Equipment("An Empty Bucket",(5,0,0),"Bucket.jpg","The smell of cheap soap still lingers.","head",(-5,15,1))
GasMask = Equipment("Gas Mask",(0,0,0),"GasMask.jpg","The best defence agains a Brian methane extrusion.","head",(5,25,10))

#Body Items
EngPhysShirt = Equipment("ENG PHYS Shirt",(0,0,0),"EngPhysShirt.jpg","Rolling Rock baby! Premium Stream my ass... More like premium pain...","body",(0,10,5))
BigHitsShirt = Equipment("Big Hits Shirt",(0,0,0),"BigHits.jpg","The Shirt of the Hero of Kyvach!","body",(50,75,25))
Chainmail = Equipment("Ocon's Chainmail",(0,0,0),"OconMail.jpg","The sacred chainmail forged by the legend himself","body",(75,100,50))
Hazmat = Equipment("Hazmat Suit",(0,0,0),"Hazmat.jpg","Protection from all sorts of McCrindle farts...","body",(0,25,15))
MAPShirt = Equipment("McMaster map with a hole in it",(0,0,0),"MACMap.jpg","A map of McMaster you can... wear? I guess?","body",(1,5,5))
PriestGown = Equipment("A Priest Gown",(0,0,0),"Gown.jpg","Wearing this gives people the impression you are a holy person...","body",(5,15,5))

#Hand Items
MSP430 = Equipment("MSP430",(0,0,0),"MSP430.jpg","A literal piece of garbage.","hand",(-5,-5,-5))
OldHeadphones = Equipment("Old Pair of Headphones",(-1,3,-1),"OldHeadphones.jpg","Old frayed apple headphones. Good for whipping.","hand",(5,0,5))
EmptyBottle = Equipment("Empty Water Bottle",(0,1,0),"EmptyBottle.jpg","Dasani, more like Dishonest! Amirite?!","hand",(1,0,1))
BanWires = Equipment("Banana Wires",(1,0,-1),"BanWires.jpg","Alligator clips added for extra whippage.","hand",(8,0,8))
Wrench = Equipment("Wrench",(-1,1,0),"Wrench.jpg","It's a wrench. 22mm.","hand",(10,0,0))
Pencil = Equipment("Pencil",(-1,-2,0),"Pencil.jpg","HB2. Sharpened.","hand",(2,0,5))
Crucifix = Equipment("Crucifix",(0,-3,0),"Crucifix.jpg","The Power of Chirst compels you!","hand",(4,0,4))
Racket = Equipment("Squash Racket",(3,-3,0),"Racket.jpg","Dr.Buijs' Racket? Voltage Divider!","hand",(5,0,10))
HotDog = Equipment("Willy Dog",(2,-2,0),"Hotdog.jpg","Definitely not vegan","hand",(1,0,2))
Pita = Equipment("Needa Pita",(1,2,0),"Pita.jpg","Better have gotten black olives on that","hand",(2,0,1))
Needle = Equipment("Dirty Needle",(0,0,0),"Needle.jpg","This isn't clean. Somone find me a SharpXchange!",'hand',(10,0,5))
Plunger = Equipment("Used Plunger",(0,0,0),"Plunger.jpg","Used. Lovely...","hand",(10,-10,10))
WineBottle = Equipment("Broken Wine Bottle",(0,0,0),"WineBottle.jpg","A broken wine bottle from 1996, good year.","hand",(25,0,15))

#Off-Hand Items
Coffee = Equipment("Coffee",(2,4,1),"Coffee.jpg","The fuel of thinkers.","off-hand",(10,0,25))
Griffiths = Equipment("Griffiths Electrodynamics",(0,1,1),"Griffiths.jpg","The holy scriptures which govern the fabric of our being","off-hand",(0,100,10))
Pint = Equipment("An Ice-Cold Pint",(2,0,0),"Pint.jpg","Ale of the Gods.","off-hand",(3,0,-5))
Diary = Equipment("Diary of the Fallen",(3,6,0),"Diary.jpg","The personal notes of an ancient Hero.","off-hand",(69,69,69))
Shield = Equipment("Old Wood Shield",(4,3,2),"Shield.jpg","An old wooden shielf used in a play, you think...","off-hand",(5,75,-5))
Casio = Equipment("Casio FX991+C",(2,2,1),"Casio.jpg","This one can do integrals. That's illegal.","off-hand",(5,5,30))
Brush = Equipment("Paint Brush",(0,0,0),"Brush.jpg","You can feel the emotions of a failed arts student coursing through this thing.","off-hand",(5,-10,20))
           
#Special Items
IronRing = Equipment("Iron Ring",(None),"IronRing.jpg","The One Ring to Rule them ALL.","hand",(1000,1000,1000))
Laser = Equipment("Femto Second Laser",(None),"Laser.jpg","Haugen's personal femtosecond laser.","hand",(500,0,999))
MinnickGlasses = Equipment("Glasses of Dr.Minnick",(None),"MinnickGlasses.jpg","The Spectacles of an ancient wizard.","head",(999,500,500))
Oscilloscope = Equipment("Kenrick's Personal Oscilloscope",(None),"Oscilloscope.jpg","The window into the electronics world...","off-hand",(0,350,350))

Items =EngHat = Equipment("Fireball Hat",(-2,-1,0),"EngHat.jpg","Kind of like the hat you bought in first year and thought you'd wear it forever...","head",(0,3,1))
PopeHat = Equipment("Pope Hat",(0,-3,0),"PopeHat.jpg","Does the Pope where a silly hat? Now you do.","head",(0,3,2))
Goggles = Equipment("Goggles",(0,-2,0),"Goggles.jpg","Got PPE?","head",(2,0,2))
WendysBag = Equipment("Wendy's Bag",(1,1,0),"WendyBag.jpg","Fully equipped with grease stains.","head",(1,0,-5))
Bucket = Equipment("An Empty Bucket",(5,0,0),"Bucket.jpg","The smell of cheap soap still lingers.","head",(-5,15,1))
GasMask = Equipment("Gas Mask",(0,0,0),"GasMask.jpg","The best defence agains a Brian methane extrusion.","head",(5,25,10))

#Body Items
EngPhysShirt = Equipment("ENG PHYS Shirt",(0,0,0),"EngPhysShirt.jpg","Rolling Rock baby! Premium Stream my ass... More like premium pain...","body",(0,10,5))
BigHitsShirt = Equipment("Big Hits Shirt",(0,0,0),"BigHits.jpg","The Shirt of the Hero of Kyvach!","body",(50,75,25))
Chainmail = Equipment("Ocon's Chainmail",(0,0,0),"OconMail.jpg","The sacred chainmail forged by the legend himself","body",(75,100,50))
Hazmat = Equipment("Hazmat Suit",(0,0,0),"Hazmat.jpg","Protection from all sorts of McCrindle farts...","body",(0,25,15))
MAPShirt = Equipment("McMaster map with a hole in it",(0,0,0),"MACMap.jpg","A map of McMaster you can... wear? I guess?","body",(1,5,5))
PriestGown = Equipment("A Priest Gown",(0,0,0),"Gown.jpg","Wearing this gives people the impression you are a holy person...","body",(5,15,5))

#Hand Items
MSP430 = Equipment("MSP430",(0,0,0),"MSP430.jpg","A literal piece of garbage.","hand",(-5,0,-5))
OldHeadphones = Equipment("Old Pair of Headphones",(-1,3,-1),"OldHeadphones.jpg","Old frayed apple headphones. Good for whipping.","hand",(5,0,5))
EmptyBottle = Equipment("Empty Water Bottle",(0,1,0),"EmptyBottle.jpg","Dasani, more like Dishonest! Amirite?!","hand",(1,0,1))
BanWires = Equipment("Banana Wires",(1,0,-1),"BanWires.jpg","Alligator clips added for extra whippage.","hand",(8,0,8))
Wrench = Equipment("Wrench",(-1,1,0),"Wrench.jpg","It's a wrench. 22mm.","hand",(10,0,0))
Pencil = Equipment("Pencil",(-1,-2,0),"Pencil.jpg","HB2. Sharpened.","hand",(2,0,5))
Crucifix = Equipment("Crucifix",(0,-3,0),"Crucifix.jpg","The Power of Chirst compels you!","hand",(4,0,4))
Racket = Equipment("Squash Racket",(3,-3,0),"Racket.jpg","Dr.Buijs' Racket? Voltage Divider!","hand",(5,0,10))
HotDog = Equipment("Willy Dog",(2,-2,0),"Hotdog.jpg","Definitely not vegan","hand",(1,0,2))
Pita = Equipment("Needa Pita",(1,2,0),"Pita.jpg","Better have gotten black olives on that","hand",(2,0,1))
Needle = Equipment("Dirty Needle",(0,0,0),"Needle.jpg","This isn't clean. Somone find me a SharpXchange!",'hand',(10,0,5))
Plunger = Equipment("Used Plunger",(0,0,0),"Plunger.jpg","Used. Lovely...","hand",(10,-10,10))
WineBottle = Equipment("Broken Wine Bottle",(0,0,0),"WineBottle.jpg","A broken wine bottle from 1996, good year.","hand",(25,0,15))

#Off-Hand Items
Coffee = Equipment("Coffee",(2,4,1),"Coffee.jpg","The fuel of thinkers.","off-hand",(10,0,25))
Griffiths = Equipment("Griffiths Electrodynamics",(0,1,1),"Griffiths.jpg","The holy scriptures which govern the fabric of our being","off-hand",(0,100,10))
Pint = Equipment("An Ice-Cold Pint",(2,0,0),"Pint.jpg","Ale of the Gods.","off-hand",(3,0,-5))
Diary = Equipment("Diary of the Fallen",(3,6,0),"Diary.jpg","The personal notes of an ancient Hero.","off-hand",(69,69,69))
Shield = Equipment("Old Wood Shield",(4,3,2),"Shield.jpg","An old wooden shielf used in a play, you think...","off-hand",(5,75,-5))
Casio = Equipment("Casio FX991+C",(2,2,1),"Casio.jpg","This one can do integrals. That's illegal.","off-hand",(5,5,30))
Brush = Equipment("Paint Brush",(0,0,0),"Brush.jpg","You can feel the emotions of a failed arts student coursing through this thing.","off-hand",(5,-10,20))
           
#Special Items
IronRing = Equipment("Iron Ring",(None),"IronRing.jpg","The One Ring to Rule them ALL.","hand",(1000,1000,1000))
Laser = Equipment("Femto Second Laser",(None),"Laser.jpg","Haugen's personal femtosecond laser.","hand",(500,0,999))
MinnickGlasses = Equipment("Glasses of Dr.Minnick",(None),"MinnickGlasses.jpg","The Spectacles of an ancient wizard.","head",(999,500,500))
Oscilloscope = Equipment("Kenrick's Personal Oscilloscope",(None),"Oscilloscope.jpg","The window into the electronics world...","off-hand",(0,350,350))

#Enemies: Enemy.name = "Name" - Enemy.info = "Description" - Enemy.location = (X,Y,Z) - Enemy.stats = (ATK, DEF, SPD) - Enemy.health = [integer]
#Example: Man = Enemy("Man","A Man",(1,1,1))
#Bosses
Minnick = Enemy("Dr.Minnick","Hello and welcome to your death!",(None),(500,500,500),[500])
Novog = Enemy("Dr.Novog","Whats up folks.",(None),(420,420,420),[400])
Haugen = Enemy("Dr.Haugen","Pedrotti Cubed!",(None),(250,0,100),[400])
Kenrick = Enemy("Kenrick Chin","The oscilloscope is the window into the electronic world.",(None),(400,50,350),[300])
Kitai = Enemy("Dr.Kitai","It's just a midterm. Don't kill youself.",(None),(250,50,10),[150])
Knights = Enemy("Dr.Knights","Whoever took the 3W text book... Shall feel my eternal wrath",(None),(200,400,1),[500])

#Special
Fallon = Enemy("Brendan Fallon","What's up dude? I'm here to bless up your shit",(None),(999,999,999),[999])

#General
Priest = Enemy("Father Frobenius","You need prayer.",(None),(10,10,10),[25])
FeralFirst1 = Enemy("Feral First Year","Have you got the LONCAPA Python code?",(None),(5,1,10),[15])
FeralFirst2 = Enemy("Drunk First Year","People say first year is the hardest!",(None),(5,1,10),[15])
Vegan = Enemy("Vegan","Did I mention I'm vegan?",(None),(15,1,5),[10])
BusDriver = Enemy("HSR Bus Driver","Is that even your bus pass?",(None),(5,10,4),10)
Hipster = Enemy("Hipster","Have you ever heard of Macklemore?",(None),(5,2,10),[10])
TAmad = Enemy("Frustrated TA","I'll have your marks back within the week, okay?",(None),(10,5,10),[25])
ArtStudent = Enemy("Arts Student","Can you come see my exhibit?",(None),(5,15,5),[20])
HighSchool = Enemy("Aspiring High School Student","What is the entrance average for Engineering???",(None),(1,5,75),[10])
MACCop = Enemy("McMaster Police Officer","Give me your student card!",(None),(50,25,10),[50])

#Place Enemy: Location.placeEnemy(name)
InsideReactor.placeEnemy(Novog)
ABBUpstairs.placeEnemy(Haugen)
BSB.placeEnemy(Minnick)
JHEBSB.placeEnemy(Kenrick)
JHEAUpstairs.placeEnemy(Kitai)
JHEUpstairs.placeEnemy(Knights)
InChapel.placeEnemy(Priest)
Archway.placeEnemy(FeralFirst1)
Keyes.placeEnemy(FeralFirst2)
Bridges.placeEnemy(Vegan)
BusStop.placeEnemy(BusDriver)
JHEField.placeEnemy(Hipster)
ETB.placeEnemy(TAmad)
ArtMus.placeEnemy(ArtStudent)
MUSC.placeEnemy(HighSchool)
Police.placeEnemy(MACCop)

#Adding Item to bus driver to test
BusDriver.item = Pencil


#Placing Items
#Definition of item locations...
#AreaName.placeItem(item)
#Example: Start.placeItem(MSP430)
#Head Items
InChapel.placeItem(PopeHat)
Police.placeItem(GasMask)
CustodialCloset.placeItem(Bucket)

#Body Items
UniHall.placeItem(BigHitsShirt)
ThodeBasement.placeItem(Chainmail)
MACMap.placeItem(MAPShirt)
KeyesSecret.placeItem(Chainmail)
InsideReactor.placeItem(Hazmat)
ChapelUpstairs.placeItem(PriestGown)

#Hand Items
Start.placeItem(MSP430)
InHatch.placeItem(Wrench)
BSB.placeItem(BanWires)
Archway.placeItem(OldHeadphones)
Mills.placeItem(EmptyBottle)
InJHE.placeItem(Pencil)
InChapel.placeItem(Crucifix)
MUSC.placeItem(Racket)
WillyDog.placeItem(HotDog)
Keyes.placeItem(Pita)
HLTHSci.placeItem(Needle)
CustodialCloset.placeItem(Plunger)
PhoenixLoft.placeItem(WineBottle)

#Off-Hand Items
JHEUpstairs.placeItem(Griffiths)
Phoenix.placeItem(Pint)
JHEField.placeItem(Casio)
ArtMus.placeItem(Coffee)
InArtMus.placeItem(Brush)
KeyesSecret.placeItem(Diary)
PhoenixLoft.placeItem(Shield)


#All items
Items=[
EngHat,
PopeHat,
Goggles,
WendysBag,
Bucket,
GasMask,
EngPhysShirt,
BigHitsShirt,
Chainmail,
Hazmat,
MAPShirt,
PriestGown,
MSP430,
OldHeadphones,
EmptyBottle,
BanWires,
Wrench,
Pencil,
Crucifix,
Racket,
HotDog,
Pita,
Needle,
Plunger,
WineBottle,
Coffee,
Griffiths,
Pint,
Diary,
Shield,
Casio,
Brush,
IronRing,
Laser,
MinnickGlasses,
Oscilloscope]

#All Locations
Locations=[
Start,
InJHE,
InHatch,
FrntHatch,
MACMap,
HLTHSci,
BusStop,
InChapel,
ArtMus,
InArtMus,
WillyDog,
Mills,
Statue,
BSBField,
JHEField,
MUSC,
Archway,
UniHall,
Phoenix,
BSB,
JHEBSB,
Police,
Keyes,
Reactor,
ABB,Thode,
JHEAnnex,
OFFCampus,
ETB,
QuantumTunnel,
InsideReactor,
ThodeBasement,
Bridges,
KeyesSecret,
CustodialCloset,
ABBUpstairs,
JHEUpstairs,
ETBUpstairs,
JHEAUpstairs,
PhoenixLoft,
ChapelUpstairs]

#All Enemies
Enemies=[
Minnick,
Novog,
Haugen,
Kenrick,
Kitai,
Knights,
Fallon,
Priest,
FeralFirst1,
FeralFirst2,
Vegan,
BusDriver,
Hipster,
TAmad,
ArtStudent,
HighSchool,
MACCop]



def WorldMap():
    global MAPS
    global Locations
    for i in Locations:
        position = i.coords
        x = position[0]
        y = position[1]
        z = position[2]
        MAPS[x][y][z] = i
    return tuple(MAPS)

def ItemDictionary():
    global Items
    ItemDictionary = {}
    for item in Items:
        name = item.name.lower()
        ItemDictionary.update({name:item})
    return ItemDictionary

def EnemyDictionary():
    global Enemies
    EnemyDictionary = {}
    for enemy in Enemies:
        name = enemy.name.lower()
        EnemyDictionary.update({name:enemy})
    return EnemyDictionary


