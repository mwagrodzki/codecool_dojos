import sys

firstNumber = int(sys.argv[1])
secondNumber = int(sys.argv[2])

while secondNumber != 0:
    if firstNumber > secondNumber:
        firstNumber = firstNumber - secondNumber
    else:
        secondNumber = secondNumber - firstNumber

print("Greatest common divisor of "+sys.argv[1]+" and "+sys.argv[2]+" is "+str(firstNumber))
#54 888 > 6
#42 56 > 14