from dispositivo import Dispositivo

class Ambiente():
	def __init__(self):
		self.dispositivos = {}
		self.commandQueue = []
		

	def add_dispositivo(self,name,dispositivo):
		self.dispositivos[name] = dispositivo

	def sendSignal(self,to):
		if(to in self.dispositivos):
			self.commandQueue.append(to)

	def fetchSignal(self):
		if(len(self.commandQueue) > 0):
			name =self.commandQueue.pop(0)
			print("signal sent to: " + name,end="; ")
			self.dispositivos[name].recieveSignal()

	def start(self):
		while True:
			self.fetchSignal()