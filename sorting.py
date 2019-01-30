def sort(listToSort):
    iterations = 1
    while iterations < len(listToSort):
        j = 0
        while j <= len(listToSort)-2:
            if listToSort[j] > listToSort[j+1]:
                temp = listToSort[j+1]
                listToSort[j+1] = listToSort[j]
                listToSort[j] = temp
            j += 1
        iterations += 1
    print(listToSort)

    
def get_list():
    while True:
        try:
            number_string = input("Please provide a list of numbers separated with space: ")
            sort_list = number_string.split(' ')
            sort_list = [int(i) for i in sort_list]
            print(sort_list)
            return sort_list
        except ValueError:
            continue

#numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]

numbers = get_list()
sort(numbers)