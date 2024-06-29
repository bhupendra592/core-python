def add_two_number(num1,num2):
    return num1+num2

print(add_two_number(10,20))

def reverse_number(num1,num2):
    num1, num2 = num2 , num1
    print(f"reverse_number is :  {num1} {num2}")
reverse_number(20,30)