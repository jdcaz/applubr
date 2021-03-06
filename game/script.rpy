﻿ls# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    from time import time
    import datetime
    charTextColor = dict()
    charTextColor["Player"] = "#c8ffc8"
    charTextColor["Narrator"] = "#c8ffc8"
    charTextColor["Announcer"] = "#cc3e2e"
    charTextColor["Cindy"] = "#c8ffc8"
    charTextColor["Denisa"] = "#c8ffc8"
    charTextColor["Jane"] = "#c8ffc8"
    charTextColor["Kathy"] = "#c8ffc8" 
    charTextColor["Justin"] = "#c8ffc8"
    charTextColor["Sunny"] = "#c8ffc8"

# Set debug mode    
define config.developer = True

# Game constants
define REGEN_RATE = 1
define DECAY_RATE = 1
define HEAL_RATE = 1

define P = DynamicCharacter("playername", color=charTextColor["Player"])
define N = Character('Narrator', color=charTextColor["Narrator"])
define A = Character('Announcer', color=charTextColor["Announcer"])
define C = Character('Cindy', color=charTextColor["Cindy"])
define D = Character('Denisa', color=charTextColor["Denisa"])
define J1 = Character('Jane', color=charTextColor["Jane"])
define K = Character('Kathy', color=charTextColor["Kathy"])
define J2 = Character('Justin', color=charTextColor["Justin"])
define S = Character('Sunny', color=charTextColor["Sunny"])

call createImageSets

    
label after_load:
    return
    

# The game starts here.

label start:
    $ choiceLeft = Position(xpos=0.25, ypos = 0.7)
    $ choiceRight = Position(xpos=0.75, ypos = 0.7)
#    $ charList = ["Player", "Cindy", "Denisa", "Jane", "Kathy", "Sunny"]
    $ charList = ["Player", "Cindy", "Denisa", "Sunny"]
    $ fighterlist = [ ("Cindy", "Cindy"), ("Denisa", "Denisa")]
        
    call createLocations
    call setUpLocations
    call createCharacters(charList, fighttypes)
    
    #######
    $ Cindy.interRelation.Player.attraction = 30
    #######
    A "Test"
    transform myzoom(i_zoom):
         zoom i_zoom
        
    transform myalpha(i_alpha):
         alpha i_alpha

    transform blink(i_pause):
        alpha 0.0
        linear i_pause alpha 1.0
        linear i_pause alpha 0.0
        pause 0.01
        repeat
        
        
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black
    show boxingGym Day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    N "Welcome to Catfight World."

    N "There will be some better text here"
    
    # call createPlayer from _call_createPlayer

    show mProtagSelect at choiceLeft
    show fProtagSelect at choiceRight
    
    menu: 
        "Choose your player gender:"
        
        "Male":
            $ playerSex = "m"
        
        "Female":
            $ playerSex = "f"
            
    label after_menu:
        if playerSex == "m":
            hide fProtagSelect
        if playerSex == "f":
            hide mProtagSelect
        "Good, you chose male. Female doesn't work yet"
        $ playerSex = "m"
        hide fProtagSelect
        hide mProtagSelect

        show mProtagSelect as protagSelect
        
    $ fname = renpy.input("What is your first name?")
    $ fname = fname.strip()
    if not fname: 
        $ fname = "John"
    $ lname = renpy.input("What is your last name?")
    $ lname = lname.strip()
    if not lname: 
        $ lname = "Smith"
    
    $ Player = Character(0, fname, lname, playerSex, charList, fighttypes)
    
    hide protagSelect
    N "Good, your name is [Player.fname] [Player.lname]"

    $ gameTime = ["Mon", 8]
    $ incrementTime = 0
    $ location = boxingGym
    $ actor = ""
    
    call generateSchedule

    call gotoLocation

    jump mainGame
    
label mainGame:
    
    call processEvents
        
    window hide
    
    jump mainGame
    
label endGame:

    # This ends the game.

    return
