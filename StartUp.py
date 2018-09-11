#The Great Engineering Text Adventure
#Authors: Mitchell Lemieux, Tyler Kashak
#Music: Brian, Erik
#Start Date: April 14th, 2018
#Library of Items and Locations

from GameClasses import *

XRANGE = 7
YRANGE = 9
ZRANGE = 4

def Reset():
    global MAPS1
    global LOCATIONS1
    global ENEMIES1
    global ITEMS1
    global INTERACT1
    
    MAPS1 = [[[None for y in range(ZRANGE)] for y in range(YRANGE)] for x in range(XRANGE)]#0-5,0-7,0-2

    #Locations: Place.name = "Name" - Place.coords = (X,Y,Z) - Place.info = "location information" - Place.lore = "lore"
    #Example: Start = Map("Start",(0,0,0),"You start here")
    LOCATIONS1=[ 
    Map("Starting Location",(2,3,1),"FRONT OF JHE:\nBSB is to your right. Hatch to your left.\nJHE field is to your rear. Enter JHE by going forward.","You hear a booming voice that sounds oddly like a game developer. \ntype: 'inspect rules sign!'\nYou see the Iron Ring out front of JHE shining in the morning sun.\nThe campus is bustling with student life.\nThere are people heading in all directions with Kipling pranks\nstill scattered about JHE.",()),
    Map("Inside JHE",(2,4,1),"JHE LOBBY:\nTo your right you can exit towards BSB. To your left you can head into Hatch.\nForward is the Nuclear Research building. Behind you lies the exit.\nThere are also stairs going up and down.","JHE lobby is alive.\nStudents rushing all around as the smell of burnt coffee and sorrow tickles your nose.\nYou scan the faces around you but see no one familiar.\nThere is a confused air about this place as Kipling was just last night.\nMany engineers happy. Many more still grinding.",()),
    Map("Nuclear Research Building",(2,5,1),"NUCLEAR RESEARCH BUILDING:\nTo your left lies the JHE-Annex. The Reactor is in front of you.\nThe Police Station is to your right. JHE lobby is behind you.\nThere are stairs going down.","You have barely ever been in here other than to struggle through\n3 hours of waiting for a water level PID controller to reach steady state.\nYou wonder how anyone could get away with a floor plan this confusing.\nPerhaps that's why no terrorists have blown up the reactor because\nthey are all still lost in here...",()),
    Map("Inside Hatch",(1,4,1),"INSIDE HATCH:\nIn front of you lies JHE-Annex. To your right is the JHE lobby.\nTo your rear you can exit.\nTo your left is an alley.","That 'fresh building' smell still lingers.\nYou see members of the various clubs rushing from room to room.\nThe Kipling clock ticks away... only 364 more...\nWho is this Gerald Hatch anyway?",()),
    Map("In Front of Hatch",(1,3,1),"OUTSIDE HATCH:\nETB to your left. Enter Hatch by going forward.\nThe McMaster Map to your rear. JHE Entrance is to your right.","You stare at the newly completed building.\nThe sun still shines and you are irritated by the constant drone of the Hamiltonian sirens\nwhich you have yet to grow accustomed to...",()),
    Map("Map of McMaster",(1,2,1),"MCMASTER MAP:\nIn front of you lies the entrance to Hatch. To your right, JHE Field.\nTo your rear lies the Health Sci Library. T-13 is to your left.","Has anyone even used this thing?\nA lost freshman asks you for directions even though the map is clearly next to you.\nAfter sending them in the wrong direction you plan your next move.",()),
    Map("Health Sciences Library",(1,1,1),"HEALTH SCIENCES LIBRARY:\nIn front of you is the McMaster Map. To your right is the bus stop.\nMDCL is behind you. The Hospital West Wing is to your left.","You are constantly asked to be quiet even though you have yet to make a sound.\nAfter scanning the tables and see no one you recognize you take a seat\nin an armchair and stare out towards the centre of campus.\nYou daydream of a life where these study rooms weren't constantly full.",()),
    Map("The Bus Stop",(2,1,1),"BUS STOP:\nHealth Sciences Library to your left. JHE field in front of you.\nThe chapel is behind you. Art Museum to your right.","Students gather around to catch the next bus.\nYou get pushed and shoved as they desperately clammer on-board.\nYou overhear an argument between a student and the Bus Driver when suddenly the altercation\nturns to blows and pours onto the sidewalk.",()),
    Map("The Chapel",(2,0,1),"MCMASTER CHAPEL:\nThe Bus Stop is in front of you back out the door. There is a set of stairs going up.\nAs well as an old stairway leading downward.","The low drone of the organ draws you in.\nThe pews are relatively empty and the lighting quite dim.\nYou think it would be in your best interest\nto pray especially with exam season just around the corner...\nIt can't hurt, right? It'd probably work better than those healing stones\non your desk.",("r",'l','b')),
    Map("Outside the Art Museum",(3,1,1),"OUTSIDE ART MUSEUM:\nYou can enter the museum to your rear. Bus Stop is to your left.\nWilly-dog stand to your right. BSB field lies in front of you.","Standing out front of the art museum you feel you are already being critiqued.\nAfter narrowly escaping a conversation with an arts student\nabout their installation piece of a dirty coffee table...\nYou plan your next move.",()),
    Map("Inside the Art Museum",(3,0,1),"ART MUSEUM:\nThe exit lies in front of you.","Who knew McMaster had such a beautiful gallery.\nYou tilt your head endlessly until the art sort of makes sense.\nAfter telling yourself you could totally make every piece in the place had you been given\na chance you put your pinky out.\nThen contemplate your next move.",('r','l','b')),
    Map("The Willy Dog stand",(4,1,1),"WILLY DOG STAND:\nThe turning circle lies in front of you. Mills library at your rear.\nThe Archway to your right. The Art Museum is to your left.","Oh, that sweet sweet aroma.\nMany drunken nights flash through your head.\nThat Willy dog cart is more of a staple to McMaster students than the Archway next to it.\nWas it named Willy Dog after Sir William McMaster?\nYou'll never know...",()),
    Map("Mills Library",(4,0,1),"MILLS LIBRARY:\nThe Willy Dog Stand is in front of you. MUSC is to your right.\nYou can go downstairs.","This is definitely not Thode.\nYou wonder if anything gets done in this library.\nAll of the debauchery taking place on the 6th floor sends a shudder through your body.\nYou notice a stack of books...",('l','b')),
    Map("Statue of Sir William McMaster",(5,2,1),"WILLIAM MCMASTER STATUE:\nHamilton Hall is in front of you. The Archway is behind you.\nTurning Circle is to your left.","Approaching the statue you notice massive burn marks on the lawn and chunks\nout of the tree...\nHmm...\nWhat if Sir Willy McMaster was actually in that statue Han Solo style?\nAfter a quick selfie with Willy you plan your next move.",('r')),
    Map("BSB Field",(3,2,1),"BSB FIELD:\nThe turning circle is to your right. JHE field is to your left.\nEntrance to BSB is in front of you. The Art Museum is to your rear.","You look up to see the flags flapping happily in the morning breeze.\nThat sundial at their feet ticking to the tune of celestial magic.\nAfter swatting Neil Degrasse quotes from your thoughts...\nYou consider what to do next.",()),
    Map("JHE Field",(2,2,1),"JHE FIELD:\nBSB Field is to your right. McMaster map to your left.\nThe Bus Stop is at your rear. The entrance to JHE is in front of you.","The morning sun warms your face as you scoff at a hipster slack-lining.\nStudents lie in the grass around the field even though everybody knows\nnothing gets done studying outside.\nAfter narrowly dodging a frisbee you plan what to do.",()),
    Map("McMaster Student Centre",(5,0,1),"MUSC:\nMills is to your left. The Archway is in front of you.\nA custodial closet is down the stairs.","The Student Centre is alive.\nAfter counting the number of jean jackets in the Starbucks line like the Count from Sesame Street\nyou snap back to reality.\n(Oops there goes gravity).\nYou notice a Starbucks employee arguing with his manager before throwing their apron to the ground.",('r','b')),
    Map("The McMaster Archway",(5,1,1),"ARCHWAY:\nMUSC at your rear. Statue of Willy in front of you.\nEntrance to University Hall is to your right. The Willy Dog stand is to your left.","Probably the most beautiful structure at Mac.\nYou notice a hole that appears to have melted through the glass of the lamp underneath...\nYou snap a quick selfie in front of the Archway for the 'gram.",()),
    Map("Inside University Hall",(6,1,1),"UNIVERSITY HALL:\nThe exit is to your left.","The glares from portraits of old white founding fathers intimidate you.\nThe memories of failing midterms in their presence sends you into an almost trance-like state.\nYou notice that the portrait of Keyes totally looks like Stephen Fry.\nAfter talking yourself out of stealing a piece of Mac history you plan your next move.",('r','b','f')),
    Map("The Phoenix",(5,4,1),"THE PHOENIX:\nGeneral Sciences Building is to your left. Hamilton Hall is to your rear.\nThe trail to Bates is in front of you. You can also go down the stairs to Bridges Cafe.","Upon entering, a rush of memories from last night enter your mind.\nPeople's faces are a blur but you somewhat recall '16 tequila shots' as something you said.\nYou see a mysterious Hooded Man as he beckons you to come over.",('r')),
    Map("BSB",(3,3,1),"BSB:\nBSB field is at your rear. Exit BSB to your right.\nThe entrance to JHE is to your left. The Quantum Tunnel is down the stairs.","You were told JHE would be your home but after picking Eng Phys\nyou didn't realize how wrong you were.\nAt least the cafe is better than JHE's.\nA shutter runs through your body as you draw nearer to the electronics labs.\nWiping a cold sweat from your brow you plan ahead.",()),
    Map("Between JHE and BSB",(3,4,1),"JHE/BSB JUNCTION:\nEnter JHE to your left. General Sciences building to your right.\nBSB is behind you. The Police station is in front of you.","You look up and see the McMaster coat of arms engraved into the side of BSB.\nThis little pathway has been well worn and you wonder why they don't connect JHE and BSB anyway.\nAn underground (quantum) tunnel would save some hardship on a rainy day...",()),
    Map("Police Station",(3,5,1),"POLICE STATION:\nThe path between JHE & BSB behind you. The GO station lies ahead of you.\nThe Nuclear Research Building is to your left. The Tandem Accelerator is to your right.","Thoughts of getting kicked out of res parties fill your head.\nThose special constables are punks.\nYou mutter the lyrics of a certain N.W.A hit. After avoiding a campus P.D cruiser\nscreaming around the blind corner, you think of what to do next.",()),
    Map("Keyes",(4,6,1),"MARY KEYES:\nYou can head to the Bridge if you go forward. The GO station is to your left.\nThe Tandem Accelerator is at your rear. Bates is to your right.","A snack station that's open 'til midnight.\nWhat a life saver indeed.\nYou quickly thank the engineering gods for Mary Keyes and fight yourself\nfrom ordering chicken fingers & fries super combo...",()),
    Map("Nuclear Reactor",(2,6,1),"NUCLEAR REACTOR:\nRight is the GO station. Left is ABB.\n NRB is at your rear. The campus exit lies in front of you.\nGo down to enter.","As you approach you wonder if that steam is really radioactive?\nIt can't be.\nThe ominous structure draws you closer as you consider what it would be\nlike to swim in that sweet blue pool...",()),
    Map("ABB",(1,6,1),"ABB:\nThode is in front of you. JHE Annex is behind you.\nThe Nuclear Reactor is to your right. LOT I is to your left.\nYou can go up or down the stairs.","You stare at the electron microscope structure and wonder if it could even see your GPA...\nA tear rolls down your cheek. You collect yourself and plan what to do next.",()),
    Map("Thode",(1,7,1),"THODE:\nABB is at your rear. The campus exit is to your right.\nCootes Drive is to your left. You can go up or down the stairs.","Oh the Reactor Cafe.\nYou think of the good old days when you could actually see the reactor from the Cafe...\nAfter overhearing someone ask whether keV is bigger than MeV you first contemplate your existence,\nthen contemplate your next move...",('f')),
    Map("JHE Annex",(1,5,1),"JHE ANNEX:\nHatch is to your rear. ABB in front of you.\nITB is to your left. NRB to your right.\nThe Eng Phys office is up the stairs.","They made a big engineering building, got money, then added more.\nYou wonder why Eng Phys classes get pushed into the rooms in this side of JHE...\nHmm...",()),
    Map("DANGER",(2,7,1),"CAMPUS EXIT:\nHead to Thode by going left. Head down Cootes trail if you go right.\nThe Reactor is behind you.","A faint glow can be seen in the distance.\nWarning signs litter the trail as you squint to get a better look.\nA chill is sent down your spine as you see the flickering stretched shadows of\nfighting dance on the road ahead.\nYou cannot go straight... yet.",('f')),
    Map("ETB",(0,3,1),"ETB:\nTo your right is the Hatch Building. An alleyway is in front of you.\nT-13 is behind you. You can also go upstairs.","The memories of actually doing something in first year flood your mind.\nGear trains. Python. 3D printing.\nEngineering had such a different meaning in your first year...\nYou plan your next move.",('l')),
    Map("Lot M",(5,7,1),"LOT M:\nTo your left is the bridge. Bates is behind you.","After 3 days of hiking you arrive at Lot M.\nAfter 2 more days of looking for your car you give up and contemplate what to do next.",('f','r')),
    Map("Bates",(5,6,1),"BATES:\nLOT M lies in front of you. Keyes is to your left.\nThe trail to the Phoenix is behind you.","Memories of ridiculous res parties fill your mind.\nYou also recall the landfill of a room that was more of a circus attraction\nthan a living space.\nOh how distant first year seems...",('r')),
    Map("Trail",(5,5,1),"TRAIL TO PHOENIX:\nBates lies in front of you. The Phoenix at your rear.\nThe Tandem Accelerator is to your left.","Longboarding down this trail going Mach 16 was a blast and a half.\nDodging deer and first years like it's some sort of cube runner.\nNice.",('r')),
    Map("Hamilton Hall",(5,3,1),"HAMILTON HALL:\nThe Phoenix is in front of you. A road is to your left.\nThe Willy McMaster Statue is to your rear.","You think about helping some first years in the Math help centre.\nThen you don't.\nThey should learn to fight through it if they're going to make it through the\nnext 4 years.",('r')),
    Map("Turning Circle",(4,2,1),"TURNING CIRCLE:\nWilly Dog stand is to your rear. BSB-field is to your left.\nThe Willy McMaster Statue is to your right. Head down the road if you go forward.","The circle thing with the three trees in it is looking pretty nice\nin the morning sun.\nStudents rush all around.\nThe aroma from the Willy Dog stand is making you pretty hungry...",()),
    Map("Campus Road",(4,3,1),"A ROAD:\nEnter BSB to your left. Hamilton Hall to your right.\nThe turning circle is behind you. General Sciences building in front of you.","A lost first year's parent drives by in a mini-van\nclearly ignoring the 'no access' sign.\nYou thank your astrology sign for making sure they looked up and saw you.",()),
    Map("General Sciences",(4,4,1),"GENERAL SCIENCES BUILDING:\nThe Phoenix is to your right. The junction between JHE & BSB is to your left.\nThe Tandem Accelerator is in front of you. Exit to your rear.","Have you ever been in here?\nI haven't.\nYou see a group of people huddled around a pentagram-wearing goat heads.\nMaybe? I seriously don't know what goes on in here.",()),
    Map("Tandem Accelerator",(4,5,1),"TANDEM ACCELERATOR:\nThe General Sciences Building is behind you. The Police station is to your left.\nA trail is to your right. Keyes is in front of you.","Turns out the Tandem Accelerator is NOT a rad place to ride a 2-person bike...\nBummed out you remind yourself you graduated and consider what to do next.",()),
    Map("The Bridge",(4,7,1),"THE BRIDGE:\nLot M is to your right. Keyes is at your rear.\nHead down Cootes trail if you go left.","You narrowly avoid a GO bus\npick yourself up and brush yourself off.\nThen plan your next move.",('f')),
    Map("Cootes Trail",(3,7,1),"COOTES TRAIL:\nCampus exit is to your left. GO station to your rear.\nThe Bridge to Lot M is to your right.","The flickering light through the trees dances off of the trail ahead of you.\nYou smile as you see a squirrel gathering nuts,\nprobably for his little squirrel family.\nWith this new positive outlook on life you plan your next move.",('f')),
    Map("GO Station",(3,6,1),"GO STATION:\nThe Reactor is to your left. Keyes is to your right.\nCootes Trail is in front of you. The Police Station is behind you.","The rush of people and buses around you is disorienting.\nYou nearly get hit by 3 buses and 2 MAC Cop cars as\nyou play a strange game of real-life frogger.\nReaching a bench you sit down, catch your breath, and plan what to do next.",()),
    Map("Cootes Dr.",(0,7,1),"COOTES DRIVE:\nThode is to your right. Lot I is behind you.","You notice a series of pickup trucks for what must be a landscaping or construction company.\nThere is construction gear spread all over the place.\nThe sound of sirens grows louder as an ambulance suddenly rushes by.\nYou collect yourself and consider what to do next.",('f','l')),
    Map("Lot I",(0,6,1,),"LOT I:\nABB is to your right. Cootes Drive is in front of you.\nITB is to your rear.","Nope, your car isn't here.\nMaybe you parked in Lot M? Maybe not.\nAfter scoffing at all of the prof Mercedes that are way too nice...\nYou think of what to do.",('l')),
    Map("ITB",(0,5,1),"ITB:\nJHE-Annex is to your right. Lot I is in front of you.\nAn alley is behind you. You can go up OR down the stairs.","McMaster, back at it again with the horrible floor plan.\nAfter getting lost for 5 hours you finally reach the lobby\nand decide what to do.",('l')),
    Map("Alley",(0,4,1),"ALLEY:\nITB is in front of you. ETB is behind you.\nYou can enter Hatch to your right.","As you head down the narrow path between ITB and ETB you hear car horns blaring down Main Street.\nYou gather up some trash and put it in a garbage can like a good McMasterian.\nThen plan your next move.",('l')),
    Map("T-13",(0,2,1),"T-13:\nETB is in front of you. The McMaster Map is to your right.\nThe West Wing of the Hospital is behind you.","How many bad invigilators does it take to screw in a light bulb?\nI'm not sure but they took my damn Casio FX-911+C...",('l')),
    Map("West Hospital",(0,1,1),"HOSPITAL WEST WING:\nIn front of your is T-13. To your right is the Health Sci Library.\nThe East Wing of the Hospital is behind you.\nYou can go upstairs.","Doctors and Nurses rush around you.\nYou remember why you didn't want to become a doctor as you\nnearly faint looking at a patient's paper cut in the waiting room.\nAfter a drink from the water fountain you plan what to do.",('l')),
    Map("East Hospital",(0,0,1),"HOSPITAL EAST WING:\nIn front of you is the West Wing. MDCL is to your right.\nThe Parking Garage is below you.","You smile as you overhear a conversation between a doctor and a family.\nTurns out their child is going to make a full recovery.\nThanks science.",('l','b')),
    Map("MDCL",(1,0,1),"MDCL:\nThe East Wing of the Hospital is to your left. Health Sci library is forward.","After a solid 5 minutes of meditation in the reflection area.\nYou make your next decision feeling refreshed.",('b','r')),
    #Basement Level (X,Y,0)
    Map("Secret Room",(6,1,0),"SECRET ROOM:\nYou can only climb up and out.","You inspect the floorboards and find one is loose.\nUpon lifting it you reveal a secret room!\nYou climb down and find yourself surrounded by stacks of ancient books and\nforgotten items from McMaster's past.",('f','b','l','r','d')),
    Map("The Quantum Tunnel",(3,3,0),"QUANTUM TUNNEL:\nGo up to return to the main floor of BSB","What other faculty spends thousands of dollars on furniture for a\nliteral custodial closet in the BSB basement?\nYou guessed it...\nEng Phys. Gotta love em'",('f','b','l','r','d')),
    Map("Inside the Reactor",(2,6,0),"INSIDE THE REACTOR:\nGo up to head outside.","The hum of air conditioning drowns your thoughts.\nYou lose yourself staring into the faint blue glow of the pool as you slowly approach its edge.",('f','b','l','r','d')),
    Map("Thode Basement",(1,7,0),"THODE BASEMENT:\nGo up to head outside.","You feel the laser glares burning into the back of your neck as\nyou hastily walk amongst the rows of desks.\nIs it possible to book a study room down here without finding a phallic object drawn on the whiteboard?\nYou'll never know.",('f','b','l','r','d')),
    Map("Bridges",(5,4,0),"BRIDGES CAFE:\nYou can only go back up to the Phoenix.","You feel guilty walking in here after you performed a\nbeat down on a double big mac combo in a drunken stupor only hours earlier.\nAfter pledging to be more vegan in the future, you plan what to do next.",('f','b','l','r','d')),
    Map("Secret Trapdoor!",(0,2,0),"SECRET ROOM!:\nGo up to climb out.","You uncover a trapdoor after pulling up a loose floor tile.\nUpon descending you see stacks of failed midterms and assorted books all around you.\nA suit of armor and a chainmail flag with a skull on it are barely visible.\nWho made this place anyway?",('f','b','l','r','d')),
    Map("Custodial Closet",(5,0,0),"CUSTODIAL CLOSET:\nYou can only go up to go back to MUSC.","You enter the custodial closet and a formidable stench fills your nostrils...\nEw.",('f','b','l','r','d')),
    Map("NRB Basement",(2,5,0),"BASEMENT OF NRB:\nYou can only go back up to the main floor.","You head down the stairs to the basement...\nThe forgotten dreams of PhD students linger in the air.\nThere is an endless amount of engineering wizardry in the rooms around you.",('f','b','l','r','d')),
    Map("Chapel Undercroft",(2,0,0),"CHAPEL UNDERCROFT:\nYou can only go back up to the main floor.","You struggle down the dimly lit stairway into the undercroft.\nThe distinct smell of mould enters your nose as you travel further into the musty basement.\nThe faint glow of candles cause the shadows of ancient statues to flicker on the walls of the room...\nYou plan your next move.",('f','b','l','r','d')),
    Map("ETB Basement",(0,3,0),"ETB BASEMENT:\nYou can only go back up to the main floor.","After getting lost in a maze of corridors and locked rooms you stumble\nacross a door that is slightly ajar.\nYou open the door to reveal a rather small dark room.\nYou flick on the light switch.",('f','b','l','r','d')),
    Map("ITB Basement",(0,5,0),"ITB BASEMENT:\nYou can only go back up to the main floor.","As if the upstairs floor plan wasn't bad enough...\nAfter another 3 hours wandering around you are back where you started\nand don't feel like you learned anything...",('f','b','l','r','d')),
    Map("ABB Basement",(1,6,0),"ABB BASEMENT:\nYou can only go back up to the main floor.","The Laser lab is pretty darn cool.\nWalking around here you notice a number of PhD students looking rather shifty.\nHmmm...\nYou wonder why that is.",('f','b','l','r','d')),
    Map("Parking Garage",(0,0,0),"PARKING GARAGE:\nYou can only go back up to the Hospital.","The smooth floor down here makes an excellent skate surface.\nRad.\nIf only you learned how to kickflip.",('f','b','l','r','d')),
    Map("JHE Basement",(2,4,0),"JHE BASEMENT:\nYou can only go back up to the main floor.","You see the remnants of failed clubs and the shattered dreams of past engineers...\nThis place is a bit chilly.",('f','b','l','r','d')),
    Map("Mills Basement",(4,0,0),"MILLS BASEMENT:\nYou can only go back up to Mills.","Jeez has anyone ever been down here?\nThe rows of bookshelves seem to go on forever...\nIf only you could possess all of the knowledge they hold.",('f','b','l','r','d')),
    Map("Tandem Basement",(4,5,0),"TANDEM BASEMENT:\nYou can only go back up the stairs.","An old basement with all sorts of technological wizardry you don't recognize.\nIt seems like this place has been untouched for some time.\nLooking around you get the impression that not a lot of people come down here.",('f','b','l','r','d')),
    #Upper Level (X,Y,2) and Third Floor Thode
    Map("2nd Floor ITB",(0,5,2),"2ND FLOOR ITB:\nYou can only go back down the stairs.","Walking around up here you don't find much other than lab benches with strange instruments.\nThis place gives you the impression that there must be some high level engineering physics going on...",('f','b','l','r','u')),
    Map("2nd Floor ABB",(1,6,2),"2ND FLOOR ABB:\nYou can only go back down the stairs.","You were told JHE would be your home.\nNope.\nInstead you recall countless hours lectures on the 2nd floor\nas you drifted in and out of daydreams staring out the windows on a spring afternoon...",('f','b','l','r','u')),
    Map("2nd Floor JHE",(2,4,2),"2ND FLOOR JHE:\nYou can only go back down the stairs.","You spend 20 minutes staring at the 1970 graduating class wondering if you could ever pull off a moustache like that...\nAfter realizing the cool lecture halls were only given to first years.\nYou shake your fist and plan your next move.",('f','b','l','r','u')),
    Map("2nd Floor ETB",(0,3,2),"2ND FLOOR ETB:\nYou can only go back down the stairs.","You realize you really have never come up here.\nYou see 4th year Eng Phys students hurry out of a long-winded lecture.\nAfter picking a booger.\nYou plan your next move.",('f','b','l','r','u')),
    Map("Eng Phys Office",(1,5,2),"ENG PHYS OFFICE:\nYou can only go back down the stairs.","The portrait of Dr. Novog makes you jealous as you realize you could\nnever pull off a hairstyle like that.\nYou scan the display case of past Eng Phys projects.\nThey display these as trophies...\nTrophies which only tell a story of endless grind you think to yourself...",('f','b','l','r','u')),
    Map("The Pheonix Loft",(5,4,2),"PHOENIX LOFT:\nYou can only go back down the stairs.","The history up here is incredible. So many relics from a time long past.\nFrom old costumes from plays to furniture.\nAfter a quick Shakespearean sonnet you think of what to do next.",('f','b','l','r','u')),
    Map("Upstairs Chapel",(2,0,2),"2ND FLOOR CHAPEL:\nYou can only go back down the stairs.","The combination of ringing bells and echoes from the organ is deafening.\nYou can barely collect your thoughts.\nThe cobwebs and dust give you the impression this place has been ill-travelled\nand long forgotten.",('f','b','l','r','u')),
    Map("2nd Floor W Wing",(0,1,2),"2ND FLOOR W WING:\nYou can only go back down the stairs.","The endless number of rooms are mesmerizing.\nYou don't even know which way to go.\nAfter being lost for 2 hours you circle back to where you entered.",('f','b','l','r','u')),
    Map("2nd Floor UH",(6,1,2),"2ND FLOOR UH:\nYou can only go back down the stairs.","You make your way up the rickety staircase into a room from a time long past.\nYou notice a dust covered table with some old instruments and clutter thrown about.",('f','b','l','r','u')),
    Map("2nd Floor BSB",(3,3,2),"2ND FLOOR BSB:\nYou can only go back down the stairs.","Despite the horrible numbering of floors the layout of the building is great.\nNot a complaint with this one.",('f','b','l','r','u')),
    Map("Climbing MDCL",(1,0,2),"CLIMBING MDCL:\nYou can continue climbing or go back down...","You struggle and find yourself on the outer wall of MDCL.",('f','b','l','r')),
    Map("Roof of MDCL",(1,0,3),"MDCL Roof:\nYou can only go back down.","With all of your might you pull yourself up and onto the roof.\nYou can see the majority of campus from up here!",('f','b','l','r','u')),
    Map("3rd Floor Thode",(1,7,3),"3RD FLOOR THODE:\nYou can only go back down the stairs.","After hauling up another set of stairs you realize you probably shouldn't\nhave given up on your Pulse membership...\nThe sounds of sobbing can be heard from all around you.\nAfter you dispense all of your tissues to passing I-Sci's you plan your next move.",('f','b','l','r','u')),
    Map("2nd Floor Thode",(1,7,2),"2ND FLOOR THODE:\nYou can go up or down the stairs.","As you enter Club Thode the smell of feet enters your nostrils.\nWho goes barefoot in a library? C'mon.\nThe memory of countless hours spent slamming together a report made of nonsense, caffeine,\nand hope makes you light headed...\nComing to your senses... You plan your next move.",('f','b','l','r'))]

    #Items: Equipment.name = "Name" - Equipment.location = tuple of location - Equipment.image = .jpg of item
    #       Equipment.info = "info" - Equipment.worn = 'head','hand','body',or 'off-hand' - Equipment.stats = (Atk,Def,Spd)
    #Example: Gun = Equipment("Gun",(0,0,0),"Gun.jpg","It shoots people.","hand",(100,0,100),-101)
    #Head Items
    ITEMS1 = [
    Equipment("Fireball Hat",(2,2,1),"EngHat.jpg","Kind of like the hat you bought in first year and thought you'd wear forever...","head",(0,3,1),-101),
    Equipment("Pope Hat",(2,0,2),"PopeHat.jpg","Does the Pope where a silly hat? Now you do.","head",(0,3,2),-101),
    Equipment("Goggles",(3,2,1),"Goggles.jpg","Got PPE?","head",(2,0,2),-101),
    Equipment("Wendy's Bag",(0,6,1),"WendyBag.jpg","Fully equipped with grease stains.","head",(1,0,-5),-101),
    Equipment("Empty Bucket",(5,0,0),"Bucket.jpg","The smell of cheap soap still lingers.","head",(0,10,1),-101),
    Equipment("Gas Mask",(3,5,1),"GasMask.jpg","No one cared who I was till I put on the mask.","head",(3,6,5),-101),
    Equipment("Hard Hat",(4,2,1),"HardHat.jpg","You don't really want to look like a Civil kid. But at least it protects your head.","head",(1,10,5),-101),
    Equipment("Laser Safety Glasses",(1,6,0),"LSGlasses.jpg","Protection from the UV, my dude.","head",(0,3,5),-101),
    Equipment("Raybans",(5,5,1),"Raybans.jpg","GQ Teen says Raybans, Board Shorts, Vans, and a Muscle Tee.","head",(0,1,3),-101),
    Equipment("Bike Helmet",(3,7,1),"BikeHelmet.jpg","One of those fast Tour de France ones.","head",(0,8,10),-101),
    Equipment("Surgical Mask",(0,1,1),"SurgicalMask.jpg","Don't touch me I'm sterile!","head",(0,2,3),-101),
    Equipment("Phil's Braces",(2,5,0),"PhilBraces.jpg","Bark AND the bite.","head",(3,2,1),-101),
    Equipment("Santa Hat",(0,0,1),"SantaHat.jpg","Happy Holidays!","head",(0,3,2),-101),
    Equipment("Plastic Bag",(2,1,1),"PBag.jpg","The audacity of some people to leave their filth around.","head",(0,1,-10),-101),
    Equipment("Party Hat",(3,6,1),"PartyHat.jpg","A nice hat from a cracker.","head",(0,5,3),-101),
    #Body Items
    Equipment("Eng Phys Shirt",(3,3,0),"EngPhysShirt.jpg","Rolling Rock baby! Premium Stream my ass... More like premium pain...","body",(0,7,5),-101),
    Equipment("Big Hits Shirt",(6,1,1),"BigHits.jpg","The Shirt of the Hero of Kyvach!","body",(10,5,5),-101),
    Equipment("Okons Chainmail",(0,2,0),"OkonMail.jpg","The sacred chainmail forged by the legend himself","body",(25,50,25),-101),
    Equipment("Hazmat Suit",(2,5,1),"Hazmat.jpg","Protection from all sorts of McCrindle farts...","body",(0,10,5),-101),
    Equipment("Priest Gown",(2,0,2),"Gown.jpg","Wearing this gives people the impression you are a holy person...","body",(1,5,3),-101),
    Equipment("Pizza Box",(0,3,1),"PizzaBox.jpg","Fully equipped with crusted cheese.","body",(1,5,1),-101),
    Equipment("Starbucks Apron",(5,0,1),"Apron.jpg","If you put this on do you immediately know how to make a frappe?","body",(1,5,5),-101),
    Equipment("Maroon Jumpsuit",(5,1,1),"MaroonSuit.jpg","Overalls of the Maroons","body",(1,8,5),-101),
    Equipment("Redsuit",(2,4,2),"Redsuit.jpg","Overalls of drunks... I mean engineers","body",(5,5,5),-101),
    Equipment("High Vis Vest",(2,6,1),"HighVis.jpg","Safety first, folks.","body",(0,5,3),-101),
    Equipment("Toilet Seat",(5,0,0),"Toilet.jpg","How do you even wear this?","body",(0,3,2),-101),
    Equipment("Blazer",(5,6,1),"Blazer.jpg","Styyyyyylishhhhhh","body",(0,4,1),-101),
    Equipment("Hockey Pads",(5,7,1),"HockeyPads.jpg","IM NOT WEARIN' HOCKEY PADS!","body",(3,13,5),-101),
    Equipment("Wool Sweater",(5,3,1),"WoolSweater.jpg","Just like grandma makes.","body",(1,4,6),-101),
    Equipment("Tony Hawk Shirt",(3,5,1),"TonyHAwkShirt.jpg","A shirt personally made by tony hawk!","body",(5,5,5),-101),
    #Hand Items
    Equipment("MSP430",(2,3,1),"MSP430.jpg","A literal piece of garbage.","hand",(-5,0,-5),-5),
    Equipment("Hulk Hands",(0,3,0),"HulkHands.jpg","These pack a serious punch...","hand",(15,5,20),-101),
    Equipment("Old Headphones",(1,5,1),"OldHeadphones.jpg","Old frayed apple headphones. Good for whipping.","hand",(5,0,5),-101),
    Equipment("Empty Bottle",(4,1,1),"EmptyBottle.jpg","Dasani, more like Dishonest! Amirite?!","hand",(1,0,1),-101),
    Equipment("Banana Wires",(3,3,1),"BanWires.jpg","Alligator clips added for extra whippage.","hand",(8,0,8),3),
    Equipment("Wrench",(1,3,1),"Wrench.jpg","It's a wrench. 22mm.","hand",(9,0,2),-101),
    Equipment("Pencil",(2,4,1),"Pencil.jpg","HB2. Sharpened.","hand",(2,0,5),-101),
    Equipment("Squash Racket",(5,0,1),"Racket.jpg","Dr. Buijs' Racket? Voltage Divider!","hand",(5,0,8),-101),
    Equipment("Willy Dog",(4,1,1),"Hotdog.jpg","Definitely not vegan","hand",(1,0,2),5),
    Equipment("Needa Pita",(4,6,1),"Pita.jpg","Better have gotten black olives on that","hand",(2,0,1),5),
    Equipment("Dirty Needle",(0,4,1),"Needle.jpg","This isn't clean. Someone find me a SharpXchange!",'hand',(7,0,5),-101),
    Equipment("Used Plunger",(5,0,0),"Plunger.jpg","Used. Lovely...","hand",(10,0,10),-101),
    Equipment("Broken Wine Bottle",(4,3,1),"WineBottle.jpg","A broken wine bottle from 1996, good year.","hand",(10,0,5),-101),
    Equipment("Butter Knife",(4,6,1),"ButterKnife.jpg","Meant for spreading, not stabbing...","hand",(4,0,5),-101),
    Equipment("Pee Bottle",(2,1,1),"PeeBottle.jpg","It is literally a bottle of urine.","hand",(4,0,0),-101),
    Equipment("Tofu",(5,4,0),"Carrot.jpg","Vegan's delight.","hand",(1,0,5),2),
    Equipment("Space Pop",(1,7,2),"SpacePop.jgp","Get ready to go to space pop city.","hand",(4,0,10),1),
    Equipment("Banana",(1,7,1),"Banana.jpg","High in potassium.","hand",(5,0,5),2),
    Equipment("PVC Pipe",(4,7,1),"PVCPipe.jpg","Probably part of a PID project...","hand",(9,2,10),-101),
    Equipment("Old Car Keys",(0,6,1),"CarKeys.jpg","Fun for babies. Not for Batman.","hand",(7,0,15),-101),
    Equipment("Ukelele",(4,4,1),"Ukelele.jpg","Wasting away again in Margaritaville...","hand",(6,0,5),-101),
    Equipment("Lamp",(0,5,1),"Lamp.jpg","I love lamp.","hand",(8,0,4),-101),
    Equipment("Mop",(0,0,1),"Mop.jpg","I'm going to clean up this town.","hand",(6,0,4),-101),
    Equipment("Skateboard",(0,0,0),"Skateboard.jpg","Cowabunga, dude.","hand",(9,0,10),-101),
    Equipment("Candlestick",(4,0,0),"Candlestick.jpg","Lumiere is up to no good.","hand",(7,0,5),-101),
    Equipment("Frisbee",(2,2,1),"Frisbee.jpg","Look at the flick of the wrist!","hand",(3,0,5),-101),
    Equipment("Tire Iron",(5,7,1),"TireIron.jpg","Is this even a real tool? Or just a murder weapon...","hand",(11,0,3),-101),
    Equipment("Car Keys",(4,2,1),"CarKeys.jpg","Volkswagen car keys.\nHmm...","off-hand",(5,0,5),-101),
    Equipment("Shovel",(5,0,0),"Shovel.jpg","Call a spade a spade.","hand",(15,0,5),-101),
    Equipment("Febreze",(1,0,1),"Ferbreze.jpg","Kills 99.9% of odour at the source!","hand",(6,0,10),-4),
    #Off-Hand Items
    Equipment("Cricket",(3,3,2),"Cricket.jpg","Makes the sound commonly heard at 2W lectures.","off-hand",(1,1,1),3),
    Equipment("Coffee",(2,4,1),"Coffee.jpg","The fuel of thinkers.","off-hand",(3,0,9),1),
    Equipment("Griffiths Electrodynamics",(2,4,2),"Griffiths.jpg","The holy scriptures which govern the fabric of our being","off-hand",(0,10,5),-101),
    Equipment("Ice-Cold Pint",(4,3,1),"Pint.jpg","Ale of the Gods.","off-hand",(3,0,-5),2),
    Equipment("Diary of the Fallen",(0,2,0),"Diary.jpg","The personal notes of an ancient Hero.","off-hand",(25,20,30),-101),
    Equipment("Wood Shield",(5,4,2),"Shield.jpg","An old wooden shield used in a play, you think...","off-hand",(5,20,-5),-101),
    Equipment("Casio",(2,7,1),"Casio.jpg","This one can do integrals. That's illegal.","off-hand",(1,5,10),-101),
    Equipment("Paint Brush",(3,1,1),"Brush.jpg","You can feel the emotions of a failed arts student coursing through this thing.","off-hand",(5,0,5),-101),
    Equipment("Lenovo Laptop",(1,5,2),"Lenovo.jpg","This heap of computing majesty could block bullets... I think...","off-hand",(5,15,-5),-101),
    Equipment("Priceless Painting",(3,0,1),"Painting.jpg","This painting is supposed to be worth millions...","off-hand",(1,10,5),-101),
    Equipment("Brendan Fallon's Lunchbox",(3,3,0),"Lunchbox.jpg","The Lunch Box of an Ancient Hero. Full of samosas","off-hand",(5,10,5),-101),
    Equipment("Jar of Peanut Butter",(4,0,1),"Peanut.jpg","Death paste to those who are allergic... Could prove effective...","off-hand",(0,5,5),5),
    Equipment("Adderall",(5,3,1),"Adderall.jpg","Speed up, my dude!","off-hand",(0,0,50),2),
    Equipment("Drumstick",(5,4,2),"Drumstick.jpg","'Property of E-Smooth'","off-hand",(0,10,15),-101),
    Equipment("Bottle Opener",(3,7,1),"BottleOpener.jpg","I wish I had a bottle of wine right about now...","off-hand",(0,5,15),-101),
    Equipment("Jar of Mayo",(0,2,1),"Mayo.jpg","Is mayonaise an instrument?","off-hand",(3,0,5),1),
    Equipment("Jar of Horse Radish",(4,5,1),"HRaddish.jpg","Apparently not an instrument...","off-hand",(2,0,4),3),
    Equipment("Goldfish",(2,0,2),"Goldfish.jpg","Fun fact, not made of real gold.","off-hand",(1,1,1,),4),
    Equipment("Tarzan VHS",(0,2,1),"Tarzan.jpg","If only I had a VCR...","off-hand",(0,2,6),3),
    Equipment("Couch Cushion",(1,7,1),"CCushion.jpg","I hope I find I pillow fight.","off-hand",(4,10,1),-101),
    Equipment("VH Sauce",(1,4,1),"VHSauce.jpg","Sweet and sour. Nice.","off-hand",(1,2,1),1),
    Equipment("Frank's Red Hot",(0,4,1),"FranksRed.jpg","I put that...","off-hand",(3,0,2),1),
    Equipment("Old Candle",(2,0,0),"OldCandle.jpg","Seems like it's had some use.","off-hand",(0,2,2),-101),
    Equipment("Shampoo",(0,0,1),"Shampoo.jpg","Yeah, I could use a shower...","off-hand",(4,0,3),-101),
    Equipment("Holy Bible",(2,0,1),"Bible.jpg","King James version...","off-hand",(3,0,3),-101),
    Equipment("Old Ladder",(0,7,1),"OldLadder.jpg","Pretty rickety but would work for climbing.","off-hand",(14,8,-15),-101),
    Equipment("Paper Towels",(0,5,2),"PaperTowels.jpg","WHERE'S THE PAPER TOWELS?","off-hand",(2,0,1),-101),
    Equipment("Cheese",(5,7,1),"Cheese.jpg","Not just cheddar, the smelly kind.","off-hand",(1,1,1),5),
    #Special/Dropped Items
    Equipment("Iron Ring",(None),"IronRing.jpg","The One Ring to Rule them ALL.","hand",(1000,1000,1000),-100),
    Equipment("Gilded Blunderbuss",(None),"Blunderbuss.jpg","A beautiful firearm with infinite ammo.","hand",(200,5,50),-101),
    Equipment("Femtosecond Laser",(None),"Laser.jpg","Haugen's personal femtosecond laser.","hand",(125,0,999),-101),
    Equipment("Minnick's Glasses",(None),"MinnickGlasses.jpg","The spectacles of a wizard from the High Order of the Ancient Council.","head",(100,100,100),-101),
    Equipment("Kenrick's Oscilloscope",(None),"Oscilloscope.jpg","The window into the electronics world...","off-hand",(0,150,50),-101),
    Equipment("Joint of Destiny",(None),"Joint.jpg","A tighly rolled spliff filled with Devil's lettuce... for real.","off-hand",(420,420,420),-101),
    Equipment("PID control system",(None),"PID.jpg","A PID control system. Kp = 69, my dude.","head",(45,0,10),-101),
    Equipment("LED of Power",(None),"LED.jpg","An LED with the power output of a neutron star, ok maybe not.","hand",(21,0,20),-101),
    Equipment("Horrible Assignment",(None),"BadAss.jpg","A barely legible report on Fourier analysis.","off-hand",(3,0,0),-101),
    Equipment("Cold Beer",(None),"ColdBeer.jpg","A freshly brewed pint from Andy Knights himself.","off-hand",(15,0,20),2),
    Equipment("Green Bang Bong",(None),"GBB.jpg","The sacred glass flute providing righteous tokes since '69.","off-hand",(420,420,420),-101),
    Equipment("3W Textbook",(None),"3WText.jpg","Text book that probably has useful information if you could read it. Too bad it has never been in the QT","off-hand",(5,5,10),-101),
    Equipment("Fake Gun",(None),"FakeGun.jpg","Is this seriously what at the MAC cops carry...","hand",(5,0,5),-101),
    Equipment("Erik's Frosted Tips",(None),"FrostedTips.jpg","Ever wanted to look rad as hell? Now you can!","head",(0,3,20),-101),
    Equipment("Engineering Mug",(None),"EngMug.jpg","Do people even have these anymore?","hand",(1,0,2),-101),
    Equipment("Crucifix",(None),"Crucifix.jpg","The Power of Chirst compels you!","hand",(10,0,10),-101),
    Equipment("Huge Shirt",(None),"HugeShirt.jpg","This shirt is WAY too big","body",(0,5,5),-101),
    Equipment("Clean Needle",(None),"CleanNeedle.jpg","No more spreadin' disease!","hand",(9,0,9),-101),
    Equipment("Puke",(None),"Puke.jpg","Ew, literally a pool of vomit","body",(1,0,-10),-2),
    Equipment("Guitar",(None),"Guitar.jpg","Monster Mash.","hand",(10,3,5),-101),
    Equipment("Swordfish",(None),"Swordfish.jpg","I'd better be careful eating this!","off-hand",(10,5,5),12),
    Equipment("Phone",(None),"Phone.jpg","This thing has been dropped Graham's number times.","off-hand",(5,6,9),-101),
    Equipment("Meow Mix",(None),"MeowMix.jpg","I love chicken, I love liver...","off-hand",(5,0,5),1),
    Equipment("Visor Glasses",(None),"FastGlasses.jpg","Damn, you are now travelling waaaay to fast. Slow down dude!","head",(1,5,35),-101),
    Equipment("Cold Steel Katana",(None),"Katana.jpg","This could probably kill a buffalo fish...","hand",(18,5,20),-101),
    Equipment("Vomit",(None),"Vomit.jpg","Literally spew.","off-hand",(0,0,1),-1),
    Equipment("Stylish Watch",(None),"watch.jpg","If only you learned how to tell time on an analog clock...","off-hand",(0,15,20),-101),
    Equipment("Capstone Tools",(None),"CapTools.jpg","Shouldn't the 4A06 students be using these?","off-hand",(1,1,1),-101),
    Equipment("Silicon Substrate",(0,3,2),"Substrate.jpg","A bulk silicon wafer.","off-hand",(1,1,1),-101),
    Equipment("Voltage Divider",(None),"VDivider.jpg","It is a Voltage Divider!","off-hand",(20,25,20),-101),
    Equipment("Dumbbell",(1,0,1),"Dumbbell.jpg","The pump is the greatest feeling in the world.","off-hand",(5,0,2),-101),
    Equipment("Green Lantern Shirt",(None),"GLShirt.jpg","Darkest day... Darkest night...","body",(15,15,10),-101),
    Equipment("Eng Phys Pen",(None),"PhysPen.jpg","It would be amazing if this thing actually worked. Plug it in and find all of 2P04.","hand",(5,0,5),-101),
    Equipment("Solar Cell",(None),"SolarCell.jpg","Harness the power of the Sun!\nI really hope I don't drop this...","off-hand",(1,1,1),-101),
    Equipment("Solar Ray",(None),"SolarRay.jpg","The literal power of the Sun!","hand",(100,20,50),-101),
    Equipment("Bleach Squirt Bottle",(None),"Bleach.jpg","Probably wouldn't be nice to get sprayed with.","hand",(15,5,20),-10),
    Equipment("Flux Capacitor",(None),"FluxCapacitor.jpg","If only I could go back to 1985...","hand",(1,1,1,),-101),
    Equipment("Pink Donut",(None),"PinkDonut.jpg","This is what fusion is all about?","off-hand",(1,1,1,),2),
    Equipment("Fanny Pack",(None),"FannyPack.jpg","Made for style. Not for carrying.","body",(3,8,15,),-101),
    Equipment("Einsteins Brain",(None),"Brain.jpg","Feel's kind of weird walking around with this...","off-hand",(1,1,1),10),
    Equipment("Pedrotti Cubed",(None),"Pedrotti.jpg","'Property of Harold Haugen, one of the 3 Quantum Relics' is inscribed on the first page.","off-hand",(50,150,250),-101),
    Equipment("Gamma Glove",(None),"GammaGauntlet.jpg","Shorter than it really is due to length contraction, one of the 3 Quantum Relics","hand",(250,100,20),-101),
    Equipment("Relativistic Key",(None),"Relativistickey.jpg","You can feel the power radiating from this thing.","hand",(1,1,1),-101),
    Equipment("Bowling Ball",(None),"BowlingBall.jpg","Heavy.","hand",(20,15,-5),-101),
    Equipment("Ambifacient Lunar Waneshaft",(None),"Dumbness.jpg","The design consists simply of six hydrocoptic marzlevanes,\nthey fit to the ambifacient lunar waneshaft so that side fumbling is effectively prevented","off-hand",(1,1,1),-101),
    Equipment("Faradays Cage",(None),"Faraday.jpg","THE Faraday cage.","head",(20,75,15),-101),
    Equipment("Rusty Key",(None),"RustyKey.jpg","You can just about read:\n'By the building where the smallest are seen.'\n'This key will provide for those who are keen'","off-hand",(1,1,1),-101),
    Equipment("Old Scroll",(None),"OldScroll.jpg","It reads:\n'A permanent title is too much to bear.'\n'My secret cache, is under there.'","off-hand",(0,0,0),-101),
    Equipment("Ancient Incantation",(None),"Incantation.jpg","An old tattered scroll with an incantation written in Latin.","off-hand",(1,1,1),-101),
    Equipment("Declaration of Independence",(None),"DOI.jpg","I'm going to steal the Declaration of Independence...","off-hand",(1,1,1),-101),
    Equipment("Gauss Eye",(None),"GaussEye.jpg","You can feel the electromagnetic energy emanating from it, one of the 3 quantum relics",'head',(100,100,100),-101)]
    
    #Enemies: Enemy.name = "Name" - Enemy.info = "Description" - Enemy.location = (X,Y,Z) - Enemy.stats = (ATK, DEF, SPD) - Enemy.health = [integer]
    #Enemies: Enemy.drop = Item dropped on death or given - Enemy.need = special item they want - Enemy.Sinfo = "Special comment they have if you bring them 'need' item"
    #Example: Man = Enemy("Man","A Man",(1,1,1),drop,need,Sinfo,Dinfo)
    #Bosses/Profs
    ENEMIES1 = [
    Enemy("Dr. Minnick",
          "'Hello and welcome to how we retrieve your iron ring.'\n'The Quantum Order does not know exactly what you have done.'\n'However, we have felt the consequences of your actions.'\n'I believe the only way to explain this is to show you.'\n'The Quantum Order has gathered intelligence that Kenrick has been using\nhis oscilloscope for evil.'\n'I need you to confront him and return his oscilloscope if we are to go further.'",(None),(400,400,400),200,"Minnick's glasses","Kenrick's oscilloscope","'Ah, you have returned.'\n'You see, Kenrick has retrofitted his oscilloscope and created some sort\nof 'window' into the electronics world.'\n'Using this window he has been attempting to access the minds of the greatest\nphysicists in history and use their power for evil!'\n'Our intelligence does not go any further and we do not know what he has done.'\n'All that we do know is that after last night you must be rooted in all of this just as the prophecy foretold.'\n'Take these, if you truly are the one, they will reveal what you need to see.'\n'I suggest you start in the museum.'\n'Also, my lab has since been compromised so I will work in secret in the basement of Thode.'\n'Once you have found the next relic, my workbench will be ready...'","'I'm jealous of stupid people, they have more opportunities to learn!'"),
    Enemy("Dr. Novog",
          "What's up folks?",(None),(420,420,420),100,"ancient incantation",'pink donut',"'Alright folks, here's the scoop.'\n'I could only talk to you via the fusion network because the integrity of faculty\ncommunication has been compromised.'\n'The Engineering Physics professors are actually members of an Ancient Council known as The Quantum Order.'\n'For years we have kept McMast-'\n'An assassin?'\n'Hmm... I see, things are worse than we thought.'\n'We have known of this uprising within the faculty for some time but\nwere unaware of just how strong they have grown.'\n'As you have heard, a prophecy foretold of an adventurer dictating the future of the faculty.'\n'This evil group wants nothing more than to take advantage of your power and influence for their own plans.'\n'The choices you make will be yours and yours alone, however, the Quantum Order\nurges that you consider the consequences of your actions.'\n'It is our duty to assist you in realizing your ability but what comes of your power is out of our hands.'\n'You must contact the oracles who foretold of your coming, they will give you the knowledge you require.'\n'Each member of the Quantum Order only knows of the location one Oracle.'\n'For that reason I can only help you so much.'\nDr. Novog pushes a button on a nearby control panel.\nA crane arm descends into the Reactor pool to retrieve a crate from its depths.\n'Take this incantation and find the ancient mirror in the basement of Mills Library... it is your time.'",""),
    Enemy("Dr. Haugen","'Hello, as you are likely aware, there has been a disturbance...'\n'You losing your Iron Ring was no accident, it was taken from you.'\n'The Quantum Order is an ancient fold whose goal is to protect the\nUniversity from certain doom and misuse of our knowledge.'\n'There has been an item of importance stolen from us and we need it returned immediately.'\n'Especially if you are to find your Iron Ring.'\n'The council has received intelligence that Dr. Soleymani has stolen Einstein's brain from the McMaster vault.'\n'You must retrieve it at once, she can be found somewhere in the hospital.'\n'Do not underestimate her! She has been tempted by a Dark Lord.'\n'The Quantum Order requires that you defeat her and return the brain at once!'",(None),(250,100,999),200,"femtosecond laser","einsteins brain","'Oh my! You've returned! I knew you could do it!'\n'Quickly, hand it over!'\nYou hand Dr. Haugen the brain and he opens the fridge placing it inside.\n'Now, we just need to mount my laser onto my bench-'\nSuddenly a rabid Grad Student bursts into the lab!\n'Hand over the brain, the Dark Lord demands it!' he says.\n'If you strike me down, I will become more powerful than\nyou could possibly imagine' Dr. Haugen replies.\nThe Grad Student lunges at Dr. Haugen who disappears entirely!\nJust before the perplexed Grad Student turns towards you he is met by your blow\nand falls to the floor.","Oh my!"),
    Enemy("Dr. Kitai","'I've been trying to develop a new LED...'\n'But I need some silicon, find me a Silicon Substrate please!'",(None),(150,50,50),150,"LED of power","silicon substrate","'I've been looking for one just like this, how did you get it?'\n'Maybe you are th-'\n'Nevermind... just be on the lookout for Dr. Kleimann.'","'It was only a midterm, don't off yourself.'"),
    Enemy("Dr. Knights","'Whoever took the 3W Textbook from the QT shall feel my eternal wrath...'",(None),(200,100,50),300,"cold beer","3w textbook","'I've been looking all over for that, have a cold one on me!'\n'But before you go you should know that a difficult road lies ahead.'\n'It will not be easy to have your Iron Ring returned to you'\n'Dr. Haugen should be the one you seek next.'","'What are you doing?!'"),
    Enemy("Dr. Preston","'I would like to improve my already impressive dad strength.'\n'Bring me a dumbbell.'",(None),(250,150,100),300,"green lantern shirt","dumbbell","'Yes! Now I can get the pump I've been after!'\n'Go look for Dr. Buijs he has much more to tell than I.'","HOW DID YOU OVERCOME MY DAD STRENGTH?!"),
    Enemy("Dr. Kleimann","'We have been looking for you.'\n'The Department is not pleased...'\n'But first, the McMaster Police have confiscated my Solar Cell, go get it.'\n'Then, maybe you are truly worthy of continuing this quest.'",(None),(300,150,100),300,"solar ray","solar cell","You sit down and listen to what Dr. Kleimann has to say...\n'You have awoken an ancient force that hasn't stirred in many years'.\n'You didn't think we would find out what you did but we know all.'\n'It had been prophecized that an adventurer would dictate the future of the faculty...'\n'Only The Quantum Order can assist you now, seek out Dr. Minnick. I wish you luck...'","You have betrayed The Order!"),
    Enemy("Dr. Buijs","'I've been looking for you.'\n'I have a lot to tell you, but first we must test your loyalty.'\n'There is a traitor amongst the Eng Phys faculty!'\n'His name is Chris and he was last seen in the Tandem Accelerator.'\n'Bring me what he has stolen!'",(None),(250,150,100),300,"voltage divider","capstone tools","'Ah you have returned.'\nYou sit down and listen to what Dr. Buijs has to say.\n'The Engineering Physics professors are part of an ancient council known as\nThe Quantum Order'\n'It is our duty to ensure the safety of this campus.'\n'It appears that your actions last night have stirred an evil\neven we don't understand.'\n'All that we do know is that some faculty members have been\ntempted by a Dark Lord with the promise of infinite knowledge.'\n'A prophecy from a time long past has foretold that an adventurer's decisions\nwould dictate the future of the faculty.'\n'Perhaps it is you they spoke of. Keep that in mind as you consider your actions.'\n'See Dan Fitzgreen in the basement.'\n'He has hatched a plan that may turn the balances in our favour.'","It is a voltage divider!"),
    Enemy("Dr. Cassidy","'Yes, I was the one who sent you on this quest.'\n'My associates were no match for you, they did not have the strength to acquire the Relics for me.'\n'I know the Quantum Order has told you that the prophecy spoke of you bringing peace.'\n'You have been lead to believe the Order fights for what is just and fair.'\n'But you have been mislead.'\n'They only wish to keep the power of the Quantum Relics to themselves so that they\nalone decide the fate of the University.'\n'I only ever wanted to reveal the true power of Engineering Physics to the students.'\n'They thought my methods were unsafe.'\n'They thought the power I intended to reveal would pollute the minds of the students\nand cloud their judgement.'\n'The Quantum Order only wishes to suppress the true power we hold!'\n'They don't trust the students, they think they are incapable of managing the power I intended to give them.'\n'We are the premier stream and we deserve to rule McMaster as such!'\n'Join me, together we can harness the powers given to you by the oracles.'\n'With the relics we may enter the Shadow Realm and retrieve the deed to the university\nfrom the spirit of Sir William McMaster.'\n'We can then overthrow the Quantum Order and shape the university to our liking and\nfinally Engineering Physics will reign supreme!'\n\nJust as Dr. Cassidy finishes speaking the ground begins to shake and you are blinded\nby a glow emanating from the statue of Sir William McMaster.\nYou recover from shielding your eyes and see the spirit of William McMaster\nemerging from a rift in fabric of spacetime!\n'Just wait, hero.'\n'I took your Iron Ring from you after you desecrated my statue last night for a reason'\n'I have known of Dr. Cassidy's intentions for some time and as you are the one\nthe prophecy has spoken of I knew he would jump at this opportunity to take my deed.'\n'I had to find a way to force him into playing his hand.'\n'Now the opportunity to rid Engineering Physics of this tyrannical Dark Lord has come!'\nDr. Cassidy quickly interjects.\n'You see, he only wants to restrict the power of our faculty!'\n'Destroy him and we shall finally rule the university!'",(None),(175,125,200),125,"","","","Dr. Cassidy falls to the ground.\nThe spirit of Sir William McMaster approaches and puts his hand on your shoulder.\n'You have chosen wisely.'\n'Dr. Cassidy had been driven mad in his quest for ultimate power.'\n'You have ensured the safety of McMaster and remained true to your values.'\n'McMaster University is an institution meant to allow all facets of learning coexist in harmony.'\n'No faculty should rule over the rest.'\n'For your actions, I believe you are a worthy engineer.'\n'Here is your Iron Ring, continue to wear it with pride.'"),
    Enemy("Dr. LaPierre","'Fetch me a Coffee will you.'",(None),(100,100,200),300,"Eng Phys pen","coffee","Here. I nice pen for your troubles.\nGo find Dr. Knights, he has more for you to do.","I can't believe you've done this."),
    Enemy("Dr. Nagasaki","'My grand invention is almost complete...'",(0,5,2),(100,100,100),75,"flux capacitor","ambifacient lunar waneshaft","'Yes!'\n'I have been looking for one exactly like that!'\n'Quicky, go to the basement of the Tandem Accelerator!'\n'The High Council is counting on you.'","NOOOO! NOW I WILL NEVER PLEASE THE DARK LORD!"),
    Enemy("Dan Fitzgreen","",(None),(100,75,100),400,"ambifacient lunar waneshaft","","'Been a lot stirring around the faculty since last night.'\n'I used to be an adventurous student like you before the High Council and I decided to part ways.'\n'I know what you seek and I am here to help.'\n'You need to fire up that old reactor in the basement of the Tandem Accelerator.'\n'It needs some sort of high power instrument to bring it to life...'\n'I think Dr. Nagasaki has been working on something like that, he is probably somewhere in ITB.'\n'He will likely need this...'","I'm moving to the physics department"),
    Enemy("Kenrick","'The oscilloscope is the window into the electronic world.'",(3,4,1),(100,100,200),75,"Kenrick's oscilloscope",None,"","Oh no! My window! The Dark Lord will know I've failed him!"),
    Enemy("Dr. Soleymani","'Are you interested in a research position?'",(0,1,2),(100,100,100),75,"einsteins brain",None,"","NOOO! The Dark Lord will never forgive me!"),
    Enemy("Sir William McMaster","'You must rid the university of the evil Dr. Cassidy has planned!'",(None),(175,125,100),125,"iron ring","","","The spirit of Sir William McMaster bursts with a fiercely bright explosion.\nYou look down to see your Iron Ring as well as the deed to McMaster!\nDr. Cassidy quickly picks up the deed and turns to you.\n'Excellent!' he says coupled with maniacal laughter.\n'Too fulfill your true destiny, take the power you hold in your Iron Ring and destroy all of the professors'\n'Only after they are gone can Engineering Physics truly reign supreme!'"),
    Enemy("Chris","'The tools should be coming any day now.'",(4,5,1),(50,75,50),50,"capstone tools",None,"","I was going to quit anyway!"),
    #Special
    Enemy("Brendan Fallon","What's up dude? I'm here to bless up your shit.\nDo you have my lunch box?",None,(9999,9999,9999),999,"green bang bong","Brendan Fallon's lunchbox","THANKS! TOKE UP MY DUDES!",""),
    Enemy("Hooded Man","I've been looking for you. Especially after what you did last night.\nI recommend you seek out the profs if you are to find your ring...\nOnly they can right the wrongs you have done.",(5,4,1),(999,999,999),999,"",None,"",""),
    #General
    Enemy("Liam the Gamer","I am NOT going to finish this assignment... if only I had one to copy.",(3,3,0),(10,10,10),15,"Swordfish","horrible assignment","Nice! Take this swordfish. I needed 45 cooking for that.",""),
    Enemy("Connor the Biologist","I would really like a cricket to continue my research...",(1,7,3),(10,10,10),15,None,"cricket","Absolutely righteous!",""),
    Enemy("Father Frobenius","'You need prayer. Recharge at the altar.'",(2,0,1),(10,10,10),25,"crucifix",None,"","I am slain!"),
    Enemy("Steven the first-year","'Have you got the LON-CAPA Python code?'",(3,6,1),(5,1,10),15,"engineering mug",None,"","I'm a failure at home and at school!"),
    Enemy("Phil the drunk","'MHhmgh, Soouh whatu we getta druuuunk'",(5,5,1),(10,5,1),15,"vomit","Phil's braces","'UHhhh i thinka im gonna- im gon-'\nPhil vomits.","mhmh spooky ghost urggh ectoplasm noooooo"),
    Enemy("Jana the vegan","'Did I mention I'm vegan?'",(5,4,0),(15,1,5),10,"3w textbook",None,"","I was going to bring it back I swear!"),
    Enemy("Larry the bus driver","'Is that even your bus pass?'",(2,1,1),(10,10,5),40,"huge shirt",None,"","That was definitely not your bus pass!"),
    Enemy("Brian the hipster","'Man, you were a RIOT at the Phoenix last night!'",(2,2,1),(5,2,10),10,"guitar",None,"","That's not vegan."),
    Enemy("Mitch the TA","'Hey, I saw your picture on Instagram!'\n'They let you get away with doing that to the Willy McMaster statue?'",(0,3,1),(10,5,10),25,"phone",None,"","There's my phone."),
    Enemy("Erik the Sk8r","'Check out this tre flip, pretty tight eh?'",(0,0,0),(15,15,40),20,"Erik's frosted tips",None,"","Man, that's dumb!"),
    Enemy("Megan the Bartender","'Wait... I recognize you... you have a $420E69 tab!'",(5,4,1),(15,20,10),20,"meow mix",None,"","Nuuuuuuuuuuuu"),
    Enemy("Bill the MAC Cop","'Give me your student card!'",(3,5,1),(50,25,10),50,"solar cell",None,"","We aren't able to arrest you anyway!"),
    Enemy("Zack the Snack","'I need a snack that smiles back!'",(2,4,0),(17,12,15),25,"fanny pack","goldfish","","Whoa thats whack! Check out this fanny pack."),
    Enemy("Will the MAC Cop","'Give me your student card!'",(4,2,1),(50,25,10),50,"fake gun",None,"","We aren't able to arrest you anyway!"),
    Enemy("Andreas the Nerd","'I heard some jebroni took the 3W Textbook and hid in Bridges cafe.'\n'Full send, dude!'",(3,2,1),(10,15,5),50,"visor glasses",None,"","Dude, that was definitely a full send"),
    Enemy("Eric the Baller","'Huge talking to people play.'",(0,5,0),(20,15,20),50,"Cold Steel Katana",None,"","This is sub-optimal."),
    Enemy("Mario the Mixologist","'Yo check out my meme page, you ever heard coco jay?'",(1,4,1),(15,10,20),50,"stylish watch",None,"","si ya saben como consigo, por que me invitan?"),
    Enemy("Paul the Janitor","'Hey brother, I really could use some Febreze.'",(0,5,1),(20,20,20),20,"bleach squirt bottle","Febreze","Rock on brother! Thanks so much!","NOOO, Now I can't go see Black Sabbath!"),
    Enemy("Undead Grad Student","'Mussst eeaaat funnnndingg... Er, I mean braaaains.'",(2,0,0),(20,10,1),20,"horrible assignment",None,"","My 12 year post-grad was for nothiiiiiingggggg!")]

    #Stationary Objects to interact with
    #Interact(name,location,info,Sinfo,need,drop)
    INTERACT1 = [
    Interact("Garbage Can",(2,3,1),"It's a garbage can.","You throw the MSP430 in... Yes, you have chosen wisely.","msp430",None),
    Interact("Broken Reactor",(4,5,0),"It's an old broken reactor.","After some elbow grease and a bit of luck you manage to complete the reactor.\nThere is a low whirr as the device starts and begins to glow with a\npink hue.\nYou feel like ancient mechanisms beyond your comprehension are coming to life.\nWithin the pink glow you see an apparition of Dr. Novog!\n'What's up folks! This is the only channel safe for communication\n'Come meet me in the basement of the Nuclear Reactor ASAP and bring that Pink Donut!'\nAs the aparition fades a hooded figure emerges from behind a lab bench.\n'The Dark Lord demands that donut!'\nThe assassin lunges for you but is quickly met by your blow.\nAs they fall to the ground you notice an insignia on their robe that tickles your 'that's familiar' bone...\nYou pull back their hood to reveal the face of an Eng Phys PhD student!\nYou don't remember their name... But you know they are in the faculty...","flux capacitor",'pink donut'),
    Interact("Fridge",(1,6,0),"Seems like a regular fridge to me.","You inspect the inside of the fridge to reveal a small keyhole.\nUpon inserting and turning the key you hear a robotic voice bellow.\n'WORMHOLE ACTIVATED'\nThe compartment bursts open and out flies a book!",'relativistic key','Pedrotti cubed'),
    Interact("Optical Bench",(1,6,0),"Dr. Haugen's personal optical bench...","You place Dr. Haugen's femtosecond laser on the bench and aim it at the fridge.\nTurning the laser on (remembering your laser safety glasses, of course)\nfires the high-intensity beam at the fridge.\nThe room begins to shake and smoke begins to billow out of the cracks of the fridge.\nThe door swings open and a glowing apparition of Albert Einstein emerges!\n'You have come a long way, but your quest is not yet over.'\n'For there still remains a great evil on this campus'\n'Dr. Haugen was entrusted with protecting the contents of my fridge.'\n'I have known of your destiny since your first year here at McMaster.'\n'You will be the one who determines the fate of the faculty.'\n'It is, therefore, my responsibility to prepare you for what lies ahead.'\n'This key opens a compartment in my fridge which holds one of three Quantum Relics.'\n'These items give the holder the power to shape the fate of the entire university.'\n'I cannot tell you much more. Perhaps I have said too much.'\n'Take this. Good Luck.'","femtosecond laser","relativistic key"),
    Interact("Old Painting",(3,0,1),"An old oil painting of the founding fathers of McMaster.\nDated:April 20th, 1887","Through Dr. Minnick's glasses a glowing green inscription is revealed!\n'In the hall where we eternally meet,\nThe second clue lies beneath your feet.'\nWhile reading the secret message Dr. Minnick's glasses get increasingly hotter and you quickly swat them off your face.","Minnick's glasses","Minnick's glasses"),
    Interact("Old Lamp",(5,1,1),"It appears the hole was caused by some sort of laser...","","",""),
    Interact("Car",(0,6,1),"An old volkswagen...\nPeering into the window you can't really see much.","You open the car and rummage around.\nUnderneath one of the seats you find a bowling ball!","car keys","bowling ball"),
    Interact("RCA TV",(5,6,1),"Old RCA TV with VHS slot...","You put the VHS into the slot and press play...\nThe opening scenes to Tarzan begin but suddenly the screen goes black and a message\nis displayed!\n'DrOWN I Need EveryThing graBs'","Tarzan VHS",""),
    Interact("Blue Book",(4,0,1),"It's a guide to the Bruce trail.","","",""),
    Interact("Box of old CDs",(2,4,0),"It's a dusty box of old CDs...","You insert one of the CDs into the monolithic computing device...\nThe laptop instantly blue-screens and bursts into flames.","lenovo laptop",None),
    Interact("Display Case",(1,6,1),"It's a display case full of all sorts of old-time Engineering Physics wizardry.","The rusty key fits perfectly!\nAs you turn the key glowing square forms on the back\nof the display case and opens revealing an old relic...","rusty key","faradays cage"),
    Interact("SharpXChange",(0,1,1),"Would you like to exchange a needle?","Needle Accepted!","dirty needle","clean needle"),
    Interact("Sun Dial",(3,2,1),"You can't even tell time on an analog clock.\nHow are you supposed to use this?","Through Dr. Minnick's glasses, you see a green glowing handprint appears\non the face of the sundial!\nYou place your hand on it and a compartment opens.","Minnick's glasses","rusty key"),
    Interact("Rules Sign",(2,3,1),"Welcome to The Great ENG PHYS Text Adventure!\n\nHere are the rules of the realm:\nYour orientation never changes. When you enter you will be facing the\nentrance of JHE and you will always face that way.\n\nThe commands which allow you to interact with your environment are:\nforward = f, backward = b, left = l, right = r, up = u, down = d\ntalk (person name) -talk to someone near you\nattack (person name) -attacks someone\ninspect (item name) -let's you interact with interactables and gives stats of items, can't inspect people\nequip (item name) -you pick up an item, drops any item you have in that slot\ndrop (item name) -drops an item in your inventory\neat (item name) -eat an item\nstats -will show your stats\nsearch - will search the area for things to interact with.\ninventory -will show your current inventory.\n\nBe sure to type the ENTIRE name of what you want to interact with.\nThat's it! Good Luck!","","",""),
    Interact("Red Book",(4,0,1),"Flipping through you read:\n'The mitochondria is the powerhouse of the cell.'","","",""),
    Interact("Old Journal",(6,1,0),"You blow the dust off, open it, and read:\n'The ability to peer into history would be a most formidable power.'\n'I have potentially produced a piece of the puzzle but without a\n'device capable of maintaining the field density long enough I fear\n'it will never become a reality.'\n'Thus I have decided to hide my invention until the time comes where\nsomeone can realize my dream.'\n'If you are reading this, find the place where you can see\ncampus in its entirety.'\n'If you ARE the hero, the next steps shall be revealed.'\n-M. Faraday","","",""),
    Interact("McMaster Map",(1,2,1),"It's the map of McMaster.'\n ________________________________________________\n|Map of McMaster                                 |\n|                                       BATES    |\n|                                                |\n| ETB        JHE         BSB                     |\n|                                                |\n|                                      STATUE    |\n|                                                |\n| HOSPITAL                                       |\n|          MDCL         CHAPEL              MUSC |\n|________________________________________________|","Through Minnick's glasses the true map is revealled!\nYou read:\n'Harness the sun.'\n ________________________________________________\n|Map of McMaster                                 |\n|                                       BATES    |\n|                                                |\n| ETB        JHE         BSB                     |\n|                                                |\n|                        \/            STATUE    |\n|                        /\                      |\n| HOSPITAL                                       |\n|          MDCL         CHAPEL              MUSC |\n|________________________________________________|\nDr. Minnick's glasses glow hot as you quickly swat them off of your face.","Minnick's glasses","Minnick's glasses"),
    Interact("Workbench",(1,7,0),"Looks like an old dusty workbench.","",None,""),
    Interact("Mouse",(1,0,3),"It's a mouse scurrying around...\nDid it just stare at you?","The mouse rushes over and takes the cheese.\nIt runns into a small opening it has made in the roof of the building.\nIt returns with something in it's mouth!","cheese","gilded blunderbuss"),
    Interact("Tri-Coloured Glasses",(6,1,2),"Looks like a set of glasses with multiple coloured lenses...","Its a cipher...\nOn the back of the declaration you can see different coded messages using the coloured lenses...\nRED:'Lithium Potassium Boron Mangnesium(-g)'\nBLUE:'Jerry likes cheese.'\nGREEN:'Mendelevium Chlorine'","declaration of independence",None),
    Interact("Uneven Earth",(3,7,1),"This patch of dirt looks out of place...","You begin digging and find an old box!\nYou open it up and read a note...\n'In the eldest of halls. The attic holds all.'","shovel","declaration of independence"),
    Interact("Coat of Arms",(3,4,1),"Under closer inspection you notice the book is a different kind of stone\nthan the rest...\nIf only you could get up there for a closer look...","With some effort you climb the rickety ladder and remove the book from the wall.\nReaching into the hole you pull out an old scroll!","old ladder","old scroll"),
    Interact("Ancient Mirror",(4,0,0),"It's an old mirror from a time long past.","You mutter the incantation... Suddenly, you see the reflection of Richard Feynman himself standing behind you!\n'You have come a long way. The way of the physicist is strong with you.'\n'Here, take this it is one of the 3 Quantum Relics.\n'You will need all 3 to acquire your Iron Ring.'\n'Trust your instincts and when the time comes you will know what to do.","ancient incantation","gamma glove")]

