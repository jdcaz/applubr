import characters
import combat

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

charList = ["Player", "Sunny", "Cindy", "Denisa"]

Cindy = characters.CharacterContainer(1, "Cindy", "MacGreggor", 'f', charList, combat.fighttypes)

Cindy.clothes = "gymClothes"
Cindy.textColor = charTextColor["Cindy"]
Cindy.worksForPlayer = True
Cindy.location = "Boxing gym"

Cindy.generalValues.confidence = 5
Cindy.generalValues.fame = 3
Cindy.generalValues.money = 200

Cindy.stats.strength = 6
Cindy.stats.fitness = 5
Cindy.stats.endurance = 5
Cindy.stats.charisma = 5
Cindy.stats.sexperience = 5
Cindy.stats.ap = 50

Cindy.bodyStats.weight = 175
Cindy.bodyStats.bodyType = 1
Cindy.bodyStats.heightType = 1
Cindy.bodyStats.breastSize = 2
Cindy.bodyStats.breastType = 2

Cindy.sexValues.orientation = 0
Cindy.sexValues.orgasm = 0
Cindy.sexValues.arousal = 0
Cindy.sexValues.exhibitionist = 5

Cindy.fighterData.dirtyFighter = 2

Cindy.fighterData.Wrestling.skill = 5
Cindy.fighterData.Wrestling.win = 5
Cindy.fighterData.Wrestling.loss = 3
Cindy.fighterData.Wrestling.humil = 0
Cindy.fighterData.Wrestling.revenge = 0
Cindy.fighterData.Wrestling.injury = 0
Cindy.fighterData.Wrestling.champion = 0
Cindy.fighterData.Wrestling.currChampion = False

Cindy.fighterData.Boxing.skill = 4
Cindy.fighterData.Boxing.win = 3
Cindy.fighterData.Boxing.loss = 3
Cindy.fighterData.Boxing.humil = 0
Cindy.fighterData.Boxing.revenge = 0
Cindy.fighterData.Boxing.injury = 0
Cindy.fighterData.Boxing.champion = 0
Cindy.fighterData.Boxing.currChampion = False

Cindy.fighterData.Catfight.skill = 3
Cindy.fighterData.Catfight.win = 2
Cindy.fighterData.Catfight.loss = 4
Cindy.fighterData.Catfight.humil = 1
Cindy.fighterData.Catfight.revenge = 0
Cindy.fighterData.Catfight.injury = 1
Cindy.fighterData.Catfight.champion = 0
Cindy.fighterData.Catfight.currChampion = False

Cindy.fighterData.Sexfight.skill = 3
Cindy.fighterData.Sexfight.win = 1
Cindy.fighterData.Sexfight.loss = 1
Cindy.fighterData.Sexfight.humil = 0
Cindy.fighterData.Sexfight.revenge = 0
Cindy.fighterData.Sexfight.injury = 0
Cindy.fighterData.Sexfight.champion = 0
Cindy.fighterData.Sexfight.currChampion = False

Cindy.fighterData.Titfight.skill = 4
Cindy.fighterData.Titfight.win = 3
Cindy.fighterData.Titfight.loss = 2
Cindy.fighterData.Titfight.humil = 0
Cindy.fighterData.Titfight.revenge = 0
Cindy.fighterData.Titfight.injury = 0
Cindy.fighterData.Titfight.champion = 0
Cindy.fighterData.Titfight.currChampion = False

Cindy.interRelation.Player.attraction = 30
Cindy.interRelation.Player.anger = 0
Cindy.interRelation.Player.intimidated = 0
Cindy.interRelation.Player.favors = 0

Cindy.interRelation.Denisa.attraction = 5
Cindy.interRelation.Denisa.anger = 10
Cindy.interRelation.Denisa.intimidated = 0
Cindy.interRelation.Denisa.favors = 0

Cindy.interRelation.Sunny.attraction = 5
Cindy.interRelation.Sunny.anger = 2
Cindy.interRelation.Sunny.intimidated = 0
Cindy.interRelation.Sunny.favors = 0

