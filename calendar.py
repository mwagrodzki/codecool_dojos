def import_schedule():
    with open('meetings.txt', "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(",") for element in lines]
    schedule = {}
    for val in table:
        schedule[int(val[0])] = [int(val[1]), val[2]]
    return schedule

def export_schedule(schedule):
    with open('meetings.txt', "w") as file:
        for key in schedule.keys():
            row = str(key) + ',' + str(schedule[key][0]) + ',' + schedule[key][1] + '\n'
            file.write(row)

def print_schedule(schedule):
    print('Your schedule for the day:')
    if schedule:
        keys = list(schedule.keys())
        keys.sort()
        for key in keys:
            end = schedule[key][0]
            title = schedule[key][1]
            print('{0} - {1} {2}'.format(key, end, title))
    else:
        print('(empty)')

def check_overlapping(schedule, start, duration):
    keys = list(schedule.keys())
    temp = keys[:]
    for key in keys:
        dur = schedule[key][0]
        if (dur-key) == 2:
            temp.append(key + 1)
    if duration == 2:
        if (start + 1) in temp:
            return True
    if start in temp:
        return True
    return False

def new_meeting(schedule):
    print('Schedule a new meeting.')
    title = input('Enter meeting title: ')
    duration = 0
    while duration == 0:
        duration = int(input('Enter duration in hours (1 or 2): '))
        if duration not in [1, 2]:
            duration = 0
    start = 0
    while start == 0:
        start = int(input('Enter start time: '))
        if start < 8 or (start + duration) > 18:
            print('ERROR: Meeting is outside of your working hours (8 to 18)!')
            start = 0
        if(check_overlapping(schedule, start, duration)):
            print('ERROR: Meeting overlaps with existing meeting!')
            start = 0
    schedule[start] = [(start + duration), title]
    print('Meeting added.\n')
    return schedule

def cancel_meeting(schedule):
    print('Cancel an existing meeting.')
    if schedule:
        while True:
            start = int(input('Enter the start time: '))
            if start in schedule:
                schedule.pop(start)
                print('Meeting canceled.\n')
                break
            else:
                print('ERROR: There is no meeting starting at that time!')
    else:
        print('ERROR: There are no meetings to cancel!\n')
    return schedule

def compact_meetings(schedule):
    next_meeting = 8
    keys = list(schedule.keys())
    keys.sort()
    temp = {}
    for key in keys:
        duration = schedule[key][0] - key
        temp[next_meeting] = [next_meeting + duration, schedule[key][1]]
        next_meeting += duration
    return temp

def menu():
    schedule = import_schedule()
    while True:
        print_schedule(schedule)
        print('\nMenu:')
        print('(s) schedule a new meeting')
        print('(c) cancel an existing meeting')
        print('(m) compact meetings')
        print('(q) quit\n')
        choice = input('Your choice: ')
        if choice == 's':
            schedule = new_meeting(schedule)
        elif choice == 'c':
            schedule = cancel_meeting(schedule)
        elif choice == 'm':
            schedule = compact_meetings(schedule)
        elif choice == 'q':
            export_schedule(schedule)
            break

menu()
