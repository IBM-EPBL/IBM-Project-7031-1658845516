# Bin 3

import time
import sys
import random
import ibmiotf.application
import ibmiotf.device

organization = "rz7zse"
deviceType = "BIN"
deviceId = "bin3"
authMethod = "token"
authToken = "bin3token"


def myCommandCallback (cmd):
	print("Command received: %s" % cmd.data)	
	print(cmd)

def start():
    try:
        deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)

    except Exception as e:
        print("Caught exception connecting device", e)
        sys.exit()

    deviceCli.connect()

    while True:
        distance = random.randint(0, 400)
        weight = random.randint(0, 250)
        
        data = {"data": { "distance"  : distance, "weight"  : weight } }

        def myOnPublishCallback():
            print("Published Distance =", distance, "Weight =",  weight, "to IBM Watson")

        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)

        if not success:
            print("Not connected to IOTF")

        time.sleep(1)
        deviceCli.commandCallback = myCommandCallback

    deviceCli.disconnect()

start()
