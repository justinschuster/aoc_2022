# Day 4 Advent of Code

def get_input():
    with open('day4/day4_input') as file:
        return file.readlines()

def find_complete_overlap(lines):
    num_contained = 0
    for line in lines:
        schedules = [i.split('-') for i in line.strip().split(',')]
        if int(schedules[0][0]) <= int(schedules[1][0]) and int(schedules[0][1]) >= int(schedules[1][1]):
            num_contained += 1
        elif int(schedules[1][0]) <= int(schedules[0][0]) and int(schedules[1][1]) >= int(schedules[0][1]):
            num_contained += 1
    return num_contained

def find_any_overlap(lines):
    num_contained = 0
    for line in lines:
        schedules = [i.split('-') for i in line.strip().split(',')]
        if int(schedules[0][0]) <= int(schedules[1][0]) and int(schedules[0][1]) >= int(schedules[1][0]):
            num_contained += 1
        elif int(schedules[0][0]) <= int(schedules[1][1]) and int(schedules[0][1]) >= int(schedules[1][1]):
            num_contained += 1
        elif int(schedules[1][0]) <= int(schedules[0][0]) and int(schedules[1][1]) >= int(schedules[0][0]):
            num_contained += 1
        elif int(schedules[1][0]) <= int(schedules[0][1]) and int(schedules[1][1]) >= int(schedules[0][1]):
            num_contained += 1
    return num_contained

lines = get_input()

# Part One
print('Part One: {}'.format(find_complete_overlap(lines)))

# Part Two
print('Part Two: {}'.format(find_any_overlap(lines)))