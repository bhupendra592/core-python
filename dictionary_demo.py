import json
sensor_data = {
    "temperature" : 20,
    "humidity" : 80,
    "deployed_in" : ["DESD","DIoT"],
    "status" : True
}

print(sensor_data)
#Acess the value : Option 1
print(sensor_data['humidity'])
# Add a new key
sensor_data["aqi"] = 100

print(sensor_data)

#Accessing values using get (temperature is key of sensordata)
temperature  = sensor_data.get('temperature')
print("value of temperature : ",temperature)
print(json.dumps(sensor_data, indent=4))

#Modify the values
sensor_data["deployed_in"].append("DAC")
sensor_data["humidity"] = 97
print(json.dumps(sensor_data, indent=4))

