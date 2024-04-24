#LCM and GCD Functions
def lcm(a, b):
	lcm = a*b

	return lcm

def gcd(a, b):
    if(b == 0):
        return abs(a)
    else:
    	gc = gcd(b, a % b)
    	
    return gc



#Arithmetic Functions
def add(a, b, c, d, lcm):
	fn1 = (a*d)
	fn2 = (b*c)
	fn3 = (fn1 + fn2) 
	num = fn3/(gcd(b, d))
	den = lcm/(gcd(b, d))

	if(fn3 == lcm):
		ans = print("The sum of your fractions is 1")
	elif(fn3 % lcm == 0):
		ans = print("The sum of your fractions is: ", fn3/lcm)
	else:
		ans = print("The sum of your fractions is: ", int(num/gcd(den, num)), "/", int(den/gcd(den, num)))
	return ans

def sub(a, b, c, d, lcm):
	fn1 = (a*d)
	fn2 = (b*c)
	fn3 = (fn1 - fn2) 
	num = fn3/(gcd(b, d))
	den = lcm/(gcd(b, d))

	if(fn3 == lcm):
		ans = print("The difference of your fractions is 1")
	elif(fn3 % lcm == 0):
		ans = print("The difference of your fractions is: ", fn3/lcm)
	else:
		ans = print("The difference of your fractions is: ", int(num/gcd(den, num)), "/", int(den/gcd(den, num)))
	return ans

def mp(a, b, c, d):
	fn1 = (a*c)
	fn2 = (b*d)

	if(fn1 == fn2):
		ans = print("The product of your fractions is 1")
	elif(fn1 % fn2 == 0):
		ans = print("The product of your fractions is: ", fn1/fn2)
	else:
		ans = print("The product of your fractions is: ", int(fn1/gcd(fn2, fn1)), "/", int(fn2/gcd(fn2, fn1)))
	return ans

def div(a, b, c, d):
	fn1 = (a*d)
	fn2 = (b*c)

	if(fn1 == fn2):
		ans = print("The quotient of your fractions is 1")
	elif(fn1 % fn2 == 0):
		ans = print("The quotient of your fractions is: ", fn1/fn2)
	else:
		ans = print("The quotient of your fractions is: ", int(fn1/gcd(fn2, fn1)), "/", int(fn2/gcd(fn2, fn1)))
	return ans



#Main
in1 = input("Input your first fraction: ")
in2 = input("Input your second fraction: ")
fr1 = in1.split("/")
fr2 = in2.split("/")

fr1 = [int(i) for i in fr1]
fr2 = [int(i) for i in fr2]
print()


if((len(fr1) < 2 or len(fr2) < 2)):
	print("One of your inputs is a whole number!")

elif(fr1[1] == 0 or fr2[1] == 0):
	print('One of your fractions is undefined')

elif( (fr1[0] == 0 or fr2[0] == 0)):
		print('One of your numerators is 0')

else:

	f1 = fr1[0] * (lcm(fr1[1], fr2[1])/fr1[1])
	f2 = fr2[0] * (lcm(fr1[1], fr2[1])/fr2[1])

	if(f1 < f2):
		print("Your first fraction is smaller than the second")

	else:
		print("First fraction:", fr1[0], "/", fr1[1])
		print("Second fraction:", fr2[0], "/", fr2[1])
		print()

		add(fr1[0], fr1[1], fr2[0], fr2[1], (lcm(fr1[1], fr2[1])))
		print()

		sub(fr1[0], fr1[1], fr2[0], fr2[1], (lcm(fr1[1], fr2[1])))
		print()

		mp(fr1[0], fr1[1], fr2[0], fr2[1])
		print()

		div(fr1[0], fr1[1], fr2[0], fr2[1])