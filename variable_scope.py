number = 10
def variable_scope():
    print(number)
# call the function
variable_scope()
# print the value of number
print(number)

#sum = 10

def display_sum():
    sum_value = 10
    print(sum_value)

display_sum()
# print(sum_value)

"""
Traceback (most recent call last):
  File "variable_scope.py", line 14, in <module>
    print(sum_value)
NameError: name 'sum_value' is not defined
"""
#Block scope
if True:
    value = 20
print(value)

cdac_acts__desd_tudent_count = 54

def display_count():
    cdac_acts__desd_tudent_count = 55
    print(cdac_acts__desd_tudent_count)

display_count()
print(cdac_acts__desd_tudent_count)

x_value = 25
def display_x_value():
    global x_value
    x_value += 30
    print("inside function",x_value)
display_x_value()
print("outside block",x_value)


