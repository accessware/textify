from .parsers.rtf import RtfParser
from . import exceptions

def textify(filename):
	if filename.lower().endswith(".rtf"):
		parser = RtfParser(filename)
	else:
		raise exceptions.UnsupportedFileTypeError("Unsupported file type.")
	text = parser.read()
	return text
