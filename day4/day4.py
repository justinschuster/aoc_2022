# Day 4 Advent of Code

schedules = []

def get_input():
    with open('day4/day4_input') as file:
        return file.readlines()

def read_schedules(lines):
    num_contained = 0
    for line in lines:
        schedules = [i.split('-') for i in line.strip().split(',')]
        if int(schedules[0][0]) <= int(schedules[1][0]) and int(schedules[0][1]) >= int(schedules[1][1]):
            num_contained += 1
        elif int(schedules[1][0]) <= int(schedules[0][0]) and int(schedules[1][1]) >= int(schedules[0][1]):
            num_contained += 1
    return num_contained

lines = get_input()
print(read_schedules(lines))