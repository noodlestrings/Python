from ast import Pass
from operator import indexOf


teachers = [['a'], ['b'], ['c'], ['d'], ['e']]
students = [['1'], ['2'], ['3'], ['4'], ['5']]
matches = []


def get_insert_index(array, targetName):
    for masterIndex, masterValue in enumerate(array):
        for subIndex, subValue in enumerate(masterValue):
            if subValue == targetName:
                masterLocation = masterIndex
                subLocation = subIndex + 1
    return [masterLocation, subLocation]


for i in range(len(students)):
    while True:
        try:
            studVoting = input(
                f"Student {students[i][0]}, please enter the name of the teacher you want to vote for: ")
            getindex = get_insert_index(teachers, studVoting.lower())
            index = getindex[0]
            teachers[index].append(students[i][0])
            print("Vote counted")
            break
        except UnboundLocalError:
            print(
                f"That was not the name of a teacher.")
print("\n")

for i in range(len(teachers)):
    while True:
        try:
            teachVoting = input(
                f"Teacher {students[i][0]}, please enter the name of the student you want to vote for: ")
            getindex = get_insert_index(students, teachVoting.lower())
            index = getindex[0]
            students[index].append(teachers[i][0])
            print("Vote counted")
            break
        except UnboundLocalError:
            print(
                f"That was not the name of a student.")

print(f"teachers : {teachers}\nstudents : {students}")

# test data: a b c c d 1 3 2 5 1

# teachers : [['a', '1'], ['b', '2'], ['c', '3', '4'], ['d', '5'], ['e']]
# students : [['1', 'a', 'e'], ['2', 'b'], ['3', 'c'], ['4'], ['5', 'd']]

#COMPARING AND FINDING MATCHES NOT DONE