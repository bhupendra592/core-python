#Open a file for reading
file_name = "iot_sensor.txt"
try:
    with open (file_name,"w") as fd:
        data = fd.write("Temp is 30c")
        print(data)
    print(fd.closed)
except Exception as e:
     print("Unknowm error occured",e)