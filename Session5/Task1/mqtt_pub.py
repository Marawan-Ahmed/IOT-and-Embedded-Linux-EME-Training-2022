import paho.mqtt.client as mqtt
import time
import random 

client=mqtt.Client("P1")


client.connect("test.mosquitto.org",1883)

while True:
    client.publish("Flint/Humidity",str(random.random()*100))
    client.publish("Flint/Temperature",str(random.random()*100))
    time.sleep(1)
