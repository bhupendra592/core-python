list1 = [1,10,20]
print(list1)
#print(id(list1))
list1.append("aman")
print(list1)
#print(id(list1))
list1[0]=100
print(list1)

for item in list1:
    print(item)
    if item == "aman":
        print(f"{item} exist in list")

for index, item in enumerate(list1):
    print(f"{item} is at index {index}")


        
