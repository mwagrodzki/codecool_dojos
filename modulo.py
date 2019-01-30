counter = 0

for i in range(1000, 99, -1):
    if i%7==0 or i%9==0:
        counter += 1
        print(str(counter)+". "+str(i))
        if counter == 25:
            break