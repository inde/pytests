from sys import argv
from os.path import exists # get the operating system to tell us tru false if file exists

script, from_file, to_file = argv

print ("Share cookies with J", (from_file, to_file))

in_box = open(from_file)
in_data = in_box.read()

print ("Your box is %d bytes big" %len(in_data)) # the % databinds

print ("Give cookies to J?") # ("Give cookies to J? %r" % exists(to_file))

has_box = exists(to_file);

give = input();

answers = ["yes", "Yes", "YES"]

if give in answers:

	out_box = open(to_file, 'w')
	out_box.write(in_data)

	out_box.close()
	in_box.close()

	print ("Alright, J now has cookies")

else:

	print('Shame on you give her cookies now!')


