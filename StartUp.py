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

#Locations: Place.name = "Name" - Place.coords = (X,Y,Z) - Place.info = "location information" - Place.lore = "lore"
#Example: Start = Map("Start",(0,0,0),"You start here")
LOCATIONS=[
Map("Starting Location",(2,3,1),"You are out front of JHE. BSB is to your right.\nHatch to your left. JHE field is to your rear.","You see the Iron Ring shining in the morning sun. The campus is bustling with student life.\nThere are people in all directions with the remnants of Kipling pranks still scattered about JHE.",()),
Map("Inside JHE",(2,4,1),"You enter JHE lobby. To your right you can exit towards BSB.\nTo your left you can head into Hatch.","JHE lobby is alive. Students rushing in all directions as the smell of\nburnt coffee and sorrow tickles your nose. You scan the faces around\nyou but see no one familiar. There is an confused air about this place\nas Kipling was just last night. Many engineers happy. Many more still\nsuffering.",()),
Map("Nuclear Research Building",(2,5,1),"You are in the Nuclear Research Building. To your left lies the JHE-Annex.\nThe Reactor is in front of you. The Police Station is to your right. JHE lobby is behind you.","NRB. You have barely ever been in here other than to suffer through\n3 hours of waiting for a water-level PID controller to reach steady state.\nYou wonder how any one could get away with a floor plan this confusing.\nPerhaps that's why no terrorists have blown up the reactor because they are\nall still lost in here...",()),
Map("Inside Hatch",(1,4,1),"You are in Hatch lobby. In front of you lies JHE-Annex.\nTo your right is the JHE lobby. To your rear you can exit Hatch.","The new Hatch building. That 'fresh building' smell still lingers.\nYou see many members of the various clubs rushing from room to room.\nThe Kipling clock ticks away... only 365 more...\nWho is this Gerald Hatch anyway?",()),
Map("In Front of Hatch",(1,3,1),"You are out front of Hatch. ETB to your left.\nThe entrance to Hatch in front of you. The McMaster Map to your rear. Starting Location to your right.","As you stare at the newly completed building you get shoved by a\ndehydrated engineer. What a punce. The sun still shines and you are\nirritated by the constant sound of Hamilton sirens which you have yet\nto grown acustomed to...",()),
Map("Map of McMaster",(1,2,1),"You are at the Map of McMaster. In front of you lies the Hatch Building.\nTo your right, JHE Field. To your rear lies the Health Sciences Library.","The map of McMaster. Has anyone even used this thing?\nA lost freshman asks you for directions even though the map is clearly\nnext to you.\nAfter sending them in the wrong direction you plan your next move.",('l')),
Map("Health Sciences Library",(1,1,1),"You are in the Health Sciences Library. In front of you is the McMaster Map.\nTo your right is the bus stop.","Health Sci Library. You are constantly asked to be quiet\neven though you have yet to make a sound.\nAfter scanning the tables and see no one you recognize you take a seat\nin an arm chair and stare out towards the centre of campus daydreaming\nof a life where these study rooms weren't constantly full.",('l','b')),
Map("The Bus Stop",(2,1,1),"You are at the Bus Stop. Health Sciences Library to your left.\nJHE field in front of you. The Chapel behind you. Art Museum to your right.","Students gather around to catch the next bus. You get pushed and shoved\nas they desperately clammer on-board. You overhear an arguement\nbetween a student and the Bus Driver when suddenly the altercation\nturns to blows and pours onto the sidewalk.",()),
Map("The Chapel",(2,0,1),"You are in the McMaster Chapel. There is a set of stairs going up.\nThe Bus Stop is in front of you back out the door.","The low drone of the organ draws you in. The pews are relatively empty\nand the lighting quite dim. You think it would be in you best interest\nto pray especially with exam season just around the corner...\nIt can't hurt, right? It'd probably work better than those healing stones\non your desk.",("r",'l','b')),
Map("Out front of the Art Museum",(3,1,1),"You are in front of the Art Museum. You can enter the museum to your rear.\nBus Stop is to your left. Willy-dog stand to your right. BSB field lies in front of you.","Standing out front of the art museum you feel you are already being\ncritiqued. After narrowly escaping a conversation with an arts student\nabout their installation piece of a dirty coffee table...\nYou plan your next move.",()),
Map("Inside the Art Museum",(3,0,1),"You are inside the art museum. The exit lies in front of you.","Who knew McMaster had such a beautiful gallery. You tilt your\nhead endlessly until the art sort of makes sense. After telling\nyourself you could totally make every piece in the place had you been given\na chance you tilt your nose up, put your pinky out, and contemplate your next move.",('r','l','b')),
Map("The Willy Dog stand",(4,1,1),"You are at the Willy Dog Stand. Statue of Sir McMaster lies in front of you.\nMills library at your rear. The Archway to your right. The Art Museum is to your left.","Oh that sweet sweet aroma. Many drunken nights flash through your head.\nThat Willy dog cart is more of a staple to McMaster students than the\nArchway next to it. Was it named Willy Dog after Sir William McMaster?\nYou'll never know...",()),
Map("Mills Library",(4,0,1),"You are inside Mills Library. The Willy Dog Stand is in front of you.\nMUSC is to your right.","This is definitely not Thode. You wonder if anything gets done in this\nlibrary. All of the debauchery taking place on the 6th floor sends a\nchill down your spine as you gather your wits.",('l','b')),
Map("Statue of Sir William McMaster",(4,2,1),"You are at Statue of Sir William McMaster. The Phoenix is in front of you.\nEntrance to University Hall is to your right. BSB field is to your left.","Do you think you'll ever do something worth a statue of yourself\nchilling on a bench? What if Sir Willy McMaster was actually in that statue\nHan Solo style? After a quick selfie with Willy you plan your next move.",('r')),
Map("BSB Field",(3,2,1),"You are in BSB Field. The Statue of Willy McMaster is to your right.\nJHE field to your left. Entrance to BSB to your front.","You look up to see the flags flapping happily in the morning breeze.\nThat sun dial at their feet ticking to the tune of celestial magic.\nAfter swatting Neil Degrasse quotes from your thoughts and a quick smell of the flowerbed...\nYou consider what to do next.",()),
Map("JHE Field",(2,2,1),"You are in JHE Field. BSB Field is to your right.\nMcMaster map to your left. The Bus Stop is at your rear.\nThe Starting location is in front of you.","The morning sun warms your face as you scoff at a hipster slack-lining.\nStudents lie in the grass around the field even though everyone knows\nnothing gets done studying outside.\nAfter narrowly dodging a frisbee you plan what to do.",()),
Map("McMaster Student Centre",(5,0,1),"You are in the Student Centre. Mills is to your left.\nThe Archway is in front of you. A custodial closet downstairs.","The Student Centre is alive. After counting the number of jean jackets\nin the Starbucks line like the Count from Sesame Street you snap back into reality.\n(Oops there goes gravity).\nThe bustling atmosphere disorients you and it becomes difficult to think straight...",('r','b')),
Map("The McMaster Archway",(5,1,1),"You are under the Archway. The Willy Dog Stand is to your left.\nMUSC at your rear. Enterance to University Hall in front of you.","Probably the most beautiful structure at Mac.\nThose Western kids have that Big Ben lookalike but this takes the cake.\nYou snap a quick selfie in front of the Archway for the 'gram.",("u",'r')),
Map("Inside University Hall",(5,2,1),"You enter University Hall. The Archway is at your rear.\nThe Statue of Willy McMaster is to your left.","The glares from portraits of old white founding fathers intimidate you.\nThe memories of failing midterms in their presence sends you into an almost trance-like state.\nYou notice that the portrait of Keyes totally looks like Stephen Fry.\nAfter talking yourself out of stealing a piece of Mac history you plan your next move.",("b",'r')),
Map("The Phoenix",(4,3,1),"YoU are in the camPus watering hole. BSB is to your left.\nThe Statue of Willy McMaster is to your rear. You can go down to Bridges Cafe.","At last, the Phoenix. A little drinky-poo wouldn't hurt anyone.\nThe clinking of glassing and the hopsy aroma makes you salivate.\nMemories of drunken karaoke flood your head and smile comes across your face.\nAfter scanning the multiple coats of arms you think of what to do next.",()),
Map("BSB",(3,3,1),"You are in BSB. BSB field is at your rear.\nThe Phoenix to your right. Starting Location is to your left.\nThe Quantum Tunnel is down the stairs.","You were told JHE would be your home but after picking Eng Phys\nyou didn't realize how wrong you were.\nAt least the cafe is better than JHE's.\nA chill runs down your spine as you draw nearer to the electronics labs.\nWiping a cold sweat from your brow you plan ahead.",()),
Map("Between JHE and BSB",(3,4,1),"You are between JHE and BSB. Enter JHE to your left.\nBSB is behind you. The Police station is in front of you.","You look up and see the McMaster coat of arms engraved into the side of BSB.\nThis little pathway has been well worn and you wonder why they don't connect JHE and BSB anyway.\nAn underground (quantum) tunnel would save some hardship on a rainy day... After ignoring a shady e-textbook salesman you consider what to do next.",()),
Map("Police Station",(3,5,1),"You are at the Police Station. The path between JHE & BSB behind you.\nMary Keyes lies ahead of you. NRB is to your left.","You didn't realize there was a Police station on campus\nThoughts of getting kicked out of res parties fill your head.\nThose special constables are punks.\nYou mutter the lyrics of a certain N.W.A hit. After avoiding a campus P.D cruiser\nscreaming around the blind corner you gather your surroundings.",('r')),
Map("Keyes",(3,6,1),"You are in Keyes. You can head to the Lot M if you go forward.\nThe Nuclear Reactor is to your left. JHE-BSB connection at your rear.","Damn, Our oWN hip res and snack station thats open 'til midnight.\nWhat a life saver indeed.\nYou quickly bless the engineering gods for Mary Keyes and fight yourself\nfrom ordering a chicken fingers & fries super combo...",()),
Map("Nuclear Reactor",(2,6,1),"You are at the McMaster Nuclear Reactor. Go down to enter.\nRight is Mary Keyes. Left is ABB.","As you approach you wonder if that steam is really radioactive?\nIt can't be.\nThe ominous stucture draws you closer as you consider what it would be\nlike to swim in that sweet blue pool...",('l')),
Map("ABB",(1,6,1),"You are in ABB. You can go upstairs. Thode is in front of you.\nJHE Annex behind you. The Nuclear Reactor is to your right.","You scan the display cases of old lab apparatus and wonder if you would\never be able to create something like this even with 20 years of study.\nMost of them look like they could serve a purpose in the dark arts...\nYou stare at the electron microscope structure and wonder if it could even see your GPA...\nA tear rolls down your cheek. You collect yourself and plan what to do next.",('l')),
Map("Club Thode",(1,7,1),"You are in Thode Library. ABB is at your rear.\nYou can head to the campus exit by going forward.","Oh the Reactor Cafe,\nYou think of the good old days when you could actually see the reactor from the Reactor Cafe...\nAfter overhearing someone ask whether keV is bigger than MeV you first contemplate your existence,\nthen contemplate your next move...",('r')),
Map("JHE Annex",(1,5,1),"You are in the JHE Annex. The entrance to Hatch is to your rear.\nABB in front of you.","They made a big engineering building, got money, then added more.\nYou wonder why Eng Phys classes get pushed into the rooms in this side of JHE...\nHmm...",('l')),
Map("DANGER",(2,7,1),"You are at the exit of campus.\nHead to club Thode by going left. Head to Mary Keyes if you go right.","A faint glow can be seen in the distance but is impossible to make out.\nWarning signs litter the trail as you squint to get a better look.\nA chill is sent down your spine as you faintly see the flickering stretched shadows of\nfighting dance on the road ahead.\nYou cannot go straight... yet.",('f')),
Map("ETB",(0,3,1),"You are at ETB. To your right is the Hatch Building.","The memories of actually doing something in first year flood your mind.\nGear trains. Python. 3D printing.\nEngineering had such a different meaning in your first year...\nYou snap out of your day dream and plan your next move.",('l','f','b')),
Map("Lot M",(3,7,1),"You arrive at Lot M. To your left is the campus exit.\nMary Keyes is behind you.","After 3 days of hiking you arrive at Lot M.\nAfter 2 more days of looking for your car you give up and contemplate what to do next.",('f','r')),
#Basement Level (X,Y,0)
Map("The Quantum Tunne",(3,3,0),"You are at the Quantum Tunnel.\nGo up to return to the main floor of BSB","What other faculty spends thousands of dollars on furniture for a\nliteral custodial closet in the BSB basement?\nYou guessed it...\nEng Phys. Gotta love em'",('f','b','l','r')),
Map("Inside the Reactor",(2,6,0),"You are inside the Nuclear Reactor.\nGo up to head outside.","The hum of air conditioning drowns your thoughts.\nYou lose yourself staring into the faint blue glow of the pool as you slowly approach its edge.",('f','b','l','r')),
Map("Club Thode Basement",(1,7,0),"SHHHH you are in the Quiet Study.\nGo up to head outside.","You feel the laser glares burning into the back of your neck as\nyou hastily walk amongst the rows of desks.\nIs it possible to book a study room down here without finding a fallic object drawn on the white board?\nYou'll never know.",('f','b','l','r')),
Map("Bridges",(4,3,0),"You are in Bridges Cafe.\nYou can only go back up to the Phoenix.","You feel guility walking in here after you performed a\nbeat down on a double big mac in a drunken stupor only hours eariler.\nYou scan the menu to try and find the most non-vegan vegan thing on the menu.\nYou settle with sweet potato fries.",('f','b','l','r')),
Map("Secret Trapdoor!",(3,6,0),"You fell into a Secret Room!\nGo up to climb out.","A dark room which you can barely see 2 feet in front of you...\nThere are stacks of failed midterms all around you.\nA suit of armor and a chainmail flag with a skull on it are barely visible.\nWho made this place anyway?",('f','b','l','r')),
Map("Custodial Closet",(5,0,0),"You are in a custodial closet.\nYou can only go up to go back to MUSC.","You enter the custodial closet and a formidable stench fills your nostrils...\nEw.",('f','b','l','r')),
Map("NRB Basement",(2,5,0),"You are in the NRB Basement.\nYou can only go back up to the main floor.","You head down the stairs to the basement...\nThe forgotten dreams of PhD students linger in the air.\nYou recall lost hours in 3L labs waiting to reach steady state...\nYou snap out of memoreies of boredom and gather your thoughts.",('f','b','l','r')),
#Upper Level (X,Y,2)
Map("2nd Floor ABB",(1,6,2),"You are on the 2nd floor of ABB.\nYou can only go back down the stairs.","You were told JHE would be your home.\nNope.\nInstead you recall countless hours of Haugen lectures on the 2nd floor\nas you drifted in and out of daydreams staring out the 2nd floor windows...",('f','b','l','r')),
Map("2nd Floor JHE",(2,4,2),"You are on the 2nd floor of JHE.\nYou can only go back down the stairs.","You spend 20 minutes staring at the 1970 graduating class wondering if you could ever pull off a moustache like that...\nAfter realizing the cool lecture halls were only given to first years...\nYou shake your fist and plan your next move",('f','b','l','r')),
Map("2nd Floor ETB",(0,3,2),"You are on the 2nd floor of ETB.\nYou can only go back down the stairs.","You realize you really have never come up here.\nYou see 4th year Eng Phys students hurry out of a long-winded lecture they dont care about.\nAfter picking a booger.\nYou plan your next move.",('f','b','l','r')),
Map("Eng Phys Office",(1,5,2),"You are oat the Eng Phys Office.\nYou can only go back down the stairs.","The portrait of Novog makes you jealous as you realize you could\nnever pull off a hair style like that.\nYou scan the display case of past Eng Phys projects.\nThey display these as trophies...\nTrophies which only tell a story of suffering you think to yourself...",('f','b','l','r')),
Map("The Pheonix Loft",(4,3,2),"You are in the Phoenix Loft.\nYou can only go back down the stairs.","The history up here is incredible. So many relics from a time long past.\nFrom old play constumes to furniture.\nAfter a quick Shakespearean sonnet you think of what to do next.",('f','b','l','r')),
Map("Upstairs Chapel",(2,0,2),"You are upstairs in the Chapel.\nYou can only go back down the stairs.","The combination of ringing bells and echoes from the organ is deafening.\nYou can barely collect your thoughts.\nThe cobwebs and dust give you the impression this place been ill-travelled\nand long forgotten.",('f','b','l','r')),
Map("2nd Floor Thode",(1,7,2),"You are on the 2nd floor of Thode.\nYou can only go back down the stairs.","As you enter Club Thode the smell of feet enters your nostrils.\nWho goes barefoot in a library? C'mon.\nThe countless hours spent slamming together a report made of nonsense, hopes,\ncaffeine, and dreams send you into a state of shock.\nComing to your senses... You plan your next move.",('f','b','l','r'))]

