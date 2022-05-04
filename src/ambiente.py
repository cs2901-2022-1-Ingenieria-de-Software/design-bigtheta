from dispositivo import Dispositivo

class Ambiente():
	def __init__(self):
		self.dispositivos = {}
		self.command_queue = []
		

	def add_dispositivo(self,name,dispositivo):
		self.dispositivos[name] = dispositivo

	def send_signal(self,to):
		if(to in self.dispositivos):
			self.command_queue.append(to)

	def fetch_signal(self):
		if(len(self.command_queue) > 0):
			name =self.command_queue.pop(0)
			print("signal sent to: " + name,end="; ")
			self.dispositivos[name].recieve_signal()

	def start(self):
		while True:
			self.fetch_signal()