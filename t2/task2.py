def read_line(line):
    list = []
    for i in line.split():
        list.append(i)
    return list


def count_neighbours(arr, i, j):
    count = -1
    height = len(arr)
    for x in range(i-1, i+2):
        try:
            width = len(arr[x])
            for y in range(j-1, j+2):
                if 0 <= x < height and 0 <= y < width:
                    count += 1
        except Exception as e:
            pass
    return count



arr = []
# Read array
with open('input2.txt') as file_input:
    for line in file_input.readlines():
        arr.append(read_line(line))

# Count neighbours
for row in range(len(arr)):
    for col in range(len(arr[row])):

        arr[row][col] = count_neighbours(arr, row, col)

with open('output1.txt', 'w') as file_output:
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            file_output.write(str(arr[row][col]) + " ")

        file_output.write('\n')

