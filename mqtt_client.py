import paho.mqtt.client as mqtt


html1 ='''
<!DOCTYPE html>
<html>
<head>
	<title>DHT 11</title>
	<meta charset="utf-8" />
</head>
<body>
	<center><img
		src="http://portal.uit.edu.vn/Styles/profi/images/logo186x150.png"/
	></center>
	<center><h1>
'''

html2 = '''
	</h1></center>
</body>
</html>
'''

def on_connect(client, userdata, flags, rc):
    print("connected with resuit code ", str(rc))

    client.subscribe("home/dht")
    client.subscribe("CoreElectronics/topic")

def on_message(client, userdata, msg):
    data = str(msg.payload)
    data = data[2:len(data)-1]
    data = data.split(" ")

    with open("/home/tpro/index.html", mode="w") as f:
        f.writelines([html1, data[0], " do C", "         ", data[1], " %", html2, "\n"])
    print(msg.topic, "\t", data[0], " do C", "\t", data[1], "%")

    if msg.payload == b"hello":
        print("Do something")

    if msg.payload == b"world":
        print("Do something else")
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect("test.mosquitto.org", 1883, 60)
client.connect("192.168.231.119", 1883, 60)
client.loop_forever()
