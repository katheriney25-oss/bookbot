import sys

from stats import analyze_text

def main():
	#check that the user provided one additional argument
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1) #exit w/ status code 1 to indicate incorrect usage

	#the second argument (index 1) is the file path
	filepath = sys.argv[1]
	
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...\n")

	results = analyze_text(filepath)

	print("----------- Word Count ----------")
	print(f"Found {results['word_count']} total words\n")

	print("--------- Character Count -------")
	for char, count in list(results['char_count'].items()):
		print(f"{char}: {count}")

if __name__ == "__main__":
	main()
