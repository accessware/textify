import sys
import textify

def cli():
	if len(sys.argv) != 3:
		print("Usage: textify <input_file> <output_file>")
		sys.exit()
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	file = open(output_file, "w")
	text = textify.textify(input_file)
	file.write(text)
	file.close()
	print("Done!")

if __name__ == "__main__":
	cli()
