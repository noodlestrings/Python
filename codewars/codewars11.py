# returns binary value of addidtion calculationz\
def add_binary(a, b):
    calc = str(bin(a + b))
    return calc[2 : len(calc)]


print(add_binary(5, 12))
