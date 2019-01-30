k = 0
j = 1
fibonacci = []

length = int(input("How many fibonacci numbers do you want: "))

for i in range(length):
    fibonacci.append(k)
    j, k = k, j + k

maxLength = len(str(fibonacci[length-1]))
counterLength = len(str(length))+2

for f in range(len(fibonacci)):
    print("{:<{a}}{:>{b}}".format(str(f+1)+".", fibonacci[f],a=counterLength,b=maxLength))
    