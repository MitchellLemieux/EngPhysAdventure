"""This function is used as our special printer to define the width and timing of lines.
It was made so that you wouldn't have to manually add newline characters to keep text alined
but also to enable spacing and other functions with words.
It actually removes any \n or newlines from the text. Adding them to the lore won't make any problems but they will
just be ignored if using this function.

"""
#Try to implement in non-annoying way, like for slow for enemy special & death info and lore but
    #fast for all other things (like 0.1-1 seconds)
    #and make sure it's disableable through speedrun and a special options
#seems to skip at LAST ONE OH BECAUSE THERE"S NO DELAY :)
import time
import re

# Having custom game settings for printT won't work for final release either because like Colours.py, PrintT is a fundamental module


def escape_ansi(line):  # used to remove ansii escape codes
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)
from Colour import coloursusedlist


#in the settings can define user reading speed (even calibrate with a testing module)
    #and can define their window character size (small-med-large) for text reading
# TODO put delay back to 2.0 seconds before game release
# TODO Make an alignment option so can align to left, centre, or right side of screen
def printT(text, char=72, delay = 2): #3 second delay seems to be optimal new reading speed for me, 2 kinda fast and 4 kinda slow
    """TIPS: Use (\S) for newline & resets paragraph, (\S) (\S) for space with pause, paragraph every punctuation 5 marks 
    This function removes newlines from our old text then prints out each line to the chacter limit and with delays inbetween
    Can override parser to make newline split using (\S). Use (\S) (\S) to split and make a blank space with a delay, resets the sentence variable
    It also splits into paragraphs every 5 punctuation marks (.,!,?) so try to avoid those
    See examples and comments for more details
    """#these are docstrings for function, which come up on idle

    # If speed run is enabled this will override the text delay and make it 0 for all outputs
    from GameFunctions import GAMESETTINGS,GAMEINFO  # Imports game settings, hopefully to avoid import problems
    if GAMESETTINGS['SpeedRun'] or GAMEINFO['devmode']:  # If either mode there is no text delay
        delay = 0
    
    # print "="*char #reference width of screen
    # removes newlines from the string and replaces it with spaces, if there's a newline at the start it removes it
    intext = text.replace('\n', ' ').lstrip().rstrip()

    # this is the custom phrase parser that splits at the right width. Probably not optimal but works and okay fast
    intext =  intext.split(" ")  # splits up input text into a list of words (using spaces)
    phrase = ""  # phrase accumulator to be separated and printed on a separate line after reaching the page width
    sentence = 0  # Paragraph counter. counts number of sentences to split via paragraphs

    for word in intext:  # loops through words in sentence list
        if (("." in word) or ("!" in word) or ("?" in word)) and (not("dr." in word.lower())): sentence += 1 #if a punctuation is in word it counts as a sentence (so try to avoid .,!,? for other uses)
        phrase = phrase + word  # adds new text phrase with no space
        lenphrase = len(escape_ansi(phrase))  # this gets the actual length of the phrase without ansii escape codes (colours)
        if ("(\S)" in word): #uses (\S) to custom deliminate spaces, should be before others are is the master short. Use of (\S) is arbitrary, can be any uncommon characters
            phrase = phrase.rstrip(word) #removes the last word from the phrase
            word = word.split("(\S)") #splits it over the delimter, so it can split right at the "(\S)", by making it a list of the last word of the phrase and start of new one
            phrase = phrase + word[0] #adds the final part of the phrase
            print(phrase)
            time.sleep(delay)
            if word[1].rstrip() == "": word = "" #if it's just a space it sets it to an empty string so it doesn't add an extra space
            else: word = word[1] + " " #Adds space to remaining word because it will skip over space addition to avoid double space case
            phrase = word #starts new phrase with the remainer word only, removes space if it's a space
            sentence = 0 #resets paragraph  counter
            continue
        elif sentence == 5: #if end of a paragraph (5 puncuation marks) it will split. Should be before character check for rare case where peroid is at the exact end of 5 sentences
            print(phrase + "\n") #prints phrase with a space inbetween for new pharagraph
            time.sleep(delay) #adds delay after to allow user time to read
            phrase = "" #resets phase
            sentence = 0 #resets the sentence counter for new paragraph
            continue #returns the loop back to the top of the loop so it doesn't add the space at the start of the next phrase
        elif lenphrase == char: #if the phrase has accumulated to JUST the right size it will split
            print(phrase) #see above
            time.sleep(delay)
            phrase = "" 
            continue 
        elif lenphrase > char : #if phrase is just over the length with next word it removes last word and prints
            phrase = phrase.rstrip(word) #removes the last word added to phrase from phrase
            print(phrase)
            time.sleep(delay)
            phrase = word #resets phrase with current word variable
        phrase += " "  # adds inbetween space after word is sucessfully added
        
    print(phrase.lstrip().rstrip())  # prints the final part of the phrase that doesn't evenly fit in so wasn't split
    time.sleep(delay/2)  # final delay but half speed b.c. half text?

