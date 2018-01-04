
label updateSexMode(step):
    if actorObj.interRelation.Player.attraction + sexMode[0] + sexMode[1] > step:
        $ sexMode[0] +=1 
        $ sexModeInc = True
        call incrementPlayerAttraction (actorObj, 2)


label getLocationPrivateSexBackground:
    show boxingGym lockerRoom
    return

label getLocationPublicSexBackground:
    show boxingGym Day
    return    

label groupSexMemberSelection:
    return
    
label startGroupSex:
    spkr "Want to find someone else to join in?"
    menu:
        "The more the merrier":
            # create a partner list from the actor's list so partners can be popped as selected
            call groupSexMemberSelection
        "You're plenty for now!":
            jump startTwoSex
    return

label getTwoPublicSexAcknowledgement:
    $ selectVal = renpy.random.randint(0,1)
    if $ selectVal == 0:
        $ textString = "Hell yeah!"
    elif $ selectVal == 1:
        if Player.sex == "m":
            $ textString = "Get your dick over here!"
        elif Player.sex == "f":
            $ textString = "Get your pussy over here!"

    return textString
    

label showSexImages(sexMode, location,  publicSex, participantObjList):
    if sexMode[0] == 0 and sexMode[1] == 0:
        show  Cindy gymPublic makeout1
        show  Cindy gymPublic makeout2
    if sexMode[0] == 1 and sexModeInc == True:
        show Cindy gymPublic makeout3 escalate1
        N "Cindy pushes you backwards and yanks her top over her head..."
        C "I think that's enough of the preliminaries, don't you?"
        show  Cindy gymPublic makeout3 escalate2
        N "You couldn't agree more and quickly follow suit."
    return
    
label doTwoSex:
    $ sexModeInc = False
    if sexMode[0] == 0:
        call showSexImages (sexMode, location, publicSex, [Player, actorObj])
        N "[actor] starts making out with you"
        call incrementPlayerAttraction (actorObj, 1)
        call updateSexMode (5)
        if sexModeInc == True:
            $ sexModeInc = False
            N " But this clearly isn't enough for her as she pulls you in tighter and sticks her tongue down your throat"
            call showSexImages (sexMode, location, publicSex, [Player, actorObj])
    
    if sexMode[0] == 1:
        $ A = 1
    else:
        $ A= 1    
        call showSexImages (sexMode, location, publicSex, [Player, actorObj])
        
    if sexMode[0] == 2:
        $ A= 1
        call showSexImages (sexMode, location, publicSex, [Player, actorObj])
        
    if sexMode[1] == 3:
        $ A= 1
        call showSexImages (sexMode, location, publicSex, [Player, actorObj])
        
    if sexMode[1] == 4:
        $ A= 1
        call showSexImages (sexMode, location, publicSex, [Player, actorObj])
        
    if sexMode[1] == 5:
        $ A= 1
        call showSexImages (sexMode, location, publicSex, [Player, actorObj])
    return
    
label twoSexMenu:
    $ option0 = True
    $ option1 = True
    $ option2 = True
    $ option3 = True
    $ option4 = True
    $ option5 = True
    $ option6 = True
    
    label sexModeMenu:
    $ sexMode = [0,0]
    menu:
        "Make out" if actorObj.interRelationoption.Player.attraction > 0 and option0:
            $ sexMode[0] = 0
        "Oral" if actorObj.interRelation.Player.attraction > 5 and option1:
            $ sexMode[0] = 2
        "Titfuck" if actorObj.interRelation.Player.attraction > 10 and option2:
            $ sexMode[0] = 3
        "69" if actorObj.interRelation.Player.attraction > 10 and option3:
            $ sexMode[0] = 4
        "Let's fuck!" if actorObj.interRelation.Player.attractoin > 15 and option4:
            $ sexMode[0] = 5
        
        "That's enough for now":
            jump endTwoSexMenu
            
    call doTwoSex
    jump sexModeMenu
    
    label endTwoSexMenu:
    return
    
label startTwoPublicSex:
    $ publicSex = True
    call getTwoPublicSexAcknowlegement ()
    $ textStr = _return
    spkr " %(textString)s  "
    call getLocationPublicSexBackground ()
    call twoSexMenu
    return
    
label getPrivateSexAcknowledgement:
    $ selectVal = renpy.random.randint(0,1)
    if $ selectVal == 0:
        $ textString = "I know just the place..."
    elif $ selectVal == 1:
        $ textString = "Lead the way..."
    return textString

label startTwoPrivateSex:
    call getPrivateSexAcknowledgement
    call getLocationPrivateSexBackground
    return
    
label startTwoSex:
        if actorObj.sexValues.exhibitionist > 5:
            spkr "Do you want to find somewhere more private or just go right now?"
            menu:
                "Let's find somewhere more private.":
                    call startTwoPublicSex
                "Oh, it's on right here!":
                    call startTwoPublicSex
        return
    
label sexDialog:
    $ option3 = False
    if actorObj.sexValues.groupSexEnabled:
        call startGroupSex
    else:
        call startTwoSex
        return


