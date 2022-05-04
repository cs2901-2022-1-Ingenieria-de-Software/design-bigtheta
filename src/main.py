from fan import *
from light import *
from ambiente import *
from remoteControl import *
import threading

def main():
	ambiente = Ambiente()
	ambiente.add_dispositivo("fan", Fan())
	ambiente.add_dispositivo("redLight", Light("red"))
	ambiente.add_dispositivo("yellowLight", Light("yellow"))
	ambiente.add_dispositivo("whiteLight", Light("white"))
	#print(ambiente.dispositivos)
	remoteControl = RemoteControl(ambiente)

	t = threading.Thread(target=ambiente.start)
	t.start()

	#remote control commands
	remoteControl.send_signal("fan")
	remoteControl.send_signal("redLight")
	remoteControl.send_signal("yellowLight")
	remoteControl.send_signal("whiteLight")
	remoteControl.send_signal("something")
	remoteControl.send_signal("fan")
	remoteControl.send_signal("redLight")
	remoteControl.send_signal("yellowLight")
	remoteControl.send_signal("whiteLight")
	remoteControl.send_signal("something")

if __name__ =="__main__":
	main()