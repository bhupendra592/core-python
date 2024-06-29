sensor_data = {
    "temperature" : 20,
    "humidity" : 80,
    "deployed_in" : ["DESD","DIoT"],
    "status" : True
}

print(sensor_data)
print(sensor_data['humidity'])
sensor_data["aqi"] = 100
print(sensor_data)