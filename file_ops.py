#file operations
"""
r for reading
w for writing
a for appending
"""
#Open a file for reading
file_name = "iot_data.txt"
try:
    with open (file_name,"r") as fd:
        data = fd.read()
        print(data)
    print(fd.closed)
except FileNotFoundError:
    print("the file not found error")
except Exception as e:
     print("Unknowm error occured",e)

# fd = open(file_name,"r")
# data = fd.read()
# print(data)
# print(fd.closed)
# fd.close()
# print(fd.closed)