###Examples###
""" #These comment out multiple lines of code using text, won't compile so is bassically a multiline comment
printT("\nYou see the Iron Ring out front of JHE shining in the morning sun.\nThe campus is bustling with student life.\nThere are people heading in all directions with Kipling pranks\nstill scattered about JHE.",72)
    #Is the default print every 72 characters with 3 second delay
printT("Dogs are I best",5,0)
    #splits sentence every 5 characters with no delay
printT("'Yes, I was the one who sent you on this quest.'\n'My associates were no match for you, they did not have the strength to acquire the Relics for me.'\n'I know the Quantum Order has told you that the prophecy spoke of you bringing peace.'\n'You have been lead to believe the Order fights for what is just and fair.'\n'But you have been mislead.'\n'They only wish to keep the power of the Quantum Relics to themselves so that they\nalone decide the fate of the University.'\n'I only ever wanted to reveal the true power of Engineering Physics to the students.'\n'They thought my methods were unsafe.'\n'They thought the power I intended to reveal would pollute the minds of the students\nand cloud their judgement.'\n'The Quantum Order only wishes to suppress the true power we hold!'\n'They don't trust the students, they think they are incapable of managing the power I intended to give them.'\n'We are the premier stream and we deserve to rule McMaster as such!'\n'Join me, together we can harness the powers given to you by the oracles.'\n'With the relics we may enter the Shadow Realm and retrieve the deed to the university\nfrom the spirit of Sir William McMaster.'\n'We can then overthrow the Quantum Order and shape the university to our liking and\nfinally Engineering Physics will reign supreme!'\n\nJust as Dr. Cassidy finishes speaking the ground begins to shake and you are blinded\nby a glow emanating from the statue of Sir William McMaster.\nYou recover from shielding your eyes and see the spirit of William McMaster\nemerging from a rift in fabric of spacetime!\n'Just wait, hero.'\n'I took your Iron Ring from you after you desecrated my statue last night for a reason'\n'I have known of Dr. Cassidy's intentions for some time and as you are the one\nthe prophecy has spoken of I knew he would jump at this opportunity to take my deed.'\n'I had to find a way to force him into playing his hand.'\n'Now the opportunity to rid Engineering Physics of this tyrannical Dark Lord has come!'\nDr. Cassidy quickly interjects.\n'You see, he only wants to restrict the power of our faculty!'\n'Destroy him and we shall finally rule the university!'",72,0.1)
    #splits this big chunk of text into paragraphs correctly with 0.1 second delay
printT("Please stop the sentence here.(\S)I repeat please stop it here!")
    #Split in the middle of a phrase through (\S)
printT("Please stop the sentence here.(\S) (\S)I repeat please stop it here!")
    #Split in middle of phrase with a space and delay inbetween
"""
#Aside
#Be careful where you place these multiline "comments" in code
#Strings following right after function signature, a class definition, or at the start of the module do get compiled as a docstring

#McMaster Map
#print "Through Minnick's glasses the true map is revealled!\nYou read:\n'Harness the sun.'\n ________________________________________________\n|Map of McMaster                                 |\n|                                       BATES    |\n|                                                |\n| ETB        JHE         BSB                     |\n|                                                |\n|                        \/            STATUE    |\n|                        /\                      |\n| HOSPITAL                                       |\n|          MDCL         CHAPEL              MUSC |\n|________________________________________________|\nDr. Minnick's glasses glow hot as you quickly swat them off of your face."
#printT("Through Minnick's glasses the true map is revealled!(\S)You read:'Harness the sun.'(\S) ________________________________________________(\S)|Map of McMaster                                 |(\S)|                                       BATES    |(\S)|                                                |(\S)| ETB        JHE         BSB                     |(\S)|                                                |(\S)|                        \/            STATUE    |(\S)|                        /\                      |(\S)| HOSPITAL                                       |(\S)|          MDCL         CHAPEL              MUSC |(\S)|________________________________________________|(\S) (\S)Dr. Minnick's glasses glow hot as you quickly swat them off of your face.",72,0.1)

