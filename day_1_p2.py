input_file = open("day_1_inputs.txt", "r")

input_lines = input_file.readlines()




# get turn directions 
turn_directions = []
for line in input_lines: 
	for char in line: 
		if char == "L" or char == "R": turn_directions.append(char)

# get nums
turn_numbers = []

for line in input_lines: 
	holder = []

	for char in line: 
		if char != " " and char != "\n":
			if char != "L" and char != "R": holder.append(char)
			if char is not str: continue
			else:
				turn_numbers.append(int("".join(holder)))
				holder = []
	turn_numbers.append(int("".join(holder)))

# perform turns and check for 0s 
answer = 0 
num = 50
for i in range(len(turn_directions)):
	direction = turn_directions[i]
	turn = turn_numbers[i]

	if direction == "L": 
		for i in range(turn):
			num = num -1
			if num == -1: num = 99
			if num == 0 : answer = answer + 1
	elif direction == "R": 
		for i in range(turn): 
			num = num + 1
			if num == 100: num = 0 
			if num == 0 : answer = answer + 1




print(answer)

