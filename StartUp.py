#The Great Engineering Text Adventure
#Authors: Mitchell Lemieux, Tyler Kashak
#Music: Brian, Erik What music do we have lol?
#Start Date: April 14th, 2018
#Library of Items and Locations
#Latest Edit 22/2/2019
"""
Rules for Writing Objects in the Eng Phys Text Adventure
0. ALWAYS check the paramaters of the object. If unsure check GameClasses.py for the constructor
1. Use " (\S)" instead of "\n" for newline characters
2. If using ANY quotes (" or ') ONLY use ' inside strings.
The " quote is used to define the string boundry and any in the sentence will break the string.
ex) "You think to yourself 'Gee, do I like quotes'! 'Lets go somewhere!' "
not) "You think to yourself "Gee, do I like quotes"! "Lets go somewhere"! "
3. When an attribute is "None" it needs to be capitalized as such: "None"
4. When Naming a MAP

Obsolete: 5. When puting a needed or dropped object.name in an interact it MUST be lowercase.
All object keys in the game are stored lowercase and used to throw a key error but are now changed in the constructor
"""


from GameClasses import *
import csv
from Colour import *

# these define bounds of the list constructor MAPS1, they control this main loop
# TODO Get rid of these ranges and make them dimension specific with dimension dictionary
XRANGE = 10  # when changing these also change the values in the CreativeMode.load() function
YRANGE = 10
ZRANGE = 4
DRANGE = 6  # Dimensional range of the map, i.e. number of different buildings/dimensions with interiors + overworld
# TODO IF game starts to slow down due to size of MAPS1 empty spaces in this definition:
#  we'll have to define some funky magic to define different map dictionaries
#  OR Redefine how the constructor works so don't have to loop through huge empty space to define an new map location

