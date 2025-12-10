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
	return id_list

id_list = separate_at_commas(input_text)

def get_x_id_list(ids): 
	x_list = []
	holder = ""

	for string in ids: 
		end_of_string_reached = False 
		
		for character in string: 
			if end_of_string_reached == True: continue 
			if character == "-": 
				x_list.append(holder)
				holder = ""
				end_of_string_reached = True
			else:
				holder = holder + character

	return x_list 

print(get_x_id_list(id_list))