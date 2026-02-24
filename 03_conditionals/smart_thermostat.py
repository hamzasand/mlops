# device_status = "active"
# temperature = 38

# if device_status == "active":
#     if temperature > 35:
#         print("High temperature alert!")
#     else:
#         print("Temperature is normal")
# else:
#     print("Device is offline")



device_status = "active"
temperature = 9

if device_status == "active":
    if temperature > 35:
        print("temperature is to high")
    else:
        print("Temperature is normale")
else:
    print("device is offline")