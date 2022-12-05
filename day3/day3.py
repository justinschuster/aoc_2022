# each rucksack has two compartments
# failed packing for 1 item per rucksack
# find errors
# A != a
# first half of items = carpartment 1, etc

def get_input():
    with open('day3/day3_input') as file:
        return file.readlines()

def halve_string(s):
    n = len(s)
    string1 = s[:len(s)//2]
    string2 = s[len(s)//2:]
    return string1, string2

def get_priority_lower(c):
    return ord(c) - 96

def get_priority_upper(c):
    return ord(c) - 38

def compare(string1, string2):
    for c in string1:
            for d in string2:
                print('{} {}'.format(c, d))
                if c == d:
                    if c.isupper():
                        return get_priority_upper(c)
                    else:
                        return get_priority_lower(c)
# Part 1
def both_compartments(lines):
    score = 0
    for line in lines:
        string1, string2 = halve_string(line)
        score += compare(string1, string2)
    return score

lines = get_input()

# Part 1
score = both_compartments(lines)
print('Part One: {}'.format(score))