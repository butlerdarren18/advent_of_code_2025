# you can pick two numeralsfrom each line. They are combined to form a number and cannot be rearranged. 
# largest possible number each line. then sum.

input_file = open("day_3_example_inputs.txt")
input_lines = input_file.readlines()


# remove empty spaces

new_lines = []

for line in input_lines: 
	holder = []
	for char in line: 
		if char != "\n": holder.append(char)
	new_lines.append(holder)

input_lines = new_lines

# determine two highest nums 


for line in input_lines:
	highest_indx = -2
	second_highest_indx = -1

	# pick the highest number 
	for i in range(len(line)):
		if line[i] >= line[highest_indx] and i < len(line)-1: highest_indx = i
	# pick the second highest number 
	for i in range(len(line)): 
		if i > highest_indx: 
			if line[i] >= line[second_highest_indx]: second_highest_indx = i


	print(line[highest_indx], line[second_highest_indx])


