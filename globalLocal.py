globalV = "3";

def iAmAFunction():
	localeV = "10"
	print("")
	print("Inside the function,")
	print("I can see the golbal variable is " + globalV)
	print("I can also see the locale variable is " + localeV)

iAmAFunction()
print("")
print("Outside the function,")
print("I can see the golbal variable is " + globalV)
print("However I can't see the locale variable " + localeV)