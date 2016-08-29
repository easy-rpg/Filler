import json
from Classes import Barbaro

class Writer(object):
	"""docstring for Writer"""
	def __init__(self, obj):
		super(Writer, self).__init__()
		self.file = open("personagens/teste.rf", 'w')
		self.file.write(json.dumps(obj.__dict__))
		self.file.close()
		
Writer(Barbaro(9))		