#Items: Equipment.name = "Name" - Equipment.location = tuple of location - Equipment.image = .jpg of item
#       Equipment.info = "info" - Equipment.worn = 'head','hand','body',or 'off-hand' - Equipment.stats = (Atk,Def,Spd)
#Example: Gun = Equipment("Gun",(0,0,0),"Gun.jpg","It shoots people.","hand",(100,0,100))
#Head Items
ITEMS = [
Equipment("Fireball Hat",(2,2,1),"EngHat.jpg","Kind of like the hat you bought in first year and thought you'd wear it forever...","head",(0,3,1)),
Equipment("Pope Hat",(2,0,2),"PopeHat.jpg","Does the Pope where a silly hat? Now you do.","head",(0,3,2)),
Equipment("Goggles",(3,2,1),"Goggles.jpg","Got PPE?","head",(2,0,2)),
Equipment("Wendy's Bag",(1,1,1),"WendyBag.jpg","Fully equipped with grease stains.","head",(1,0,-5)),
Equipment("An Empty Bucket",(5,0,0),"Bucket.jpg","The smell of cheap soap still lingers.","head",(-5,10,1)),
Equipment("Gas Mask",(3,5,1),"GasMask.jpg","The best defence agains a Brian methane extrusion.","head",(5,10,10)),
Equipment("Hard Hat",(4,2,1),"HardHat.jpg","You don't really want to look like a Civil kid. But at least it protects your head.","head",(1,15,5)),
Equipment("Fast Visor Glasses",(1,7,2),"FastGlasses.jpg","Damn, you are now travelling waaaay to fast. Slow down dude!","head",(3,4,30)),
#Body Items
Equipment("Eng Phys Shirt",(3,3,0),"EngPhysShirt.jpg","Rolling Rock baby! Premium Stream my ass... More like premium pain...","body",(0,10,5)),
Equipment("Big Hits Shirt",(5,2,1),"BigHits.jpg","The Shirt of the Hero of Kyvach!","body",(25,30,20)),
Equipment("Ocons Chainmail",(3,6,0),"OconMail.jpg","The sacred chainmail forged by the legend himself","body",(75,100,50)),
Equipment("Hazmat Suit",(2,5,1),"Hazmat.jpg","Protection from all sorts of McCrindle farts...","body",(0,10,10)),
Equipment("McMaster map",(1,2,1),"MACMap.jpg","A map of McMaster you can... wear? I guess?","body",(1,5,5)),
Equipment("Priest Gown",(2,0,2),"Gown.jpg","Wearing this gives people the impression you are a holy person...","body",(1,5,3)),
Equipment("Pizza Box",(3,1,1),"PizzaBox.jpg","Fully equipped with crusted cheese.","body",(1,5,1)),
Equipment("Starbucks Apron",(5,0,1),"Apron.jpg","If you put this on do you immediately know how to make a frappe?","body",(1,5,5)),
#Hand Items
Equipment("MSP430",(2,3,1),"MSP430.jpg","A literal piece of garbage.","hand",(-5,0,-5)),
Equipment("Old Headphones",(1,7,1),"OldHeadphones.jpg","Old frayed apple headphones. Good for whipping.","hand",(5,0,5)),
Equipment("Empty Bottle",(5,1,1),"EmptyBottle.jpg","Dasani, more like Dishonest! Amirite?!","hand",(1,0,1)),
Equipment("Banana Wires",(3,3,1),"BanWires.jpg","Alligator clips added for extra whippage.","hand",(8,0,8)),
Equipment("Wrench",(1,3,1),"Wrench.jpg","It's a wrench. 22mm.","hand",(10,0,0)),
Equipment("Pencil",(2,4,1),"Pencil.jpg","HB2. Sharpened.","hand",(2,0,5)),
Equipment("Squash Racket",(5,0,1),"Racket.jpg","Dr.Buijs' Racket? Voltage Divider!","hand",(5,0,10)),
Equipment("Willy Dog",(4,1,1),"Hotdog.jpg","Definitely not vegan","hand",(1,0,2)),
Equipment("Needa Pita",(3,6,1),"Pita.jpg","Better have gotten black olives on that","hand",(2,0,1)),
Equipment("Dirty Needle",(1,1,1),"Needle.jpg","This isn't clean. Somone find me a SharpXchange!",'hand',(10,0,5)),
Equipment("Used Plunger",(5,0,0),"Plunger.jpg","Used. Lovely...","hand",(10,0,10)),
Equipment("Broken Wine Bottle",(4,3,1),"WineBottle.jpg","A broken wine bottle from 1996, good year.","hand",(25,0,15)),
Equipment("Used Condom",(2,1,1),"Condom.jpg","The audacity of some people to leave their filth around. Probably would suck to get hit by...","hand",(10,0,-10)),
Equipment("Eng Phys Pen",(3,3,0),"PhysPen.jpg","It would be amazing if this thing actually worked. Plug it in and find all of 2P04","hand",(15,0,10)),
Equipment("Butter Knife",(3,6,1),"ButterKnife.jpg","Meant for spreading, not stabbing...","hand",(4,0,5)),
Equipment("Pee Bottle",(2,1,1),"PeeBottle.jpg","It is literally a bottle of urine.","hand",(10,0,0)),
Equipment("Tofu",(4,3,0),"Carrot.jpg","Vegan's delight","hand",(1,1,5)),
#Off-Hand Items
Equipment("Coffee",(2,4,1),"Coffee.jpg","The fuel of thinkers.","off-hand",(10,0,25)),
Equipment("Griffiths Electrodynamics",(2,4,2),"Griffiths.jpg","The holy scriptures which govern the fabric of our being","off-hand",(0,100,10)),
Equipment("An Ice-Cold Pint",(4,3,1),"Pint.jpg","Ale of the Gods.","off-hand",(3,0,-5)),
Equipment("Diary of the Fallen",(3,6,0),"Diary.jpg","The personal notes of an ancient Hero.","off-hand",(69,69,69)),
Equipment("Wood Shield",(4,3,2),"Shield.jpg","An old wooden shielf used in a play, you think...","off-hand",(5,75,-5)),
Equipment("Casio",(2,2,1),"Casio.jpg","This one can do integrals. That's illegal.","off-hand",(5,5,30)),
Equipment("Paint Brush",(3,0,1),"Brush.jpg","You can feel the emotions of a failed arts student coursing through this thing.","off-hand",(5,0,20)),
Equipment("Lenovo Laptop",(1,5,2),"Lenovo.jpg","This heap of computing majesty could block bullets... I think...","off-hand",(5,30,-5)),
Equipment("Priceless Painting",(3,0,1),"Painting.jpg","This painting is supposed to be worth millions...","off-hand",(1,20,5)),
Equipment("Brendan Fallons Lunchbox",(3,3,0),"Lunchbox.jpg","The Lunch Box of an Ancient Hero. Full of samosas","off-hand",(5,25,15)),
Equipment("Jar of Peanut Butter",(4,0,1),"Peanut.jpg","Death paste to those who are allergic... Could prove effective...","off-hand",(0,5,5)),
Equipment("Adderall",(4,0,1),"Adderall.jpg","Speed up, my dude!","off-hand",(0,0,50)),
Equipment("Drumstick",(4,3,2),"Drumstick.jpg","'Property of E-Smooth'","off-hand",(0,15,25)),
#Special/Dropped Items
Equipment("Iron Ring",(None),"IronRing.jpg","The One Ring to Rule them ALL.","hand",(1000,1000,1000)),
Equipment("Femtosecond Laser",(None),"Laser.jpg","Haugen's personal femtosecond laser.","hand",(500,0,999)),
Equipment("Minnicks Glasses",(None),"MinnickGlasses.jpg","The Spectacles of an ancient wizard.","head",(999,500,500)),
Equipment("Kenricks Oscilloscope",(None),"Oscilloscope.jpg","The window into the electronics world...","off-hand",(0,350,350)),
Equipment("Joint of Destiny",(None),"Joint.jpg","A tighly rolled spliff filled with Devil's lettuce... for real.","off-hand",(420,420,420)),
Equipment("PID control system",(None),"PID.jpg","A PID control system. Kp = 69, my dude.","head",(69,0,10)),
Equipment("LED of Power",(None),"LED.jpg","An LED with the power output of a neutron star, ok maybe not.","hand",(100,0,50)),
Equipment("Horrible Assignment",(None),"BadAss.jpg","A barely legible report on Fourier analysis.","off-hand",(1,1,5)),
Equipment("Cold Beer",(None),"ColdBeer.jpg","A freshly brewed pint from Andy Knights himself.","off-hand",(20,0,-20)),
Equipment("Green Bang Bong",(None),"GBB.jpg","The sacred glass flute providing righteous tokes since '69.","off-hand",(420,420,420)),
Equipment("3W Textbook",(None),"3WText.jpg","Text book that probably has useful information if you could read it. Too bad it has never been in the QT","off-hand",(15,5,10)),
Equipment("Fake Gun",(None),"FakeGun.jpg","Is this seriously what at the MAC cops carry...","hand",(5,0,5)),
Equipment("Eriks Frosted Tips",(None),"FrostedTips.jpg","Ever wanted to look rad as hell? Now you can!","head",(0,3,20)),
Equipment("Engineering Mug",(None),"EngMug.jpg","Do people even have these anymore?","hand",(1,0,2)),
Equipment("Crucifix",(None),"Crucifix.jpg","The Power of Chirst compels you!","hand",(10,0,10)),
Equipment("Huge Shirt",(None,"HugeShirt.jpg","This shirt is WAY too big","body",(0,5,5)),
Equipment("Puke",(None),"Puke.jpg","Ew, literally a pool of vomit","body",(1,0,-10)),
Equipment("Guitar",(None),"Guitar.jpg","Monster Mash.","hand",(5,0,10)),
Equipment("Phone",(None),"Phone.jpg","This thing has been dropped Graham's number times.",(5,6,9),
Equipment("Meow Mix",(None),"MeowMix.jpg","I love chicken, I love liver...","off-hand",(5,0,5))]


#Enemies: Enemy.name = "Name" - Enemy.info = "Description" - Enemy.location = (X,Y,Z) - Enemy.stats = (ATK, DEF, SPD) - Enemy.health = [integer]
#Enemies: Enemy.drop = Item dropped on death or given - Enemy.need = special item they want - Enemy.Sinfo = "Special comment they have if you bring them 'need' item"
#Example: Man = Enemy("Man","A Man",(1,1,1),drop,need,Sinfo,Dinfo)
#Bosses
ENEMIES = [
Enemy("Dr.Minnick","I'm jealous of people who are stupid, they have more opportunities to learn!",(3,3,1),(500,500,500),500,"minnicks glasses",None,"",""),
Enemy("Dr.Novog","Whats up folks.",(2,6,0),(420,420,420),400,"iron ring",None,"Smoke up folks! You've earned your Iron Ring!",""),
Enemy("Dr.Haugen","Pedrotti Cubed!",(1,6,2),(250,0,100),400,"femtosecond laser",None,"Oh my! You've earned the right to use my laser!",""),
Enemy("Kenrick","The oscilloscope is the window into the electronic world.",(3,4,1),(400,50,350),300,"kenricks oscilloscope",None,"Here, take this. It is the windor into the electronics world!",""),
Enemy("Dr.Kitai","It's just a midterm. Don't kill youself.",(0,3,2),(75,50,10),150,"led of power",None,"I've beeen looking all over for this! Where did you find it? Take this!",""),
Enemy("Dr.Knights","Whoever took the 3W text book... Shall feel my eternal wrath",(4,3,1),(200,100,1),500,"cold beer",None,"Here, you've earned this",""),
#Special
Enemy("Brendan Fallon","What's up dude? I'm here to bless up your shit",None,(9999,9999,9999),999,"green bang bong",None,"THANKS! TOKE UP MY DUDES!",""),
#General
Enemy("Father Frobenius","You need prayer.",(2,0,1),(10,10,10),25,"crucific",None,"","I am slain!"),
Enemy("Steven the first year","Have you go the LONCAPA Python code?",(3,6,1),(5,1,10),15,'engineering mug',None,"","I'm a failure at school and at home!"),
Enemy("Phil the drunk","MHhmgh, Soouh whatu we getta druuuunk",(5,1,1),(10,5,1),15,"puke",None,"","mhmh spooky ghost urggh ectoplasm noooooo"),
Enemy("Susie the vegan","Did I mention I'm vegan?",(4,3,0),(15,1,5),10,"3w textbook",None,"","I was going to bring it back I swear!"),
Enemy("Larry the bus driver","Is that even your bus pass?",(2,1,1),(5,10,4),10,"huge shirt",None,"","That was definitely not your bus pass!"),
Enemy("Brian the hipster","Have you ever heard of Frank Ocean?",(2,2,1),(5,2,10),10,"guitar",None,"","That's not vegan."),
Enemy("Mitch the TA","Where's my phone?",(0,3,1),(10,5,10),25,"phone",None,"","There's my phone."),
Enemy("Erik the arts student","Can you come see my exhibit?",(3,0,1),(5,15,5),20,"eriks frosted tips",None,"","Man, that's dumb!"),
Enemy("Megan the Bartender","Hey kid, want some beer?",(4,3,1),(1,20,75),20,"meow mix",None,"","Nuuuuuuuuuuuu"),
Enemy("Bill the MAC Cop","Give me your student card!",(3,5,1),(50,25,10),75,"fake gun",None,"","We aren't able to arrest you anyway!")]

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



