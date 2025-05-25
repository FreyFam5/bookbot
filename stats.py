def get_num_words(filepath: str) -> int:
	with open(filepath) as f:
		file_text: str =  f.read()
		word_array: list = file_text.split()
		return len(word_array)


def get_num_char(filepath: str) -> dict:
	char_dict: dict[str, int] = {}

	with open(filepath) as f:
		# Searches through every char in the text to find the number of each character and puts it into the dict
		for c in f.read() :
			char = c.lower()
			if char not in char_dict:
				char_dict[char] = 0
			char_dict[char] += 1
	return char_dict


def sort_on(dict):
	return dict["num"]


def get_list_of_char(char_dict: dict[str, int]) -> list[dict]:
	char_list: list[dict] = []
	for char in char_dict:
		char_list.append({"name": char, "num": char_dict[char]})
	char_list.sort(reverse=True, key=sort_on)
	return char_list