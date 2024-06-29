#shalow copy
import copy
l1 = [1,2,3]
l2 = l1
print(l1)
print(l2)
l2.append(4)
print(l2)
print("*****l1*******",l1)

#deep copy
l3 = copy.deepcopy(l1)
l3.append(100)
print("----l1---",l1)
print("----l3---",l3)