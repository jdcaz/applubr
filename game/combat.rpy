init python:

    fighttypes = [("Wrestling","Wrestling"), ("Boxing","Boxing"), ("Catfight","Catfight"), ("Sexfight","Sexfight"), ("Titfight","Titfight")]

    fightattires  = [("Normal","Normal"), ("Normal, topless","Normal, topless"), ("Underwear","Underwear"), ("Underwear, topless","Underwear, topless"), ("Nude","Nude")]

    wrestlingrules = [("Normal", "Normal"), ("Submission only", "Submission only"), ("Sexual submission only", "Sexual submission only"), ("No-holds barred", "No-holds barred")]
    boxingrules = [("Gloves", "Gloves"), ("Gloves, no rules", "Gloves, no rules"), ("Bare-knuckle", "Bare-knuckle"),  ("Bare-knuckle, no rules", "Bare-knuckle, no rules")]
    catfightrules = [("Rules", "Rules"), ("No rules", "No rules")]
    sexfightrules = [("Sex only", "Sex only"), ("No rules", "No rules")]
    titfightrules = [("Tits only", "Tits only"), ("No rules", "No rules")]

    WRESTLING_DIRTY_MAX = 3
    BOXING_DIRTY_MAX = 3
    CATFIGHT_DIRTY_MAX = 8
    SEXFIGHT_DIRTY_MAX = 5
    TITFIGHT_DIRTY_MAX = 3

    WRESTLING_SEX_MAX = 3
    BOXING_SEX_MAX = 3
    CATFIGHT_SEX_MAX = 3
    SEXFIGHT_SEX_MAX = 3
    TITFIGHT_SEX_MAX = 3
    
    STRIP_MAX = 2
    
    # stat scale factors
    HEALTH_SCALE = 5
    HEALTH_DROP_SCALE = 10
    HEALTH_DIFF_SCALE = 4
    ENERGY_SCALE = 8
    ENERGY_DROP_SCALE = 16
    ENERGY_DIFF_SCALE = 6
    RAGE_SCALE = 2
    INJURY_SCALE = 2
    AROUSAL_SCALE = 2
    DIRTY_SCALE = 2
    
    CLINCH_SCALE = 2
    
    ANGER_TO_RAGE = 3
    ATTRACTION_TO_AROUSAL = 3
    RAGE_TO_DIRTY = 2
    RAGE_TO_WILD = 3
    PAIN_TO_INIT = 2
    
    SKILL_TO_DAMAGE = 2
    STRENGTH_TO_DAMAGE = 3
    
    DAMAGE_TO_CLOTHING_DAMAGE = 2
    
    class FightModule:
        def __init__(self, fighterlist, fighttype, fightattire, rules, location):
            self.fighterlist = fighterlist
            self.fighttype = fighttype
            self.fighttype = fighttype
            self.audenergy = 0
            self.injurycaused = False
            for fighter in self.fighterlist:
                self.audenergy += fighter.stats.fame
                
            self.sexlevel = 0
            self.fightattire = fightattire
            self.set_fight_dirty_level()
            self.set_strip_level()

            if fighttype == "Catfight":
                self.fightModule = CatfightModule(fighterlist, fightattire, rules,  location, self.sexlevel, self.dirtylevel, self.striplevel)
            elif fighttype == "Boxing":
                self.fightModule = BoxingModule(fighterlist, fightattire, rules,  location, self.sexlevel, self.dirtylevel, self.striplevel)
            elif fighttype == "Titfight":
                self.fightModule = TitfightModule(fighterlist, fightattire, rules,  location, self.sexlevel, self.dirtylevel, self.striplevel)
            elif fighttype == "Sexfight":
                self.fightModule = SexfightModule(fighterlist, fightattire, rules,  location, self.sexlevel, self.dirtylevel, self.striplevel)
            elif fighttype == "Wrestling":
                self.fightModule = WrestlingModule(fighterlist, fightattire, rules,  location, self.sexlevel, self.dirtylevel, self.striplevel)
            elif fighttype == "Sreetfight":
                self.fightModule = StreetFightModule(fighterlist, fightattire, rules,  location, self.sexlevel, self.dirtylevel, self.striplevel)
                           
            self.initialize_fight_stats()
            

        def set_strip_level(self):            
            if self.fightattire == "Normal" or self.fightattire == "Underwear":
                self.striplevel = 0
            elif self.fightattire == "Normal, topless" or self.fightattire == "Underwear, topless":
                 self.striplevel = 1
            else:
                self.striplevel = 2

                
        def set_fight_dirty_level(self):
            if self.fighttype == "Wrestling":
                if self.rules == "No holds barred":
                    self.fightdirtylevel = 1
                else:
                    self.fightdirtylevel = 0
                    
            elif self.fighttype == "Boxing":
                if self.rules == "Gloves, no rules" or self.rules == "Bare-knuckle, no rules":
                    self.fightdirtylevel = 1
                else:
                    self.fightdirtylevel = 0
                    
            elif self.fighttype == "Catfight":
                if self.rules == "No rules":
                    self.fightdirtylevel = 1
                else:
                    self.fightdirtylevel = 0
                    
            elif self.fighttype == "Sexfight":
                if self.rules == "No rules":
                    self.fightdirtylevel = 1
                else:
                    self.fightdirtylevel = 0
                    
            elif self.fighttype == "Titfight":
                if self.rules == "No rules":
                    self.fightdirtylevel = 1
                else:
                    self.fightdirtylevel = 0
            
                    
        def initialize_fight_stats(self):
            k = 0
            for fighter in self.fighterlist:
                fighter.fightStats.rage = 0
                opponentList = self.fighterlist[:]
                for opponent in opponentList.pop(fighter):
                    fighter.fightStats.rage = getattr(fighter.interRelation, opponent.name).anger/ANGER_TO_RAGE
                    fighter.fightStats.arousal = getattr(fighter.interRelation, opponent.name).attraction/ATTRACTION_TO_AROUSAL
                    
                fighter.fightStats.pain = fighter.fighterData.currInjury
                fighter.fightStats.averagePain = fighter.fightStats.calculate_average_pain()
                fighter.fightStats.damage = fighter.fighterData.currInjury
                fighter.fightStats.health = (fighter.stats.endurance + fighter.stats.strength/2 - fighter.stats.currInjury) * HEALTH_SCALE
                fighter.fightStats.healthmax = (fighter.stats.endurance + fighter.stats.strength/2 - fighter.stats.currInjury) * HEALTH_SCALE
                fighter.fightStats.energy = (fighter.stats.fitness + fighter.stats.strength/2 - fighter.stats.currInjury) * ENERGY_SCALE
                fighter.fightStats.energymax = (fighter.stats.fitness + fighter.stats.strength/2 - fighter.stats.currInjury) * ENERGY_SCALE
                k += 1
                
        def calculate_initiative(self):
            initlist = list()
            for fighter in self.fighterlist:
                # calculate initiative as speed + skill
                initlist.append(fighter.stats.speed + getattr(self.fighter.fighterData, self.fighttype) - fighter.fightstats.averagePain)
            total = 0
            for val in initlist:
                # sum fighter initiative values
                total += val
            # roll over total initiative
            roll = renpy.random.randint(1, total)
            if roll <= initlist[0]:
                # fighter 1 attacks, initiative becomes attack bonus
                return (0, roll)
            else:
               # fighter 2 attacks
               return (1, roll-initlist[0])
             
        def calculate_damage(self):
            # subtract damage from target's health
            self.fighterlist[self.fightModule.attackresult[0]].fightStats.health -= self.fightModule.attackresult[2]
            # subtract energy damage from target's energy  (if applicable)
            self.fighterlist[self.fightModule.attackresult[0]].fightStats.energy -= self.fightModule.attackresult[4]
            # subtract energy from attacker's energy
            self.fighterlist[int(not self.fightModule.attackresult[0])].fightStats.energy -= self.fightModule.attackresult[3]
               
        def calculate_injury(self):
           # get current pain by body part
           currVal = getattr(self.fighterlist[self.fightModule.attackresult[0]].fightStats.pain, self.fightModule.attackresult[1])
           # increment current body part pain by damage divided by half endurance
           setattr(self.fighterlist[self.fightModule.attackresult[0]].fightStats.pain, self.fightModule.attackresult[1], currVal +2*self.fightModule.attackresult[2]/self.fighterlist[self.fightModule.attackresult[0]].stats.endurance)
           # roll for body part injury by rolling body part pain
           roll = renpy.randint(0, getattr(self.fighterlist[self.fightModule.attackresult[0]].fightStats.pain, self.fightModule.attackresult[2]))
           if roll > self.fighterlist[self.fightModule.attackresult[0]].stats.endurance * INJURY_SCALE:
               self.injurycaused = True
               # Increment injury count for body part
               setattr(self.fighterlist[self.fightModule.attackresult[0]].stats.injury, self.fightModule.attackresult[1], getattr(self.fighterlist[self.fightModule.attackresult[0]].stats.injury, self.fightModule.attackresult[1])+1)
               # reduce current pain by half
               setattr(self.fighterlist[self.fightModule.attackresult[0]].fightStats.pain, self.fightModule.attackresult[2], getattr(self.fighterlist[self.fightModule.attackresult[0]].fightStats.pain, self.fightModule.attackresult[2])/2)
             
        def increment_rage(self):
           # increment rage if fighter health > fighter energy (not tired)
           if self.fightModule.attackresult[0].fightStats.health > self.fightModule.attackresult[0].fightStats.energy:
               # increment rage by half scaled damage
               self.fightModule.attackresult[0].fightStats.rage += self.fightModule.attackresult[2]/RAGE_SCALE
           else: # decrement rage by half difference between energy and health (tiredness)
               self.fightModule.attackresult[0].fightStats.rage -= (self.fightModule.attackresult[0].fightStats.energy - self.fightModule.attackresult[0].fightStats.health)/2

                
        def update_fight_status(self):
           if self.fightModule.incrementdirtylevel:
               self.dirtylevel += 1
           if self.fightModule.incrementsexlevel:
               self.sexlevel += 1

               
        def change_fight_type(self):
           # fight devolves towards sexfight or catfight (or combination)
           if self.dirtylevel >= 3:
               self.fightModule = CatfightModule(fighter1, fighter2, fightattire, rules,  location)
           if self.sexlevel >= 3:
               self.fightModule = SexfightModule(fighter1, fighter2, fightattire, rules,  location)
    

        def eval_audience_reaction(self):
           # audience high momentum, reversals, ...
            self.audenergy = 0
            
        def do_face_off(self):
            self.fightModule.face_off()
            
        def run_turn(self):
           initiative = calculate_initiative()
           self.fightModule.run_turn(initiative) # create fightModule.attackresult and fightModule.text
           apply_damage()
           calculate_injury()
           increment_rage()
           update_fight_status()
           change_fight_type()
           eval_audience_reaction()
           display_fight_text()
            
        def do_finish(self):
             self.fightModule.do_finish()

       def display_fight_text(self):
           A = 1

    ###### Boxing Module ######
    class BoxingModule:
        def __init__BoxingModule(fighterlist, fightattire, rules,  location, self.sexlevel, self.dirtylevel, self.striplevel):
            self.fighttype = "Boxing"
            self.fighterlist = fighterlist
            self.fightattire = fightattire
            self.rules = parse_rules()
            self.location = location
            
            self.position = [(0,0,0), (0,0,0)] # fighter venue positions and facing status
                # facing statii: 0: facing opponent, 1: facing sideways, 2: facing backwards, 3: down on back, 4: down on face, 5: down on side, 6: on ropes facing opponent, 7: on ropes facing out, 8: in corner facing opponent, 9: in corner facing out
            self.hold = False # is anyone being held
            self.grabbing = [["", ""],["",""]] # what is being grabbed
            self.breakhold = False # did a hold get broken this round
            
            self.move = [0, 0, 0] # delta for move
            self.knockdown = [0,0] # did someone get knocked down this round

            self.initiative = 0
            self.momentum = 0
            self.momentumchange = 0
            self.momentummult = 0
            self.prevmomentum = 0
            
            self.attacker = 0 # numerical id for fighter attacking
            self.attackbonus = 0 # initiative bonus for attacking fighter
            self.defender = 0 # numerical id for fighter defending

            self.maxdamage = 0 # used to determine crits
            self.damagemod = 0 # general damage bonus            

            self.dirtydamage = 2 # damage bonus for dirty attack
            self.dirtycount = 0 # tracking # of dirty attacks
            self.dirtymax = BOXING_DIRTY_MAX
            
            self.counter = False
            
            self.attackresult = [0,"",0,0,0] # target fighter, body part, damage, attacker energy drain, target energy drain
            self.incrementdirtylevel = False
            self.incrementsexlevel = False
            self.dialoglist = list()
            
            self.defending = [False, False] # is a fighter guarding
            self.down = [False, False] # is a fighter down
            self.clinch = False # are the fighters in a clinch
            self.dirtyattack = False            
            
            self.attacklist = list()
            self.problist = list()
            self.attackidx = 0
             
        def parse_rules(self):
            # Boxing
            if rules[0] == "Gloves":
                self.rules = 0
                self.damagemod = -2
            elif rules[0] == "Gloves, no rules":
                self.rules = 1
                self.damagemod = -2
                self.dirtymod = 2
            elif rules[0] == "Bare-knuckle":
                self.rules = 2
                self.damagemod = 0
            elif rules[0] == "Bare-knuckle, no rules":
                self.rules = 3
                self.damagemod = 0
                self.dirtymod = 2
                
                
        def face_off(self):
            self.fighterlist
            
        def run_turn(self):
            set_attacker()
            self.attackbonus = self.initiative[1]
            self.breakclinch = False
            self.breakhold = False            
            self.knockdown = False
            
            for hands in self.grabbing:
                if any(hands):
                    self.hold = True
                else:
                    self.hold = False
            
            set_attacker()

            # both fighters in same location
            if position[self.attacker][0:2] == position[self.defender][0:2]:
                populate_prob_list()
                select_attack()
                get_target()
                get_counter()
            else:
                move_to_opponent() # FIXME: need to create 
                self.momentumchamge = -1*

            calculate_damage()
            calculate_knockdown()
            if self.updatelocation:
                update_location()
                self.updatelocation = False
            update_momentum()
            update_strip_level()
            update_dirty_level()
            calculate_fight_change()
            cleanup_round()
            generate_text()
            
        def set_attacker(self):
            self.attacker = self.initiative[0] # position in fighterlist of attacker
            self.defender = int(not self.initiative[0]) # position in fighterlist of defender
            self.dirtyattack = False # reset dirty attack
            
            self.defending[attacker] = False # unset attacker defending
            
            if initiative[0] == 1:
                # momentum positive for fighter 1, negative for 2
                self.momentmult = -1
                
            
        def populate_prob_list(self):
            if self.clinch:
                # clinch attack list
                self.attacklist = ["Punch", "Break", "Push", "Titfight", "Kiss", "Dirty"]
            elif self.hold:
                # holding attack lists
                self.attacklist = ["Punch", "Break", "Kiss", "Push", "Grab", "Dirty"]
            else:
                # normal attack list
                self.attacklist = ["Wild swing", "Jab", "Cross", "Hook", "Uppercut", "Drop",  "Cover up", "Clinch", "Disengage", "Dirty"]

            self.problist = [0]*len(attacklist)
            # increment dirty prob by fighter's scaled dirty stat
            self.problist[-1] += self.fighterlist[self.attacker].dirtyFighter/DIRTY_SCALE
        
            # clinch attacks
            if self.clinch:                
                self.problist[0] += 1 # punch
                self.problist[1] += 1 # break
                self.problist[2] += 1 # push
                # increment push and break probability by energy diff
                if self.fighterlist[self.attacker].fightStats.energy > self.fighterlist[defender].fightstats.energymax:
                    val = self.fighterlist[self.attacker].fightStats.energy - self.fighterlist[self.attacker].fightstats.energymax
                    self.problist[1] += val/ENERGY_DIFF_MULT
                    self.problist[2] += val/ENERGY_DIFF_MULT
                # increment break probability by health diff
                if self.fighterlist[self.attacker].fightStats.health > self.fighterlist[defender].fightstats.health:
                    val = self.fighterlist[self.attacker].fightStats.health - self.fighterlist[defender].fightstats.health
                    self.problist[1] += val/HEALTH_DIFF_MULT
                # increment titfight chance by half rage and arousal
                self.problist[3] += (self.fighterlist[self.attacker].fightstats.rage/RAGE_SCALE + self.fighterlist[self.attacker].fightstats.arousal/AROUSAL_SCALE)/2 
                # increment kiss chance by arousal
                self.problist[4] += self.fighterlist[self.attacker].fightstats.arousal/AROUSAL_SCALE
                # increment punch and dirty chance by rage
                self.problist[0] += self.fighterlist[self.attacker].fightstats.rage/RAGE_SCALE
                self.problist[-1] += self.fighterlist[self.attacker].fightstats.rage/RAGE_SCALE

            # holding attacks
            elif self.hold:
                self.problist[0] += 1 # punch
                self.problist[1] += 1 # break
                self.problist[2] += 1 # kiss
                self.problist[3] += 1 # push
                self.problist[4] += 1 # grab
                self.problist[5] += 1 # dirty
                # increment push and break probability by energy diff
                if self.fighterlist[self.attacker].fightStats.energy > self.fighterlist[defender].fightstats.energymax:
                    val = self.fighterlist[self.attacker].fightStats.energy - self.fighterlist[self.attacker].fightstats.energymax
                    self.problist[1] += val/ENERGY_DIFF_MULT
                    self.problist[3] += val/ENERGY_DIFF_MULT
                # increment break probability by health diff
                if self.fighterlist[self.attacker].fightStats.health > self.fighterlist[defender].fightstats.health:
                    val = self.fighterlist[self.attacker].fightStats.health - self.fighterlist[defender].fightstats.health
                    self.problist[1] += val/HEALTH_DIFF_MULT
                # increment kiss chance by arousal
                self.problist[2] += self.fighterlist[self.attacker].fightstats.arousal/AROUSAL_SCALE
                # increment punch, grab, and dirty chance by rage
                self.problist[0] += self.fighterlist[self.attacker].fightstats.rage/RAGE_SCALE
                self.problist[3] += self.fighterlist[self.attacker].fightstats.rage/RAGE_SCALE
                self.problist[-1] += self.fighterlist[self.attacker].fightstats.rage/RAGE_SCALE
                
                if all(self.grabbing[attacker]):
                    # attacker has both hands occupied, zero punching and new grab
                    self.problist[0] = 0
                    self.problist[4] = 0
                
            # normal attacks
            else:
                # foxy boxer
                self.problist[0] += 1 # wild sing
                self.problist[-1] +=1  # dirty attack
                # increment chance for wild swing by scaled rage
                self.problist[0] += self.fighterlist[self.attacker].fightStats.rage/RAGE_TO_WILD
                # increment chance for dirty attack by scaled rage
                self.problist[-1] += self.fighterlist[self.attacker]
                
                # probabilities for ok boxer
                if getattr(self.fighterlist[self.attacker].fighterData, self.fighttype).skill > 5:
                    self.problist[1]+= 3 # jab
                    self.problist[2]+= 3 # cross
                    self.problist[3]+= 2 # hook
                    self.problist[4]+= 2 # uppercut
                    self.problist[5]+= 1 # drop
                    
                # proababilities for better boxer
                if getattr(self.fighterlist[self.attacker].fighterData, self.fighttype).skill > 10:
                    self.problist[3]+= 1 # hook
                    self.problist[4]+= 1 # uppercut
                    self.problist[5]+= 2 # drop
                    
                # decrement punch probabilites by reduced health
                if self.fighterlist[self.attacker].fightStats.health < self.fighterlist[self.attacker].fightstats.healthmax:
                    val = (self.fighterlist[self.attacker].fightstats.healthmax-self.fighterlist[self.attacker].fightStats.health)/HEALTH_DROP_MULT
                    self.problist[1]-= val # jab
                    self.problist[2]-= val  # cross
                    self.problist[3]-= val # hook
                    self.problist[4]-= val # uppercut
                    self.problist[5]-= val # drop
                    
                # decrement punch probabilites by reduced energy
                if self.fighterlist[self.attacker].fightStats.energy < self.fighterlist[self.attacker].fightstats.energymax:
                    val = (self.fighterlist[self.attacker].fightstats.energymax-self.fighterlist[self.attacker].fightStats.energy)/ENERGY_DROP_MULT
                    self.problist[1]-= val # jab
                    self.problist[2]-= val  # cross
                    self.problist[3]-= val # hook
                    self.problist[4]-= val # uppercut
                    self.problist[5]-= val # drop
                    
                # increment probability of all defense by negative momentum
                if self.momentum * momentmult < 0:
                    self.problist[6] -= momentum # cover up
                    self.problist[7] -= momentum # clinch
                    self.problist[8] -= momentum # disengage                
                    
                # increment probability of blocking and disengaging by difference in health if self.attacker weaker
                if self.fighterlist[self.attacker].fightStats.health < self.fighterlist[defender].fightstats.health:
                    self.problist[6] += self.fighterlist[defender].fightstats.health - self.fighterlist[self.attacker].fightStats.health
                    self.problist[8] += self.fighterlist[defender].fightstats.health - self.fighterlist[self.attacker].fightStats.health              
                    
                # increment probability of clinch and decrement probability of moving away by difference in energy if attacker more tired
                if self.fighterlist[self.attacker].fightStats.energy < self.fighterlist[defender].fightstats.energy:
                    self.problist[7] += self.fighterlist[defender].fightstats.energy  - self.fighterlist[self.attacker].fightStats.energy
                    self.problist[8] -= self.fighterlist[defender].fightstats.energy - self.fighterlist[self.attacker].fightStats.energy            



                    
        def select_attack():
            rollmax = sum(problist)
            roll = renpy.randint(1,rollmax)
            for idx, val in problist:
                if roll <= sum(problist[0:idx+1]):
                    self.attackidx = idx
                    
                    
        def get_target(self):
            if self.clinch:
                get_clinch_target()
            elif self.hold:
                get_hold_target()
            else:
                get_normal_target()

            if len(targetlist):
                roll  = renpy.randint(0, len(targetlist-1))
                self.attackresult[1] = targetlist[roll]
            else:
                self.attackresult[1] = ""
                
            if self.attackresult[1] == ("neck" or "pussy"):
                self.dirtyattack = True
                

        def get_clinch_target(self):
            if self.attackidx == 0: # clinch punch
                targetlist = ["stomach", "back", "lBoob", "rBoob"]
            elif self.attackidx == 1: # break
                targetlist = list()
                self.clinch = False
                self.breakclinch = True
            elif self.attackidx == 2: # push
                # Cause location to change based on fighter position
                targetlist = list()
                create_movement(2) # move both
            elif self.attackidx == 3: # titfight
                targetlist = ["lBoob", "rBoob"]
            elif self.attackidx == 4: # kiss
                targetlist = list()
                update_arousal(1)
            elif self.attackidx == 5: # dirty
                self.dirtyattack = True
                dirtyattacklist = ["pussyknee", "boobgrind", "headbutt"]
                roll  = renpy.randint(0, len(dirtyattacklist-1))
                if roll == 1: # pussyknee
                    targetlist = ["pussy"]
                    roll = 0
                elif roll == 2: # boobgrind
                    targetlist = ["lBoob", "rBoob"]
                elif roll == 3: # headbutt
                    targetlist = ["face"]

            
        def get_grab_target(self):
            # attacker has both hands occupied
            if all(self.grabbing[attacker]):
                if self.attackidx == 1: # break
                    self.targetlist = list()
                    self.grabbing = [[False, False], [False, False]]
                elif self.attackidx == 2: # kiss
                    self.targetlist = list()
                    increment_arousal(1)
                elif self.attackidx == 3: # push
                    self.targetlist = ()
                    create_movement(2)
                elif self.attackidx == 5: # dirty
                    self.dirtyattack = True
                    dirtyattacklist = ["pussyknee", "headbutt", "bite"]
                    roll  = renpy.randint(0, len(dirtyattacklist-1))
                    if roll == 0:
                        targetlist = ["pussy"]
                    elif roll == 1:
                        targetlist = ["face"]
                    elif roll == 2:
                        targetlist = ["lBoob", "rBoob"]
            # attacker has one occupied hand
            elif any(self.grabbing[attacker]):
                if self.attackidx == 0: # punch
                    targetlist = ["head", "face", "neck", "lArm", "rArm", "lBoob", "rBoob", "stomach", "pussy"]
                    for target in self.grabbing[attacker]:
                        if target:
                            targetlist.pop(target)                    
                elif self.attackidx == 1: # break
                    self.grabbing = [[False, False], [False, False]]
                elif self.attackidx == 2: # kiss
                    self.targetlist = list()
                    increment_arousal(1)                    
                elif self.attackidx == 3: # push
                    self.targetlist = list()
                    generate_movement(2)
                elif self.attackidx == 4: # squeeze (grab)
                    for hand in self.grabbing[attacker]:
                        if hand:
                            targetlist = [hand]
                elif self.attackidx == 5: # dirty
                    self.dirtyattack = True
                    dirtyattacklist = ["pussyknee", "headbutt", "bite"]
                    roll  = renpy.randint(0, len(dirtyattacklist-1))
                    if roll == 0:
                        targetlist = ["pussy"]
                    elif roll == 1:
                        targetlist = ["face"]
                    elif roll == 2:
                        targetlist = ["lBoob", "rBoob"]
            # defender has a hold
            elif self.grabbing[defender]:
                if self.attackidx == 0: # punch
                    targetlist = ["head", "face", "neck", "lArm", "rArm", "lBoob", "rBoob", "stomach", "pussy"]
                    for target in self.grabbing[attacker]:
                        if target:
                            targetlist.pop(target)                    
                elif self.attackidx == 1: # break
                    self.grabbing = [[False, False], [False, False]]
                elif self.attackidx == 2: # kiss
                    self.targetlist = list()
                    increment_arousal(1)                    
                elif self.attackidx == 3: # push
                    self.targetlist = list()
                    generate_movement(2)
                elif self.attackidx == 4: # grab
                    targetlist = ["head", "lBoob", "rBoob", "pussy"]
                elif self.attackidx == 5: # dirty
                    self.dirtyattack = True
                    dirtyattacklist = ["pussyknee", "headbutt", "bite"]
                    roll  = renpy.randint(0, len(dirtyattacklist-1))
                    if roll == 0:
                        targetlist = ["pussy"]
                    elif roll == 1:
                        targetlist = ["face"]
                    elif roll == 2:
                        targetlist = ["lBoob", "rBoob"]
            else:
                # no current holds
                targetlist = ["head", "lBoob", "rBoob", "pussy"]

            
        def get_normal_target(self):
            if self.attackidx == 0:  # wild swing
                targetlist = ["head", "face", "neck", "lArm", "rArm", "lBoob", "rBoob", "stomach", "pussy"]
            elif self.attackidx == 1:  # jab
                targetlist = ["head", "face", "lBoob", "rBoob", "stomach"]
            elif self.attackidx == 2:  # cross
                targetlist = ["head", "face", "lBoob", "rBoob", "stomach"]
            elif self.attackidx == 3:  # hook
                targetlist = ["head", "face", "lBoob", "rBoob", "stomach"]
            elif self.attackidx == 4:  # uppercut
                targetlist = ["head", "face", "lBoob", "rBoob", "stomach"]
            elif self.attackidx == 5:  # drop
                targetlist = ["head", "face", "lBoob", "rBoob"]
            elif self.attackidx == 6:  # cover up
                targetlist = list()
                self.defending[self.attacker] = True
            elif self.attackidx == 7:  # clinch
                targetlist = list()
                self.clinch = True
            elif self.attackidx == 8:  # disengage
                targetlist = list()
                create_movement(self.defender)                        
                
            elif self.attackidx == 9:  # dirty
                dirtyattacklist = ["knee", "kick", "grind", "headbutt", "bite"]
                if self.rules > 1:
                    dirtyattacklist.append(grab)
                roll  = renpy.randint(0, len(dirtyattacklist-1))


        def get_counter(self):
            A = 1
            
            
        def calculate_damage(self):
            if self.clinch:
                # increment arousal from being in clinch
                increment_arousal(1)
                                     
            damage = 0
            # max damage = mod strength + mod skill + fight damage mod - attacker average pain - tiredness mod
            self.maxdamage = fighterlist[self.attacker].stats.strength/STRENGTH_TO_DAMAGE + getattr(self.fighterlist[self.attacker].fighterData, self.fighttype).skill/SKILL_TO_DAMAGE + self.damagemod - self.fighterlist[self.attacker].fightStats.averagePain - (self.fighterlist[self.attacker].fightstats.energymax-self.fighterlist[self.attacker].fightStats.energy)/ENERGY_DROP_MULT
            if self.maxdamage > 1:
                damage += renpy.randint(1, self.maxdamage)
            else:
                damage += 1
                
            if self.dirtyattack:
                damage += self.dirtydamage
                self.maxdamage += self.dirtydamage
                
            if self.defending[self.defender]:
                # if defender is defending reduce damage by mod skill
                damage -= getattr(self.fighterList[defender].fighterData, self.fighttype).skill/SKILL_TO_DAMAGE
                
            # increment damage by injury level
            if getattr(self.fighterlist[self.defender].stats.injury, self.attackresult[1]) > 0:
                damage += getattr(self.fighterlist[self.defender].stats.injury, self.attackresult[1])
            self.attackresult[2] = damage
            
            
        def update_location(self):
            A = 1
        def update_momentum(self):
            A = 1
        def update_strip_level(self):
            A = 1
        def update_dirty_level(self):
            if self.dirtyattack:
                self.dirtycount += 1
                roll = randint(0, self.dirtycount)
                if roll > self.dirtymax * self.dirtycount:
                    # the dirtier the fight gets, the more it takes to make it dirtier
                    self.dirtylevel += 1
                
        def cleanup_round(self):
            A = 1


        def generate_text(self):
            A = 1
        
        
        def update_strip_level(self):
            
            
        def create_movement(self, mover):
            dir = (0,0,0)
            while not any(dir):
                dir[0] = renpy.randint(-1,1)
                dir[1] = renpy.randint(-1,1)
            self.move = [mover, dir[0], dir[1]]
            
            
        def do_finish(self):

        def update_position(self):
            if self.move[0] == 2:
                # both move
            else:
                # one moves

        def update_arousal(self, val):
            for fighter in fighterList:
                # increment arousal
                fighter.fightStats.arousal += val
            
            
    class TitfightModule:
        def __init__(self, fighter1, fighter2, fightattire, rules,  location):
            self.fighter1 = figher1
            self.fighter2 = fighter2
            self.fightattire = fightattire
            self.rules = rules
            self.location = location
            self.momentum = 0
            self.prevmomentum = 0
            self.attackresult = [0,"",0,0]

             
        def evaluateDamage(self, damage, fighter1, target):
             
        def face_off(self):
            
        def run_turn(self):
            
        def do_finish(self):
            
        def create_fight_text(self):

            
    class CatfightModule:
        def __init__(self, fighter1, fighter2, fightattire, rules,  location):
            self.fighter1 = figher1
            self.fighter2 = fighter2
            self.fightattire = fightattire
            self.rules = rules
            self.location = location
            self.momentum = 0
            self.prevmomentum = 0
            self.attackresult = [0,"",0,0] # Target fighter, body part, damage, attacker energy drain


        def evaluateDamage(self, damage, fighter1, target):
         
        def face_off():
            
        def run_turn(inititativeresult):
            
        def do_finish():

            
    class SexfightModule:
        def __init__(self, fighter1, fighter2, fightattire, rules,  location):
            self.fighter1 = figher1
            self.fighter2 = fighter2
            self.fightattire = fightattire
            self.rules = rules
            self.location = location
            self.momentum = 0
            self.prevmomentum = 0
            self.attackresult = [0,"",0,0]

             
        def evaluateDamage(self, damage, fighter1, target):
             
        def face_off():
            
        def run_turn():
            
        def do_finish():

            
    class WrestlingModule:
        def __init__(self, fighter1, fighter2, fightattire, rules,  location):
            self.fighter1 = figher1
            self.fighter2 = fighter2
            self.fightattire = fightattire
            self.rules = rules
            self.location = location
            self.momentum = 0
            self.prevmomentum = 0
            self.attackresult = [0,"",0,0]

             
        def evaluateDamage(self, damage, fighter1, target):
             
        def face_off():
            
        def run_turn():
            
        def do_finish():

            
    class StreetFightModule:
        def __init__(self, fighter1, fighter2, fightattire, rules,  location):
            self.fighter1 = figher1
            self.fighter2 = fighter2
            self.fightattire = fightattire
            self.rules = rules
            self.location = location
            self.momentum = 0
            self.prevmomentum = 0
            self.attackresult = [0,"",0,0]

             
        def evaluateDamage(self, damage, fighter1, target):
             
        def face_off():
            
        def run_turn():
            
        def do_finish():

            
label execute_fight(fighter1, fighter2, fighttype, fightattire, rules, location):
    return
   
l
