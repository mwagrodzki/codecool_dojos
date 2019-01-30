import random

x, y = 0, 0

x_table = [x, x, x-1, x+1, x]
y_table = [y, y-1, y, y, y+1]
    
coordinates = zip(x_table, y_table)
coordinates = set(coordinates)

print(coordinates)

for k, i in coordinates:
    print("%d %d" % (k, i))
    if k == -1:
        break



a = random.randrange(0,10)

print(a)