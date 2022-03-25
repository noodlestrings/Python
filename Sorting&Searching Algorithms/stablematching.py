teachers = [['a'], ['b'], ['c'], ['d'], ['e']]
students = [['1'], ['2'], ['3'], ['4'], ['5']]
matches = []
nonMutualMatches = []
leftOver = []


def get_insert_index(array, targetName):
    for masterIndex, masterValue in enumerate(array):
        for subIndex, subValue in enumerate(masterValue):
            if subValue == targetName:
                masterLocation = masterIndex
                subLocation = subIndex + 1
    return [masterLocation, subLocation]


def remove_teachers(matches, teachers):
    for match in matches:
        for teacher in teachers:
            if teacher[0] in match:
                teachers.remove(teacher)


def remove_students(matches, students):
    for match in matches:
        for student in students:
            if student[0] == match[0]:
                students.remove(student)


while len(teachers) >= 1 and len(students) >= 1:
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

    for student in students:
        studentVote = student[1:]
        for teacher in teachers:
            for vote in studentVote:
                if vote in teacher and student[0] in teacher:
                    matches.append([student[0], teacher[0]])

    remove_teachers(matches, teachers)

    remove_students(matches, students)

    for student in students:
        for teacher in teachers:
            for vote in student[1:]:
                if vote == teacher[0]:
                    nonMutualMatches.append([student[0], teacher[0]])
                    remove_teachers(nonMutualMatches, teachers)
                    remove_students(nonMutualMatches, students)

    for teacher in teachers:
        for student in students:
            for vote in teacher[1:]:
                if vote == student[0]:
                    nonMutualMatches.append([student[0], teacher[0]])
                    remove_teachers(nonMutualMatches, teachers)
                    remove_students(nonMutualMatches, students)

    if len(teachers) < 1 and len(students) < 1:
        continue

    for index, student in enumerate(students):
        leftOver.append([student[0], teachers[index][0]])
    teachers.clear()
    students.clear()


# outside of while loop
print("\nThese matches include teachers and students who voted for each other:")
for x in range(len(matches)):

    print(
        f"Student {matches[x][0]} is matched with Teacher {matches[x][1]}")

print("\nThese matches are non-mutual matches (where only one party has voted for the other):")
for x in range(len(nonMutualMatches)):
    print(
        f"Student {nonMutualMatches[x][0]} is matched with Teacher {nonMutualMatches[x][1]}")

print("\nHere are the remaining that did not vote for each other but have been assigned to each other: ")
for x in range(len(leftOver)):
    print(f"Student {leftOver[x][0]} is matched with Teacher {leftOver[x][1]}")
