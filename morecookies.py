from sys import argv

script, cookie = argv

print ("Do you want to eat the", cookie)

answers = ["yes", "Yes", "YES"]
prompt = "> "
yousaid = input(prompt)

if yousaid in answers:

	cookie_box = open(cookie, 'w')
	print('let me fill the box again, what sort of cookies you want in there?')

	cookie1 = input ('choose cookie: ')
	cookie2 = input ('choose cookie: ')	
	cookie3 = input ('choose cookie: ')

	print('Let me get that for you\n')

	print('Here are your cookies in the box\n')

	cookie_box.write(cookie1)
	cookie_box.write('\n')
	cookie_box.write(cookie2)
	cookie_box.write('\n')
	cookie_box.write(cookie3)
	cookie_box.write('\n')

	cookie_box.close()


	txt_again = open('cookie.txt')

	print (txt_again.read()) 

else:
	
	print('Good boy, keep them for later')
