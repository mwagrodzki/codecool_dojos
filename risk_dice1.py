import random

def getSides(unitMin, unitMax, side):
    while True:
        try:
            result = int(input("How many units between "+str(unitMin)+" and "+str(unitMax)+" for "+str(side)+" side: "))
            if unitMin <= result <= unitMax
            #if unitMin <= result and result <= unitMax:
                return result
        except ValueError:
            continue

def getUnits(unitNumber):
    unitList = []
    for i in range(unitNumber):
        unitList.append(random.randrange(1,6))

    unitList.sort(reverse=True)
    return unitList

def printSides(attackList, defenseList):
    print()
    print("Dice:")
    print("  Attacker: "+ str(attackList).replace('[','').replace(', ','-').replace(']',''))
    print("  Defender: "+ str(defenseList).replace('[','').replace(', ','-').replace(']',''))

def outcome(attackList, defenseList):
    attackerLoss = 0
    defenderLoss = 0
    battleNumber = 0

    if len(defenseList) <= len(attackList):
        battleNumber = len(defenseList)
    else:
        battleNumber = len(attackList)

    for i in range(battleNumber):
        if attackList[i] > defenseList[i]:
            defenderLoss+=1
        else:
            attackerLoss+=1
    print()
    print("Outcome:")
    print("  Attacker: Lost "+ str(attackerLoss) +" units")
    print("  Defender: Lost "+ str(defenderLoss) +" units")

attackUnitNumber = getSides(1,3,"attacking")
defenseUnitNumber = getSides(1,2,"defending")

attackUnitList = getUnits(attackUnitNumber)
defenseUnitList = getUnits(defenseUnitNumber)

printSides(attackUnitList, defenseUnitList)
outcome(attackUnitList, defenseUnitList)