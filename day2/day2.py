my_scoring = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

scoring_guide = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

hands = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

def get_input():
    with open('day2/day2_input') as file:
        lines = file.readlines()
    return lines

def scoring(lines):
    score = 0
    for line in lines:
        line = line.strip().split(' ')
        score += my_scoring[line[1]]
        if line[1] == scoring_guide[line[0]]:
            score += 6
        elif line[1] == hands[line[0]]:
            score += 3
    return score  

lines = get_input()

# Part One
score = scoring(lines)
print('Final Score: {}'.format(score))