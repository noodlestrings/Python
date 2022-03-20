teachers = [['a'], ['b'], ['c'], ['d'], ['e']]
students = [['1'], ['2'], ['3'], ['4'], ['5']]
matches = []
nonMutualMatches = []


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

# test data: a b c c e 1 3 4 2 5

# students : [['1', 'a', 'e'], ['2', 'b'], ['3', 'c'], ['4'], ['5', 'd']]
# teachers : [['a', '1'], ['b', '2'], ['c', '3', '4'], ['d', '5'], ['e']]
# matches: [['1', 'a'], ['4', 'c'], ['5', 'e']]

for teacher in teachers:
    temp = []
    teachmatches = []
    for teachersVotes in teacher[1:]:
        temp.append(teachersVotes)
        teachmatches = temp.copy()
        for student in students:
            studtemp = []
            studmatches = []
            for studentVotes in student:
                studtemp.append(studentVotes)
                studmatches = studtemp.copy()
                if student[0] in teachmatches and teacher[0] in studmatches:
                    studteachmatches = [student[0], teacher[0]]
                    matches.append(studteachmatches)
                    break
print(f"These are the matches: {matches}")


for studentIndex, student in enumerate(students):
    for match in matches:
        if match[0] == student[0]:
            students[studentIndex] = []
studentsRemaining = list(filter(None, students))

for teacherIndex, teacher in enumerate(teachers):
    for match in matches:
        if match[1] == teacher[0]:
            teachers[teacherIndex] = []
teachersRemaining = list(filter(None, teachers))

print(
    f"students remaining:{studentsRemaining}\nteachers remaining:{teachersRemaining}\nmatches:{matches}")

# students remaining:[['2', 'd'], ['3', 'b']]
# teachers remaining:[['b', '2'], ['d']]
# matches:[['1', 'a'], ['4', 'c'], ['5', 'e']]


