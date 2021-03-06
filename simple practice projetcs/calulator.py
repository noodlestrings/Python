
import math

running = True
ans = 0
while running:
    print("These are the operators available:")
    print("'+'          '-'          '/'          '*'\n'sqrt'       'square'\n'sin(x)'     'cos(x)'     'tan(x)'")
    print("'log(x)' - base 10        'ln(x)'      'logY(x)'")
    print("Enter 'q' to quit")
    operation = input("Please enter an operator: ")

    def add(ans):
        numsToAdd = []
        numberOfAdds = int(
            input("Enter the number of numbers that you would like to add: "))
        for i in range(numberOfAdds):
            inp = float(input(f"Enter number {i+1}: "))
            numsToAdd.append(inp)
        total = sum(numsToAdd)
        ans = total
        print(total)
        return ans

    def minus(ans):
        print("The operation will take place as follows: (first number) - (second number)")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        ans = result
        print(result)
        return ans

    def divide(ans):
        numerator = float(input("Please enter the numerator: "))
        denominator = float(input("Please enter the denominator: "))
        result = numerator/denominator
        ans = result
        print(result)
        return ans

    def multiply(ans):
        numsToMultiply = []
        numberOfMultiplications = int(
            input("Enter the number of numbers that you would like to multiply: "))
        for i in range(numberOfMultiplications):
            inp = float(input(f"Enter number {i+1}: "))
            numsToMultiply.append(inp)
        total = math.prod(numsToMultiply)
        ans = total
        print(total)
        return ans

    def log(ans):
        logNum = float(
            input("Enter the number that you want to find the log (base 10) of: "))
        result = math.log10(logNum)
        ans = result
        print(result)
        return ans

    def ln(ans):
        logNum = float(
            input("Enter the number that you want to find the natural log of: "))
        result = math.log(logNum)
        ans = result
        print(result)
        return ans

    def logY(ans, logBase):
        # logBase = float(
        #    input("Enter the log base that you want to operate with: "))
        logNum = float(
            input(f"Enter the number you want to find the log of (in base {logBase}): "))
        result = math.log(logNum, logBase)
        ans = result
        print(result)
        return ans

    if operation == "+":
        add(ans)
    elif operation == "-":
        minus(ans)
    elif operation == "/":
        divide(ans)
    elif operation == "*":
        multiply(ans)
    elif "ln" in operation.lower():
        ln(ans)
    elif "log" in operation.lower() and len(operation) == 3 or operation[3] == "(":
        log(ans)

    elif operation.lower() == "q":
        pass
        running = False
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for digit in digits:
        if digit in operation:
            logY(ans, int(operation[3:]))
            break
