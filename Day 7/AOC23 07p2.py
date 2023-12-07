file_path = "Day 7/input.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]


def get_hand_type(card):

    # Hand types
    # 0 = Five of a kind, where all five cards have the same label: AAAAA
    # 1 = Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    # 2 = Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # 3 = Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    # 4 = Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    # 5 = One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    # 6 = High card, where all cards' labels are distinct

    card_one_matches = card.count(card[0])
    letter_count = {}

    for char in card:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    if "J" in letter_count:
        temp_letter_count = {}
        temp_card = ""
        for char in card:
            if char != "J":
                temp_card += char

        for char in temp_card:
            if char in temp_letter_count:
                temp_letter_count[char] += 1
            else:
                temp_letter_count[char] = 1

        if len(temp_letter_count) >= 1:
            largest = max(temp_letter_count, key=temp_letter_count.get)
            card = card.replace("J", largest)

    letter_count = {}

    for char in card:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    if len(letter_count) == 1:
        return 0
    elif len(letter_count) == 2:
        letter1 = list(letter_count.keys())[0]
        letter2 = list(letter_count.keys())[1]
        if letter_count[letter1] == 4 or letter_count[letter2] == 4:
            return 1
        else:
            return 2
    elif len(letter_count) == 3:
        letter1 = list(letter_count.keys())[0]
        letter2 = list(letter_count.keys())[1]
        letter3 = list(letter_count.keys())[2]
        if letter_count[letter1] == 3 or letter_count[letter2] == 3 or letter_count[letter3] == 3:
            return 3
        else:
            return 4
    elif len(letter_count) == 4:
        return 5
    else:
        return 6

def custom_sort(s):
    hand = s[0]
    strength_order = "AKQT98765432J"
    return tuple(strength_order.index(char) for char in hand)

card_list = []
card_list_with_types = []
rank = len(lines_array)
score = 0

for lin in lines_array:
    hand = lin.split()
    card_list.append([hand[0], hand[1]])


for each in card_list:
    hand_type = get_hand_type(each[0])
    card_list_with_types.append([hand_type, each[0], each[1]])

sorted_list = sorted(card_list_with_types, key=lambda x: x[0])
hands_dict = {}

for hand in range(len(sorted_list)):
    current_card_rank = sorted_list[hand][0]
    current_card_hand = sorted_list[hand][1]
    current_card_bet = sorted_list[hand][2]
    if current_card_rank in hands_dict:
        hands_dict[current_card_rank].append([current_card_hand, current_card_bet])
    else:
        hands_dict[current_card_rank] = [[current_card_hand, current_card_bet]]

for key in hands_dict:
    if len(hands_dict[key]) == 1:
        temp_hand = hands_dict[key]
        score += rank * int(temp_hand[0][1])
        rank -= 1
    else:
        temp_list = []

        for each in hands_dict[key]:
            temp_list.append(each)

        sorted_list = sorted(temp_list, key=custom_sort)

        for each in sorted_list:
            score += rank * int(each[1])
            rank -= 1

print(f"score: {score}")



