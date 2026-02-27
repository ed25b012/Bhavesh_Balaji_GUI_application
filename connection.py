from paho.mqtt import client as mqtt_client
import json
import random
import time
def on_message(client, userdata, message):
    print("Received:", message.payload.decode())

client2 = mqtt_client.Client(client_id="hyperloop_dashboard")
client2.on_message = on_message
client2.connect("broker.hivemq.com", 1883)
client2.subscribe("hyperloop/pod/data")
client2.loop_start()
time.sleep(5)

client = mqtt_client.Client(client_id="hyperloop_pod1")
client.connect("broker.hivemq.com", 1883)
client.loop_start()
pod_data = {
    "pod": "Avishkar-1",
    "speed": random.randint(600, 900),
    "battery": random.randint(30, 100),
    "status": "Operational"
}
client.publish("hyperloop/pod/data", json.dumps(pod_data))
time.sleep(5)
