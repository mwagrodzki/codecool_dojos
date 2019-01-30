def getNumber():
    while True:
        try:
            result = int(input("How many units greater than 0 and less than 4000: "))
            if result > 0 and result < 4000:
                return result
        except ValueError:
            continue

data = [
    (1000, 'M'),
    (900, 'CM'),
    ...
]

def romanize(number):
    roman = ''
    temp = number
    while temp > 0:
        if temp >= 1000:
            roman += "M"
            temp -= 1000
        elif temp >= 900:
            roman += "CM"
            temp -= 900
        elif temp >= 500:
            roman += "D"
            temp -= 500
        elif temp >= 400:
            roman += "CD"
            temp -= 400
        elif temp >= 100:
            roman += "C"
            temp -= 100
        elif temp >= 90:
            roman += "XC"
            temp -= 90
        elif temp >= 50:
            roman += "L"
            temp -= 50
        elif temp >= 40:
            roman += "XL"
            temp -= 40
        elif temp >= 10:
            roman += "X"
            temp -= 10
        elif temp >= 9:
            roman += "IX"
            temp -= 9
        elif temp >= 5:
            roman += "V"
            temp -= 5
        elif temp >= 4:
            roman += "IV"
            temp -= 4
        elif temp >= 1:
            roman += "I"
            temp -= 1
    print("Roman representation of number "+str(number)+" is: "+roman)

arabic = getNumber()
romanize(arabic)

#https://en.wikipedia.org/wiki/Roman_numerals#Basic_decimal_pattern