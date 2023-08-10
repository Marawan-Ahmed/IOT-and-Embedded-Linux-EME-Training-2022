import paho.mqtt.client as mqtt
import time
import random 

client=mqtt.Client("P1")


client.connect("test.mosquitto.org",1883)

while True:
    client.publish("Flint/Alarm1","ON" if (random.random() > 0.5) else "OFF")
    client.publish("Flint/Alarm2","ON" if (random.random() > 0.5) else "OFF")
    client.publish("Flint/Temperature",str(round(random.random()*100,2)))
    client.publish("Flint/Switch","ON" if (random.random() > 0.5) else "OFF")
    time.sleep(1)
