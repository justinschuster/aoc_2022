def get_input():
    with open('day1_input') as file:
        lines = file.readlines()
    return lines

def total_calories(lines):
    elf_calories = 0
    for line in lines:
        if line == '\n':
            continue
        else:
            line.replace('n', '')
            elf_calories += int(line)
    print(elf_calories)

def ind_elf_cals(lines):
    elf_calories = []
    curr_elf_count = 0
    for line in lines:
        if line == '\n':
            elf_calories.append(curr_elf_count)
            curr_elf_count = 0
        else:
            line.replace('\n', '')
            curr_elf_count += int(line)
    return elf_calories

def top_three(ind_elf_cals):
    sum = 0
    for i in range(3):
        max_cal = max(ind_elf_cals)
        sum += max_cal
        ind_elf_cals.remove(max_cal)
    print(sum)

lines = get_input()
cals = ind_elf_cals(lines)
top_three(cals)