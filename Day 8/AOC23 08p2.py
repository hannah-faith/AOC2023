import math

file_path = "Day 8/input.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]

directions = lines_array[0].split(", ")
lines_array.pop(0)
lines_array.pop(0)
node_dictionary = {}

def create_node_dict(node_map):
    for node in node_map:
        temp_array = node.split(" ")
        temp_array.pop(1)
        temp_array[1] = temp_array[1][1:4]
        temp_array[2] = temp_array[2][:3]

        node_dictionary[temp_array[0]] = [temp_array[1], temp_array[2]]

create_node_dict(lines_array)
current_nodes = []
for key in node_dictionary:
    if key[2] == "A":
        current_nodes.append(key)

current_node = ""
steps = 0
flag = True
final_steps = []

for every_start in current_nodes:
    steps = 0
    flag = True
    current_node = every_start
    while flag:
        for each in directions[0]:
            steps += 1
            if each == "R":
                current_node = node_dictionary[current_node][1]
            else:
                current_node = node_dictionary[current_node][0]
            if current_node[2] == "Z":
                flag = False
                final_steps.append(steps)

print(f"final steps: {final_steps}")
print(f"LCM: {math.lcm(*final_steps)}")