def Reset():
    global MAPS1
    global LOCATIONS1
    global ENEMIES1
    global ITEMS1
    global INTERACT1

    # Using List comprehensions to define the null map space of the game for objects to be put into
    # Ineffecient due to number of empty spaces and each dimension being 10x10x5 but whatever for now
    MAPS1 = [ [ [ [None for dim in range(DRANGE)] for z in range(ZRANGE)] for y in range(YRANGE)] for x in range(XRANGE) ]
    #MAPS1 = [ [ [None for y in range(ZRANGE)] for y in range(YRANGE)] for x in range(XRANGE)]

    #def __init__(self,name,location,info,lore,walls,inside)
    #Locations: Place.name = "Name" - Place.location = (X,Y,Z) - Place.info = "location information" - Place.lore = "lore"
    #Example: Start = Map("Start",(0,0,0),"RONT OF JHE:\nBSB is to your right.","You start here",(),False)
    LOCATIONS1=[
    # --- OVERWORLD: Dimension 0 ---
    Map("Front of JHE",(2,3,1,0),"~~:","You see the "+interactcolour+"Iron Ring "+textcolour+"out "+mapcolour+"front of JHE"+textcolour+" shining in the "+interactcolour+"morning sun"+textcolour+".\nThe campus is bustling with student life.\nThere are people heading in all directions with "+itemcolour+"Kipling pranks"+textcolour+" still scattered about JHE.(\S) (\S)Due to  your hangover your actions are limited. (\S)You feel compelled to stay on this specific section of campus to " +indicatecolour+ "search" +textcolour+ " for your " +itemcolour+ "ring" +textcolour+ ". (\S)You must type in commands to control your body but only certain commands will work.(\S)In your state, you should probably type '" +indicatecolour+ "help" +textcolour+ "'.",(),False),
    Map("JHE Lobby",(2,4,1,0),"~~:","JHE lobby is alive.\nStudents rushing all around as the smell of burnt "+itemcolour+"coffee "+textcolour+"and sorrow tickles your nose.\nYou scan the faces around you but see no one familiar.\nThere is a confused air about this place as Kipling was just last night. (\S) Many engineers are happy. Many more still grinding.",(),True),
    Map("Nuclear Research Building",(2,5,1,0),"~NUCLEAR RESEARCH BUILDING~:\nTo your left lies the JHE-Annex. The Reactor is in front of you.\nThe Police Station is to your right. JHE lobby is behind you.\nThere are stairs going down.","You have barely ever been in here other than to struggle through\n3 hours of waiting for a water level PID controller to reach steady state.\nYou wonder how anyone could get away with a floor plan this confusing.\nPerhaps that's why no terrorists have blown up the reactor because\nthey are all still lost in here...",(),True),
    Map("Hatch Building",(1,4,1,0),"~~","That 'fresh building' smell still lingers.\nYou see members of the various clubs rushing from room to room including a man carrying a rocket.\nThe "+interactcolour+"Kipling clock"+textcolour+" ticks away... only 364 more...\nWho is this Gerald Hatch anyway?",(),True),
    Map("Front of Hatch",(1,3,1,0),"~~:\nETB to your left. Enter Hatch by going forward.\nThe McMaster Map to your rear. JHE Entrance is to your right.","You stare at the newly completed building.\nThe sun still shines and you are irritated by the constant drone of the Hamiltonian sirens\nwhich you have yet to grow accustomed to...",(),False),
    Map("McMaster Map",(1,2,1,0),"~~:\n","Has anyone ever used this thing?\nA lost freshman asks you for directions even though the map is clearly next to you.\nAfter sending them in the wrong direction you plan your next move.",(),False),
    Map("Health Sciences Library",(1,1,1,0),"~~:\n","You are constantly asked to be quiet even though you have yet to make a sound.\nAfter scanning the tables and see no one you recognize you take a seat\nin an "+interactcolour+"armchair"+textcolour+" and stare out towards the centre of campus.\nYou daydream of a life where these study rooms weren't constantly full.",(),True),
    Map("Bus Stop",(2,1,1,0),"~~:\n","Students gather around to catch the next bus.\nYou get pushed and shoved as they desperately clammer on-board.\nYou overhear an argument between a student and the "+personcolour+"Bus Driver"+textcolour+" when suddenly the altercation\nturns to blows and pours onto the sidewalk.",(),False),
    Map("McMaster Chapel",(2,0,1,0),"~~:\n.","The low drone of the "+interactcolour+"organ"+textcolour+" draws you in.\nThe pews are relatively empty and the lighting quite dim.\nYou think it would be in your best interest\nto pray especially with exam season just around the corner...\nIt can't hurt, right? It'd probably work better than those healing stones\non your desk.",("r",'l','b'),True),
    Map("Front of Art Museum",(3,1,1,0),"~~:","Standing out front of the art museum you feel you are already being critiqued.\nAfter narrowly escaping a conversation with an art student\nabout their installation piece of a "+interactcolour+"dirty coffee table"+textcolour+"...\nYou plan your next move.",(),False),
    Map("Art Museum",(3,0,1,0),"~~:\nThe exit lies in front of you.","Who knew McMaster had such a beautiful gallery.\nYou tilt your head endlessly until the art sort of makes sense.\nAfter telling yourself you could totally make every piece in the place had you been given\na chance you put your pinky out.\nThen contemplate your next move.",('r','l','b'),True),
    Map("Willy Dog stand",(4,1,1,0),"~~:","Oh, that sweet sweet aroma of the classic "+itemcolour+"Willy Dog"+textcolour+".\nMany drunken nights flash through your head.\nThat "+interactcolour+"Willy dog cart"+textcolour+" is more of a staple to McMaster students than the Archway next to it.\nWas it named Willy Dog after Sir William McMaster?\nYou'll never know...",(),False),
    Map("Mills Library",(4,0,1,0),"~Y~:\nThe Willy Dog Stand is in front of you. MUSC is to your right.\nYou can go downstairs.","This is definitely not Thode.\nYou wonder if anything gets done in this library.\nAll of the debauchery taking place on the 6th floor sends a shudder through your body.\nYou notice a "+interactcolour+"stack of books"+textcolour+"...",('l','b'),True),
    Map("William McMaster Statue",(5,2,1,0),"~~:\nHamilton Hall is in front of you. The Archway is behind you.\nTurning Circle is to your left.","Approaching the statue you notice massive burn marks on the lawn and chunks\nout of the ...\nHmm...\nWhat if Sir Willy McMaster was actually in that statue Han Solo style?\nAfter a quick selfie with Willy you plan your next move.",('r'),False),
    Map("BSB Field",(3,2,1,0),"~:\n","You look up to see the "+interactcolour+"flags"+textcolour+" flapping happily in the morning breeze.\nThat "+interactcolour+"sundial"+textcolour+" at their feet ticking to the tune of celestial magic.\nAfter swatting Neil Degrasse quotes from your thoughts...\nYou consider what to do next.",(),False),
    Map("JHE Field",(2,2,1,0),"~~:\n","The morning sun warms your face as you scoff at a hipster "+interactcolour+"slack-lining"+textcolour+".\nStudents lie in the grass around the field even though everybody knows\nnothing gets done studying outside.\nAfter narrowly dodging a "+itemcolour+"frisbee"+textcolour+" you plan what to do.",(),False),
    Map("MUSC",(5,0,1,0),"~~:\n","The "+mapcolour+"Student Centre"+textcolour+" is alive.\nAfter counting the number of jean jackets in the Starbucks line like the Count from Sesame Street\nyou snap back to reality.\n(Oops there goes gravity).\nYou notice a Starbucks employee arguing with his manager before throwing their "+itemcolour+"apron"+textcolour+" to the ground.",('r','b'),True),
    Map("McMaster Archway",(5,1,1,0),"~~:\n","Probably the most beautiful structure at Mac.\nYou notice a hole that appears to have melted through the glass of the "+interactcolour+"lamp"+textcolour+" underneath...\nYou snap a quick selfie in front of the Archway for the 'gram.",(),False),
    Map("University Hall",(6,1,1,0),"~~:\n","The glares from portraits of old McMaster founding fathers intimidate you.\nThe memories of failing midterms in their presence sends you into an almost trance-like state.\nYou notice that the portrait of Keyes totally looks like Stephen Fry.\nAfter talking yourself out of stealing a piece of Mac history you plan your next move.",['r','b','f','d'],True),
    Map("Phoenix Bar & Grill",(5,4,1,0),"~~:\n","Upon entering, a rush of memories from last night enter your mind.\nPeople's faces are a blur but you somewhat recall '16 "+itemcolour+"tequila"+textcolour+" shots' as something you said.\nYou see a mysterious "+personcolour+"Hooded Man"+textcolour+" as he beckons you to come over.",('r'),True),
    Map("BSB",(3,4,1,0),"~BSB~:\n ","You were told JHE would be your home but after picking Eng Phys\nyou didn't realize how wrong you were.\nAt least the cafe is better than JHE's.\nA shudder runs through your body as you draw nearer to the electronics labs.\nWiping a "+itemcolour+"cold sweat"+textcolour+" from your brow you plan ahead.",(),True, (3,3,0)),
        # ---  Aesthetic Highlighting ---
    Map("Front of BSB",(3,3,1,0),"~:","You look up and see the McMaster "+interactcolour+"coat of arms"+textcolour+" engraved into the "+mapcolour+"Front of BSB"+textcolour+".\nThis little pathway has been well worn and you wonder why they don't connect JHE and BSB anyway.\nAn "+mapcolour+"underground (quantum) tunnel"+textcolour+" would save some hardship on a rainy day...",(),False),
    Map("Police Station",(3,5,1,0),"~~:\nThe path between JHE & BSB behind you. The GO station lies ahead of you.\nThe Nuclear Research Building is to your left. The Tandem Accelerator is to your right.","Thoughts of getting kicked out of res parties fill your head.\nThose special constables are punks.\nYou mutter the lyrics of a certain N.W.A hit. After avoiding a campus PD cruiser\nscreaming around the blind corner, you think of what to do next.",(),True),
    Map("Mary Keyes",(4,6,1,0),"~~:\nYou can head to the Bridge if you go forward. The GO station is to your left.\nThe Tandem Accelerator is at your rear. Bates is to your right.","A snack station that's open 'til midnight.\nWhat a life saver indeed.\nYou quickly thank the engineering gods for Mary Keyes and fight yourself\nfrom ordering chicken fingers & fries super combo...",(),True),
    Map("Nuclear Reactor Building",(2,6,1,0),"~~:","As you approach you wonder if that steam is really radioactive?\nIt can't be.\nThe ominous structure draws you closer as you consider what it would be\nlike to swim in that sweet blue "+interactcolour+"pool"+textcolour+"...You lose yourself staring into the faint blue glow of the "+interactcolour+"pool"+textcolour+" as you slowly approach its edge.",(),True),
    Map("ABB",(1,6,1,0),"~~:\nThode is in front of you. JHE Annex is behind you.\nThe Nuclear Reactor is to your right. LOT I is to your left.\nYou can go up or down the stairs.","You stare at the electron microscope structure and wonder if it could even see your GPA...\nA tear rolls down your cheek. You collect yourself and plan what to do next.",(),True),
    Map("Thode",(1,7,1,0),"~~:\nABB is at your rear. The campus exit is to your right.\nCootes Drive is to your left. You can go up or down the stairs.","Oh the Reactor Cafe.\nYou think of the good old days when you could actually see the reactor from the Cafe...\nAfter overhearing someone ask whether keV is bigger than MeV you first contemplate your existence,\nthen contemplate your next move...",('f'),True),
    Map("JHE Annex",(1,5,1,0),"~~:\nHatch is to your rear. ABB in front of you.\nITB is to your left. NRB to your right.\nThe Eng Phys office is up the stairs.","They made a big engineering building, got money, then added more.\nYou wonder why Eng Phys classes get pushed into the rooms in this side of JHE...\nHmm...",(),True),
    Map("Campus Exit",(2,7,1,0),"~EXIT~:\nHead to Thode by going left. Head down Cootes trail if you go right.\nThe Reactor is behind you.","A faint glow can be seen in the distance.\nWarning signs litter the trail as you squint to get a better look.\nA chill is sent down your spine as you see the flickering stretched shadows of\nfighting dance on the road ahead.\nYou cannot go straight... yet.",('f'),False),
    Map("ETB",(0,3,1,0),"~~:\nTo your right is the Hatch Building. An alleyway is in front of you.\nT-13 is behind you. You can also go upstairs.","The memories of actually doing something in first year flood your mind:\nGear trains; Python; 3D printing.\nEngineering had such a different meaning in your first year...\nYou plan your next move.",('l'),True),
    Map("Lot M",(5,7,1,0),"~~:\nTo your left is the bridge. Bates is behind you.","After 3 days of hiking you arrive at Lot M.\nAfter 2 more days of looking for your car you give up and contemplate what to do next.",('f','r'),False),
    Map("Bates",(5,6,1,0),"~~:\nLOT M lies in front of you. Keyes is to your left.\nThe trail to the Phoenix is behind you.","Memories of ridiculous res parties fill your mind.\nYou also recall the landfill of a room that was more of a circus attraction\nthan a living space.\nOh how distant first year seems...",('r'),True),
    Map("Residence Square",(5,5,1,0),"~~:\nBates lies in front of you. The Phoenix at your rear.\nThe Tandem Accelerator is to your left.","Longboarding down this trail going Mach 16 was a blast and a half.\nDodging deer and first years like it's some sort of cube runner.\nNice.",('r'),False),
    Map("Hamilton Hall",(5,3,1,0),"~~:\nThe Phoenix is in front of you. A road is to your left.\nThe Willy McMaster Statue is to your rear.","You think about helping some first years in the Math help centre.\nThen you don't.\nThey should learn to fight through it if they're going to make it through the\nnext 4 years.",('r'),True),
    Map("Turning Circle",(4,2,1,0),"~~:\nWilly Dog stand is to your rear. BSB-field is to your left.\nThe Willy McMaster Statue is to your right. Head down the road if you go forward.","The circle thing with the three trees in it is looking pretty nice\nin the morning sun.\nStudents rush all around.\nThe aroma from the Willy Dog stand is making you pretty hungry...",(),False),
    Map("Scholar's Road",(4,3,1,0),"~ ~:\n","A lost first year's parent drives by in a mini-van clearly ignoring the "+interactcolour+"no access sign"+textcolour+". You thank your astrology sign for making sure they looked up and saw you.",(),False),
    Map("GSB",(4,4,1,0),"~~:","Have you ever been in here?\nI haven't.\nYou see a group of people huddled around a pentagram-wearing goat heads.\nMaybe? I seriously don't know what goes on in here.",(),True),
    Map("Tandem Accelerator",(4,5,1,0),"~~:\nThe General Sciences Building is behind you. The Police station is to your left.\nA trail is to your right. Keyes is in front of you.","Turns out the Tandem Accelerator is NOT a rad place to ride a 2-person bike...\nBummed out you remind yourself you graduated and consider what to do next.",(),True),
    Map("Cootes Drive",(4,7,1,0),"~~:\nLot M is to your right. Keyes is at your rear.\nHead down Cootes trail if you go left.","You narrowly avoid a GO bus\npick yourself up and brush yourself off.\nThen plan your next move.",('f'),False),
    Map("Cootes Trail",(3,7,1,0),"~~:\nCampus exit is to your left. GO station to your rear.\nThe Bridge to Lot M is to your right.","The flickering light through the trees `ces off of the trail ahead of you.\nYou smile as you see a squirrel gathering nuts,\nprobably for his little squirrel family.\nWith this new positive outlook on life you plan your next move.",('f'),False),
    Map("GO Station",(3,6,1,0),"~~:\nThe Reactor is to your left. Keyes is to your right.\nCootes Trail is in front of you. The Police Station is behind you.","The rush of people and buses around you is disorienting.\nYou nearly get hit by 3 buses and 2 MAC Cop cars as\nyou play a strange game of real-life frogger.\nReaching a bench you sit down, catch your breath, and plan what to do next.",(),False),
    Map("Cootes at Main Street",(0,7,1,0),"~~:\nThode is to your right. Lot I is behind you.","You notice a series of pickup trucks for what must be a landscaping or construction company.\nThere is construction gear spread all over the place.\nThe sound of sirens grows louder as an ambulance suddenly rushes by.\nYou collect yourself and consider what to do next.",('f','l'),False),
    Map("Lot I",(0,6,1,0),"~~:\nABB is to your right. Cootes Drive is in front of you.\nITB is to your rear.","Nope, your car isn't here.\nMaybe you parked in Lot M? Maybe not.\nAfter scoffing at all of the prof Mercedes that are way too nice...\nYou think of what to do.",('l'),False),
    Map("ITB",(0,5,1,0),"~~:\nJHE-Annex is to your right. Lot I is in front of you.\nAn alley is behind you. You can go up OR down the stairs.","McMaster, back at it again with the horrible floor plan.\nAfter getting lost for 5 hours you finally reach the lobby\nand decide what to do.",('l'),True),
    Map("Alley",(0,4,1,0),"~~:\nITB is in front of you. ETB is behind you.\nYou can enter Hatch to your right.","As you head down the narrow path between ITB and ETB you hear car horns blaring down Main Street.\nYou gather up some trash and put it in a garbage can like a good McMasterian.\nThen plan your next move.",('l'),False),
    Map("T-13",(0,2,1,0),"~~:\nETB is in front of you. The McMaster Map is to your right.\nThe West Wing of the Hospital is behind you.","How many bad invigilators does it take to screw in a light bulb?\nI'm not sure but they took my damn Casio FX-911+C...",['l','d'],True),
    Map("Hospital West Wing",(0,1,1,0),"~~:","Doctors and Nurses rush around you. You remember why you didn't want to become a doctor as you nearly faint looking at a patient's paper cut in the waiting room. After a drink from the "+interactcolour+"water fountain"+textcolour+" you plan what to do.",('l'),True),
    Map("Hospital East Wing",(0,0,1,0),"~~:\nIn front of you is the West Wing. MDCL is to your right.\nThe Parking Garage is below you.","You smile as you overhear a conversation between a doctor and a family.\nTurns out their child is going to make a full recovery.\nThanks science.",('l','b'),True),
    Map("MDCL",(1,0,1,0),"~~:\n","After a solid 5 minutes of meditation in the reflection area. You make your next decision feeling refreshed.",['b','r','u'],True),
    #Basement Level (X,Y,0)
    Map("Secret Room",(6,1,0,0),"~SECRET ROOM~:\nYou can only climb up and out.","You inspect the floorboards and find one is loose.\nUpon lifting it you reveal a secret room!\nYou climb down and find yourself surrounded by stacks of ancient books and\nforgotten items from McMaster's past.",('f','b','l','r','d'),True),
    Map("Quantum Tunnel",(3,4,0,0),"~QUANTUM TUNNEL~:\nGo up to return to the main floor of BSB","What other faculty spends thousands of dollars on furniture for a\nliteral custodial closet in the BSB basement?\nYou guessed it...\nEng Phys. Gotta love em'",('f','b','l','r','d'),True),
    Map("Nuclear Reactor",(2,6,0,0),"~~:\nGo up to head outside.","The hum of air conditioning drowns your thoughts.",('f','b','l','r','d'),True),
    Map("Thode Basement",(1,7,0,0),"~~:\nGo up to head outside.","You feel the laser glares burning into the back of your neck as\nyou hastily walk amongst the rows of desks.\nIs it possible to book a study room down here without finding a phallic object drawn on the whiteboard?\nYou'll never know.",('f','b','l','r','d'),True),
    Map("Bridges Cafe",(5,4,0,0),"~~:\nYou can only go back up to the Phoenix.","You feel guilty walking in here after you performed a\nbeat down on a double big mac combo in a drunken stupor only hours earlier.\nAfter pledging to be more vegan in the future, you plan what to do next.",('f','b','l','r','d'),True),
    Map("Secret Trapdoor!",(0,2,0,0),"~!~:\nGo up to climb out.","You uncover a trapdoor after pulling up a loose floor tile.\nUpon descending you see stacks of failed midterms and assorted books all around you.\nA suit of armor and a chainmail flag with a skull on it are barely visible.\nWho made this place anyway?",('f','b','l','r','d'),True),
    Map("Custodial Closet",(5,0,0,0),"~~:\nYou can only go up to go back to MUSC.","You enter the custodial closet and a formidable stench fills your nostrils...\nEw.",('f','b','l','r','d'),True),
    Map("NRB Basement",(2,5,0,0),"~NRB~:\nYou can only go back up to the main floor.","You head down the stairs to the basement...\nThe forgotten dreams of PhD students linger in the air.\nThere is an endless amount of engineering wizardry in the rooms around you.",('f','b','l','r','d'),True),
    Map("Chapel Undercroft",(2,0,0,0),"~~:\nYou can only go back up to the main floor.","You struggle down the dimly lit stairway into the undercroft.\nThe distinct smell of mould enters your nose as you travel further into the musty basement.\nThe faint glow of candles cause the shadows of ancient statues to flicker on the walls of the room...\nYou plan your next move.",('f','b','l','r','d'),True),
    Map("ETB Basement",(0,3,0,0),"~~:\nYou can only go back up to the main floor.","After getting lost in a maze of corridors and locked rooms you stumble\nacross a door that is slightly ajar.\nYou open the door to reveal a rather small dark room.\nYou flick on the light switch.",('f','b','l','r','d'),True),
    Map("ITB Basement",(0,5,0,0),"~~:","As if the upstairs floor plan wasn't bad enough...\nAfter another 3 hours wandering around you are back where you started\nand don't feel like you learned anything...",('f','b','l','r','d'),True),
    Map("ABB Basement",(1,6,0,0),"~~:\nYou can only go back up to the main floor.","The Laser lab is pretty darn cool.\nWalking around here you notice a number of PhD students looking rather shifty.\nHmmm...\nYou wonder why that is.",('f','b','l','r','d'),True),
    Map("Parking Garage",(0,0,0,0),"~~:\nYou can only go back up to the Hospital.","The smooth floor down here makes an excellent skate surface.\nRad.\nIf only you learned how to kickflip.",('f','b','l','r','d'),True),
    Map("JHE Basement",(2,4,0,0),"~~:\nYou can only go back up to the main floor.","You see the remnants of failed clubs and the shattered dreams of past engineers...\nThis place is a bit chilly.",('f','b','l','r','d'),True),
    Map("Mills Basement",(4,0,0,0),"~~:\nYou can only go back up to Mills.","Jeez has anyone ever been down here?\nThe rows of bookshelves seem to go on forever...\nIf only you could possess all of the knowledge they hold.",('f','b','l','r','d'),True),
    Map("Tandem Accelerator Basement",(4,5,0,0),"~~:\nYou can only go back up the stairs.","An old basement with all sorts of technological wizardry you don't recognize.\nIt seems like this place has been untouched for some time.\nLooking around you get the impression that not a lot of people come down here.",('f','b','l','r','d'),True),
    Map("Hamilton Hall Basement", (5, 3, 0, 0),"~~:","You often stumbled down here and awkwardly to wait for your math class. You shudder at the memory and carry on.",('r'), True),

        #Map("Quantum Tunnel",(3,3,-1),"TANDEM BASEMENT:\nYou can only go back up the stairs.","An old basement with all sorts of technological wizardry you don't recognize.\nIt seems like this place has been untouched for some time.\nLooking around you get the impression that not a lot of people come down here.",('f','b','l','r','d'),True),
    #Map("WEST Hospital Basement",(1,0,0),"HOSPITAL EAST BASEMENT:\nIn front of you is the West Wing. MDCL is to your right.\nThe Parking Garage is below you.","You smile as you overhear a conversation between a doctor and a family.\nTurns out their child is going to make a full recovery.\nThanks science.",('l','b')),
    #2nd Level (X,Y,2)
    Map("2nd Floor ITB",(0,5,2,0),"~~:\nYou can only go back down the stairs.","Walking around up here you don't find much other than lab benches with strange instruments.\nThis place gives you the impression that there must be some high level engineering physics going on...",('f','b','l','r','u'),True),
    Map("2nd Floor ABB",(1,6,2,0),"~~:\nThe Eng Phys Office is behind you. You can down the stairs to ABB.","You were told JHE would be your home.\nNope.\nInstead you recall countless hours lectures on the 2nd floor\nas you drifted in and out of daydreams staring out the windows on a spring afternoon...",('f','l','r','u'),True),
    Map("2nd Floor JHE",(2,4,2,0),"~~:\nTo the left is 2nd Floor Hatch. You can go down the stairs to JHE Lobby.","You spend 20 minutes staring at the 1970 graduating class wondering if you could ever pull off a moustache like that...\nAfter realizing the cool lecture halls were only given to first years.\nYou shake your fist and plan your next move.",('f','b','r'),True),
    Map("2nd Floor ETB",(0,3,2,0),"~~:\nYou can only go back down the stairs.","You realize you really have never come up here.\nYou see 4th year Eng Phys students hurry out of a long-winded lecture.\nAfter picking a booger.\nYou plan your next move.",('f','b','l','r','u'),True),
    Map("Eng Phys Office",(1,5,2,0),"~~:\n2nd Floor Abb is infront of you. 2nd Floor Hatch is behind you. You can go down the stairs to JHE Annex.","The portrait of Dr. Novog makes you jealous as you realize you could\nnever pull off a hairstyle like that.\nYou scan the display case of past Eng Phys projects.\nThey display these as trophies...\nTrophies which only tell a story of endless grind you think to yourself...",('l','r','u'),True),
    Map("2nd Floor Hatch",(1,4,2,0),"~~:\nIn front of you lies the Eng Phys Office. To your right is 2nd Floor JHE.\nHatch is downstairs.","You see various meeting rooms with 1st years occupying them.\nThe MES office is full but nothing seems to be getting done.\nThere's therapy dogs scattered everywhere for Paws and Play.\nYou can't get a session with a real therapist but at least there is this",('b','l','u'),True),
    Map("Pheonix Loft",(5,4,2,0),"~~:\nYou can only go back down the stairs.","The history up here is incredible. So many relics from a time long past.\nFrom old costumes from plays to furniture.\nAfter a quick Shakespearean sonnet you think of what to do next.",('f','b','l','r','u'),True),
    Map("Upstairs Chapel",(2,0,2,0),"~~:\nYou can only go back down the stairs.","The combination of ringing bells and echoes from the organ is deafening.\nYou can barely collect your thoughts.\nThe cobwebs and dust give you the impression this place has been ill-travelled\nand long forgotten.",('f','b','l','r','u'),True),
    Map("2nd Floor W Wing",(0,1,2,0),"~~:\nYou can only go back down the stairs.","The endless number of rooms are mesmerizing.\nYou don't even know which way to go.\nAfter being lost for 2 hours you circle back to where you entered.",('f','b','l','r','u'),True),
    Map("2nd Floor UH",(6,1,2,0),"~~:\nYou can only go back down the stairs.","You make your way up the rickety staircase into a room from a time long past.\nYou notice a dust covered table with some old instruments and clutter thrown about.",('f','b','l','r','u'),True),
    Map("2nd Floor BSB",(3,4,2,0),"~~:\nYou can only go back down the stairs.","Despite the horrible numbering of floors the layout of the building is great.\nNot a complaint with this one.",('f','b','l','r'),True),
    Map("Climbing MDCL",(1,0,2,0),"~~:\nYou can continue climbing or go back down...","You struggle and find yourself on the outer wall of MDCL.",('f','b','l','r'),True),
    #3rd Level (X,Y,3)
    Map("MDCL Roof",(1,0,3,0),"~~:\nYou can only go back down.","With all of your might you pull yourself up and onto the roof.\nYou can see the majority of campus from up here!",('f','b','l','r','u'),False),
    Map("3rd Floor Thode",(1,7,3,0),"~~:\nYou can only go back down the stairs.","After hauling up another set of stairs you realize you probably shouldn't\nhave given up on your Pulse membership...\nThe sounds of sobbing can be heard from all around you.\nAfter you dispense all of your tissues to passing I-Sci's you plan your next move.",('f','b','l','r','u'),True),
    Map("2nd Floor Thode",(1,7,2,0),"~~:\nYou can go up or down the stairs.","As you enter Club Thode the smell of feet enters your nostrils.\nWho goes barefoot in a library? C'mon.\nThe memory of countless hours spent slamming together a report made of nonsense, caffeine,\nand hope makes you light headed...\nComing to your senses... You plan your next move.",('f','b','l','r'),True),
    Map("3rd Floor JHE Stairs", (2, 4, 3, 0), "~~:\nYou can only go back down the stairs.",
            "You reach the top of the stairwell but the doors into the 3rd floor are barred with solid sheet metal. "
            "You can't go any further It seems like more construction and but you wonder where they'll put the "
            "displaced 1st years in the meantime.", ('f', 'b', 'l', 'r', 'u'), True),
    Map("3rd Floor BSB", (3, 4, 3,0), "~3RD FLOOR BSB~:\nYou can only go back down the stairs.",
            "You swear you see a tumbleweed roll by. There's no one in sight but plenty of bathrooms. Is the Geography "
            "department up here?? After learning about the Oak Ridges Moraine bring yourself back to reality.",
            ('f', 'b', 'l', 'r', 'u'), True),

    # --- BSB: Dimension 1 ---
    # JHE lobby with a link out to BSB interrior
    # Map("JHE Lobby", (2, 4, 1, 0), "~~:","JHE lobby is alive.\nStudents rushing all around as the smell of burnt coffee and sorrow tickles your nose.\nYou scan the faces around you but see no one familiar.\nThere is a confused air about this place as Kipling was just last night. (\S) Many engineers happy. Many more still grinding.",(), True, 0, [("r", 0, 1, 1, 1)]),
    Map("BSB South Door", (0, 1, 1, 1), "~BSB First Floor South Door~:\n", "Yeah, you're in a doorway", (), True, 1,[("l", 2, 4, 1, 0)]),

    # --- CAPSTONE ROOM: Dimension 2 ---
    Map("Capstone Doorway", (1, 7, 3, 1), "Capstone Doorway~:\n",
            "You walk into the room that is a mess. This is a disaster,\nhow did this happen? Do these people live here?",
            ('u'), True, 1),
    Map("Circuit Smart", (6, 7, 3, 1), "Circuit Smart~:\n",
            "(Print text of spagetti)\nIf you unplugged one wire of this these people would go insane.", ('d', 'u'),
            True, 1),
    Map("Milli", (6, 6, 3, 1), "Milli~:\n", "Great Job Mili!", ('d', 'u'), True, 1),
    Map("NANOrims", (6, 5, 3, 1), "NANOrims~:\n", "NANNNOOORYMMSS.", ('d', 'u'), True, 1),
    Map("S.T.A.R.S.", (5, 5, 3, 1), "S.T.A.R.S.~:\n",
            "S.T.A.R.S. PLEASE WORK.\nYou see a man wearing a pink shirt and a giant robot point a cannon where ever he goes.\nIs this how the world ends?",
            ('d', 'u'), True, 1),  # S.T.A.R.S. System T69
    Map("FRAS", (5, 6, 3, 1), "FRAS~:\n", "Yeah that's a tank. This is a 3D printed Tank.", ('d', 'u'), True, 1),
    Map("T.A. Area", (4, 7, 3, 1), "T.A. Area~:\n","Is this where the PSRs get lost? Also just storage space for STARS", ('d', 'u'), True, 1),
    Map("ZebraShark", (4, 6, 3, 1), "ZebraShark~:\n", "Where are they? O.m.g. is that a pool downstairs?",('d', 'u'), True, 1),
    Map("THE ECLIPSE", (4, 5, 3, 1), "THE ECLIPSE~:\n","AW DANG The Eclipse! But yeah this windshield is a bit much", ('d', 'u'), True, 1),
    Map("Electronics Lab", (3, 7, 3, 1), "Peter's Lab~:\n", "I'm just glad to not have to be in here anymore.",('d', 'u'), True, 1),
    Map("Peter Jonasson's Office", (3, 6, 3, 1), "Peter Johnason's Office~:\n", "The grand sorcerer's mystic place",('d', 'u'), True, 1),

    # --- GREEN LAKE: Dimension 3 ---
    Map("Green Lake",(0,0,0,3),"~~","You wake up in a peaceful place. The water is rushing by down on a nearby like. The leaves are blowing in the wind casting shadows in the green clearing. You feel the warm sun kissing your skin. (\S)Standing just in front of log house you see an old black lab. Sitting patiently waiting for you to throw his ball. He sits beside a sign that reads: Freds' Place.",('f','b','l','r','u','d'),True),

    # --- HAUNTED FOREST EXPANSION: Dimension 4 ---
    Map("Forest Entrance", (4, 0, 0, 4), "FOREST ENTRANCE: (\S)You can go forward... or back the way you came.",
            "You enter the dense brush full of curiousity. (\S)You feel a cool breeze rush past you as if it is an omen of danger lurking within. (\S)'Be careful in here...' you think to yourself.", ('l', 'r','b'), False),
    Map("Forest", (4, 1, 0, 4), "FOREST: (\S)","The brush... it is thicc. (\S)You narrowly avoid stepping in a puddle.", ('l', 'r'), False),
    Map("Forest", (4, 2, 0, 4), "FOREST: (\S)","The crunch of leaves beneath your feet is all you hear besides the wind whistling...", ('l', 'f'), False),
    Map("Forest", (5, 2, 0, 4), "FOREST: (\S)","A chipmunk rushes past you giving your 'fight or flight' reflex a workout...", ('r', 'f'), False),
    Map("Forest", (5, 1, 0, 4), "FOREST: (\S)","A small break in the trees above allows a rush of light to temporarily shine on your face...", ('l'), False),
    Map("Forest", (5, 0, 0, 4), "FOREST: (\S)","You get the feeling you cannot go anywhere but back the way you came...", ('l', 'r', 'b'), False),
    Map("Forest", (6, 1, 0, 4), "FOREST: (\S)","You wonder if it is time to drink your urine... (\S)I heard Bear Grylls did that once.", ('b', 'f'), False),
    Map("Forest", (7, 1, 0, 4), "FOREST: (\S)","You enter a small clearing... (\S)You can go in any of the cardinal directions.", (), False),
    Map("Forest", (7, 0, 0, 4), "FOREST: (\S)","I wonder who actually took the time to map out the Bruce Trail? (\S)Like c'mon...", ('r', 'b'), False),
    Map("Forest", (6, 0, 0, 4), "FOREST: (\S)","You get the feeling you cannot go anywhere but back the way you came...", ('f', 'b', 'l'), False),
    Map("Forest", (8, 1, 0, 4), "FOREST: (\S)","You enter a small clearing... (\S)You can go in any of the cardinal directions except backwards.", ('b'),False),
    Map("Forest", (9, 1, 0, 4), "FOREST: (\S)","Early settlers used to think that pinecones were tree poop... (\S)When they stepped on one they would say: (\S)'Oh no I got tree poop on my tootsies.'",('r','f'),False),
    Map("Forest", (9, 0, 0, 4), "FOREST: (\S)","You feel like you hear muttering in the distance... (\S)Must be the wind.", ('r', 'b'), False),
    Map("Forest", (8, 0, 0, 4), "FOREST: (\S)","You get the feeling you cannot go anywhere but back the way you came...", ('f', 'b', 'l'), False),
    Map("Forest", (8, 2, 0, 4), "FOREST: (\S)", "You see a red-tail squirrel... (\S)A common pest in cottage country.",('f', 'l'), False),
    Map("Forest", (9, 2, 0, 4), "FOREST: (\S)","Does humming while hiking make the trail go by faster? (\S)Better to just enjoy the nature around you...",('r', 'b'), False),
    Map("Forest", (9, 3, 0, 4), "FOREST: (\S)","A air goes cold and still... (\S)You feel as if you are being watched.", ('f', 'r'), False),
    Map("Forest", (8, 3, 0, 4), "FOREST: (\S)","You wonder how many colours of leaf there could possibly be... (\S)I mean, on the wavelength level... (\S)Nevermind.",('b', 'l'), False),
    Map("Forest", (8, 4, 0, 4), "FOREST: (\S)","Has any one tree ever been perfectly replicated? In the same forest? (\S)Across the world? Across time? (\S)Hmmm... ",('l', 'r'), False),
    Map("Forest", (8, 5, 0, 4), "FOREST: (\S)","You stumble over a tree root almost as if it reached out and clipped your leg...You must be seeing things...",('f', 'r'), False),
    Map("Forest", (7, 5, 0, 4), "FOREST: (\S)","The song 'Trees' by Rush seems to be making a lot of sense right about now...", ('f', 'b'), False),
    Map("Forest", (6, 5, 0, 4), "FOREST: (\S)",
        "A coyote howls in the distance... (\S)They are just underfed dogs... Harmless. (\S)Right?", ('f', 'l'), False),
    Map("Forest", (6, 4, 0, 4), "FOREST: (\S)", "Runnin' on empty... runnin' on... (\S)Runnin' bliiind!", ('b', 'l'),
        False),
    Map("Forest", (7, 4, 0, 4), "FOREST: (\S)",
        "You get the feeling you cannot go anywhere but back the way you came...", ('b', 'r', 'f'), False),
    Map("Forest", (7, 2, 0, 4), "FOREST: (\S)",
        "You skip across the rocks in a shallow river and make it to the other side... (\S)You feel athletic.",
        ('r', 'f'), False),
    Map("Forest", (6, 2, 0, 4), "FOREST: (\S)",
        "Your knees feel tired as if an undergrad spent at a desk begins to take a toll on you.", ('l', 'b'), False),
    Map("Forest", (6, 3, 0, 4), "FOREST: (\S)",
        "You enter a small clearing... (\S)You can go in any of the cardinal directions except forward.", ('f'), False),
    Map("Forest", (7, 3, 0, 4), "FOREST: (\S)",
        "You get the feeling you cannot go anywhere but back the way you came...", ('f','b','r'), False),
    Map("Forest", (5, 3, 0, 4), "FOREST: (\S)",
        "A leaf falls from a tree perfectly hitting your face as you walk by... (\S)Nature does projectile motion now?",
        ('f', 'b'), False),
    Map("Forest", (4, 3, 0, 4), "FOREST: (\S)",
        "You enter a small clearing... (\S)You can go in any of the cardinal directions except backward.", ('b'),
        False),
    Map("Forest", (3, 3, 0, 4), "FOREST: (\S)", "'A small scramble up a few rocks never hurt nobody...'(\S)In that very moment you scrape your knee...(\S)Ouch.",('f','b'),False),
    Map("Forest", (2, 3, 0, 4), "FOREST: (\S)", "You hear a bustle in the hedgerow... (\S)'Don't get alarmed now.' (\S)You think to yourself...",('l','f'),False),
    Map("Forest", (2, 2, 0, 4), "FOREST: (\S)",
        "You enter a small clearing... (\S)You can go in any of the cardinal directions except right.", ('r'), False),
    Map("Forest", (2, 1, 0, 4), "FOREST: (\S)",
        "You enter a small clearing... (\S)You can go in any of the cardinal directions except right.", ('r'), False),
    Map("Forest", (2, 0, 0, 4), "FOREST: (\S)",
        "You enter a small clearing... (\S)You can go in any of the cardinal directions except backward.", ('b'),
        False),
    Map("Forest", (1, 0, 0, 4), "FOREST: (\S)", "You hear giggling through the brush... (\S)'Of course, a child's laugh in the forest... perfectly normal.' (\S)You think to yourself...",('b','f'),False),
    Map("Forest", (0, 0, 0, 4), "FOREST: (\S)",
        "You get the feeling you cannot go anywhere but back the way you came...", ('l','b','f'), False),
    Map("Forest", (3, 0, 0, 4), "FOREST: (\S)",
        "A small incline in the path you take starts to activate your quads... (\S)This should add some definition...",
        ('r', 'b'), False),
    Map("Forest", (3, 1, 0, 4), "FOREST: (\S)", "The incline grows fierce as you begin a slight scramble upwards...",
        ('r', 'l'), False),
    Map("Forest", (3, 2, 0, 4),
        "FOREST: (\S)You emerge from the brush to reveal a lookout of sorts... (\S)You collect your surroundings and imagine a clock-like directional system... (\S)At 12 o'clock you see a glint of something metallic. At 1 o'clock you see smoke coming from a chimney. (\S)At 8 o'clock you hear giggling. (\S)At 4 o'clock you hear muttering. (\S)At 10 o'clock you smell what can only be desribed as the Hamilton industrial area. (\S)At 3 o'clock the brush appears much drier than the rest of the forest...",
        "You get the feeling you cannot go anywhere but back the way you came...", ('r', 'l'), False),
    Map("Forest", (1, 1, 0, 4), "FOREST: (\S)",
        "You get the feeling you cannot go anywhere but back the way you came...", ('l', 'f', 'b'), False),
    Map("Forest", (1, 2, 0, 4), "FOREST: (\S)",
        "You see a bird fly overhead... (\S)It would be a lot easier to navigate this forest from a view up there...",
        ('f', 'b'), False),
    Map("Forest", (0, 2, 0, 4), "FOREST: (\S)",
        "You enter a small clearing... (\S)You can go in any of the cardinal directions except left.", ('l'), False),
    Map("Forest", (0, 1, 0, 4), "FOREST: (\S)",
        "You get the feeling you cannot go anywhere but back the way you came...", ('l', 'r', 'b'), False),
    Map("Forest", (0, 3, 0, 4), "FOREST: (\S)",
        "Through the thick brush it appears the trail winds left and right and the ground becomes more and more damp...",
        ('f', 'l'), False),
    Map("Forest", (1, 3, 0, 4), "FOREST: (\S)",
        "The brush grows thicker and less light makes it through the trees... (\S)You feel colder too.", ('r', 'b'),
        False),
    Map("Forest", (1, 4, 0, 4), "FOREST: (\S)",
        "You see the silhouette of a man from within the brush... (\S)He looks rather shady as the embers from his lit cigarette give you fleeting glimpses of his scruffy face... (\S)You are on high alert.",
        ('l', 'f'), False),
    Map("Forest", (2, 4, 0, 4), "FOREST: (\S)",
        "The darkness of the trail now begins to play on your mind... (\S)Was that a shadow moving? (\S)Must be the wind...",
        ('f', 'b'), False),
    Map("Forest", (3, 4, 0, 4), "FOREST: (\S)",
        "The darkness of the trail subsides which briefly reveals the rocky and uneven terrain beneath your feet.",
        ('r', 'b'), False),
    Map("Forest", (3, 5, 0, 4), "FOREST: (\S)",
        "You accidently step into a puddle... (\S)Agh, a soaker... just what you needed... (\S)You shake your foot dry and move on.",
        ('r', 'f'), False),
    Map("Forest", (2, 5, 0, 4), "FOREST: (\S)",
        "Out of the corner of your eye you spot a black... cat? (\S)It rushes by from your right to left... (\S)Strange.",
        ('l', 'b'), False),
    Map("Forest", (2, 6, 0, 4), "FOREST: (\S)",
        "You enter a small clearing... (\S)You can go in any of the cardinal directions.", (), False),
    Map("Forest", (1, 6, 0, 4), "FOREST: (\S)",
        "You enter a small clearing... (\S)You can go in any of the cardinal directions except left.", ('l'), False),
    Map("Forest", (1, 5, 0, 4), "FOREST: (\S)",
        "Through the dense brush the smell of a musty swamp begins to carry a slightly sulfuric odour... (\S)Hmmm...",
        ('r', 'b'), False),
    Map("Forest", (0, 5, 0, 4), "FOREST: (\S)",
        "The leaves beneath your feet grow increasingly slippery... (\S)You trek with care as you feel a slip is imminent. (\S)Good thing you did your 'Slips, Trips, and Falls' training.", ('f', 'l'), False),
    Map("Forest", (0, 4, 0, 4), "FOREST: (\S)",
        "You get the feeling you cannot go anywhere but back the way you came...", ('l', 'b', 'r'), False),
    Map("Forest", (3, 6, 0, 4), "FOREST: (\S)",
        "The rushing water of a nearby river temporarily dampens the sound of the leaves beneath your feet (\S) and the birds above your head... (\S)The water appears to rush from behind you to in front of you.",
        ('f', 'b'), False),
    Map("Forest", (4, 6, 0, 4), "FOREST: (\S)",
        "You enter a small clearing... (\S)You can go in any of the cardinal directions except right.", ('r'), False),
    Map("Forest", (4, 5, 0, 4), "FOREST: (\S)",
        "You take a look behind you and through the dense brush you see what looks like (\S)a clearing atop a nearby hill. (\S)Interesting...",
        ('r', 'l'), False),
    Map("Forest", (4, 4, 0, 4), "FOREST: (\S)",
        "You enter a small clearing... (\S)You can go in any of the cardinal directions except left.", ('l'), False),
    Map("Forest", (5, 4, 0, 4), "FOREST: (\S)",
        "The fallen trees around you being to place your mind in a metaphysical state... (\S)Do you think anyone heard their cries as they fell? (\S)Nevermind...",
        ('r', 'b'), False),
    Map("Forest", (5, 5, 0, 4), "FOREST: (\S)",
        "At this point you feel as if you are in the densest part of the forest. (\S)Almost as if the forest spreads equally around you in all directions...",
        ('r', 'l'), False),
    Map("Forest", (5, 6, 0, 4), "FOREST: (\S)",
        "You come across a small pond... (\S)After some quick searching you spot a beautifully 'skipable' stone... (\S)One flick of the wrist later and it skips 7 times! (\S)Is that a record?",
        ('l', 'f'), False),
    Map("Forest", (6, 6, 0, 4), "FOREST: (\S)",
        "You enter a small clearing... (\S)You can go in any of the cardinal directions except backward.", ('b'),
        False),
    Map("Forest", (7, 6, 0, 4), "FOREST: (\S)",
        "Wait... (\S)Is poison ivy the one with the red stems and mapcolour spots? White spots with red stems? (\S)Uh oh...",
        ('f', 'b'), False),
    Map("Forest", (8, 6, 0, 4), "FOREST: (\S)",
        "It appears a small trail has been made here. (\S)A seemingly clear path heads off to the right... (\S)You notice some footprints in the mud.",
        ('f', 'b'), False),
    Map("Forest", (9, 6, 0, 4), "FOREST: (\S)",
        "You see a plastic bag stuck to a tree. (\S)Some people... (\S)You channel your inner David Suzuki and pick up the trash placing it in your pocket.",
        ('r', 'f'), False),
    Map("Forest", (9, 5, 0, 4), "FOREST: (\S)",
        "The path begins to open up and you feel as if this is a spot frequented by campers... (\S)Some trees nearby appear to be cut with a saw rather than simply broken... (\S)After a quick nature check you plan your next move.",
        ('l','r',), False),
    Map("Forest", (9, 4, 0, 4), "FOREST: (\S)",
        "You enter a small clearing... (\S)A fire pit lies in the middle... (\S)You can go in any of the cardinal directions except backward.",
        ('l', 'b', 'r'), False),
    Map("Forest", (4, 7, 0, 4), "FOREST: (\S)",
        "The path ahead appears brighter and drier... (\S)This excites you as your feet could use an 'airing out'. (\S)You fear for the safety of the ecosystem being exposed to your feet and decide to keep them covered...",
        ('l', 'f'), False),
    Map("Forest", (5, 7, 0, 4), "FOREST: (\S)",
        "Is that the sound of a woodpecker or are your knee joints turning to powder? (\S)You soldier on...",
        ('r', 'b'), False),
    Map("Forest", (5, 8, 0, 4), "FOREST: (\S)", "You notice slash marks on the side of a tree... (\S)Are they from an animal? A murderer? (\S)Better not stick around to find out.",('f', 'l'), False),
    Map("Forest", (6, 8, 0, 4), "FOREST: (\S)",
        "A rabbit happily bounces by and you take a moment to watch it go... (\S)It seemed rather fast... you wonder what could have caused it to flee so quickly... (\S)Hmmm... ",
        ('r', 'b'), False),
    Map("Forest", (6, 9, 0, 4), "FOREST: (\S)",
        "As you trek along the crunch of leaves which you have become acustomed to (\S)suddenly is replaced with a much harder object... (\S)You look down and notice a metallic object poking through the forest floor... ",
        ('r', 'f'), False),
    Map("Forest", (5, 9, 0, 4), "FOREST: (\S)",
        "You get the feeling you cannot go anywhere but back the way you came...", ('b','l','f'), False),
    Map("Forest", (2, 7, 0, 4), "FOREST: (\S)",
        "Are there brown bears in southern Ontario? (\S)Grizzlies? (\S)Or was that bigfoot you just saw off in the distance...",
        ('f', 'l'), False),
    Map("Forest", (3, 7, 0, 4), "FOREST: (\S)",
        "The makeshift trail you have been travelling upon appears to head slightly upwards ahead... (\S)If only you had brought your trusty compass this may have been easier.",
        ('r', 'b'), False),
    Map("Forest", (3, 8, 0, 4), "FOREST: (\S)",
        "You enter a small clearing... (\S)A fire pit lies in the middle... (\S)You can go in any of the cardinal directions except backward.",
        ('f'), False),
    Map("Forest", (2, 8, 0, 4), "FOREST: (\S)",
        "The familiar and earthy cologne of the forest is suddenly disrupted with a horrid stench... (\S)To your horror you notice a nearby dead dear... (\S)You cover your nose and mouth to avoid the smell.",
        ('l', 'b'), False),
    Map("Forest", (2, 9, 0, 4), "FOREST: (\S)",
        "You find signs of a potential nearby campsite which may have been used recently... (\S)Trash litters the area and you silently apologize to the forest on behalf of (\S)your species.",
        ('l', 'f'), False),
    Map("Forest", (3, 9, 0, 4), "FOREST: (\S)",
        "This is definitely a site where campers have frequented. (\S)You take a moment to sit on one of the nearby stumps before getting ready to move on.",
        ('f', 'b'), False),
    Map("Forest", (4, 9, 0, 4), "FOREST: (\S)",
        "The forest is a beautiful and green as ever. (\S)Good thing the human eye response is centred around green. (\S)Otherwise you would have totally just stepped on that non-poisonous Ontario snake!",
        ('r', 'f'), False),
    Map("Forest", (4, 8, 0, 4), "FOREST: (\S)", "All around you you see fallen trees and stumps of trees which have been cut down... (\S)'Deforestation is such a shame' you think to yourself while shaking your fist.", ('r', 'b'), False),
    Map("Forest", (6, 7, 0, 4), "FOREST: (\S)",
        "The brush grows thick once more... (\S)You wish you would have brought a machete or some method of clearing your path. (\S)Oh well..",
        ('l', 'f'), False),
    Map("Forest", (7, 7, 0, 4), "FOREST: (\S)",
        "The thick brush subsides and you begin to see what can only be described as a beaten path...", ('f', 'b'),
        False),
    Map("Forest", (8, 7, 0, 4), "FOREST: (\S)",
        "The bustling of animal activity temporarily distracts you... (\S)You see two squirrels chasing one another in the distance. (\S)Wow, a lot of nature on display today.",
        ('f', 'b'), False),
    Map("Forest", (9, 7, 0, 4), "FOREST: (\S)",
        "For a moment it appears that the brush becoming less intense will be a blessing... (\S)Then you are greeted with the skeletal remains of an animal. (\S)What a shame.",
        ('b', 'r'), False),
    Map("Forest", (9, 8, 0, 4), "FOREST: (\S)",
        "The familiar smell of a wood fire floods your senses... (\S)Where could that be coming from...", ('f', 'r'),
        False),
    Map("Forest", (8, 8, 0, 4), "FOREST: (\S)",
        "Footprints litter the forest floor... (\S)Almost as if this trail has been travelled many times, and recently...",
        ('f', 'b'), False),
    Map("Forest", (7, 8, 0, 4), "FOREST: (\S)",
        "The sturdy and tall bodies of southern Ontarian trees slowly become fewer and farther inbetween... (\S)You notice a tree stump nearby...",
        ('l', 'b'), False),
    Map("Forest", (7, 9, 0, 4), "FOREST: (\S)",
        "You certainly recognize that this area has been frequently travelled and (\S)the smell of smoke grows stronger with each step.",
        ('f', 'l'), False),
    Map("Forest", (8, 9, 0, 4), "FOREST: (\S)","Through the brush you can faintly make out what appears to be a cabin to your right... (\S)It makes sense then, why the nearby trees were cut and where they have gone... (\S)You see a 'DO NOT ENTER' sign nailed to a nearby tree. (\S)It might be a good idea to make sure whoever lives there is gone before trying to go inside.", ['f', 'b','r'], False,0, [("r", 0, 0, 0, 5)]),
    Map("Forest", (1, 7, 0, 4), "FOREST: (\S)",
        "A tree branch falls and lands nearby. (\S)It almost seems as if the tree threw it at you... Strange..",
        ('l', 'r'), False),
    Map("Forest", (1, 8, 0, 4), "FOREST: (\S)",
        "You lose focus as you trek along... (\S)An abnormality in the trees catches your eye. (\S)One tree has bark removed and what appears to be an inscription carved upon its base.",
        ('l', 'r'), False),
    Map("Forest", (1, 9, 0, 4), "FOREST: (\S)",
        "As you continue you notice several articles of hiking apparel. (\S)Most of it is torn to shreds with clear signs of a struggle. (\S)You remain on high alert.",
        ('f', 'r'), False),
    Map("Forest", (0, 9, 0, 4), "FOREST: (\S)",
        "A few of the nearby trees have slashes in them. (\S)Not just small slashes, these look like huge chunks cut from the tree. (\S)Almost as if it came from a heavier tool like an axe.",
        ('l', 'f'), False),
    Map("Forest", (0, 8, 0, 4), "FOREST: (\S)",
        "You see what can only be described as a gate formed out of the forest. (\S)The trees are intertwined in such a natural way it appears that it was created by the forest itself.",
        ('l', 'r'), False),
    Map("Forest", (0, 7, 0, 4), "FOREST: (\S)",
        "Behind you the trail begins ascending rather quickly... (\S)The brush begins to become increasingly thin as you sense a clearing is nearby.",
        ['l', 'r','b'], False),
    Map("Forest Sanctuary", (0, 6, 0, 4), "FOREST SANCTUARY: (\S)",
        "The clearing is beautiful. (\S)All around you are insects and animals in a display of environmental harmony. (\S)Light shines brightly from above and a beam settles upon a stone pedestal with an inscription which emerges from the forest floor.",
        ('b', 'l', 'r'), False),
    # --- CABIN IN THE WOODS: Dimension 5 ---
    Map("Cabin Main Room", (0, 0, 0, 5), "CABIN MAIN ROOM: (\S)","With a long creaking sound the door swings open... (\S)It is very apparent that this place is lived in. (\S)You wonder what else may lie within. To your left is the door back to the woods.",('b', 'f'), False,0, [("l", 8, 9, 0, 4)]),
    Map("Cabin Kitchen", (1, 0, 0, 5), "CABIN KITCHEN: (\S)","Dishes fill the sink and meat hangs from the ceiling... Its fresh... (\S)This looks and smells like it is from the 50's.",('r', 'b'), False),
    Map("Cabin Bedroom", (1, 1, 0, 5), "CABIN BEDROOM: (\S)","A single bed is in the middle of the room. (\S)A dim lamp resides on a rickety bedside table. (\S)The wind blows gently through an open window as you notice a desk with some scattered notes upon it.",('r', 'f'), False),
    Map("Cabin Bathroom", (0, 1, 0, 5), "CABIN BATHROOM: (\S)","Nothing too out of the ordinary in here... (\S)The toilet is a bit old fashio- wait... (\S)Is the toilet paper actually bark? (\S)Clearly we ARE dealing with a madman. (\S)You look around the bathroom... Behind the door... under the sink...",('l', 'f', 'b'), False)
    ]

    #Items: Equipment.name = "Name" - Equipment.location = tuple of location - Equipment.image = .jpg of item
    #       Equipment.info = "info" - Equipment.worn = 'head','hand','body',or 'off-hand' - Equipment.stats = (Atk,Def,Spd)
    #Example: Gun = Equipment("Gun",(0,0,0),"Gun.jpg","It shoots people.","hand",(100,0,100),"")
    # TODO Sort items back into "Head", "Body", "Hand", "Off-hand", "Special" (quest items). Via CSVs is the easiest way
    ITEMS1 = [
    Equipment("Cheese", (5,7,1,0), "Cheese.jpg", "Not just cheddar, the smelly kind.", "off-hand", (1,1,1),5),
    Equipment("Delicious Meal", (None), "Meal.jpg", "A beautiful, home-cooked, meal.", "off-hand", (1,1,1),25),
    Equipment("Shovel", (5,0,0,0), "Shovel.jpg", "Call a spade a spade.", "hand", (15,0,5),""),
    Equipment("Wrench", (1,3,1,0), "Wrench.jpg", "It's a wrench. 22mm.", "hand", (9,0,2),""),
    Equipment("LED of Power", (None), "LED.jpg", "An LED with the power output of a neutron star, ok maybe not.", "hand", (21,0,20),""),
    Equipment("Green Bang Bong", (None), "GBB.jpg", "The sacred glass flute providing righteous tokes since '69.", "off-hand", (69,69,69),""),
    Equipment("Squid Hat", (3, 4, 3,0), "SquidHat.jpg", "The finest headwear you can aquire at Canada's Wonderland. Making you the fairest of all the arthropods.", "head", (4, 4, 7), ""),
    Equipment("WAW Case", (2, 4, 3,0), "WAWCase.jpg", "Call of Duty World at War for the PS3. The first game to introduce Zombies Mode. A fine game but definitely not school appropriate. You open the case and the disk isn't in it.","off-hand", (1, 1, 1), ""),
    Equipment("Gas Mask", (3,5,1,0), "GasMask.jpg", "No one cared who I was till I put on the mask.", "head", (3,6,5),""),
    Equipment("Surgical Mask", (0,1,1,0), "SurgicalMask.jpg", "Don't touch me I'm sterile!", "head", (0,2,3),""),
    Equipment("Tofu", (5,4,0,0), "Carrot.jpg", "Vegan's delight.", "hand", (1,0,5),2),
    Equipment("Jar of Horse Radish", (4,5,1,0), "HRaddish.jpg", "Apparently not an instrument...", "off-hand", (2,0,4),3),
    Equipment("Squash Racket", (5,0,1,0), "Racket.jpg", "Dr. Buijs' Racket? Voltage Divider!", "hand", (5,0,8),""),
    Equipment("Goggles", (3,2,1,0), "Goggles.jpg", "Got PPE?", "head", (2,0,2),""),
    Equipment("Bike Helmet", (3,7,1,0), "BikeHelmet.jpg", "One of those fast Tour de France ones. Does this belong to Dr. Minnick? Great!", "head", (0,8,10),""),
    Equipment("Empty Bottle", (4,1,1,0), "EmptyBottle.jpg", "Dasani, more like Dishonest! Amirite?!", "hand", (1,0,1),""),
    Equipment("Hard Hat", (4,2,1,0), "HardHat.jpg", "You don't really want to look like a Civil kid. But at least it protects your head.", "head", (1,10,5),""),
    Equipment("Priest Gown", (2,0,2,0), "Gown.jpg", "Wearing this gives people the impression you are a holy person...", "body", (10,40,10),""),
    Equipment("Used Plunger", (5,0,0,0), "Plunger.jpg", "Used. Lovely...", "hand", (10,0,10),""),
    Equipment("Dumbbell", (1,0,1,0), "Dumbbell.jpg", "The pump is the greatest feeling in the world.", "off-hand", (5,0,2),""),
    Equipment("Febreze", (1,0,1,0), "Ferbreze.jpg", "Kills 99.9% of odour at the source!", "hand", (35,0,10),-4),
    Equipment("MSP430", (2,3,1,0), "MSP430.jpg", "A literal piece of garbage.", "hand", (-5,0,-5),-5),
    Equipment("Declaration of Independence", (None), "DOI.jpg", "I'm going to steal the Declaration of Independence...", "off-hand", (1,1,1),""),
    Equipment("Needa Pita", (4,6,1,0), "Pita.jpg", "Better have gotten black olives on that", "hand", (2,0,1),5),
    Equipment("Bottle Opener", (3,7,1,0), "BottleOpener.jpg", "I wish I had a bottle of wine right about now...", "off-hand", (0,5,15),""),
    Equipment("Car Keys", (4,2,1,0), "CarKeys.jpg", "Volkswagen car keys with an 'R' on the keychain. Hmm...", "off-hand", (5,0,5),""),
    Equipment("Erik's Frosted Tips", (None), "FrostedTips.jpg", "Ever wanted to look rad as hell? Now you can!", "head", (0,3,20),""),
    Equipment("Pedrotti Cubed", (None), "Pedrotti.jpg", "'Property of Harold Haugen, one of the 3 Quantum Relics' is inscribed on the first page.", "off-hand", (50,150,250),""),
    Equipment("Puke", (None), "Puke.jpg", "Ew, literally a pool of vomit", "body", (1,0,-10),-2),
    Equipment("Adderall", (5,3,1,0), "Adderall.jpg", "Speed up, my dude!", "off-hand", (0,0,50),2),
    Equipment("Visor Glasses", (None), "FastGlasses.jpg", "Damn, you are now travelling waaaay to fast. Slow down dude!", "head", (1,5,35),""),
    Equipment("Plastic Bag", (2,1,1,0), "PBag.jpg", "The audacity of some people to leave their filth around.", "head", (0,1,-10),""),
    Equipment("Engineering Mug", (None), "EngMug.jpg", "Do people even have these anymore?", "hand", (20,20,20),""),
    Equipment("Broken Wine Bottle", (4,3,1,0), "WineBottle.jpg", "A broken wine bottle from 1996, good year.", "hand", (10,0,5),""),
    Equipment("Jar of Peanut Butter", (4,0,1,0), "Peanut.jpg", "Death paste to those who are allergic... Could prove effective...", "off-hand", (0,5,5),5),
    Equipment("Toilet Seat", (5,0,0,0), "Toilet.jpg", "How do you even wear this?", "body", (0,3,2),""),
    Equipment("VH Sauce", (1,4,1,0), "VHSauce.jpg", "Sweet and sour. Nice.", "off-hand", (1,2,1),1),
    Equipment("Banana", (1,7,1,0), "Banana.jpg", "High in potassium.", "hand", (5,0,5),2),
    Equipment("Ice-Cold Pint", (4,3,1,0), "Pint.jpg", "Ale of the Gods.", "off-hand", (3,0,-5),2),
    Equipment("Pencil", (2,4,1,0), "Pencil.jpg", "HB2. Sharpened.", "hand", (2,0,5),""),
    Equipment("Cricket", (3,4,2,0), "Cricket.jpg", "Makes the sound commonly heard at 2W lectures.", "off-hand", (1,1,1),3),
    Equipment("EpiPen", (5,7,1,0), "EpiPen.jpg", "Epinephrine Autoinjector 0.3mg. Replace if discolored. Store at 68C. Incase of alergic reaction remove the top...wait, why are you reading this label? Isn't there something else you should be doing? ", "off-hand", (7,0,5),-2),
    Equipment("Wood Shield", (5,4,2,0), "Shield.jpg", "An old wooden shield used in a play, you think...", "off-hand", (5,20,-5),""),
    Equipment("Cold Steel Katana", (None), "Katana.jpg", "This could probably kill a buffalo fish...", "hand", (45,5,20),""),
    Equipment("Flux Capacitor", (None), "FluxCapacitor.jpg", "If only I could go back to 1985...", "hand", (1,1,1),""),
    Equipment("Swordfish", (None), "Swordfish.jpg", "I'd better be careful eating this!", "off-hand", (50,10,30),20),
    Equipment("Ancient Incantation", (None), "Incantation.jpg", "An old tattered scroll with an incantation written in Latin.", "off-hand", (1,1,1),""),
    Equipment("Meow Mix", (None), "MeowMix.jpg", "I love chicken, I love liver...", "off-hand", (5,0,5),1),
    Equipment("Phone", (None), "Phone.jpg", "This thing has been dropped Graham's number times.", "off-hand", (5,6,9),""),
    Equipment("Casio", (2,7,1,0), "Casio.jpg", "This one can do integrals. That's illegal.", "off-hand", (1,5,10),""),
    Equipment("Vomit", (None), "Vomit.jpg", "Literally spew.", "off-hand", (0,0,1),-1),
    Equipment("Bleach Squirt Bottle", (None), "Bleach.jpg", "Probably wouldn't be nice to get sprayed with.", "hand", (15,5,20),-10),
    Equipment("Drumstick", (5,4,2,0), "Drumstick.jpg", "'Property of E-Smooth'", "off-hand", (0,10,15),""),
    Equipment("Self Worth", (None), "DOI.jpg", "Wow, I had this in my all along! Now all I have to do is wait to go back to my bad habits and this will be worthless!", "off-hand", (20,20,20),-10),
    Equipment("Blazer", (5,6,1,0), "Blazer.jpg", "Styyyyyylishhhhhh", "body", (0,4,1),""),
    Equipment("Empty Bucket", (5,0,0,0), "Bucket.jpg", "The smell of cheap soap still lingers.", "head", (0,10,1),""),
    Equipment("Old Scroll", (None), "OldScroll.jpg", "It reads: 'A permanent title is too much to bear.' 'My secret cache, is under there.'", "off-hand", (0,0,0),""),
    Equipment("PID control system", (None), "PID.jpg", "A PID control system. Kp = 69, my dude.", "head", (45,69,10),""),
    Equipment("Voltage Divider", (None), "VDivider.jpg", "It is a Voltage Divider!", "off-hand", (20,25,20),""),
    Equipment("Frank's Red Hot", (0,4,1,0), "FranksRed.jpg", "I put that...", "off-hand", (3,0,2),1),
    Equipment("Santa Hat", (0,0,1,0), "SantaHat.jpg", "Happy Holidays!", "head", (0,3,2),""),
    Equipment("Banana Wires", (3,4,1,0), "BanWires.jpg", "Alligator clips added for extra whippage.", "hand", (8,0,8),3),
    Equipment("Party Hat", (3,6,1,0), "PartyHat.jpg", "A nice hat from a cracker.", "head", (0,5,3),""),
    Equipment("Jar of Mayo", (0,2,1,0), "Mayo.jpg", "Is mayonaise an instrument?", "off-hand", (3,0,5),1),
    Equipment("Shampoo", (0,0,1,0), "Shampoo.jpg", "Yeah, I could use a shower...", "off-hand", (4,0,3),""),
    Equipment("Candlestick", (4,0,0,0), "Candlestick.jpg", "Lumiere is up to no good.", "hand", (7,0,5),""),
    Equipment("Gamma Glove", (None), "GammaGauntlet.jpg", "Shorter than it really is due to length contraction, one of the 3 Quantum Relics", "hand", (250,100,20),""),
    Equipment("Clean Needle", (None), "CleanNeedle.jpg", "No more spreadin' disease!", "hand", (25,0,9),""),
    Equipment("Laser Safety Glasses", (1,6,0,0), "LSGlasses.jpg", "Protection from the UV, my dude.", "head", (0,10,5),""),
    Equipment("Tarzan VHS", (0,2,1,0), "Tarzan.jpg", "If only I had a VCR...", "off-hand", (0,2,6),3),
    Equipment("Priceless Painting", (3,0,1,0), "Painting.jpg", "This painting is supposed to be worth millions...", "off-hand", (1,10,5),""),
    Equipment("Paint Brush", (3,1,1,0), "Brush.jpg", "You can feel the emotions of a failed arts student coursing through this thing.", "off-hand", (5,0,5),""),
    Equipment("Pizza Box", (0,3,1,0), "PizzaBox.jpg", "Fully equipped with crusted cheese.", "body", (1,5,1),3),
    Equipment("Haugen's Clothes", (None), "HaugenShirt.jpg", "OH My. The clothes of the gentle dolphin now gone. Feels kinda wet.", "body", (5,10,10),10),
    Equipment("3W Textbook", (None), "3WText.jpg", "Text book that probably has useful information if you could read it. Too bad it has never been in the QT", "off-hand", (5,5,10),""),
    Equipment("Fireball Hat", (2,2,1,0), "EngHat.jpg", "Kind of like the hat you bought in first year and thought you'd wear forever...", "head", (0,3,1),""),
    Equipment("Raybans", (5,5,1,0), "Raybans.jpg", "GQ Teen says Raybans, Board Shorts, Vans, and a Muscle Tee.", "head", (0,1,3),""),
    Equipment("Gilded Blunderbuss", (None), "Blunderbuss.jpg", "A beautiful firearm with infinite ammo.", "hand", (200,5,50),""),
    Equipment("Einstein's Brain", (None), "Brain.jpg", "Feel's kind of weird walking around with this...", "off-hand", (1,1,1),10),
    Equipment("Tony Hawk Shirt", (3,5,1,0), "TonyHAwkShirt.jpg", "A shirt personally made by tony hawk!", "body", (5,5,5),""),
    Equipment("Capstone Tools", (None), "CapTools.jpg", "Shouldn't the 4A06 students be using these?", "off-hand", (1,1,1),""),
    Equipment("Kenrick's Oscilloscope", (None), "Oscilloscope.jpg", "The window into the electronics world...", "off-hand", (0,150,50),""),
    Equipment("Femtosecond Laser", (None), "Laser.jpg", "Haugen's personal femtosecond laser.", "hand", (125,0,999),""),
    Equipment("Gauss Eye", (None), "GaussEye.jpg", "You can feel the electromagnetic energy emanating from it, one of the 3 quantum relics", "head", (100,100,100),""),
    Equipment("Okons Chainmail", (0,2,0,0), "OkonMail.jpg", "The sacred chainmail forged by the legend himself", "body", (25,50,25),""),
    Equipment("Hazmat Suit", (2,5,1,0), "Hazmat.jpg", "Protection from all sorts of McCrindle farts...", "body", (0,10,5),""),
    Equipment("Old Candle", (2,0,0,0), "OldCandle.jpg", "Seems like it's had some use.", "off-hand", (0,2,2),""),
    Equipment("Tire Iron", (5,7,1,0), "TireIron.jpg", "Is this even a real tool? Or just a murder weapon...", "hand", (11,0,3),""),
    Equipment("Ukelele", (4,4,1,0), "Ukelele.jpg", "Wasting away again in Margaritaville...", "hand", (6,0,5),""),
    Equipment("Fanny Pack", (None), "FannyPack.jpg", "Made for style. Not for carrying.", "body", (10,60,30),""),
    Equipment("STARS Wireless Fix", (None), "StarsFix.jpg", "IT took 6 weeks to make this code? Who knew debugging could be this hard?", "off-hand", (1,1,1),""),
    Equipment("Brendan Fallon's Lunchbox", (3,4,0,0), "Lunchbox.jpg", "The Lunch Box of an Ancient Hero. Full of samosas.", "off-hand", (5,10,5),""),
    Equipment("Eng Phys USB Pen", (None), "PhysPen.jpg", "It would be amazing if this thing actually worked. If I had a laptop I could plug it in and find all of 2P04.", "hand", (5,0,5),""),
    Equipment("Ambifacient Lunar Waneshaft", (None), "Dumbness.jpg", "The design consists simply of six hydrocoptic marzlevanes, they fit to the ambifacient lunar waneshaft so that side fumbling is effectively prevented", "off-hand", (1,1,1),""),
    Equipment("Space Pop", (1,7,2,0), "SpacePop.jgp", "Get ready to go to space pop city.", "hand", (4,0,10),1),
    Equipment("Hockey Pads", (5,7,1,0), "HockeyPads.jpg", "IM NOT WEARIN' HOCKEY PADS!", "body", (3,13,5),""),
    Equipment("Starbucks Apron", (5,0,1,0), "Apron.jpg", "If you put this on do you immediately know how to make a frappe?", "body", (1,5,5),""),
    Equipment("Pink Donut", (None), "PinkDonut.jpg", "This is what fusion is all about?", "off-hand", (1,1,1),2),
    Equipment("Relativistic Key", (None), "Relativistickey.jpg", "You can feel the power radiating from this thing.", "hand", (1,1,1),""),
    Equipment("Willy Dog", (4,1,1,0), "Hotdog.jpg", "Definitely not vegan", "hand", (1,0,2),5),
    Equipment("Solar Ray", (None), "SolarRay.jpg", "The literal power of the Sun!", "hand", (100,20,50),""),
    Equipment("Helm of Orin Bearclaw", (1,0,3,0), "SkullHelmet.jpg", "A note left beside the helmet says 'A leftover relic from a purple hero'", "head", (35,30,10),""),
    Equipment("Maroon Jumpsuit", (5,1,1,0), "MaroonSuit.jpg", "Overalls of the Maroons", "body", (1,8,5),""),
    Equipment("Pope Hat", (2,0,2,0), "PopeHat.jpg", "Does the Pope where a silly hat? Now you do.", "head", (0,3,2),""),
    Equipment("Lamp", (0,5,1,0), "Lamp.jpg", "I love lamp.", "hand", (8,0,4),""),
    Equipment("Redsuit", (2,4,2,0), "Redsuit.jpg", "Overalls of drunks... I mean engineers", "body", (5,5,5),""),
    Equipment("Butter Knife", (4,6,1,0), "ButterKnife.jpg", "Meant for spreading, not stabbing...", "hand", (4,0,5),""),
    Equipment("Eng Phys Shirt", (3,4,0,0), "EngPhysShirt.jpg", "Rolling Rock baby! Premium Stream my ass... More like premium pain...", "body", (0,7,5),""),
    Equipment("PVC Pipe", (4,7,1,0), "PVCPipe.jpg", "Probably part of a PID project...", "hand", (9,2,10),""),
    Equipment("Big Hits Shirt", (6,1,1,0), "BigHits.jpg", "The Shirt of the Hero of Kyvach!", "body", (10,5,5),""),
    Equipment("Couch Cushion", (1,7,1,0), "CCushion.jpg", "I hope I find I pillow fight.", "off-hand", (4,10,1),""),
    Equipment("Crucifix", (None), "Crucifix.jpg", "The Power of Chirst compels you!", "hand", (10,0,10),""),
    Equipment("Joint of Destiny", (None), "Joint.jpg", "A tighly rolled spliff filled with Devil's lettuce... for real.", "off-hand", (420,420,420),""),
    Equipment("Minnick's Glasses", (None), "MinnickGlasses.jpg", "The spectacles of a wizard from the High Order of the Ancient Council.", "head", (50,50,50),""),
    Equipment("Mop", (0,0,1,0), "Mop.jpg", "I'm going to clean up this town.", "hand", (6,0,4),""),
    Equipment("Cold Beer", (None), "ColdBeer.jpg", "A freshly brewed pint from Andy Knights himself.", "off-hand", (15,0,20),2),
    Equipment("Brian's Guitar", (None), "Guitar.jpg", "You now have Brian's power to shred some sick tunes! ROCK ON.", "hand", (35,35,35),""),
    Equipment("Old Headphones", (1,5,1,0), "OldHeadphones.jpg", "Old frayed apple headphones. Good for whipping.", "head", (5,0,5),""),
    Equipment("Old Car Keys", (0,6,1,0), "CarKeys.jpg", "Fun for babies. Not for Batman.", "hand", (7,0,15),""),
    Equipment("Coffee", (2,4,1,0), "Coffee.jpg", "The fuel of thinkers.", "off-hand", (3,0,9),1),
    Equipment("Hulk Hands", (0,3,0,0), "HulkHands.jpg", "These pack a serious punch...", "hand", (15,5,20),""),
    Equipment("Old Ladder", (0,7,1,0), "OldLadder.jpg", "Pretty rickety but would work for climbing.", "off-hand", (14,8,-15),""),
    Equipment("Goldfish", (2,0,2,0), "Goldfish.jpg", "Fun fact, not made of real gold.", "off-hand", (1,1,1),4),
    Equipment("Horrible Assignment", (None), "BadAss.jpg", "A barely legible report on Fourier analysis.", "off-hand", (3,0,0),""),
    Equipment("Silicon Substrate", (0,3,2,0), "Substrate.jpg", "A bulk silicon wafer.", "off-hand", (1,1,1),""),
    Equipment("Faraday's Cage", (None), "Faraday.jpg", "Faraday cage.", "head", (20,75,15),""),
    Equipment("Frisbee", (2,2,1,0), "Frisbee.jpg", "Look at the flick of the wrist!", "hand", (3,0,5),""),
    Equipment("Rusty Key", (None), "RustyKey.jpg", "You can just about read: 'By the building where the smallest are seen.' 'This key will provide for those who are keen'", "off-hand", (1,1,1),""),
    Equipment("Iron Ring", (None), "IronRing.jpg", "The One Ring to Rule them ALL.", "hand", (1000,1000,1000),-1000),
    Equipment("Pee Bottle", (2,1,1,0), "PeeBottle.jpg", "It is literally a bottle of urine.", "hand", (4,0,0),""),
    Equipment("Bowling Ball", (None), "BowlingBall.jpg", "Heavy.", "hand", (20,15,-5),""),
    Equipment("Wendy's Bag", (0,6,1,0), "WendyBag.jpg", "Fully equipped with grease stains.", "head", (1,0,-5),""),
    Equipment("High Vis Vest", (2,6,1,0), "HighVis.jpg", "Safety first, folks.", "body", (0,5,3),""),
    Equipment("Phil's Braces", (2,5,0,0), "PhilBraces.jpg", "Bark AND the bite.", "head", (3,2,1),""),
    Equipment("Potato", (None), "Potato.jpg", "A most versatile vegetable. Good for breakfast, lunch, and dinner.", "off-hand", (1,1,1),5),
    Equipment("Holy Bible", (2,0,1,0), "Bible.jpg", "King James version...", "off-hand", (3,0,3),""),
    Equipment("Griffiths Electrodynamics", (2,4,2,0), "Griffiths.jpg", "The holy scriptures which govern the fabric of our being", "off-hand", (0,10,5),""),
    Equipment("Skateboard", (0,0,0,0), "Skateboard.jpg", "Cowabunga, dude.", "hand", (9,0,10),""),
    Equipment("Diary of the Fallen", (0,2,0,0), "Diary.jpg", "The personal notes of an ancient Hero.", "off-hand", (25,20,30),""),
    Equipment("Green Lantern Shirt", (None), "GLShirt.jpg", "Darkest day... Darkest night...", "body", (15,15,10),""),
    Equipment("Dirty Needle", (0,4,1,0), "Needle.jpg", "This isn't clean. Someone find me a SharpXchange!", "hand", (7,0,5),""),
    Equipment("Stylish Watch", (None), "watch.jpg", "If only you learned how to tell time on an analog clock...", "off-hand", (0,15,20),""),
    Equipment("Huge Shirt", (None), "HugeShirt.jpg", "This shirt is WAY too big", "body", (0,5,5),""),
    Equipment("Fake Gun", (None), "FakeGun.jpg", "Is this seriously what at the MAC cops carry...", "hand", (5,0,5),""),
    Equipment("Wool Sweater", (5,3,1,0), "WoolSweater.jpg", "Merino Wool. Just like grandma makes.", "body", (1,4,6),""),
    Equipment("Solar Cell", (None), "SolarCell.jpg", "Harness the power of the Sun! I really hope I don't drop this...", "off-hand", (1,1,1),""),
    Equipment("Paper Towels", (0,5,2,0), "PaperTowels.jpg", "WHERE'S THE PAPER TOWELS?", "off-hand", (2,0,1),""),
    Equipment("Crocs of the Cartographer", (None), "DadCrocks.jpg", "Grass stains on it from where you dad would cut the lawn every Sunday. Blue jeans, no shirt. (\S)f I think he used to be an alumni here?", "body", (4, 20, 69),""),
    # TODO Find a fix for duplicate items or differiators, idk, maybe : XX designation that isn't appearent, IDK location problem, maybe simple as not checking for location but maybe that causes bugs
    Equipment("Tyler's Visor Glasses", (None), "FastGlasses.jpg","Damn, you are now travelling waaaay to fast. Slow down dude!", "head", (1, 5, 35), ""),
    Equipment("Tyler's Big Hits Shirt", (None), "BigHits.jpg", "The Shirt of the Hero of Kyvach!", "body",(10, 5, 5), ""),
    Equipment("Tyler's Hulk Hands", (None), "HulkHands.jpg", "These pack a serious punch...", "hand", (15, 5, 20),""),
    Equipment("Tyler's Green Bang Bong", (None), "GBB.jpg","The sacred glass flute providing righteous tokes since '69.", "off-hand", (69, 69, 69), ""),
    Equipment("LON-CAPA Code", (5, 3, 0, 0), "LONCAPA.jpg","This sacred Python code has saved many an engineering a tight pinch. Or just too lazy to do their own work. I wonder who made it?", "off-hand", (1, 1, 1), ""),
    Equipment("Student Card", (5,1,1,0), "SCard.jpg","Someone just dropped their student card here? The owner is Lemieux M., I guess he doesn't need it anymore.","off-hand", (1, 1, 1), ""),
    Equipment("Rubber Chicken", (None), "RChicken.jpg","Rub a dub dub in my tub.","off-hand", (3, 3, 3), 3),
    Equipment("Tennis Ball", (0, 0, 0, 3), "TennisBall.jpg","The slobery wet ball that belongs to Fred. He's probably looking for it.", "hand", (1, 1, 1), ""),
    Equipment("Dog biscuit", (0, 0, 0, 3), "DogBiscuit.jpg", "Probably better known as a cookie. One of Fred's favourite snacks.", "off-hand", (1, 1, 1), 3),
    Equipment("Softwood 2x4 Stud", (0, 0, 0, 3), "Soft2x3Stud.jpg", "A prime peice of Douglas Fir. Useful to be made into whatever you can imagine", "off-hand", (1, 1, 1), ""),
    # --- Aesthetic Objects ---
    Equipment("Kipling Pranks", (2,3,1,0), "KPranks.jpg", "The leftover pranks from the 2017-2018 year. You should probably leave these here.", "off-hand", (2, 2, 2), 3),
    Equipment("Tequila Shot Glass", (5,4,1,0), "ShotGlass.jpg", "Maybe you shouldn't touch this stuff after what happened last night.", "off-hand", (10, 0, 10), -5),
    Equipment("Cold Sweat", (3,4,1,0), "ColdSweat.jpg", "A pool of sweat on the ground. Gross.", "off-hand",(0, 0, 0), 1),
    Equipment("Polaroid Photograph", (None), "PolaroidPhoto.jpg", "What? Do people still make these? Next thing you know you'll find an 8-inch floppy disk laying around. (\S)The photo shows you smashed out of your mind at the " +mapcolour+ "Phoenix" +textcolour+ ". Looks like a good time.", "off-hand", (0, 0, 0), -2),
    Equipment("Flashcard", (None), "Flashcard.jpg", "The cards are full of notes for studying some crazy biology. Watch out for paper cuts.", "off-hand",(3, 0, 0), 1),

    #--- Haunted Forest Items ---
    Equipment("Golden Apple", (1, 0, 0, 5), "GApple.jpg", "This luxurious apple glowes in the light. A rare commodity as eating it restores full health.","off-hand", (1, 1, 1), 1000),
    Equipment("Staff of the Indomitable", (0, 6, 0, 4), "TStaff.jpg", "A trusted protector of the forest donned with leaves of brilliant colour.","hand", ( 150, 75, 125), ""),
    Equipment("Staff of the Unwavering", (0, 6, 0, 4), "BStaff.jpg", "A loyal trail guardian once owned by the descendant of a grand wizard.","hand", ( 75, 175, 125), ""),
    
    Equipment("1 Stick", (3, 0, 0, 4), "Stick.jpg", "It is a stick found in the forest.", "hand", (5, 5, 5), -1),
    Equipment("2 Sticks", (9, 1, 0, 4), "Stick.jpg", "2 sticks bundled together.", "hand", (10, 10, 10),-1),
    Equipment("3 Sticks", (0, 3, 0, 4), "Stick.jpg", "3 sticks bundled together.", "hand", (12, 12, 12),-1),
    Equipment("4 Sticks", (1, 5, 0, 4), "Stick.jpg", "4 sticks bundled together.", "hand", (14, 14, 14),-1),
    Equipment("5 Sticks", (5, 6, 0, 4), "Stick.jpg", "5 sticks bundled together.", "hand", (15, 15, 15),-1),

    Equipment("Fireplace Tongs", (5, 6, 0, 4), "Tongs.jpg", "This looks useful for grabbing things out of a fire.", "hand", (15, 15, 15),""),

    Equipment("Trail Mix", None, "TrailMix.jpg", "A lot of calories in this!", "off-hand", (1, 1, 1), 8),
    Equipment("Pointy Stick", (5, 4, 0, 4), "Stick.jpg", "It is a pointy stick found in the forest.", "hand",(20, 20, 20), -5),
    Equipment("Old Mitten", (2, 3, 0, 4), "OldGlove.jpg", "It is an old mitten who appears to have lost its mate.","off-hand", (2, 6, 3), ""),
    Equipment("Heavy Rock", (3, 4, 0, 4), "HeavyRock.jpg", "This rock is really cool looking but a lot of work to carry around.", "hand", (5, 5, 5),-1),
    Equipment("Small Rock", (7, 5, 0, 4), "SmallRock.jpg", "A small rock about the size of a plum.", "hand",(4, 2, 7), -25),
    Equipment("Aged Glasses", (3, 1, 0, 4), "AgedGlasses.jpg",
                  "Old ratty spectacles... The prescription in these is rather intense!", "head", (-5, -10, 5), ""),
    Equipment("Kindling", (7, 4, 0, 4), "Kindling.jpg", "This would start a fire real good.", "off-hand", (1, 1, 1),
                  -1),
    Equipment("Redberry", (8, 6, 0, 4), "Redberry.jpg", "It is a redberry. Potentially edible?", "off-hand",
                  (1, 1, 1), 5),
    Equipment("Broken Bone", (9, 7, 0, 4), "BrokenBone.jpg",
                  "The broken bone of an animal. You can tell the marrow has been sucked out.", "hand", (12, 1, 8),
                  -10),
    Equipment("Greenberry", (3, 7, 0, 4), "Greenberry.jpg", "It is a green berry with lateral veins. Potentially edible?",
                  "off-hand", (1, 1, 1), -100),
    Equipment("Log", (4, 8, 0, 4), "Log.jpg", "A decently big log. Campfire songs flood your mind.", "hand",
                  (10, 8, 2), -15),
    Equipment("Small Knife", (6, 9, 0, 4), "Smallknife.jpg",
                  "A sinister and small knife. There appears to be some sort of red residue. (\S)Wait...", "hand",
                  (20, 4, 15), -1),
    Equipment("Hiking Shoe", (1, 9, 0, 4), "Hikingshoe.jpg", "It is a lone hiking shoe. Missing its mate",
                  "off-hand", (1, 1, 1), -10),
    Equipment("Soda Pop Rings", (3, 9, 0, 4), "SodaRings.jpg",
                  "The plastic rings which hold a 6-pack of cans together. (\S)Turtles love to wear them apparently.",
                  "off-hand", (1, 1, 1), -10),
    Equipment("Wolf Meat", None, "Wolfmeat.jpg", "This looks remotely edible...", "off-hand", (1, 1, 1), 5),
    Equipment("Small Squirrel Meat", None, "SSMeat.jpg", "This looks barely edible...", "off-hand", (1, 1, 1), 5),
    Equipment("Big Squirrel Meat", None, "BSMeat.jpg", "This looks kind of edible...", "off-hand", (1, 1, 1), 5),
    Equipment("Rusty Hammer", (1, 0, 0, 5), "RHammer.jpg",
                  "It is an old rusty hammer... (\S)It looks like somone actually made this by hand.", "hand",
                  (25, 10, 10), ""),
    Equipment("Poopy Plunger", (0, 1, 0, 5), "PPlungeer.jpg",
                  "My goodness it is covered in fecal matter. (\S)Why did you even pick this bio-hazardous weapon up?",
                  "hand", (12, 8, 9), ""),
    Equipment("Old Work Boot", (0, 0, 0, 5), "OWBoot.jpg",
                  "An old boot with holes all over... (\S)One of them is in the perfect spot to be an ollie hole... (\S)No way!",
                  "off-hand", (5, 15, 3), ""),
    Equipment("Screwdriver", (7, 9, 0, 4), "SDriver.jpg",
                  "A rusted Philips-head screwdriver... (\S)You feel handy.", "hand", (12, 10, 8), -25),
    # -- Quest Items --
    Equipment("Furnace Door", None, "FDoor.jpg", "A sturdy cast-iron door. (\S)Better get three coffins ready...", "body", (10, 100, 5), ""),
    Equipment("Jar of Olives", None, "JoOlives.jpg", "Kalamata's? No way!", "off-hand", (1, 1, 1), 8),
    Equipment("Old Pickaxe", None, "OldPickaxe.jpg", "An old pickaxe.", "hand", (12, 8, 5), ""),
    Equipment("Woodsman's Axe", None, "Woodsmansaxe.jpg",
                  "A magical axe which appears to cause the forest to kneel at its feet.", "hand", (20, 5, 8), ""),
    Equipment("Charcoal", None, "Charcoal.jpg", "A dusty lump of charcoal.", "off-hand", (1, 1, 1), -10),
    Equipment("Makeshift Explosive", None, "Makeshiftexplosive.jpg",
                  "A match wont do. (\S)If only you had a hot enough source to light this.", "off-hand", (1, 1, 1), -10),
    Equipment("Ring Pop", None, "Ringpop.jpg", "A small sugary treat", "off-hand", (1, 1, 1), 5),
    Equipment("Matches", None, "Matches.jpg", "Perhaps I should preparea firepit for these.", "off-hand", (1, 1, 1),-10),
    Equipment("Gunpowder", None, "Gunpowder.jpg", "You should look for a canister of some sort to put this in.", "off-hand", (1, 1, 1),-10),
    Equipment("Small Key", None, "Smallkey.jpg","A small metallic key found within a cookie jar in the Cabin in the woods.", "off-hand", (1, 1, 1),-1)
    ]  # DON"T FORGET TO REMOVE THE LAST COMA!

    #Enemies: Enemy.name = "Name" - Enemy.info = "Description" - Enemy.location = (X,Y,Z) - Enemy.stats = (ATK, DEF, SPD) - Enemy.health = [integer]
    #Enemies: Enemy.drop = Item dropped on death or given - Enemy.need = special item they want - Enemy.Sinfo = "Special comment they have if you bring them 'need' item"
    #Example: Man = Enemy("Man","A Man",(1,1,1),drop,need,Sinfo,Dinfo)
    #Bosses/Profs
    ENEMIES1 = [
    Enemy("Dr. Minnick",
          "'Hello and welcome to how we retrieve your " +wincolour+ "iron ring" +textcolour+ ".'\n'The " +indicatecolour+ "Quantum Order" +textcolour+ " does not know exactly what you have done.'\n'However, we have felt the consequences of your actions.'\n'I believe the only way to explain this is to show you.'\n'The " +indicatecolour+ "Quantum Order" +textcolour+ " has gathered intelligence that " +personcolour+ "Kenrick" +textcolour+ " has been using\nhis " +itemcolour+ "oscilloscope" +textcolour+ " for evil.'\n'I need you to confront him and return his " +itemcolour+ "oscilloscope" +textcolour+ " if we are to go further. He may not give it up without a fight.'",(None),(400,400,400),200,"Minnick's glasses","Kenrick's oscilloscope","'Ah, you have returned.'\n'You see, " +personcolour+ "Kenrick" +textcolour+ " has retrofitted his " +itemcolour+ "oscilloscope" +textcolour+ " and created some sort\nof 'window' into the electronics world.'\n'Using this window he has been attempting to access the minds of the greatest\nphysicists in history and use their power for evil!'\n'Our intelligence does not go any further and we do not know what he has done.'\n'All that we do know is that after last night you must be rooted in all of this just as the prophecy foretold.'\n'Take these, if you truly are the one, they will reveal what you need to see.'\n'I suggest you start in the " +mapcolour+ "Art Museum" +textcolour+ ".'\n'Also, my lab has since been compromised so I will work in secret in the " +mapcolour+ "basement of Thode" +textcolour+ ".'\n'Once you have found the next " +wincolour+ "quantum relic" +textcolour+ ", my workbench will be ready...'","'I'm jealous of stupid people, they have more opportunities to learn!'",False),
    Enemy("Dr. Novog",
          "What's up folks?",(None),(420,420,420),100,"ancient incantation",'pink donut',"'Alright folks, here's the scoop.''I could only talk to you via the fusion network because the integrity of faculty\ncommunication has been compromised.'\n'The Engineering Physics professors are actually members of an Ancient Council known as The " +indicatecolour+ "Quantum Order" +textcolour+ ".'\n'For years we have kept McMast-'\n'An assassin?'\n'Hmm... I see, things are worse than we thought.'\n'We have known of this uprising within the faculty for some time but\nwere unaware of just how strong they have grown.'\n'As you have heard, a prophecy foretold of an adventurer dictating the future of the faculty.'\n'This evil group wants nothing more than to take advantage of your power and influence for their own plans.'\n'The choices you make will be yours and yours alone, however, the " +indicatecolour+ "Quantum Order" +textcolour+ "\nurges that you consider the consequences of your actions.'\n'It is our duty to assist you in realizing your ability but what comes of your power is out of our hands.'\n'You must contact the oracles who foretold of your coming, they will give you the knowledge you require.'\n'Each member of the " +itemcolour+ "Quantum Order" +textcolour+ " only knows of the location one Oracle.'\n'For that reason I can only help you so much.'\n" +personcolour+ "Dr. Novog" +textcolour+ " pushes a button on a nearby control panel.\nA crane arm descends into the Reactor pool to retrieve a crate from its depths.\n'Take this " +itemcolour+ "incantation" +textcolour+ " and find the " +interactcolour+ "ancient mirror" +textcolour+ " in the " +mapcolour+ "basement of Mills Library" +textcolour+ "... it is your time.'","Folks Folks Folks!",False),
    Enemy("Dr. Haugen","'Hello, as you are likely aware, there has been a disturbance...'\n'You losing your " +wincolour+ "Iron Ring" +textcolour+ " was no accident, it was taken from you.'\n'The " +indicatecolour+ "Quantum Order" +textcolour+ " is an ancient fold whose goal is to protect the\nUniversity from certain doom and misuse of our knowledge.'\n'There has been an item of importance stolen from us and we need it returned immediately.'\n'Especially if you are to find your " +wincolour+ "Iron Ring" +textcolour+ ".'\n'The council has received intelligence that " +personcolour+ "Dr. Soleymani" +textcolour+ " has stolen " +itemcolour+ "Einstein's brain" +textcolour+ " from the McMaster vault.'\n'You must retrieve it at once, she can be found somewhere in the " +mapcolour+ "hospital" +textcolour+ ".'\n'Do not underestimate her! She has been tempted by a Dark Lord.'\n'The " +indicatecolour+ "Quantum Order" +textcolour+ " requires that you defeat her and return the " +itemcolour+ "brain" +textcolour+ " at once!'",(None),(250,100,999),200,"femtosecond laser","Einstein's Brain","'" +indicatecolour+ "Oh my" +textcolour+ "! You've returned! I knew you could do it!'\n'Quickly, hand it over!'\nYou hand " +personcolour+ "Dr. Haugen" +textcolour+ " the " +itemcolour+ "brain" +textcolour+ " and he opens the " +indicatecolour+ "fridge" +textcolour+ " placing it inside.\n'Now, we just need to mount my " +itemcolour+ "laser" +textcolour+ " onto my bench-'\nSuddenly a rabid " +personcolour+ "Grad Student" +textcolour+ " bursts into the lab!\n'Hand over the " +itemcolour+ "brain" +textcolour+ ", the Dark Lord demands it!' he says.\n'If you strike me down, I will become more powerful than\nyou could possibly imagine' " +personcolour+ "Dr. Haugen" +textcolour+ " replies.\nThe " +personcolour+ "Grad Student" +textcolour+ " lunges at " +personcolour+ "Dr. Haugen" +textcolour+ " who disappears entirely!\nJust before the perplexed " +personcolour+ "Grad Student" +textcolour+ " turns towards you he is met by your blow\nand falls to the floor.","Oh my!",False),
    Enemy("Dr. Kitai","I've been trying to develop a new " +itemcolour+ "LED" +textcolour+ "...'\n'But I need some silicon, find me a " +itemcolour+ "Silicon Substrate" +textcolour+ " please!'",(None),(150,50,50),150,"LED of power","silicon substrate","'I've been looking for one just like this, how did you get it?'\n'Maybe you are th-'\n'Nevermind... just be on the lookout for " +personcolour+ "Dr. Kleiman" +textcolour+ ".'","'It was only a midterm, don't off yourself.'",False),
    Enemy("Dr. Knights","'Whoever took the " +itemcolour+ "3W Textbook" +textcolour+ " from the " +mapcolour+ "QT" +textcolour+ " shall feel my eternal wrath...'",(None),(200,100,50),300,"3w textbook","3w textbook","'I've been looking all over for that, have a cold one on me!'\n'But before you go you should know that a difficult road lies ahead.'\n'It will not be easy to have your " +wincolour+ "Iron Ring" +textcolour+ " returned to you'\n'Return the " +itemcolour+ "3W Texbook" +textcolour+ " to the " +mapcolour+ "Quantum Tunnel" +textcolour+ ", then " +personcolour+ "Dr. Haugen" +textcolour+ " should be the one you seek next.'","'What are you doing?!'",False),
    Enemy("Dr. Preston","'I would like to improve my already impressive dad strength.'\n'Bring me a " +itemcolour+ "dumbbell" +textcolour+ ".'",(None),(250,150,100),300,"green lantern shirt","dumbbell","'Yes! Now I can get the pump I've been after!'\n'Go look for " +personcolour+ "Dr. Buijs" +textcolour+ " he has much more to tell than I.'","HOW DID YOU OVERCOME MY DAD STRENGTH?!",False),
    Enemy("Dr. Kleimann","'We have been looking for you.'\n'The Department is not pleased...'\n'But first, the " +personcolour+ "McMaster Police" +textcolour+ " have confiscated my " +itemcolour+ "Solar Cell" +textcolour+ ", go get it.'\n'Then, maybe you are truly worthy of continuing this quest.'",(None),(300,150,100),300,"solar ray","solar cell","You sit down and listen to what " +personcolour+ "Dr. Kleimann" +textcolour+ " has to say...\n'You have awoken an ancient force that hasn't stirred in many years'.\n'You didn't think we would find out what you did but we know all.'\n'It had been prophecized that an adventurer would dictate the future of the faculty and only The " +indicatecolour+ "Quantum Order" +textcolour+ " can assist you now, seek out " +personcolour+ "Dr. Minnick" +textcolour+ ". I wish you luck...'","You have betrayed The Order!",False),
    Enemy("Dr. Buijs","'I've been looking for you.'\n'I have a lot to tell you, but first we must test your loyalty.'\n'There is a traitor amongst the Eng Phys faculty!'\n'His name is " +personcolour+ "Chris" +textcolour+ " and he was last seen in the " +mapcolour+ "Tandem Accelerator" +textcolour+ ".'\n'Bring me what he has stolen!'",(None),(250,150,100),300,"voltage divider","capstone tools","'Ah you have returned.'\nYou sit down and listen to what " +personcolour+ "Dr. Buijs" +textcolour+ " has to say.\n'The Engineering Physics professors are part of an ancient council known as\nThe " +indicatecolour+ "Quantum Order" +textcolour+ "'\n'It is our duty to ensure the safety of this campus.'\n'It appears that your actions last night have stirred an evil\neven we don't understand.'\n'All that we do know is that some faculty members have been\ntempted by a Dark Lord with the promise of infinite knowledge.'  'A prophecy from a time long past has foretold that an adventurer's decisions\nwould dictate the future of the faculty.'\n'Perhaps it is you they spoke of. Keep that in mind as you consider your actions.'\n'See " +personcolour+ "Dan Fitzgreen" +textcolour+ " in the " +mapcolour+ "basement" +textcolour+ ".'\n'He has hatched a plan that may turn the balances in our favour.'","It is a voltage divider!",False),
    Enemy("Dr. Cassidy","'Yes, I was the one who sent you on this quest.'\n'My associates were no match for you, they did not have the strength to acquire the " +wincolour+ "Relics" +textcolour+ " for me.'\n'I know the " +indicatecolour+ "Quantum Order" +textcolour+ " has told you that the prophecy spoke of you bringing peace.'\n'You have been lead to believe the Order fights for what is just and fair.'\n'But you have been mislead.'\n'They only wish to keep the power of the " +wincolour+ "Quantum Relics" +textcolour+ " to themselves so that they\nalone decide the fate of the University.'\n'I only ever wanted to reveal the true power of Engineering Physics to the students.'\n'They thought my methods were unsafe.'\n'They thought the power I intended to reveal would pollute the minds of the students\nand cloud their judgement.'\n'The " +indicatecolour+ "Quantum Order" +textcolour+ " only wishes to suppress the true power we hold!'\n'They don't trust the students, they think they are incapable of managing the power I intended to give them.'\n'We are the premier stream and we deserve to rule McMaster as such!'\n'Join me, together we can harness the powers given to you by the oracles.'\n'With the " +wincolour+ "relics" +textcolour+ " we may enter the Shadow Realm and retrieve the deed to the university\nfrom the spirit of " +personcolour+ "Sir William McMaster" +textcolour+ ".'\n'We can then overthrow the " +indicatecolour+ "Quantum Order" +textcolour+ " and shape the university to our liking and\nfinally Engineering Physics will reign supreme!'\n\nJust as " +personcolour+ "Dr. Cassidy" +textcolour+ " finishes speaking the ground begins to shake and you are blinded\nby a glow emanating from the statue of " +personcolour+ "Sir William McMaster" +textcolour+ ".\nYou recover from shielding your eyes and see the spirit of " +personcolour+ "William McMaster" +textcolour+ "\nemerging from a rift in fabric of spacetime!\n'Just wait, hero.'\n'I took your " +wincolour+ "Iron Ring" +textcolour+ " from you after you desecrated my statue last night for a reason'\n'I have known of " +personcolour+ "Dr. Cassidy's" +textcolour+ " intentions for some time and as you are the one\nthe prophecy has spoken of I knew he would jump at this opportunity to take my deed.'\n'I had to find a way to force him into playing his hand.'\n'Now the opportunity to rid Engineering Physics of this tyrannical Dark Lord has come!'\n" +personcolour+ "Dr. Cassidy" +textcolour+ " quickly interjects.\n'You see, he only wants to restrict the power of our faculty!'\n'Destroy him and we shall finally rule the university!'",(None),(175,125,200),125,'iron ring',"","","" +personcolour+ "Dr. Cassidy " +textcolour+ "falls to the ground.\nThe spirit of " +personcolour+ "Sir William McMaster" +textcolour+ " approaches and puts his hand on your shoulder.\n'You have chosen wisely.'\n'" +personcolour+ "Dr. Cassidy" +textcolour+ " had been driven mad in his quest for ultimate power.'\n'You have ensured the safety of McMaster and remained true to your values.'\n'McMaster University is an institution meant to allow all facets of learning coexist in harmony.'\n'No faculty should rule over the rest.'\n'For your actions, I believe you are a worthy engineer.'\n'Here is your " +wincolour+ "Iron Ring" +textcolour+ ", continue to wear it with pride.'",False),
    Enemy("Dr. LaPierre","'Bring me a " +itemcolour+ "Coffee" +textcolour+ " please.\n I am rather tired.'",(None),(100,100,200),300,"Eng Phys USB pen","coffee","Here is a nice " +itemcolour+ "pen" +textcolour+ " for your troubles.\nGo find " +personcolour+ "Dr. Knights" +textcolour+ ", he has more for you to do.","I can't believe you've done this.",False),
        # ---  Aesthetic Highlighting - --
    Enemy("Dr. Nagasaki","'My grand invention is almost complete...'",(0,5,2,0),(100,100,100),75,"flux capacitor","ambifacient lunar waneshaft","'Yes!'\n'I have been looking for one exactly like that!'\n'Quicky, go to the basement of the Tandem Accelerator!'\n'The High Council is counting on you.'","NOOOO! NOW I WILL NEVER PLEASE THE DARK LORD!",False),
    Enemy("Dan Fitzgreen","Hello, although I've turned to the dark side to do Physics Labs\n I'm still a great guy. Did I mention I worked at CERN!?",(None),(100,75,100),400,"ambifacient lunar waneshaft","","'Been a lot stirring around the faculty since last night.'\n'I used to be an adventurous student like you before the High Council and I decided to part ways.'\n'I know what you seek and I am here to help.'\n'You need to fire up that old reactor in the basement of the Tandem Accelerator.'\n'It needs some sort of high power instrument to bring it to life...'\n'I think Dr. Nagasaki has been working on something like that, he is probably somewhere in ITB.'\n'He will likely need this...'","I'm moving to the physics department",False),
    Enemy("Kenrick","'The oscilloscope is the window into the electronic world.'",(3,3,1,0),(100,100,200),75,"Kenrick's oscilloscope",None,"","Oh no! My window! The Dark Lord will know I've failed him!",False),
    Enemy("Dr. Soleymani","'Are you interested in a research position?'",(0,1,2,0),(30,30,30),50,"Einstein's Brain",None,"","NOOO! The Dark Lord will never forgive me!",False),
    Enemy("Sir William McMaster","'You must rid the university of the evil Dr. Cassidy has planned!'",(None),(175,125,100),125,"iron ring","","","The spirit of Sir William McMaster bursts with a fiercely bright explosion.\nYou look down to see your Iron Ring as well as the deed to McMaster!\nDr. Cassidy quickly picks up the deed and turns to you.\n'Excellent!' he says coupled with maniacal laughter.\n'Too fulfill your true destiny, take the power you hold in your Iron Ring and destroy all of the rest of the Quantum Order!'\n'Only after they are gone can Engineering Physics truly reign supreme!'",False),
    Enemy("Chris","'The tools should be coming any day now.'",(4,5,1,0),(50,75,50),50,"capstone tools",None,"","I was going to quit anyway!",False),
    #Special
    Enemy("Brendan Fallon","What's up dude? I'm here to bless up your shit.\nDo you have my lunch box?",None,(9999,9999,9999),999,"green bang bong","Brendan Fallon's lunchbox","THANKS! TOKE UP MY DUDES!","",False),
    Enemy("Hooded Man","I've been looking for you. Especially after what you did last night.\nI recommend you seek out the profs if you are to find your ring...\nOnly they can right the wrongs you have done.",(5,4,1,0),(999,999,999),999,"iron ring",None,"","NO!!! HOW DID YOU KNOW IT WAS ME?",False),
    Enemy("yourself","Wait, but I'm you? Sorry I'm a little busy to think about this right now.",None,(100,100,100),100,"self worth",None,"","Congratulations, you've conquered yourself! It wasn't that hard!",False),
    Enemy("your dad", "Tell your mom the mower's fixed. I'm going to wash the lawn.", None, (250, 250, 250), 200, "crocs of the cartographer", None, "Let's rock & roll!", "At least I don't have to pay the mortgage!",True),
    Enemy("Alex Jones", "YOU THINK YOU'RE A TOUGH GUY. YOU'RE AN INTELLECTUAL DUMBASS", None, (300, 300, 300), 200, " ", None, "WE'RE GUNNA DEFEAT THIS ANTI-HUMAN SCUM. WE'RE GUNNA ROCK THEIR WORLD@", "I HATE YOU. COWARDDD!!!!",True),
    #Enemy("Special Man","I've been looking for you. Especially after what you did last night.\nI recommend you seek out the profs if you are to find your ring...\nOnly they can right the wrongs you have done.",(5,4,1),(999,999,999),999,"",None,"",""),
    #General
    Enemy("Liam the Gamer","I am NOT going to finish this assignment... if only I had one to copy.",(3,4,0,0),(10,10,10),15,"Swordfish","horrible assignment","Nice! Take this swordfish. I needed 45 cooking for that.","",False),
    Enemy("Connor the Biologist","I would really like a cricket to continue my research...",(1,7,3,0),(10,10,10),15,"PID control system","cricket","Thanks! I don't know what this does but you can have it!","'I can't believe you've done this.",False),
    Enemy("Father Frobenius","'You need prayer. Recharge at the altar.'",(2,0,1,0),(10,10,10),25,"crucifix",None,"","I am slain!",True),
    Enemy("Steven the first-year","'Have you got the LON-CAPA Python code?'",(3,6,1,0),(5,1,10),15,"engineering mug","LON-CAPA Code","Thanks man! Now I can get a 12 in at least 6 math courses.","I'm a failure at home and at school!",False),
    Enemy("Phil the drunk","'MHhmgh, Soouh whatu we getta druuuunk'",(5,5,1,0),(10,5,1),15,"coffee","phil's braces","'UHhhh i thinka im gonna- im gon-' Phil vomits. Thanks man, I'll buy you a coffee. I gotta go rock climbing!","mhmh spooky ghost urggh ectoplasm noooooo",False),
    Enemy("Jana the vegan","'Did I mention I'm vegan?'",(5,4,0,0),(15,1,5),10,"3w textbook",None,"","I was going to bring it back I swear!",False),
    Enemy("Larry the bus driver","'Is that even your bus pass?'",(2,1,1,0),(10,10,5),40,"huge shirt",None,"","That was definitely not your bus pass!",True),
    Enemy("Rod the bowler","'Righteous! Could you help me get into my car?\nI lost my keys and can't find my car.\nI REALLY need what is in there.'",(5,7,1,0),(14,20,5),40,"delicious meal","bowling ball","Thanks!\nNow I can learn to bowl that perfect strike.\nTake this, I just cooked it up.","Ouch!",False),
    Enemy("Brian the Weeb","'HAHA, you were a RIOT at the Phoenix last night! (\S)Also I'm really hungry, can you bring me a potato'",(2,2,1,0),(5,2,10),10,"brian's guitar","potato","THANKS MAN! I was super hungry.","That's not vegan.",False),
    Enemy("Mitch the TA","'Hey, I saw your picture on Instagram!'\n'They let you get away with doing that to the Willy McMaster statue?'",(0,3,1,0),(10,5,10),25,"phone",None,"","There's my phone.",True),
    Enemy("Erik the Sk8r","'Check out this tre flip, pretty tight eh? Also have you seen my drumstick?'",(0,0,0,0),(15,15,40),20,"Erik's frosted tips",'drumstick',"Aww thanks man! Here, you can have this!","Man, that's dumb!",False),
    Enemy("Megan the Bartender","'Wait... I recognize you... you have a $420E69 tab!'",(5,4,1,0),(15,20,10),20,"meow mix",None,"","Nuuuuuuuuuuuu",False),
    Enemy("Bill the MAC Cop","'Give me your student card!'",(3,5,1,0),(50,25,10),50,"solar cell",'student card',"","We aren't able to arrest you anyway!",False),
    Enemy("Stefan Boltzmann","Taste my lightning!",(None),(95,50,75),75,"pink donut",None,"","'I WILL GET YOU FOR THIS!'\nAs Boltzmann falls to the ground you notice the pink plasma desorb from his body.\nThe donut then floats in the mid-air and an apparition of Dr. Novog forms!\n'Whats up folks?'\n'The faculty is in big trouble, I need you to bring this energy source to the basement of the nuclear reactor.'\n'I will explain more then!'",False),
    Enemy("Zack the Snack","'I need a snack that smiles back!'",(2,4,0,0),(17,12,15),25,"fanny pack","goldfish","Whoa thats whack! Check out this fanny pack.","Why are you the way you are?",False),
    Enemy("Will the MAC Cop","'Give me your student card!'",(4,2,1,0),(50,25,10),50,"fake gun",None,"","We aren't able to arrest you anyway!",True),
    Enemy("Andreas the Nerd","'I heard some jebroni took the 3W Textbook and hid in Bridges cafe.'\n'Full send, dude!'",(3,2,1,0),(10,15,5),50,"visor glasses",None,"","Dude, that was definitely a full send",True),
    Enemy("Eric the Baller","'Huge talking to people play.'",(0,5,0,0),(20,15,20),50,"Cold Steel Katana",None,"","This is sub-optimal.",True),
    Enemy("Mario the Mixologist","'Yo check out my meme page, you ever heard coco jay?'",(1,4,1,0),(15,10,20),50,"stylish watch",None,"","si ya saben como consigo, por que me invitan?",True),
    Enemy("Paul the Janitor","'Hey brother, I really could use some Febreze.'",(0,5,1,0),(20,20,20),20,"bleach squirt bottle","Febreze","Rock on brother! Thanks so much!","NOOO, Now I can't go see Black Sabbath!",False),
    Enemy("Undead Grad Student","'Mussst eeaaat funnnndingg... Er, I mean braaains.'",(2,0,0,0),(20,10,1),20,"horrible assignment","einstein's brain","","My 12 year post-grad was for nothiiiiiingggggg!",False),
    Enemy("Daniel Parent", "Hi I'm amazing and Daniel", (3,4,1,0),(30,30,40),50,"STARS Wireless Fix",None,"Thanks!","FINALLY!",True),
    Animal("Fred the Good Boy", "You talk to Fred. His wise eyes stare at you. It's almost as if he understands what you're saying but he'd rather have have you play with the ball.", (0,0,0,3),(9999,9999,9999),9999,"tennis ball","tennis ball","Fred barks happily. He chews on it for a second and then kicks it back happily to you.","","He smiles at you happily! His tail wags but you can tell he just wants to play with the ball.",True),
    Enemy("Nicole the Assistant", "Hi! Welcome to the Engineering Physics Office. What can I help you with? Dr. Lapierre should be just across the tunnel in ABB if you're looking for him.", (1, 5, 2, 0),(15,30,15),40,None,None,"","NO! Did I send you too many emails?",True),
    Animal("Liam the Library Dog","You talk to Liam and it seems to help. Maybe this theropy stuff does work.",(4,0,1,0), (9999, 9999, 9999), 9999, None, None,"", "","Liam cuddles beside you while you scratch/pet him. He's really good at his job.",True),
    Enemy("Devan the most Unhelpful", "You ask Devan if he knows anything about your " +itemcolour+ "iron ring" +textcolour+ ". (\S)He says: 'How'd you hear about this? What did the " +indicatecolour+ "quantum order" +textcolour+ " tell you? We can't speak here, come meet me in " +mapcolour+ "JHE Basement" +textcolour+ ".'", (1,3,1,0), (25, 25, 25), 50, None, None,"", "I WASNT'T GOING TO GIVE YOU A GOOD MARK ANYWAYS!", False),
    Enemy("Hannah the Helpful", "Hey are you okay after what happened at the " +mapcolour+ "Phoenix" +textcolour+ "? Do you need help?", (1,4,2,0), (25, 25, 25), 50, None, None,"", "No! How am I going to make a great capstone now!", True),
    Enemy("Matt the Vuk", "Man you're crazy haha. I wouldn't be walking after what you did at the " +mapcolour+ "Phoenix" +textcolour+ ".",(4,4,1,0), (25, 25, 25), 50, None, None, "", "Now how am I supposed to be the ultimate Eng Phys guy?", True),
    Enemy("Arthur the D'art","Even though I'm in seven courses right now I'd love to talk!",(5,3,1,0), (25, 25, 25), 50, None, None, "", "At least it's better than Eng Phys!",True),
    Enemy("Angus the Barber", "He's dressed in a pirate costume and saying: 'Four FOURS!'", (0,7,1,0),(25, 25, 25), 50, None, None, "", "You'll spend an eternity on this ship!", True),
    Enemy("Neil the Man", "Neil is quietly studying with his headphones on. Best not to disturb him.", (3,4,0,0),(50, 50, 50), 75, None, None, "", "Well this is better than 2P with Phil!", True),
    Enemy("Keara the Mera", "Hey! Aren't you the guy that ruined the " +mapcolour+ "McMaster statue" +textcolour+ " last night?", (5,0,1,0),(25, 25, 25), 50, None, None, "", "Why would you do that!?", True),
    Enemy("Dawson the Tie Dye Guy", "Sa dude! These psychedelics rock!", (0,4,1,0),(25, 25, 25), 50, None, None, "", "Dudeee, why?", True),
    Enemy("Danya the Daniel", "Don't bug me I'm studying. No quests please. I would love something vegan to eat though.",(1,1,1,0),(25,25,25),50,"flashcard","tofu","Oh thanks! I'll need this later!","Veganism is the moral baseline!",False),
        # --- Haunted Forest People ---

    Enemy("Little Girl", "Hi, I think I'm lost... (\S)Have you seen my mitten?", (0, 0, 0, 4), (10, 10, 10), 10,"ring pop", "old mitten",
              "Oh thank you! That is my mitten. (\S)Here, take my candy. It is the only way I can thank you. BYE!",
              "AHHH Nooooo, why would you kill a little girl?",False),
    Enemy("Hiker","'Make sure you watch out for that crazy guy deeper in the woods...' (\S) 'I am pretty sure he has an axe that controls this forest somehow.' (\S)'He never leaves his cabin without it unless you could somehow get him out of there in a hurry...'",(9,5,0,4),(25,10,10),50,
          "trail mix",None,None,"NOO MY TRAIL MIX! Why would you kill an innocent hiker?",True),
    Enemy("Shady Guy", "'Hey, you got any suckers?' (\S)'Something sweet maybe?'", (1, 4, 0, 4), (25, 15,20), 40, "matches", "ring pop", "'Hey thanks!' (\S)'Maybe you can use this to make a fire while you're out here in these creepy woods...'", "'Why would you kill me! I did not want to be killed!'",False),
    Animal("Wolf", "You talk at the wolf but it just stares at you blankly.", (9, 3, 0, 4), (15, 15, 50), 20, "Wolf Meat", None, None, "ARRRROOOOOOOOOO!","You would pet the wolf but it's kinda scary. It might bite you!",True),
    Animal("Small Squirrel", "You talk at the small squirel but it doesn't respond. Are you going insane?",(7,4,0,4),(5,5,30),10,"small squirrel meat",None,None,"It didn't put up much of a fight.","You put your hand out and the squirrel climbs up your hand! You play with it for a bit before carying on",True),
    Animal("Big Squirrel", "You yell at it 'YOU'D MAKE A TASTY MEAL'. It doesn't seem to mind.", (4, 7, 0, 4), (5, 20, 30), 10, "big squirrel meat", None, None, "Thicc boi didn't put up much of a fight...","You put your hand out and the squirrel climbs up your hand! You play with it for a bit before carying on",True),
    Enemy("Elderly Man", "'Oh hi there young one!'(\S)'My eyes aren't like they used be...' (\S)'My life spent in the mines may have taken its toll.' (\S)'I have this note here that I would love to be able to read if only I had my glasses...'",(8,0,0,4),(20,10,5),45,"old pickaxe","aged glasses","'Oh thank you!' (\S)'Let me read this note I have here...' (\S)'Equal parts sulfur and charcoal makes a good boom with some high heat.' (\S)'Hmmm whatever that means... Here take this old pick! (\S)'I dont have any use for it.'","'Nooooo! Why would you kill an old man??'",False),
    ]

    #Stationary Objects to interact with
    #Interact(name,location,info,Sinfo,need,drop)
    INTERACT1 = [
    #Interact("Attack Fan",(1,1,1),"It's a garbage can.","You throw the MSP430 in... Yes, you have chosen wisely.","msp430","Vomit"),
    Interact("Garbage Can",(2,3,1,0),"It's a garbage can.","You throw the MSP430 in... Yes, you have chosen wisely.","msp430","Vomit",False),
    Interact("Broken Reactor",(4,5,0,0),"It's an old broken reactor.","After some elbow grease and a bit of luck you manage to complete the reactor.\nThere is a low whirr as the device starts and begins to glow with a\npink hue.\nSuddenly, you hear the door crash open behind you!\nDr. Kleimann enters in a hurry.\n'Finally, the power I need!' he says as he rushed past you and reaches for the glowing plasma.\nThe plasma appears to bend to his will and is absorbed by his outstretched hand!\n'I AM COMPLEEEEEEEEETE!' he bellows in a demonic tone.\n'You fool, did you not recognize the deliberate mispelling of this mortal's name?'\n'Two n's? That is a characteristic of a name fit for a physics GOD!'\n'It is I, "+personcolour+"STEFAN BOLTZMANN"+textcolour+"! And you have given me the power I need to free myself\nfrom this mortal form!'\nAfter glowing, levitating, and transforming... "+personcolour+"Stefan Boltzmann"+textcolour+" lunges at you!","flux capacitor",None,False),
    Interact("Fridge",(1,6,0,0),"Seems like a regular fridge to me.","You inspect the inside of the fridge to reveal a small keyhole.\nUpon inserting and turning the key you hear a robotic voice bellow.\n'WORMHOLE ACTIVATED'\nThe compartment bursts open and out flies a book!",'relativistic key','Pedrotti cubed',False),
    Interact("Optical Bench",(1,6,0,0),"Dr. Haugen's personal optical bench...","You place Dr. Haugen's femtosecond laser on the bench and aim it at the fridge.\nTurning the laser on (remembering your laser safety glasses, of course)\nfires the high-intensity beam at the fridge.\nThe room begins to shake and smoke begins to billow out of the cracks of the fridge.\nThe door swings open and a glowing apparition of Albert Einstein emerges!\n'You have come a long way, but your quest is not yet over.'\n'For there still remains a great evil on this campus'\n'Dr. Haugen was entrusted with protecting the contents of my fridge.'\n'I have known of your destiny since your first year here at McMaster.'\n'You will be the one who determines the fate of the faculty.'\n'It is, therefore, my responsibility to prepare you for what lies ahead.'\n'This key opens a compartment in my fridge which holds one of three Quantum Relics.'\n'These items give the holder the power to shape the fate of the entire university.'\n'I cannot tell you much more. Perhaps I have said too much.'\n'Take this. Good Luck.'","femtosecond laser","relativistic key",False),
    Interact("Old Painting",(3,0,1,0),"An old oil painting of the founding fathers of McMaster.\nDated:April 20th, 1887","Through Dr. Minnick's glasses a glowing green inscription is revealed!\n'In the hall where we eternally meet,\nThe second clue lies beneath your feet.'\nWhile reading the secret message Dr. Minnick's glasses get increasingly hotter and you quickly swat them off your face.","Minnick's glasses","Minnick's glasses",False),
    # TODO Make all these interactables into items and fix anything that breaks with quests.
    Interact("Old Lamp",(5,1,1,0),"It appears the hole was caused by some sort of laser...","","","",True),
    Interact("Red Car",(0,6,1,0),"A red Dodge Avenger...\nPeering into the window you can't really see much.","",None,None,True),
    Interact("Blue Car",(0,6,1,0),"A blue Ford Mustang...\nPeering into the window you can't really see much.","You smash open the window with the tire iron, breaking it in the process.\nYou unlock and open the door...\nTo reveal a potato.","tire iron","potato",False),
    Interact("Old Car",(0,6,1,0),"An old Datsun...\nPeering into the window you can't really see much.","You open the door of the old car. You try the starter... (\S) (\S)Dead. Nothing much in here besides junk.",'old car keys','rubber chicken',False),
    Interact("New Car",(0,6,1,0),"A new Volkswagen...\nPeering into the window you can't really see much.","You open the car and rummage around.\nUnderneath one of the seats you find a bowling ball!","car keys","bowling ball",False),
    Interact("RCA TV",(5,6,1,0),"Old RCA TV with VHS slot...","You put the VHS into the slot and press play...\nYou watch Disney's 1999 Tarzan and soak up all the nostalgia you can. This is definetly better than finding your ring.","Tarzan VHS","",False),
    Interact("Red Book",(4,0,1,0),"It's a guide to living outdoors. (\S)Flipping through the pages you read: (\S)'Hedysarum alpinum also known as the greenberry is characterized by it's lateral veins.' (\S)'If ingested, casues immediate starvation and death.'","","","",False),
    Interact("Blue Book",(4,0,1,0),"It's a biology textbook. (\S)Flipping through you read: (\S)'The mitochondria is the powerhouse of the cell.'","","","",True),
    Interact("Old Journal",(6,1,0,0),"You blow the dust off, open it, and read:\n'The ability to peer into history would be a most formidable power.'\n'I have potentially produced a piece of the puzzle but without a\n'device capable of maintaining the field density long enough I fear\n'it will never become a reality.'\n'Thus I have decided to hide my invention until the time comes where\nsomeone can realize my dream.'\n'If you are reading this, find the place where you can see\ncampus in its entirety.'(\S)'If you ARE the hero, the next steps shall be revealed.'(\S)-M. Faraday","","","",False),
    #Interact("Box of old CDs",(2,4,0),"It's a dusty box of old CDs...","You insert one of the CDs into the monolithic computing device...\nThe laptop instantly blue-screens and bursts into flames.","lenovo laptop",None),
    Interact("Display Case",(1,6,1,0),"It's a display case full of all sorts of old-time Engineering Physics wizardry.","The rusty key fits perfectly!\nAs you turn the key glowing square forms on the back\nof the display case and opens revealing an old relic...","rusty key","Faraday's Cage",False),
    Interact("SharpXChange",(0,1,1,0),"Would you like to exchange a needle?","Needle Accepted!","dirty needle","clean needle",False),
    Interact("Sun Dial",(3,2,1,0),"You can't even tell time on an analog clock.\nHow are you supposed to use this?","Through Dr. Minnick's glasses, you see a green glowing handprint appears\non the face of the sundial!\nYou place your hand on it and a compartment opens.","Minnick's glasses","rusty key",False),
    Interact("Rules Sign",(2,3,1,0),"It reads: (\S)THERE ARE NO RULES","","","",False),
    Interact("McMaster Map",(1,2,1,0),
             "It's the map of McMaster.'(\S) ________________________________________________(\S)|Map of McMaster                                 |(\S)|                                       BATES    |(\S)|                                                |(\S)| ETB        JHE         BSB                     |(\S)|                                                |(\S)|                                      STATUE    |(\S)|                                                |(\S)| HOSPITAL                                       |(\S)|          MDCL         CHAPEL              MUSC |(\S)|________________________________________________|"
             ,
             "Through Minnick's glasses the true map is revealled!(\S)You read:'Harness the sun.'(\S) ________________________________________________(\S)|Map of McMaster                                 |(\S)|                                       BATES    |(\S)|                                                |(\S)| ETB        JHE         BSB                     |(\S)|                                                |(\S)|                        \/            STATUE    |(\S)|                        /\                      |(\S)| HOSPITAL                                       |(\S)|          MDCL         CHAPEL              MUSC |(\S)|________________________________________________|(\S) (\S)Dr. Minnick's glasses glow hot as you quickly swat them off of your face."
             ,"Minnick's glasses","Minnick's glasses",False),
    Interact("Workbench",(1,7,0,0),"Looks like an old dusty workbench.","",None,"",True),
    Interact("Lenovo Laptop",(2,4,1,0),"This heap of computing majesty could block bullets... I think...","You plug in the Eng Phs USB Pen.\nYou find all of 2P04 files, who uses FlexPDE anymore? You also find a \nweird exe called the Eng Phys Text Adventure! That sounds like fun.\nYou hear a drumming in your ears, is that coming from the pen?","eng phys usb pen","",False),
    Interact("Mouse",(1,0,3,0),"It's a mouse scurrying around...\nDid it just stare at you?","The mouse rushes over and takes the cheese.\nIt runs into a small opening it has made in the roof of the building.\nIt returns with something in it's mouth!","cheese","gilded blunderbuss",False),
    Interact("Tri-Coloured Glasses",(6,1,2,0),"Looks like a set of glasses with multiple coloured lenses...","Its a cipher...\nOn the back of the declaration you can see different coded messages using the coloured lenses...\n'1.Lithium Carbon Boron Magnesium(-g) '2.BLUE:'Jerry likes presents.' '3.Guardians of De Galaxy character.'","declaration of independence",None,False),
    Interact("Uneven Earth",(3,7,1,0),"This patch of dirt looks out of place...","You begin digging and find an old box!\nYou open it up and read a note...\n'In the eldest of halls. The attic holds all.'","shovel","declaration of independence",False),
    Interact("Coat of Arms",(3,3,1,0),"Under closer inspection you notice the book is a different kind of stone\nthan the rest...\nIf only you could get up there for a closer look...","With some effort you climb the rickety ladder and remove the book from the wall.\nReaching into the hole you pull out an old scroll!","old ladder","old scroll",False),
    Interact("Ancient Mirror",(4,0,0,0),"It's an old mirror from a time long past.","You mutter the incantation... Suddenly, you see the reflection of Richard Feynman himself standing behind you!\n'You have come a long way. The way of the physicist is strong with you.'\n'Here, take this it is one of the 3 Quantum Relics.\n'You will need all 3 to acquire your Iron Ring.'\n'Trust your instincts and when the time comes you will know what to do.","ancient incantation","gamma glove",False),
    Interact("Pack-a-Punch", (None), "Punch your fists into the air and raise a rebel yell! (\S)"
             "There's a lots of bad'uns out there you need to send to hell!" ,
             "Pack-a-Punch Machine:(\S) To use this machine enter your item and another to sacrafice. Depending on the relative stats of the sacrifice, the stats of the upgrade will double or have the sacrifice added to them.",None, None,False),
    Interact("Lake Painting", (3, 0, 1, 0), "A painting of a beautiful lake. It brings you peace.", "You feel a pull. All of a sudden you're being pulled into the painting and all around you it's getting bright. (\S)You wake up to the sound of birds chirping and a soft breeze.", "old car keys", None,True),
    Interact("Portkey", (0, 0, 0, 3), "This portkey looks like the way back. Whatever magic brought you here must be related to this lake.", "Your world compresses as you're pulled violently into something. (\S)You're back in the Art Museum. Were you ever gone?", None, None,True),
    Interact("Rick's Crafting Bench", (0, 0, 0, 3), "This bench can create anything made of wood or diamond.","You spend hours crafting the device to the precision you need. It's perfect.","softwood 2x4 stud", "sharpxchange",True),
    # --- Aesthetic Interacts ---
    Interact("Iron Ring Statue", (2,3,1,0), "The beautiful statue shines in the light. 'From the Class of 2017'. It reminds you of your lost ring, which you remember you should go find.", "", None, "", True),
    Interact("Morning Sun", (2,3,1,0), CLEARSCREEN+"You stare at the sun for an hour. You're practically blind now and can't remember what you were doing before." , "", None, "", True),
    Interact("Kipling Game", (2,4,1,0), "It's a laser pointer arcade game. Wow this is fun. And it counts your score! How did they have time to make this?", "", None, "", True),
    Interact("Kipling Clock", (1,4,1,0), "Days to Kipling: 364 until that next fateful day. Hopefully there's no one in your situation next year.", "", None, "", True),
    Interact("Armchair", (1,1,1,0), "It looks comfortable at first but it's really not. Do they really expect you to do work in these things?", "", None, "", True),
    Interact("Organ", (2,0,1,0), "A hammond B3 Organ. A fine specimen.", "", None, "", True),
    Interact("Dirty Coffee Table", (3,1,1,0), "A very boujee coffee table display art piece. You don't want to tell the art students how you really feel about this.", "", None, "", True),
    Interact("Willy dog cart", (4,1,1,0), "The man in the cart eyes you warily as you ask for your 5th hotdog of the day. You hand him a fiver and walk away.", "", None, "", True),
    Interact("McMaster Statue", (5,2,1,0), "There are marks of defilement all over the statue. You wonder if this has anything to do with the happenings of last night?", "", None, "", True),
    Interact("Canadian Flag", (3,2,1,0), "This majestic flag waves gracefully in the wind. Canada and proud. ", "", None, "", True),
    Interact("Slackline", (2,2,1,0), "You attempt to walk across this but you don't have the coordination or skill. Practice makes perfect.", "", None, "", True),
    Interact("Reactor Pool", (2,6,1,0), "The blue pool of the McMaster Nuclear Reactor (MNR). Swimming is not advised.", "", None, "", True),
    Interact("No Access Sign", (4, 3, 1, 0), "You read the sign which definitely says 'no vehicle access' and wonder how it could ever be misinterpreted...", "", None, "", True),
    Interact("Water Fountain", (0, 1, 1, 0), "You take a big gulp of Hamilton's finest filtered dihydrogen monoxide... yum", "", None, "", True),

    # --- Haunted Forest Expansion ---
    Interact("Gap in the Trees",(3,7,1,0),"It is a gap in the trees... a path is barely visible. (\S)It might be best to get a better idea on how to survive out there before trying to take on the trail.","",None,None,False),
    Interact("Opening in the Trees",None,"With your knowledge you can now travel through the forest.","You push your way through the brush and after a while you lose track of where you entered from...",None,None,False),
    Interact("Trail to Cootes Drive",(4,0,0,4),"What was that place?","You push your way through the brush and after a while you make it to Cootes Drive...",None,None,False),
    Interact("Sulfur Deposit", (0, 4, 0, 4),
                 "It appears to be a sulfur deposit. (\S)If only you had a way of mining this...",
                 "You swing your pick at the rock. (\S)After some time, a fine sulfur power forms on the surface. (\S)You have no way of collecting it so perhaps you may need to bring whatever you want to work on here...",
                 "old pickaxe", "mined sulfur deposit",False),
    Interact("Mined Sulfur Deposit", None,
                 "It appears to be a mined sulfur deposit. (\S)A powdery residue is on the surface. (\S)You should bring the other required ingredient here...",
                 "You mix some of the charcoal and sulfur dust together making a rudimentary version of gunpowder.",
                 "charcoal", "gunpowder",False),
    Interact("Tree Carving", (1, 8, 0, 4),"Upon closer inspection it reads: (\S)The man of the woods hates loud noises. (\S)He came running after my friend's and I set off a firework. (\S)I managed to esca- (\S)The note abruptlet ends and you notice a blood stain further down the tree.","",None,None,True),
    Interact("Dead Deer", (2, 8, 0, 4),"Poor thing... (\S)Looking closer you notice the wounds are not jagged like an animal would inflict. (\S)They are sharp and clean...","", None, None,True),
    Interact("Empty Soda Can", (3, 9, 0, 4), "It is an empty soda can... what could you possibly do with that?","You fill the can with gunpowder. (\S)This would surely make a boom if you could get it hot enough...","gunpowder", "makeshift explosive",False),
    Interact("Slashes", (5, 8, 0, 4),
                 "Some slahses are jagged and wild whereas others are clean and sharp... (\S)It almost looks as something was clutching the tree before being torn away from it.",
                 "", None, None,True),
    Interact("Stump", (7, 8, 0, 4),
                 "This looks like a stump someone has used to cut logs on. (\S)Whoever has been swinging this axe must be strong as it has been nearly beaten to a pulp!",
                 "", None, None,True),
    Interact("Animal Skeleton", (9, 7, 0, 4),
                 "A nearly complete skeleton. (\S)The animal isn't identifiable but it is about the size of dog. (\S)The head has been removed and the bones licked clean...",
                 "", None, None,True),
    Interact("Note on Tree", (6, 4, 0, 4),
                 "It is a note nailed to the tree... it reads: (\S)THIS IS MY FOREST AND I AM NOT AFRAID OF PROTECTING IT. (\S)THOSE WHO HAVE NO RESPECT FOR THIS TRANQUIL PLACE WILL BE HUNTED DOWN. (\S)MY SENSE OF HEARING IS PERFECT AND IF I HEAR ANY TERROSIM IN MY FOREST... (\S)IM COMIN'",
                 "", None, None,True),

    Interact("Smouldering Firepit", (9, 4, 0, 4),
                 "It is a firepit. Recently died so still warm (\S)Perhaps if I wanted some warmth I should get a log in here.",
                 "Will all your might you break the log in half and place it in the pit. (\S)Now you need a means of making sure the fire starts quickly and easily.",
                 "log", "firepit with log",False),
    Interact("Firepit with Log", (None),
                 "The fire is nearly ready to light. All we need is some kindling.",
                 "You add kindling to the firepit. (\S)Now it should start easily with the help of a source.",
                 "kindling", "lit firepit",False),
    Interact("Lit Firepit", (None),
                 "You put the kindling inside. It catches quickly and the after some time the fire roars to life. (\S)After some temporary day-dreaming by the fire you notice embers start to form at the base with a yellow-hot glow.",
                 "You throw in the makeshift explosive and run away quickly. (\S)3... 2... 1... you count. (\S)BOOOM (\S)The makeshift explosive goes off brilliantly (\S)In the distance you hear a loud slam followed by a bellowing roar. (\S)'IM COMIN' you hear echo through the woods.","makeshift explosive",None,False),

    Interact("Worn Chest", (1, 1, 0, 5),
                 "A dust covered chest... (\S)However the keyhole seems polished and hand prints are visible on the top of the chest.",
                 "The small key fits perfectly. (\S)With a slight turn a loud click is heard. (\S)You swing the lid of the chest open to reveal the Woodsman's Axe!",
                 "small key", "woodsman's axe",False),
    Interact("Dusty Couch", (0, 0, 0, 5),
                 "A dusty couch where one side is clearly worn more than the other. (\S)Cookie crumbs are everywhere.",
                 "", None, None,True),
    Interact("Nature Painting", (0, 0, 0, 5), "It is an old oil painting of the Fitzroy in Patagonia.", "", None,
                 None,True),
    Interact("Note on Desk", (1, 1, 0, 5),
                 "You pull the note off the table to read: (\S)'More noises out there in my forest...' (\S)'These city folk need to stop ruining the environment with their loud noises and rappity hippity hop.' (\S)'I came across a group of hikers disturbing the growth rate of the forest with their loud music.' (\S)'I was sure to take care of them...' (\S)'Another offering to Quaorke the tree god.'",
                 "", None, None,True),
    Interact("Cast-Iron Furnace", (0, 0, 0, 5),
                 "The glow from within is bright... you warm up next to it for a moment. (\S)Someone was clearly tending to this before leaving in a hurry. (\S)You notice the door screwed to the front of the furnace is conveniently about the size of your chest...",
                 "With some work you manage to unscrew the door and it clunks to the ground. (\S)Some nearby twine fits through the loops and you fashion a makeshift chestplate!",
                 "screwdriver", "furnace door",False),

    Interact("Deep Firepit", (3, 8, 0, 4),
                 "This firepit looks deep but recently used... If you wanted one of the charcoals you would need something to reach down that far.",
                 "You bend over the edge and reach down using your stick to extend your reach. (\S)You are barely able to pull up a decently sized charcoal from the pit. (\S)You drop the stick in the process... ooops.",
                 "fireplace tongs", "charcoal",False),
    Interact("Gate of the Forest", (0, 7, 0, 4),
                 "An impenetrable gate formed out of the forest itself. (\S)If only you had a way of cutting through this.",
                 "You raise the axe and prepare to swing it at the gate. (\S)With a thwack a limb extends from the forest above and wraps around your wrist! (\S)Frozen in place, the tree removes the axe from your grasp and pulls it over to the gate. (\S)The branches which make up the gate move until an axe shape is formed. (\S)The axe fits perfectly in the space and begins to glow. The glow intensifies until you are forced to shield your eyes. (\S)Once the light finally dims you look are astonished to see the gate is gone!",
                 "woodsman's axe", None,False),
    Interact("Stone Pedestal", (0, 6, 0, 4),
                 "You read the note: 'You have proven yourself in the Forest. Take this power and these gifts.' (\S)'Before you lies two staves of equal power but different use.'  (\S)'Feel free to use the escape rope to return to the point from which you came.'",
                 "", None, None,False),
    Interact("Escape Rope", (0, 6, 0, 4), "", "", None, None,False),
    Interact("Cookie Jar", (1, 0, 0, 5), "It is a cookie monster cookie jar sealed tight!",
                 "You swing the rusty hammer at the cookie jar and with a crash it shatters everywhere! (\S)Within the broken cookies and ceramic shards you spot a small metallic key.",
                 "rusty hammer", "small key",False),
    Interact("Old Fridge", (1, 0, 0, 5),
                 "This thing hasn't been plugged in for some time... (\S)It is clearly used as a storage space rather than a refrigerator.",
                 "You swing open the door to reveal some pretty rancid stuff. (\S)Most of it is something stored in vinegar which barely looks appetizing.",
                 None, "jar of olives",False),
    Interact("Cutting Board", (1, 0, 0, 5),
                 "Well worn. (\S)The blood stains and knife marks on this thing are serious... (\S)Someone clearly has a heavy hand and a taste for red meat.",
                 "", None, None,True)
    ]

Reset()

# TODO If Rebuild: Make this into a dictionary with an adjacency list (Graph/path). Not sure if in object or not
def WorldMap():
    global MAPS1
    global LOCATIONS1
    global ENEMIES1
    global ITEMS1
    for i in LOCATIONS1:
        position = i.location
        x = position[0]
        y = position[1]
        z = position[2]
        dim = position[3]
        MAPS1[x][y][z][dim] = i
    for i in ENEMIES1:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            dim = position[3]
            MAPS1[x][y][z][dim].placeEnemy(i)
        else:
            i.location = (None,None,None,None)
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
            dim = position[3]
            MAPS1[x][y][z][dim].placeItem(i)
        else:
            i.location = (None,None,None,None)
    for i in INTERACT1:
        if i.location:
            position = i.location
            x = position[0]
            y = position[1]
            z = position[2]
            dim = position[3]
            MAPS1[x][y][z][dim].placeItem(i)
        else:
            i.location = (None,None,None,None)
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

