class BaseParser:
	def __init__(self, filename):
		self.filename = filename
		self.file = None

	def read(self):
		pass

	def close(self):
		self.file = None
