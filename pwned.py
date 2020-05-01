import getpass, hashlib, requests

a = """
  ____
 /    \_________________
{      ________________/
 \____/PWNED PASSWORDS

Has your password been PWNED?
Author: @captainblb

"""
print a

while True:
	password = getpass.getpass("Enter password to test: ")

	print "Searching for your password from over 500 million leaked passwords..."
	result = hashlib.sha1(password.encode())
	hash = result.hexdigest()

	first5 = hash[0:5]
	rest =  hash[5:(len(hash))].upper()

	URL = "https://api.pwnedpasswords.com/range/" + first5

	r = requests.get(url = URL)
	passwords = r.content.splitlines()

	for p in passwords:
		x = p.split(":")
		hash = x[0]
		num = x[1]

		if rest == hash:
			hash_found = 1
			break
		else:
			hash_found = 0

	if hash_found == 1:
		print '\033[91m' + "PWNED!"
		print "Your password has been leaked " + num + " times." + '\033[0m'
	else:
		print '\033[92m' + "You're OK!"
		print "Looks like your password hasn't been leaked, yet..." + '\033[0m'
