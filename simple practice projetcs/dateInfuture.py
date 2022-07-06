from datetime import date
current = str(date.today())

current = current.split("-")
"""[year, month, day]"""
print(current)

isLeapYear = False
if int(current[0]) % 4 == 0:
    isLeapYear = True

#MAKE SURE FEBRUARY IS COUNTED FOR
numberOfDays = [["01", 31], ["02", 28], ["03", 31], ["04", 30], ["05", 31], ["06", 30], ["07", 31], ["08", 31], ["09", 30], ["10", 31], ["11", 30], ["12", 31]]

userq = int(input("How many days into the future would you like to know the date for: "))

count=0
workingMonth=""
breakPrimLoop=False

#THIS LOOPS FROM THE 1ST OF JAN NOT FROM USERQ YET
for month in numberOfDays:
    if breakPrimLoop:
        break
    dayOfMonth = 0
    for i in range(1, month[1] + 1):
        workingMonth=month[0]
        if count != userq:
            dayOfMonth += 1
            count+=1
        else:
            breakPrimLoop = True
            break

print(f"day of the month : {dayOfMonth} \ncount : {count} \nmonth : {workingMonth}")

            