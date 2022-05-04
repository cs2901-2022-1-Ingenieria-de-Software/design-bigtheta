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
	remoteControl.sendSignal("fan")
	remoteControl.sendSignal("redLight")
	remoteControl.sendSignal("yellowLight")
	remoteControl.sendSignal("whiteLight")
	remoteControl.sendSignal("something")
	remoteControl.sendSignal("fan")
	remoteControl.sendSignal("redLight")
	remoteControl.sendSignal("yellowLight")
	remoteControl.sendSignal("whiteLight")
	remoteControl.sendSignal("something")

if __name__ =="__main__":
	main()