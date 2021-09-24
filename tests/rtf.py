import sys
sys.path.append("..")
import textify

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: rtf.py <input_file> <output_file>")
		sys.exit()
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	file = open(output_file, "w")
	text = textify.textify(input_file)
	file.write(text)
	file.close()
	print("Done!")
