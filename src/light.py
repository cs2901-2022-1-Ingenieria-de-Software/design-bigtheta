from dispositivo import *

class Light(Dispositivo):
	def __init__(self,color,*args):
		self.color = color
		super().__init__(*args)
	