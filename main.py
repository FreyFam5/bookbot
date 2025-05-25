from stats import *
import sys

def get_book(input: list) -> str:
	# Checks if the input argument has enough arguments to use
	if len(input) < 2:
		print("Usage: python3 main.py <path_to_book>")
		return sys.exit(1)
	return input[1]


def main():
	file_path: str = get_book(sys.argv)

	num_of_char: list = get_list_of_char(get_num_char(file_path))
	num_of_words: int = get_num_words(file_path)
	print("========== BOOKBOT ==========")
	print(f"Analyzing book found at {file_path}...")
	print("-------- Word Count ---------")
	print(f"Found {num_of_words} total words")
	print("------ Character Count ------")
	# Prints the character count to look nice and to only print the alphabetical characters
	for idx in range(0, len(num_of_char) - 1):
		current: dict[str, int] = num_of_char[idx]
		if current["name"].isalpha():
			print(f"{current["name"]}: {current["num"]}")
	print("============ End ===========")

main()