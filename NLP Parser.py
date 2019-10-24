"""
This Parser is defined to be our version of the natural language processor.
It's main goal is to take in inputs from the user in a way that reduces frustration of trying to do actions.
Some of this will be done through teaching/tutorials, some through having the ability to quickly address things,
some is done through being able to interpret a wide variety of language, and the last is having robustness to handle
the wide variety of situations that may be encountered.
Generally the Eng Phys Text Adventure is very simple two word(ish) parser.
It's looking for a Verb (function) and a Noun (object).
Our basic level is having an explicit system with Verb Full Noun (with spellchecking)

1. The next layer of abstraction is Verb then partial noun.
2. Verb then noun at any point.
3. Any combination of verb and noun.
4. Multiple objects and commands in single line
5. Quick verb and quick noun address
e. Any combination of these with spellchecking included.

Research
Could support adjectives or multiple words to be mores specific and distinguish
Get rid of certain words like the, in, about, etc
Infocom-type parsers are based on the grammer of english. A lot more complex but more robust. Would be too advanced to
implement and might just use authoring at that point.
http://www.ifwiki.org/index.php/Infocom-type_parser
When something is mentioned in the description but not interactable in the game it is a crime (people want it):
    http://www.ifwiki.org/index.php/Mimesis
A game that lacks mimesis is not necessarily a failure,
    and a game that contains nothing but mimesis is not necessarily enjoyable.
Need to make sure to communicate allowable actions to player so it's clear, no paralysis, etc
    https://emshort.blog/2010/06/07/so-do-we-need-this-parser-thing-anyway/
    Lots of time goes to accounting for thounds of player options rather than creating interesting stories or puzzles
Formal Parser testing
    https://emshort.blog/2008/11/24/lick-tree-purchase-antlers/

* I would rather restrict the player options but make it clear. Their can be synonym words but not going too far
If we say it can do anything we can't account for it all, but if we tell them the basics they only do that so there's
no more point to develope anything further

* Part of helping the game may come from making sure nouns and verbs are distinct but that may be impossible.
* The next best possibility is to make sure that these are all distinguishable based on situational context e.g. (what
is in the immediate area, what type of object is the noun referring to, and possibly how the order or size the word.
* This will be a large work in progress needed lots of testing and implementation. Other material should be referenced
but make no mistake that this parser will be VERY GAME SPECIFIC. Meaning not only will it most likely only work for this
game but only for this implementation/update of the game. That's hopefully why this is the last update with a lot of
the balancing and testing happening at the end.

This is a parser based game or text based adventure

Ours boils down to basically several different vanilla commands (after getting rid of others)
These functions should be object based methods but whatever for now. that will be rebuild
Equip:
Get
Drop:
Move:
Attack:
Talk:
Inspect/Interact:
Open
Examine
Read
Inventory:
Eat:
Look:


Download latest update then add this and update the feature list.
"""

# How does the spellcheck work?

# How can we use parts of the noun/object?

# How can we search within a sentence to find the verb and the noun?

# How can we make the parser robust?

# How can teach and handle cases that lead the user to understand the parser the best?

# How can we keep the text input fun and engaging, for any level of player?


sentence = raw_input('What do you want to do?\n').lower.split(" ",1)

