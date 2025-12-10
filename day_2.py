input_file = open('day_2_input.txt', 'r')
input_text = input_file.readline()


def separate_at_commas(txt) -> str:
	id_list = []
	holder = ""
	for character in txt:
		if character == ",":
			id_list.append(holder)
			holder = ""
		else: holder = holder + character
	print(id_list)


separate_at_commas(input_text)