#function for checking if value entered is int
def get_int():
    try:
        return int(input("Type an integer:"))
    except ValueError:
        print("Not an integer.")
        return get_int() 
#function for checking if value entered is int   

#get result of function so its only called once
function_result = get_int()
#get result of function so its only called once

#calculations for cubing and squaring the number
cube_calc = function_result**3
square_calc = function_result**2
#calculations for cubing and squaring the number

#options to make sure that difference is printed as positive
total_calc_pos = cube_calc - square_calc
total_calc_neg = square_calc - cube_calc
#options to make sure that difference is printed as positive 


if (cube_calc - square_calc) < 0:
	print(total_calc_neg)
elif (cube_calc - square_calc) > 0:
	print(total_calc_pos)
