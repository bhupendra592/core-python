"""
*
* *
* * *

"""
no_of_rows = 5
for i in range(1,no_of_rows+1):
    for j in range(i):
        print(f"{j}")
        print("*", end=" ")
    print()