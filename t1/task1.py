def read_list(line):
    list = []
    for i in line.split():
        list.append(i)
    return list


def join_lists(l1, l2):
    total_list = []
    for i in l1:
        total_list.append(i)
    for i in l2:
        total_list.append(i)
    total_list.sort()
    return total_list


with open('input1.txt') as file_input:
    list1 = read_list(next(file_input))
    list2 = read_list(next(file_input))
    print(list1)
    print(list2)
res = join_lists(list1, list2)
print(res)
with open('output1.txt', 'w') as file_output:
    for elem in res:
        file_output.write(elem + ' ')

