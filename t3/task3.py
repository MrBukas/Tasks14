from student import Student

def read_student(line):
    parts = line.split()
    return Student(
        fio=f"{parts[0]} {parts[1]} {parts[2]}",
        course=parts[3],
        group=parts[4]
    )


students = []
with open('input3.txt') as file_input:
    for line in file_input:
        students.append(read_student(line))


for st in students:
    print(st)

students.sort()
print()

for st in students:
    print(st)

with open('output3.txt', 'w') as file_output:
    for std in students:
        file_output.write(str(std) + '\n')




