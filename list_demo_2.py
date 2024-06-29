# list_of_subject = ["RTOS",'iot',"""EOS"""]
# print(list_of_subject.index('iot'))
# for index_of_subject, subject in enumerate(list_of_subject):
#     print("{0} is stored at index {1}".format(subject,index_of_subject))


list_of_numbers = [1,2,3,5]
#gives last element
print(list_of_numbers[-1])

#slicing in list

sub_list_of_list_of_numbers = list_of_numbers[1:3]
print(sub_list_of_list_of_numbers)

l2 = list_of_numbers[2:]
print(l2)
l3 = list_of_numbers[:3]
print(l3)
#reverse a list
list_of_numbers.reverse()
print(list_of_numbers)