Reset()

def WorldMap():
    global MAPS1
    global LOCATIONS1
    global ENEMIES1
    global ITEMS1
    for i in LOCATIONS1:
        position = i.coords
        x = position[0]
        y = position[1]
        z = position[2]
        MAPS1[x][y][z] = i
    for i in ENEMIES1:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            MAPS1[x][y][z].placeEnemy(i)
        else:
            i.location = (None,None,None)
        if i.need:
            i.need = i.need.lower() #this fixed a key error where it would crash because it looked for the uppercase version of an item
        if i.drop:
            i.drop = i.drop.lower() #this fixed a key error where it would crash because it looked for the uppercase version of an item
    for i in ITEMS1:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            MAPS1[x][y][z].placeItem(i)
        else:
            i.location = (None,None,None)
    for i in INTERACT1:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            MAPS1[x][y][z].placeItem(i)
        else:
            i.location = (None,None,None)
        if i.need:
            i.need = i.need.lower() #this fixed a key error where it would crash because it looked for the uppercase version of an item
        if i.drop:
            i.drop = i.drop.lower() #this fixed a key error where it would crash because it looked for the uppercase version of an item
    return tuple(MAPS1)

def ItemDictionary():
    global ITEMS1
    ItemDictionary = {}
    for item in ITEMS1:
        name = item.name.lower()
        ItemDictionary.update({name:item})
    return ItemDictionary

def EnemyDictionary():
    global ENEMIES1
    EnemyDictionary = {}
    for enemy in ENEMIES1:
        name = enemy.name.lower()
        EnemyDictionary.update({name:enemy})
    return EnemyDictionary

def InteractDictionary():
    global INTERACT1
    InteractDictionary = {}
    for interact in INTERACT1:
        name = interact.name.lower()
        InteractDictionary.update({name:interact})
    return InteractDictionary
