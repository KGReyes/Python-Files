import sqlite3

datab = sqlite3.connect("records.db")
cursor = datab.cursor()

try:
	cursor.execute("CREATE TABLE records (email TEXT, password TEXT, name TEXT, age INTEGER, course TEXT, school TEXT)")
except:
	print("", end = "")

print("Choose an option: ")
print(" (1) Login")
print(" (2) Signup")
print(" (3) Change Password")
print(" (4) Delete an Account") 
print("")

try:
	ans = int(input("Option: "))
	print("")
except:
	ans = None
	print("", end = "")

if ans == 1:

	print("Please enter your details to login: ")
	currmail = input("Email: ")
	currpass = input("Password: ")
	user = cursor.execute("SELECT * FROM records WHERE email = ? AND password = ?",
		(currmail, currpass)).fetchall()
	print("")
	if len(user) != 0:

		for p in user:
			print("Welcome {}!".format(p[2]))
			print("")
			print("Details:")
			print("Email: {}".format(p[0]))
			print("Password: {}".format(p[1]))
			print("Name: {}".format(p[2]))
			print("Age: {}".format(p[3]))
			print("Course: {}".format(p[4]))
			print("School: {}".format(p[5]))

	else:
		print("You entered the wrong email or password")
		print("")
		print("If you haven't signed up yet, please do so first.")


elif ans == 2:

	print("Welcome! Enter your details below: ")
	email = input("Email: ")
	password = input("Password: ")
	name = input("Name: ")
	age = input("Age: ")
	course = input("Course: ")
	school = input("School: ")

	cursor.execute("INSERT INTO records VALUES (?, ?, ?, ?, ?, ?)", 
		[email, password, name, age, course, school])

	print("")
	print("Thank you for signing up!")


elif ans == 3:

	print("Please login first")
	currmail = input("Email: ")
	currpass = input("Password: ")
	user = cursor.execute("SELECT * FROM records WHERE email = ? AND password = ?",
		(currmail, currpass)).fetchall()
	print("")
	if len(user) != 0:
		for n in user:
			newpass = input("Input your New Password: ")
			cursor.execute("UPDATE records SET password = ? WHERE email = ? AND password = ?",
				(newpass, currmail, currpass))
		print("")
		print("Your password has been updated!")
	else:
		print("You entered the wrong email or password")


elif ans == 4:
	
	print("Please login first")
	currmail = input("Email: ")
	currpass = input("Password: ")
	user = cursor.execute("SELECT * FROM records WHERE email = ? AND password = ?",
		(currmail, currpass)).fetchall()
	print("")
	if len(user) != 0:
		print("Are you sure you want to delete this account?")
		print("Y for Yes, N for No.")
		print("")
		choice = input("Y/N: ")

		if choice == "Y":
			cursor.execute("DELETE FROM records WHERE email = ? AND password = ?",
				(currmail, currpass))
			print("")
			print("Account successfully deleted!")
		else:
			print("")
			print("Halting Program")
	else:
		print("You entered the wrong email or password")

else:
	print("Wrong input! Please restart.")

datab.commit()
cursor.close()