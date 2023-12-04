file_path = "Day 4/input.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]

winning_numbers = {}
scratch_cards = {}
index = 0

for lin in lines_array:
    card_number = ""
    for char in range(8):
        if lin[char].isdigit():
            card_number += lin[char]

    winning_numbers[card_number] = (lin[(lin.index(":") + 2):(lin.index("|") - 1)].split(" "))
    scratch_cards[card_number] = [lin[(lin.index("|") + 2):].split(" ")]

def remove_blank_winner_strings(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, list):
            dictionary[key] = [item for item in value if item != ""]

def remove_blank_card_strings(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, list):
            for inner_list in value:
                if isinstance(inner_list, list):
                    inner_list[:] = [item for item in inner_list if item != ""]

def check_winning_conditions(dictionary):
    for key, value in dictionary.items():
        for card in value:
            total_winnings = 0
            for nums in card:
                if nums in winning_numbers[key]:
                    total_winnings += 1
            for i in range(total_winnings):
                card_key = str(int(key) + i + 1)
                card_to_copy = dictionary[card_key][0]
                dictionary[card_key].append(card_to_copy)

remove_blank_winner_strings(winning_numbers)
remove_blank_card_strings(scratch_cards)
check_winning_conditions(scratch_cards)

total_in_scratch_cards = 0
for key, value in scratch_cards.items():
    total_in_scratch_cards += len(value)

print(f"Total in Scratch Cards: {total_in_scratch_cards}")