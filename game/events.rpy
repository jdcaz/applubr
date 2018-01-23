init python:
    class GameEvents():
        def __init__(self): pass
    
        def setGameEvents(self):
            self.watchedCindyTrainingVideo = False               
            
            return

label cindyTrainingEvent:

    if not Player.gameEvents.watchedCindyTrainingVideo:
        
        N "You arrive at the gym to find your best (and only) fighter Cindy training"
        $ config.skipping = False
        $ renpy.movie_cutscene("vids/cindy/cindyTraining1.mp4")
        $ config.skipping = True
        
        N "As you approach, Cindy sees you and slides into a more advantageous position"
        
        $ config.skipping = False
        $ renpy.movie_cutscene("vids/cindy/cindyTraining2.mp4")
        $ config.skipping = True
        
    call playerConversationImages
    
    C "Hey there [Player.fname], you coming to talk or did you have something else in mind?"
        
    call generalConversation (Cindy)
    
    if Cindy.fighterData.readyToFight:
        $ fightIsOn = True
        
    return    
   
label doTraining:
    return
    
label processEvents:
    
    if location.name == "Boxing gym":
        if Cindy.location == location.name:
            $ actor = "Cindy"
            call cindyTrainingEvent
        
    return
