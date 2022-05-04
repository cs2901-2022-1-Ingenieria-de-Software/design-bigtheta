class Dispositivo():
	def __init__(self):
		self.on = False

	def recieveSignal(self):
		self.on= not self.on
		print("state:",self.on)