def get_input():
    with open('day3/day3_input') as file:
        return file.readlines()

def halve_string(s):
    n = len(s)
    string1 = s[:len(s)//2]
    string2 = s[len(s)//2:]
    return string1, string2

def compare(string1, string2):
    for c in string1:
            for d in string2:
                if c == d:
                    return get_value(c)

def get_value(c):
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96

# Part 1
def both_compartments(lines):
    score = 0
    for line in lines:
        string1, string2 = halve_string(line)
        score += compare(string1, string2)
    return score

def badges(lines):
    score = 0
    for i in range(0, len(lines), 3):
        line1 = lines[i].replace('\n', '')
        line2 = lines[i+1].replace('\n', '')
        line3 = lines[i+2].replace('\n', '')
        common = set(line1).intersection(line2).intersection(line3)
        score += get_value(list(common)[0])
    return score

lines = get_input()

# Part One
score = both_compartments(lines)
print('Part One: {}'.format(score))

# Part Two
score = badges(lines)
print('Part Two: {}'.format(score))