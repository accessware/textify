from .base import BaseParser
from striprtf.striprtf import rtf_to_text

class RtfParser(BaseParser):
	def read(self):
		self.file = open(self.filename, "r")
		text = self.file.read()
		self.close()
		text = rtf_to_text(text)
		return text

	def close(self):
		self.file.close()
		super().close()
