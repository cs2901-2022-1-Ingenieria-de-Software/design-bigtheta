class RemoteControl():
	def __init__(self,ambiente):
		self.ambiente = ambiente

	def sendSignal(self,to):
		self.ambiente.sendSignal(to)