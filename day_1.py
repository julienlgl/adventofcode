from data.data_1_1 import calories
from util import print_header


def get_calories_by_elf(calories):
    calories_by_elf = []
    current_elf_calories = 0

    for calorie_line in calories:
        # Next elf
        if calorie_line == 0:
            calories_by_elf.append(current_elf_calories)
            current_elf_calories = 0

        # Same elf
        else:
            current_elf_calories = current_elf_calories + calorie_line

    calories_by_elf.sort(reverse=True)

    return calories_by_elf


# PART 1
print_header(day=1, part=1, expected_result=68292)

calories_by_elf = get_calories_by_elf(calories=calories)

print(f"Elf carrying the most calories : {calories_by_elf[0]} [Calories]")


# PART 2
print_header(day=1, part=1, expected_result=203203)

total = 0
for calories in calories_by_elf[:3]:
    total = total + calories

print(f"Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total : {total} [Calories]")
