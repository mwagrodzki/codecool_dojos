import sys

number = sys.argv[1]
system = sys.argv[2]

counter = 0
result = 0
if system == '2':
    while counter < len(number):
        result += int(number[counter]) * (2**(len(number) - counter - 1))
        counter += 1
    result = str(int(result))
    system = '10'

elif system == '10':
    number = int(number)
    result = ''
    while number > 1:
        result += str(int(number % 2))
        number = number / 2
    result = result[::-1]
    system = '2'
    while len(result) % 4 != 0:
        result = '0' + result

string = '| %s | %s |' % (result, system)

print('/'+'-'*(len(string)-2)+'\\')
print(string)
print('\\'+'-'*(len(string)-2)+'/')
