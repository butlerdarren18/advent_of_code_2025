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


# convert to int 
ints = []
for line in input_lines: 
	string = "".join(line)
	ints.append(int(string))

print(ints)