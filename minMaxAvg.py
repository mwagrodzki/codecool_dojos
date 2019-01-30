def minimum(list):
    k = list[0]
    iteration = 1

    while iteration < len(list):
        if k > list[iteration]:
            k = list[iteration]
        iteration += 1
    print("Minimum "+str(k))
    #https://www.draw.io/#G1kovDyIns99OfjnCnf15F8nxLYobvYJG2

def maximum(list):
    k = list[0]
    iteration = 1

    while iteration < len(list):
        if k < list[iteration]:
            k = list[iteration]
        iteration += 1
    print("Maximum "+str(k))
    #https://www.draw.io/#G1FSsQYABTbQrwr_KuPFKGFPNMbVSB6uC4

def average(list):
    k = 0
    iteration = 0

    while iteration < len(list):
        k = k + list[iteration]
        iteration += 1
    print("Average "+str(k/len(list)))
    #https://www.draw.io/#G1gof1tcRbnN3C8UbEJ35QXdzIxm770ssN

def classMin(list):
    a = 0
    i = 1
    l = len(list)
    for i in range(1,l):
        if list[i] < list[a]:
            a = i
    print("classMin "+ str(list[a]))

numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
#numbers = [-5, 23, 0, "kitten", -9, 12, 99, [2, 44], None, 105, -43]

minimum(numbers)
classMin(numbers)
maximum(numbers)
average(numbers)


asd = [1, None, 3, [4, 5], 6]

for sublist_or_el in asd:
    if isinstance(sublist_or_el, int):
        print("sublist "+str(sublist_or_el))
