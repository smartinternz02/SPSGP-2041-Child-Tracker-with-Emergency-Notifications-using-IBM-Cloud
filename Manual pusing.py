
#pip install wiotp-sdk
#for package installation

import wiotp.sdk.device
import json
import time

myConfig={
    "identity": {
        "orgId":"hj5fmy",
    "typeId":"NodeMCU",
    "deviceId":"12345"
        
    },
    "auth":{
        "token":"12345678"
    }
}
client=wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
  name="Smartbridge"
  latitude=17.4219272
  longitude=78.5488783
  myData={'name': name, 'lat': latitude, 'lon': longitude}
  client.publishEvent(eventId="status", msgFormat="json", data=myData, onPublish=None)
  print("data published", myData)
  time.sleep(5)
client.disconnect()