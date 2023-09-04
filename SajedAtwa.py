# question 1
import math
def seconds_to_weeks(seconds_float):
	return seconds_float / 604800

x_int = seconds_to_weeks(700000)
print(x_int)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# question 2
import math
def roots_of_equation(a_int,b_int,c_int):
	x_int = (-b_int + (math.sqrt(pow(b_int,2) - (4 * a_int * c_int)))) / (2 * a_int)
	y_int = (-b_int - (math.sqrt(pow(b_int,2) - (4 * a_int * c_int))))/ (2 * a_int)
	return x_int , y_int
d_int = roots_of_equation(4,8,4)
print(d_int)
# question 3
first_str = input("enter a string: ")
second_str = input("enter a string: ")
third_str = input("enter a string: ")
def string_concatenation(first_str,second_str,third_str):
	conc_str = first_str + second_str + third_str
	return conc_str
here_str = string_concatenation(first_str,second_str,third_str)
print(here_str)
# question 4
import math
def finding_root_of_number(x_int,n_int):
	int_y = x_int **(n_int ** -1)
	return int_y
int_c =  finding_root_of_number(27,3)
print(int_c)
# question 5
