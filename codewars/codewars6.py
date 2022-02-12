# someone wants to see how many litres they have to drink given an amount of time in hours. They should drink 0.5 L every hour. The calculation must be rounded
# down if it is a decimal.
import math


def litres(time):
    try:
        calculation = time * 0.5
        return int(calculation)
    except ValueError:
        calculation = time * 0.5
        rounded_calc = calculation.floor()
        return rounded_calc


print(litres(11.8))