Denisa = characters.CharacterContainer(1, "Denisa", "Jones", 'f', charList, combat.fighttypes)
Denisa.textColor = charTextColor["Denisa"]

Denisa.generalValues.confidence = 5
Denisa.generalValues.fame = 3
Denisa.generalValues.money = 200

Denisa.stats.strength = 5
Denisa.stats.fitness = 5
Denisa.stats.endurance = 6
Denisa.stats.charisma = 5
Denisa.stats.sexperience = 5
Denisa.stats.ap = 50

Denisa.bodyStats.weight = 172
Denisa.bodyStats.bodyType = 1
Denisa.bodyStats.heightType = 1
Denisa.bodyStats.breastSize = 2
Denisa.bodyStats.breastType = 2

Denisa.sexValues.orientation = 0
Denisa.sexValues.orgasm = 0
Denisa.sexValues.arousal = 0
Denisa.sexValues.exhibitionist = 5

Denisa.fighterData.dirtyFighter = 2

Denisa.fighterData.Wrestling.skill = 2
Denisa.fighterData.Wrestling.win = 2
Denisa.fighterData.Wrestling.loss = 5
Denisa.fighterData.Wrestling.humil = 2
Denisa.fighterData.Wrestling.revenge = 0
Denisa.fighterData.Wrestling.injury = 0
Denisa.fighterData.Wrestling.champion = 0
Denisa.fighterData.Wrestling.currChampion = False

Denisa.fighterData.Boxing.skill = 4
Denisa.fighterData.Boxing.win = 4
Denisa.fighterData.Boxing.loss = 3
Denisa.fighterData.Boxing.humil = 0
Denisa.fighterData.Boxing.revenge = 0
Denisa.fighterData.Boxing.injury = 1
Denisa.fighterData.Boxing.champion = 0
Denisa.fighterData.Boxing.currChampion = False

Denisa.fighterData.Catfight.skill = 5
Denisa.fighterData.Catfight.win = 5
Denisa.fighterData.Catfight.loss = 2
Denisa.fighterData.Catfight.humil = 0
Denisa.fighterData.Catfight.revenge = 1
Denisa.fighterData.Catfight.injury = 1
Denisa.fighterData.Catfight.champion = 0
Denisa.fighterData.Catfight.currChampion = False

Denisa.fighterData.Sexfight.skill = 5
Denisa.fighterData.Sexfight.win = 4
Denisa.fighterData.Sexfight.loss = 2
Denisa.fighterData.Sexfight.humil = 1
Denisa.fighterData.Sexfight.revenge = 1
Denisa.fighterData.Sexfight.injury = 0
Denisa.fighterData.Sexfight.champion = 0
Denisa.fighterData.Sexfight.currChampion = False

Denisa.fighterData.Titfight.skill = 4
Denisa.fighterData.Titfight.win = 2
Denisa.fighterData.Titfight.loss = 3
Denisa.fighterData.Titfight.humil = 0
Denisa.fighterData.Titfight.revenge = 0
Denisa.fighterData.Titfight.injury = 1
Denisa.fighterData.Titfight.champion = 0
Denisa.fighterData.Titfight.currChampion = False

Denisa.interRelation.Player.attraction = 10
Denisa.interRelation.Player.anger = 0
Denisa.interRelation.Player.intimidated = 0
Denisa.interRelation.Player.favors = 0

Denisa.interRelation.Cindy.attraction = 5
Denisa.interRelation.Cindy.anger = 10
Denisa.interRelation.Cindy.intimidated = 0
Denisa.interRelation.Cindy.favors = 0

Denisa.interRelation.Sunny.attraction = 5
Denisa.interRelation.Sunny.anger = 2
Denisa.interRelation.Sunny.intimidated = 0
Denisa.interRelation.Sunny.favors = 0


fight = combat.FightModule([Cindy, Denisa], "Boxing", "Normal", "Gloves", "Boxing gym")

fight.run_turn()