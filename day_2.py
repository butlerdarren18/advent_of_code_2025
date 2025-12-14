input_file = open('day_2_example_input.txt', 'r')
input_text = input_file.read()


# separate the lists at the commas 
id_pairs = []
id_temp = []
for char in input_text: 
	if not char == "," and not char == "\n":
		id_temp.append(char)
	if char == ",":
		id_pairs.append(id_temp)
		id_temp = []
id_pairs.append(id_temp)


# Separate the pairs from eachother 
x_id_char_lists = []
y_id_char_lists = []

for pair in id_pairs:
	holder = []

	for char in pair: 
		if not char == "-": holder.append(char)
		else:
			x_id_char_lists.append(holder)
			holder = []
	y_id_char_lists.append(holder)


# convert to strings
x_id_string_list = []
for xid in x_id_char_lists: x_id_string_list.append("".join(xid))

y_id_string_list = []
for yid in y_id_char_lists: y_id_string_list.append("".join(yid))

#convert to ints 
x_ints = []
for xid in x_id_string_list: x_ints.append(int(xid))

y_ints = []
for yid in y_id_string_list: y_ints.append(int(yid))

# get every possible id
possible_ids = []

for i in range(len(x_ints)): 
	for j in range(x_ints[i], y_ints[i] + 1): 
		possible_ids.append(j)

# get the ids with even quantities of numerals
even_ids =[] 
for x in possible_ids: 
	length = len(str(x))
	if (length/2).is_integer(): even_ids.append(x)

print(even_ids)
