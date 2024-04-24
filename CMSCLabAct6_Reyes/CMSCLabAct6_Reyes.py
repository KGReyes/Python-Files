print("Prime Numbers Between Two Numnbers")
print()

low = int(input ("Input the lower value: "))
high = int(input ("Input the higher value: "))

print()
print("These are the prime numbers within your range: ")

for prime in range (low, high + 1):
	if prime > 1:
		for n in range (2, prime):
			if (prime % n) == 0:
				break

		else:
			print(prime)