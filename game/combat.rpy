init python:
    
    class FightModule:
        def __init__(self, fighter1, fighter2, fightType, outfit, rules):
            self.fighter1 = figher1
            self.fighter2 = fighter2
            self.fightType = fightType
            self.damage = 0
            self.target = ""
            self.position = ""
            self.fightType = fightType
            if fightType == "Catfight":
                self.fightModule = CatfightModule()
            elif fightType == "Boxing":
                self.fightModule = BoxingModule()
            elif fightType == "Titfight":
                self.fightModule = TitfightModule()
            elif fightType == "Sexfight":
                self.fightModule = SexfightModule()
            elif fightType == "Wrestling":
                self.fightModule = WrestlingModule()
            elif fightType == "Sreetfight":
                self.fightModule = StreetFightModule()
                            
        def calculateInitiative(self):
            f1init = fighter1.stats.speed + getattr(self.fighter1.fighterData, self.fightType)
            f2init = fighter2.stats.speed + getattr(self.fighter1.fighterData, self.fightType)
            total = f1init + f2init
            roll = renpy.random.randint(1, total)
            if roll < f1init:
                return 1
           else:
               return 2
             
         def evaluateDamage(self, damage, fighter1, target):
             
         def calculateInjury(self):
             
         def incrementRage(self):
                
         def getPosition(self):
             
         def fightStatus(self):
             
         def changeFightType(self):
    
        def evalAudienceReaction(self):
            
        def runFIght(self):
             
             
    class CatfightModule:
        def __init__(self, fighter1, fighter2):
            self.fighter1 = figher1
            self.fighter2 = fighter2

    class BoxingModule:
        def __init__(self, fighter1, fighter2):
            self.fighter1 = figher1
            self.fighter2 = fighter2
             
    class TitfightModule:
        def __init__(self, fighter1, fighter2):
            self.fighter1 = figher1
            self.fighter2 = fighter2
             
    class SexfightModule:
        def __init__(self, fighter1, fighter2):
            self.fighter1 = figher1
            self.fighter2 = fighter2
             
    class WrestlingModule:
        def __init__(self, fighter1, fighter2):
            self.fighter1 = figher1
            self.fighter2 = fighter2
             
    class StreetFightModule:
        def __init__(self, fighter1, fighter2):
            self.fighter1 = figher1
            self.fighter2 = fighter2
             
label calculateAveragePain:
    $ actor.fighterData.averagePain = (actor.fighterData.averagePain.head + actor.fighterData.averagePain.face + actor.fighterData.averagePain.neck + actor.fighterData.averagePain.arms + actor.fighterData.averagePain.back + actor.fighterData.averagePain.boobs*2 + actor.fighterData.averagePain.pussy*2 + actor.fighterData.averagePain.legs)/10
    return

label setUpFightTypes:
    python:
        fightTypes = [("Wrestling","Wrestling"), ("Boxing","Boxing"), ("Catfight","Catfight"), ("Sexfight","Sexfight"), ("Titfight","Titfight")]
    
        fightAttires  = [("Normal","Normal"), ("Normal, topless","Normal, topless"), ("Underwear","Underwear"), ("Underwear, topless","Underwear, topless"), ("Nude","Nude")]
    
        wrestlingRules = [("Normal", "Normal"), ("Submission only", "Submission only"), ("Sexual submission only", "Sexual submission only"), ("No-holds barred", "No-holds barred")]
        boxingRules = [("Gloves", "Gloves"), ("Gloves, no rules", "Gloves, no rules"), ("Bare-knuckle", "Bare-knuckle"),  ("Bare-knuckle, no rules", "Bare-knuckle, no rules")]
        catfightRules = [("Rules", "Rules"), ("No rules", "No rules")]
        sexfightRules = [("Sex only", "Sex only"), ("No rules", "No rules")]
        titfightRules = [("Tits only", "Tits only"), ("No rules", "No rules")]
    
        wrestlingDirtyMax = 3
        boxingDirtyMax = 3
        catfightDirtyMax = 3
        sexfightDirtyMax = 3
        titfightDirtyMax = 3
    
        stripMax = 3
    
    return

label getFightStripLevel:
    if fightAttire == "Normal" or fightAttire == "Underwear":
        $ stripLevel = 0
    elif fightAttire == "Normal" or fightAttire == "Underwear":
        $ stripLevel = 1
    elif fightAttire == "Normal, topless" or fightAttire == "Underwear, topless":
         $ stripLevel = 2
    else:
        $ stripLevel = 3
    return

label doStrip:
    if fighter1.fname == "Cindy" and fighter2.fname = "Denissa" or fighter2.fname == "Cindy" and fighter1.fname = "Denissa":
        if stripLevel = 1:
            call CindyAndDenisaRemoveGlovesImage
        if stripLevel = 2:
            call CindyAndDenisaRemoveTopsImage
        if stripLevel = 3:
            call CindyAndDenisaRemoveBottomsImage
    return    
    
label getFightDirtyLevel:
    if fightType == "wrestling":
        if fightLevel == "No holds barred":
            $ fightDirtyLevel = 2
        else:
            $ fightDirtyLevel = 1
            
    elif fightType == "boxing":
        if fightLevel == "Gloves, no rules" or fightLevel == "Bare-knuckle, no rules":
            $ fightDirtyLevel = 2
        else:
            $ fightDirtyLevel = 1
            
    elif fightType == "catfight":
        if fightLevel == "No rules":
            $ fightDirtyLevel = 2
        else:
            $ fightDirtyLevel = 1
            
    elif fightType == "sexfight":
        if fightLevel == "No rules":
            $ fightDirtyLevel = 2
        else:
            $ fightDirtyLevel = 1
            
    elif fightType == "titfight":
        if fightLevel == "No rules":
            $ fightDirtyLevel = 2
        else:
            $ fightDirtyLevel = 1

    return fightDirtyLevel
    
label checkDirtyLevel(dirtyLevel, dirtyMax):
    if dirtyLevel < dirtyMax:
        if fighter1.fightFields.rage/2 >= fighter1.fightFields.opponentHate or  fighter2.fightFields.rage/2 >= fighter2.fightFields.opponentHate:
            $ dirtyLevel += 1
            if stripLevel < stripMax:
                $ stripLevel += 1
                call doStrip
    return
    
label endOfRoundCleanup:
    return
    
label globalFightStructure(fighter1, fighter2):
    call preFightSetup(fighter1, fighter2)
    call faceOff(fighter1, fighter2)
    
    if fightType == "wrestling":
        call wrestling(fighter1, fighter2)
    elif fightType == "boxing":
         call boxing(fighter1, fighter2)
    elif fightType == "catfight":
         call catfight(fighter1, fighter2)
    elif fightType == "sexfight":
         call sexfight(fighter1, fighter2)
    elif fightType == "titfight":
         call titfight(fighter1, fighter2)
         
    call endFight(fighter1, fighter2)
    
    return
   
label preFightSetup(fighter1, fighter2):
    return
    
label faceOff(fighter1, fighter2):
    return
    
label wrestling(fighter1, fighter2):
    return

label boxing(fighter1, fighter2):
    return    
    
label catfight(fighter1, fighter2):
    return
    
label sexfight(fighter1, fighter2):
    return
    
label titfight(fighter1, fighter2):
    return
    
label endFight(fighter1, fighter2):
    return
