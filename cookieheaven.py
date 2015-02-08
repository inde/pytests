from sys import argv


script, name = argv
prompt = "> "

print ("whats your name")
name = input(prompt)


print ('Let me ask you something about cookies\n') # , (name, script)

print ('Do you like cookies', name)
likes = input(prompt)

answers = ["yes", "Yes", "YES"]

if likes in answers:

	print('welcome to heaven!')

else:

	print('you should burn in hell!')
