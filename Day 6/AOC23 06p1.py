file_path = "Day 6/input.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]

new_time = [word.strip() for word in lines_array[0].split(" ")[1:] if word.strip()]
new_distance = [word.strip() for word in lines_array[1].split(" ")[1:] if word.strip()]

wins = 1

for i in range(len(new_time)):
    time = int(new_time[i])
    distance = int(new_distance[i])
    race_wins = 0

    for i in range(time):
        hold = i
        multiplier = time - i
        outcome = multiplier * hold

        if outcome > distance:
            race_wins += 1

    if race_wins > 0:
        wins *= race_wins

print(f"wins: {wins}")