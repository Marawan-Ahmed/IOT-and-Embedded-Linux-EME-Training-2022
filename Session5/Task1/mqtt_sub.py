import paho.mqtt.client as mqtt

def mqtt_connect_func(client,userdata,flags,rc):
	print ("Connected with code {}".format(rc))
	client.subscribe("Flint/Humidity")
	client.subscribe("Flint/Temperature")
	
def mqtt_on_message_func(client,userdata,msg):
	print(msg.topic+" = "+msg.payload.decode('ascii'))
	


client=mqtt.Client()
client.on_connect=mqtt_connect_func
client.on_message=mqtt_on_message_func

client.connect("test.mosquitto.org",1883)


client.loop_forever()
