import paho.mqtt.client as mqtt

def mqtt_connect_func(client,userdata,flags,rc):
	print ("Connected with code {}".format(rc))
	client.subscribe("Flint/Alarm1")
	client.subscribe("Flint/Alarm2")
	client.subscribe("Flint/Temperature")
	client.subscribe("Flint/Switch")
	
def mqtt_on_message_func(client,userdata,msg):
	if msg.topic == "Flint/Alarm1":
		print("Alarm1 is " + msg.payload.decode('ascii'))
	elif msg.topic == "Flint/Alarm2":	
		print("Alarm2 is " + msg.payload.decode('ascii'))
	elif msg.topic == "Flint/Temperature":	
		print("Temperature equal " + msg.payload.decode('ascii')+" degC")
	elif msg.topic == "Flint/Switch":		
		print("Switch is " + msg.payload.decode('ascii'))
	


client=mqtt.Client()
client.on_connect=mqtt_connect_func
client.on_message=mqtt_on_message_func

client.connect("test.mosquitto.org",1883)


client.loop_forever()
