class RemoteControl():
	def __init__(self,ambiente):
		self.ambiente = ambiente

	def send_signal(self,to):
		self.ambiente.send_signal(to)