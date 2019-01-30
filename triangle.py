class ContinueI(Exception):
    pass

def get_list():
    while True:
        try:
            number_string = input("Please provide 6 numbers in the range from -100 to 100 (separated with space): ")
            number_list = number_string.split(' ')
            number_list = [int(i) for i in number_list]
            if len(number_list) != 6:
                continue
            for i in number_list:
                if i > 100 or i < -100:
                    raise ContinueI

            return number_list
        except ValueError:
            pass
        except ContinueI:
            continue


def calculate_area(coordinates):
    x1, y1, x2, y2, x3, y3 = coordinates
    area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    print("Area of the triangle equals: "+str(abs(area)))
    #https://www.mathopenref.com/coordtrianglearea.html

coordinateList = get_list()
calculate_area(coordinateList)

#0 0 0 3 5 0 Your program should print 7.5
#0 0 2 2 4 0 Your program should print 4