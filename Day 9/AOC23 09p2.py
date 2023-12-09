file_path = "Day 9/input.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]

sum = 0

history_list = []

for lin in lines_array:
    history_list.append(lin.split(" "))

store_list = []
compare_list = []
index = 0

for each in history_list:
    store_list.append([each])
    compare_list = each

    while any(item != 0 for item in compare_list):

        temp_list = []

        for i in range(len(compare_list) - 1):
            first_num = int(compare_list[i])
            second_num = int(compare_list[i + 1])
            child = second_num - first_num
            temp_list.append(child)

        compare_list = temp_list
        store_list[index].append(temp_list)

    index += 1
    compare_list = []

temp_one = 0

for i in range(len(store_list)):
    store_list[i].reverse()

    for j in range(len(store_list[i]) - 1):
        first_num = temp_one
        second_num = int(store_list[i][j + 1][0])
        temp_one = second_num - first_num

    sum += temp_one
    temp_one = 0

print(f"sum: {sum}")