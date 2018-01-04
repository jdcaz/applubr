init python:
    
    HEALTH_SCALE = 5
    ENERGY_SCALE = 8
    
    class FightModule:
        def __init__(self, fighterList, fightType, outfit, rules, location):
            self.fighterList = fighterList
            self.fightType = fightType
            self.fightType = fightType
            self.audienceEnergy = 0
            for fighter in self.fighterList:
                self.audienceEnergy += fighter.stats.fame
                
            if fightType == "Catfight":
                self.fightModule = CatfightModule(fighter1, fighter2, outfit, rules,  location)
            elif fightType == "Boxing":
                self.fightModule = BoxingModule(fighter1, fighter2, outfit, rules,  location)
            elif fightType == "Titfight":
                self.fightModule = TitfightModule(fighter1, fighter2, outfit, rules,  location)
            elif fightType == "Sexfight":
                self.fightModule = SexfightModule(fighter1, fighter2, outfit, rules,  location)
            elif fightType == "Wrestling":
                self.fightModule = WrestlingModule(fighter1, fighter2, outfit, rules,  location)
            elif fightType == "Sreetfight":
                self.fightModule = StreetFightModule(fighter1, fighter2, outfit, rules,  location)
                
            initialize_fight_stats()
            
            
        def initialize_fight_stats():
            k = 0
            for fighter in self.fighterList:
                fighter.fightStats.rage = 0
                opponentList = self.fighterList[:]
                for opponent in opponentList.pop(fighter)
                    fighter.fightStats.opponentHate = getattr(fighter.interRelation, opponent.name).anger
                    
                fighter.fightStats.pain = fighter.fighterData.currInjury
                fighter.fightStats.averagePain = fighter.fightStats.calculate_average_pain()
                fighter.fightStats.damage = fighter.fighterData.currInjury
                fighter.fightStats.health = (fighter.stats.endurance + fighter.stats.fitness + fighter.stats.strength/2 - fighter.stats.currInjury) * HEALTH_SCALE
                fighter.fightStats.energy = (fighter.stats.endurance + fighter.stats.fitness + fighter.stats.strength/2 - fighter.stats.currInjury) * ENERGY_SCALE
                k += 1
                
        def calculateInitiative(self):
            initList = list()
            for fighter in self.fighterList:
                initList.append(fighter1.stats.speed + getattr(self.fighter1.fighterData, self.fightType))
            total = 0
            for val in initList:
                total += val
            roll = renpy.random.randint(1, total)
            if roll < initList[0]:
                return (1, roll)
           else:
               return (2, roll-f1init)
             
        def calculate_damage(self):               
               
         def calculate_Injury(self):
             
         def increment_rage(self):
                
         def fight_status(self):
             
         def change_fight_type(self):
    
        def eval_audience_reaction(self):
            self.audienceEnergy
            
        def do_face_off(self):
            self.fightModule.face_off()
            
        def run_turn(self):
            self.fightModule.run_turn()
            calculate_damage()
            calculate_injury()
            increment_rage()
            get_position()
            if self.fightModule.changeFightType[0] = 1:
                change_fight_type()
            eval_audience_reaction()
            
        def do_finish(self):
             self.fightModule.do_finish()

             
    class BoxingModule:
        def __init__(self, fighter1, fighter2):
            self.fighter1 = figher1
            self.fighter2 = fighter2
            self.outfit = outfit
            self.rules = rules
            self.location = location
            self.momentum = 0
            self.prevmomentum = 0
            self.attackResult = [0,"",0,0] # Target fighter, body part, damage, attacker energy drain
            self.dialogList = list()

             
        def evaluateDamage(self, damage, fighter1, target):
             
        def face_off(self):
            self.
            
        def run_turn(self):
            
        def do_finish(self):

        def update_position(self):
             
            
    class TitfightModule:
        def __init__(self, fighter1, fighter2, outfit, rules,  location):
            self.fighter1 = figher1
            self.fighter2 = fighter2
            self.outfit = outfit
            self.rules = rules
            self.location = location
            self.momentum = 0
            self.prevmomentum = 0
            self.attackResult = [0,"",0,0]

             
        def evaluateDamage(self, damage, fighter1, target):
             
        def face_off():
            
        def run_turn():
            
        def do_finish():

            
    class CatfightModule:
        def __init__(self, fighter1, fighter2, outfit, rules,  location):
            self.fighter1 = figher1
            self.fighter2 = fighter2
            self.outfit = outfit
            self.rules = rules
            self.location = location
            self.momentum = 0
            self.prevmomentum = 0
            self.attackResult = [0,"",0,0] # Target fighter, body part, damage, attacker energy drain


        def evaluateDamage(self, damage, fighter1, target):
         
        def face_off():
            
        def run_turn():
            
        def do_finish():

            
    class SexfightModule:
        def __init__(self, fighter1, fighter2, outfit, rules,  location):
            self.fighter1 = figher1
            self.fighter2 = fighter2
            self.outfit = outfit
            self.rules = rules
            self.location = location
            self.momentum = 0
            self.prevmomentum = 0
            self.attackResult = [0,"",0,0]

             
        def evaluateDamage(self, damage, fighter1, target):
             
        def face_off():
            
        def run_turn():
            
        def do_finish():

            
    class WrestlingModule:
        def __init__(self, fighter1, fighter2, outfit, rules,  location):
            self.fighter1 = figher1
            self.fighter2 = fighter2
            self.outfit = outfit
            self.rules = rules
            self.location = location
            self.momentum = 0
            self.prevmomentum = 0
            self.attackResult = [0,"",0,0]

             
        def evaluateDamage(self, damage, fighter1, target):
             
        def face_off():
            
        def run_turn():
            
        def do_finish():

            
    class StreetFightModule:
        def __init__(self, fighter1, fighter2, outfit, rules,  location):
            self.fighter1 = figher1
            self.fighter2 = fighter2
            self.outfit = outfit
            self.rules = rules
            self.location = location
            self.momentum = 0
            self.prevmomentum = 0
            self.attackResult = [0,"",0,0]

             
        def evaluateDamage(self, damage, fighter1, target):
             
        def face_off():
            
        def run_turn():
            
        def do_finish():

            
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
