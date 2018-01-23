
# From events.rpy
class GameEvents():
    def __init__(self): pass

    def setGameEvents(self):
        self.watchedCindyTrainingVideo = False

        return


class BodyParts:
    def __init__(self):
        self.head = 0
        self.face = 0
        self.neck = 0
        self.lArm = 0
        self.rArm = 0
        self.back = 0
        self.lBoob = 0
        self.rBoob = 0
        self.stomach = 0
        self.pussy = 0
        self.lLeg = 0
        self.rLeg = 0


class FightRecords:
    def __init__(self):
        self.skill = 0
        self.standing = 0
        self.win = 0
        self.loss = 0
        self.humil = 0
        self.revenge = 0
        self.champion = 0
        self.currChampion = False


class FightStats:
    def __init__(self):
        self.health = 0
        self.healthmax = 0
        self.energy = 0
        self.energymax = 0
        self.arousal = 0
        self.arousalmax = 20
        self.rage = 0
        self.ragemax = 20
        self.pain = BodyParts()
        self.averagepain = self.calculate_average_pain()
        self.damage = BodyParts()
        self.topdamage = 0  # for stripping top
        self.bottomdamage = 0  # for stripping bottom

    def calculate_average_pain(self):
        k = 0
        total = 0
        for key, val in self.pain.__dict__.iteritems():
            total += val
            k += 1
        return total / float(k)


class FighterData:
    def __init__(self, fighttypes):
        self.dirtyFighter = 0
        self.readyToFight = True
        for tuple in fighttypes:
            setattr(self, tuple[0], FightRecords())


class BodyStats:
    def __init__(self, sex):
        self.weight = 180
        self.bodyType = 0  # 0, 1, 2, 3: normal, athletic, voluptous, out of shape
        self.heightType = 0  # 0, 1, 2 : short, normal, tall
        if sex == "m":
            self.cockSize = 0  # 0, 1, 2 big, huge, enormous
        elif sex == "f":
            self.breastSize = 0  # 0, 1, 2: big, huge, enormous
            self.breastType = 1  # 0, 1, 2: Soft, heavy, dense


class CharacterStats:
    def __init__(self):
        self.strength = 5
        self.fitness = 5
        self.endurance = 5
        self.speed = 5
        self.charisma = 5
        self.sexperience = 5
        self.confidence = 5
        self.confidenceMax = 30
        self.fame = 0
        self.mood = 25
        self.moodMax = 30
        self.currInjury = 0
        self.totalInjury = 0
        self.injury = BodyParts()


class GeneralValues:
    def __init__(self):
        self.money = 500


class SexValues:
    def __init__(self):
        self.orientation = 0  # 0, 1, 2: bi, hetero, homo
        self.orgasm = 0
        self.orgasmMax = 30
        self.arousal = 0
        self.exhibitionist = 0
        self.exhibitionistMax = 30
        self.groupSexEnabled = False
        self.groupSexList = []


class InterRelationStats:
    def __init__(self, charList):
        for name in charList:
            setattr(self, name, InterRelationStatsValues)

    def __iter__(self):
        for attr, value in self.__dict__.iteritems():
            yield attr


class InterRelationStatsValues:
    def __init__(self):
        self.attraction = 0
        self.attractionMax = 20
        self.anger = 0
        self.angerMax = 20
        self.intimidated = 0
        self.intimidatedMax = 20
        self.favors = 0
        self.favorsMax = 20
        self.lastFight = ""


class CharacterContainer:
    def __init__(self, id, fname, lname, sex, charList, fighttypes):
        self.id = id
        if id == 0:
            self.gameEvents = GameEvents()
            self.gameEvents.setGameEvents()

        self.active = True
        self.fname = fname
        self.lname = lname
        self.sex = sex
        self.textColor = "#c8ffc8"
        self.clothes = ""
        self.worksForPlayer = False

        self.location = ""

        self.generalValues = GeneralValues()
        self.stats = CharacterStats()
        self.fightStats = FightStats()
        self.bodyStats = BodyStats(sex)
        self.sexValues = SexValues()

        self.interRelation = InterRelationStats(charList)

        if sex == "f":
            self.fighterData = FighterData(fighttypes)

    def group_sex_update(self):
        for character in dict(self.interRelation):
            if not character == "Player":
                if self.interRelation.character.attraction > 10:
                    self.sexValues.groupSex = True
                    if character not in self.sexValues.groupSexList:
                        self.sexValues.groupSexList.append((character, character))
                else:
                    if character in self.sexValues.groupSexList:
                        self.sexValues.groupSexList.pop(character)

    # TODO: Create this
    # def run_end_of_day(self):
    #     recover()
    #     update_relations()

    def update_injury_count(self):
        total = 0
        for key, val in self.fightStats.__dict__.iteritems():
            total += val
        self.stats.currInjury = total

    # def recover():
    #
    # def update_relations():