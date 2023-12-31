file_path = "Day 1/input.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]

nums = []

for lin in lines_array:
    tempArray = []
    numWords = [("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"),
    ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9"),
    ("1", "1"), ("2","2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8"), ("9", "9")]

    for word in numWords:
        spelled = word[0]
        actual = word[1]
        indices = [index for index in range(len(lin)) if lin.startswith(spelled, index)]

        if len(indices) > 0:
            for eachInd in indices:
                tempArray.append((actual, eachInd))

    sorted_list = sorted(tempArray, key=lambda x: x[1])
    fullNum = int(sorted_list[0][0] + sorted_list[-1][0])
    nums.append(fullNum)

print(sum(nums))