file_path = "Day 3/input.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]

schematic_array = []
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_', '=', '/']
numString = ""
numSum = 0
validDict = {}

for lin in lines_array:
    row = []
    for char in lin:
        row.append(char)
    schematic_array.append(row)

def createWindow(row, col):
    window = []

    for i in range(col - 1, col + 2):
        row_window = []
        for j in range(row - 1, row + 2):
            if 0 <= i < len(schematic_array) and 0 <= j < len(schematic_array[0]):
                row_window.append(schematic_array[i][j])
            else:
                row_window.append("~")
        window.append(row_window)
    return window

def checkWindow(window, row, col):
    for i in range(0, len(window)):
        for j in range(0, len(window[0])):
            if window[i][j] == '*':
                return (False, (row + (i - 1), col + (j - 1)))
    return True, None

def calculateGrandTotal(valid_dict):
    grandTotalSum = 0

    for key, value in valid_dict.items():
        if isinstance(value, set) and len(value) == 2:
            valueList = list(value)
            product = valueList[0] * valueList[1]
            grandTotalSum += product

    return grandTotalSum

for i in range(0, len(schematic_array)):
    flagArray = []
    for j in range(0, len(schematic_array[0])):
        if schematic_array[i][j].isdigit():
            numString += schematic_array[i][j]
            window = createWindow(j, i)
            flagArray.append(checkWindow(window, i, j))
            if j == len(schematic_array[0]) - 1 or schematic_array[i][j+1] == "." or schematic_array[i][j+1] in symbols:
                foundFlag = True
                for each in flagArray:
                    if each[0] == False:
                        foundFlag = False
                        if each[1] in validDict:
                            if int(numString) not in validDict[each[1]]:
                                validDict[each[1]].add(int(numString))
                        else:
                            validDict[each[1]] = {int(numString)}
                numString = ""
                flagArray = []

print(f"Grand Total: {calculateGrandTotal(validDict)}")






