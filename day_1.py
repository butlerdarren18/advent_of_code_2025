# NOTES : 
# 	You have a safe with a dial 0-99
# 	The input is a list of rotation directions 
# 
# 	It's kind of just basic arithmatic 
#  
#	L / - if we drop below -1 turns into 99
# 	R / + if we go above 100 turns into 0 

input_file = open("day_1_input.txt", "r")

input_lines = input_file.readlines()

def convert_lines_to_strings() -> list: 
	new_lines = []

	for line in input_lines: 
		new_line = "".join(line)
		if not new_line == "\n": new_lines.append(line)
	return new_lines



def get_turn_directions() -> list: 
	turn_directions = []
	for line in convert_lines_to_strings(): 
		for character in line:
			if character == "L" or character == "R": 
				turn_directions.append(character)
	return turn_directions

turn_directions = get_turn_directions()

def get_numbers(): 
	split_lines = []
	numbers = []
	#TURN EACH LINE INTO AN ARRAY OF CHARS 
	for line in convert_lines_to_strings():
		new_line = []
		split_lines.append(line.split())
		for character in line: 
			if not character == "\n": 
				if not character == "L": 
					if not character == "R": 
						new_line.append(character)
		new_line = "".join(new_line)
		numbers.append(int(new_line))
	return numbers
numbers = get_numbers()

def turn_left(start_number:int, turn_number:int) -> int: 
	num = start_number
	for i in range(turn_number): 
		num -= 1
		if num == -1: num = 99
	return num 

def turn_right(start_number:int, turn_number:int) -> int: 
	num = start_number 
	for i in range(turn_number): 
		num += 1 
		if num == 100: num = 0 
	return num




