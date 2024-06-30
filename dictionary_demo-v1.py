import json
sensor_data =  {
    "temperature" : 20,
    "humidity" : 80,
    "deployed_in" : ["DESD","DIoT"],
    "status" : True
}

print("--------Dict Pre Pop Operation -----")
print(json.dumps(sensor_data, indent=4))
#Remove a key value pair
sensor_data.pop('status')
print("--------Dict Post Pop Operation -----")
print(json.dumps(sensor_data, indent=4))
#Using Del statement
del sensor_data['deployed_in']
print("--------Dict Post del Operation -----")
print(json.dumps(sensor_data, indent=4))
#Using Del statement

sensor_data.update(
    {
        "lat" : 97.5,
        "lon" : 20.2,
        "acc_x_axis" : 76.2,
        "acc_y_axis" : 88.2,
        "acc_z_axis" : 90.2
    }
)
print("--------Dict Post update Operation -----")
print(json.dumps(sensor_data, indent=4))

#List of keys to delete
keys_to_delete_in_sensor_data = ["acc_y_axis","acc_z_axis"]

for key in keys_to_delete_in_sensor_data:
    if key in sensor_data:
        del sensor_data[key]

print("--------Dict Post Delete Operation -----")
print(json.dumps(sensor_data, indent=4))
"""
ToDo:
    Ask the user to enter the two keys 
    that need be deleted from the dict
"""
delete_key_list = []
key_to_delete1 = input("Enter the key to be deleted from dict 1 : ")
key_to_delete2 = input("Enter the key to be deleted from dict 2 : ")
delete_key_list.append(key_to_delete1)
delete_key_list.append(key_to_delete2)

for key in delete_key_list:
    if key in sensor_data:
        sensor_data.pop(key)

print("--------Dict Post Delete Operation -----")
print(json.dumps(sensor_data, indent=4))

#Get all the keys in dict
print("-----List of keys--------")
keys_of_the_sensor_data = sensor_data.keys()
print(keys_of_the_sensor_data)
print("-----All the values of dict--------")
values_of_the_sensor_data = sensor_data.values()
print(values_of_the_sensor_data)