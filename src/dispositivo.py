class Dispositivo():
	def __init__(self):
		self.on = False

	def recieve_signal(self):
		self.on= not self.on
		print("state:",self.on)