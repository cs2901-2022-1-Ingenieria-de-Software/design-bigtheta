from fan import Fan
from light import Light
from ambiente import Ambiente
from remoteControl import RemoteControl
import threading

def main():
	ambiente = Ambiente()
	ambiente.add_dispositivo("fan", Fan())
	ambiente.add_dispositivo("redLight", Light("red"))
	ambiente.add_dispositivo("yellowLight", Light("yellow"))
	ambiente.add_dispositivo("whiteLight", Light("white"))
	#print(ambiente.dispositivos)
	remote_control = RemoteControl(ambiente)

	t = threading.Thread(target=ambiente.start)
	t.start()

	#remote control commands
	remote_control.send_signal("fan")
	remote_control.send_signal("redLight")
	remote_control.send_signal("yellowLight")
	remote_control.send_signal("whiteLight")
	remote_control.send_signal("something")
	remote_control.send_signal("fan")
	remote_control.send_signal("redLight")
	remote_control.send_signal("yellowLight")
	remote_control.send_signal("whiteLight")
	remote_control.send_signal("something")

if __name__ =="__main__":
	main()