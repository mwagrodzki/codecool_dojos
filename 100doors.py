def generateDoors(length):
    a = []
    for i in range(length):
        a.append(0)
    return a
def printDoors(doorList):
    string = "The following doors are open: "
    for i in range(len(doorList)):
        if doorList[i] == 1:
            string = string + str(i+1)+", "
    print(string[:len(string)-2])

doors = generateDoors(100)
#0 closed, 1 open
for i in range(len(doors)):
    for j in range(len(doors)):
        if (j+1)%(i+1) == 0:
            doors[j] = 1-doors[j]

printDoors(doors)