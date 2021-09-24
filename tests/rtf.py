import sys
sys.path.append("..")
import textify

file = open("rtf.txt", "w")
text = textify.textify("test.rtf")
file.write(text)
file.close()
