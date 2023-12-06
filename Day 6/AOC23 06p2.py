file_path = "Day 6/input.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]

concatenate_nums = lambda lst: int(''.join(lst))

new_time = [word.strip() for word in lines_array[0].split()[1:] if word.strip()]
new_distance = [word.strip() for word in lines_array[1].split()[1:] if word.strip()]

time = concatenate_nums(new_time)
distance = concatenate_nums(new_distance)
wins = 1

race_wins = 0
for i in range(time):
    outcome = (time - i) * i
    if outcome > distance: race_wins += 1

if race_wins > 0: wins *= race_wins

print(f"wins: {wins}")