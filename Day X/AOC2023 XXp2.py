file_path = "Day 2/test2.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]

for lin in lines_array:



    print(lin)