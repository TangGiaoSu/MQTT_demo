import paho.mqtt.publish as publish

#publish.single("CoreElectronics/test", "hello", hostname="test.mosquitto.org")
#publish.single("CoreElectronics/topic", "world", hostname="test.mosquitto.org")
publish.single("home/tun", "hello", hostname="192.168.231.119")
publish.single("CoreElectronics/topic", "world", hostname="192.168.231.119")
print("done")
