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

losing_hands = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
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
        score += scoring_one_line(line[0], line[1])
    return score

def scoring_one_line(opp, player):
    if player == scoring_guide[opp]:
        return 6
    elif player == hands[opp]:
        return 3
    else:
        return 0

# Part 2 scoring
# X means lose
# Y means draw
# Z means win
def new_scoring(lines):
    score = 0
    for line in lines:
        line = line.strip().split(' ')
        if line[1] == 'X':
            hand = losing_hands[line[0]]
            score += my_scoring[hand]
        elif line[1] == 'Y':
            hand = hands[line[0]]
            score += my_scoring[hand]
            score += 3
        elif line[1] == 'Z':
            hand = scoring_guide[line[0]]
            score += my_scoring[hand]
            score += 6
    return score

lines = get_input()

# Part One
score = scoring(lines)
print('Part One: {}'.format(score))

# Part Two
score = new_scoring(lines)
print('Part Two: {}'.format(score))