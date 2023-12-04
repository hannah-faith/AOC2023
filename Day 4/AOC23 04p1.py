file_path = "Day 4/input.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]

winning_numbers = []
scratch_cards = []
index = 0
total_score = 0
first_flag = True

for lin in lines_array:

    winning_numbers.append(lin[(lin.index(":") + 2):(lin.index("|") - 1)].split(" "))
    scratch_cards.append(lin[(lin.index("|") + 2):].split(" "))

for each in winning_numbers:
    for nums in each:
        if nums == "":
            each.remove(nums)


for each in scratch_cards:
    for nums in each:
        if nums == "":
            each.remove(nums)

    temp_score = 1
    exponent = 0
    final_score = 0
    for nums in each:
        if nums in winning_numbers[index]:
            if first_flag:
                first_flag = False
            else:
                exponent += 1

    if first_flag == False:
        final_score = temp_score * 2**exponent
        total_score += final_score
    index += 1
    first_flag = True

print(f"total score: {total_score}")