import  paho.mqtt.client as mqtt
import json
import thread
import requests

def send_data_to_server(msg):
    print "Topic : ", msg.topic
    message = json.loads(msg.payload)

    data_array = {
        "networkId":message["node"],
        "dataList":[
            {"key":"Temperature", "value":message["temperature"]},
            {"key":'Humidity', "value":message["humidity"]}
        ]
    }

    headers = {"content-type": "application/json"}

    print data_array

    try:
        r = requests.post("https://192.168.10.1:8080/EMCSBackEnd/rest/sensor-data", data=json.dumps(data_array), headers=headers)
        print r.status_code
    except Exception as e:
        print e


def on_connect(client, userdata, rc):
    print "Connected with result code " + str(rc)
    client.subscribe("node")

def on_message(client, userdata, 
    thread.start_new_thread(send_data_to_server, (msg,))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost")

client.loop_forever()
