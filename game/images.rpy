
label createImageSets:
    image boxingGym Day = "locations/boxingGym/boxingGym_day.png"
    image boxingGym lockerRoom = "locations/boxingGym/lockerRoom.png"

    image fProtagSelect = "player/protag_f_1.png"
    image mProtagSelect = "player/protag_m_1.png"
        
    image Cindy gymClothes happy aroused = "cindy/gymClothes/happy_midAroused.png"
    image Cindy gymClothes angry readyToFight = "cindy/gymClothes/angry_readyToFight.png"
    image Cindy gymClothes confident readyToFight = "cindy/gymClothes/confident_readyToFight.png"
    
    image Cindy gymPublic makeout1 = "events/sex/Cindy/gymMakeout1.png"
    image Cindy gymPublic makeout2 = "events/sex/Cindy/gymMakeout2.png"
    image Cindy gymPublic makeout3 escalate1 = "events/sex/Cindy/gymMakeout3_escalate1.png"
    image Cindy gymPublic makeout3 escalate2 = "events/sex/Cindy/gymMakeout3_escalate2.png"
    
        
    return
    
    
label playerConversationImages:
    
    if actor == "Cindy":
        if Cindy.generalValues.mood > 20 and Cindy.sexValues.arousal > 20:
            if Cindy.clotes == "gymClothes":
                show Cindy gymClothes happy aroused
                return
    
    return
    
    
label getWalkinImages:
    
    return
    
    
label getFaceOffImages:
    return
    
label getFightImages:
    return
