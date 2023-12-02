import re

file_path = "Day 2/input.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]

def parse_game_input(input_string):
    pattern = re.compile(r'Game (\d+):')
    match = pattern.search(input_string)
    game_number = int(match.group(1))

    turns_str = input_string.split('; ')
    turns_str[0] = turns_str[0][(turns_str[0].index(":") + 2):]

    gameList = [game_number]

    for each in turns_str:
        tempList = each.split(', ')
        turnList = []
        for cubes in tempList:
            turn = cubes.split(' ')
            tempTuple = (int(turn[0]), turn[1])
            turnList.append(tempTuple)
        gameList.append(turnList)

    return gameList


primaryList = []

for each in lines_array:
    primaryList.append(parse_game_input(each))

validGameIds = 0

for each in primaryList:
    gameNum = each[0]
    noGameNum = each[1:]
    flag = True
    for turn in noGameNum:
        for roll in turn:
            if roll[1] == 'red':
                if roll[0] > 12:
                    flag = False
                    break
            if roll[1] == 'green':
                if roll[0] > 13:
                    flag = False
                    break
            if roll[1] == 'blue':
                if roll[0] > 14:
                    flag = False
                    break
    if flag:
        validGameIds += gameNum

print(validGameIds)