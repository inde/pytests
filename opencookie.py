from sys import argv

script, cookie = argv

cookie_file = open(cookie)

print ("Here is your cookie ", cookie_file.read())

print ("Look for the cookie again:")
cookie_again = input('> ')

txt_again = open(cookie_again)

print (txt_again.read()) 