#Search of Pokemon
#Battle Simulator :D
#Export Pokemon CSV of all types

import csv
import time

print('(1) Search for a Pokemon')
print('(2) Battle Simulator')
print('(3) Export a CSV based on Type')

print()

user = input('Enter your choice: ')
print()



if(user == "1"): #Pokemon Search

	with open ("pokemon.csv") as file:
		
		reader = csv.reader(file)

		choose = input("Search for a Pokemon: ")
		print()

		for p in reader:
			if p[1] == choose:

				print('Name: {}'.format(p[1]))
				print('Type 1: {}'.format(p[2]))

				if(p[3] == ''):
					print('Type 2: None')
				else:
					print('Type 2: {}'.format(p[3]))

				print('Combat Power: {}'.format(p[4]))
				print('HP: {}'.format(p[5]))
				print('Attack: {}'.format(p[6]))
				print('Defense: {}'.format(p[7]))
				print('Sp. Atk: {}'.format(p[8]))
				print('Sp. Def: {}'.format(p[9]))
				print('Speed: {}'.format(p[10]))
				print('Generation: {}'.format(p[11]))
				print('Legendary: {}'.format(p[12]))
				break

		else:
			print('That Pokemon does not appear in our records.')



elif(user == "2"): #Battle Simulator

	with open ("pokemon.csv", newline ='') as file:
		
		reader = csv.reader(file)

		poke1 = input("Choose your first Pokemon: ")
		poke2 = input("Choose your second Pokemon: ")
		print()

		for p1 in reader:
			if p1[1] == poke1:
				row1 = [p1 for p1 in file]


	with open ("pokemon.csv", newline ='') as file:

		reader2 = csv.reader(file)

		for p2 in reader2:
			if p2[1] == poke2:
				row2 = [p2 for p2 in file]

		if (p1[1] != poke1 and p2[1] != poke2):
			print("Your Pokemons don't match our records")

		elif (p1[1] != poke1):
			print('The first Pokemon does not match our records')

		elif (p2[1] != poke2):
			print("The second Pokemon does not match our records")

		else:
			print('Battle Details')
			print('Combat Power of {} is: {}'.format(p1[1], p1[4]))
			print('Combat Power of {} is: {}'.format(p2[1], p2[4]))

			print()
			print('A battle is commencing!')
			print()

			time.sleep(1)

			if(p1[4] > p2[4]):
				print('{} wins the battle!'.format(p1[1]))

			elif(p1[4] == p2[4]):
				print("It's a stalemate!")
			else:
				print('{} wins the battle!'.format(p2[1]))




elif(user == "3"): #Choosing Pokemon type

	poketype = []
	with open ("pokemon.csv") as file:


		reader = csv.reader(file)
		header = next(reader)
		
		poke = input("Choose a pokemon type: ")
		
		for n in reader:
			if n[2] == poke:
				poketype.append(n)


	with open("PokeTypes.csv", "w") as file:
		
		writer = csv.writer(file)
		writer.writerow(header)

		if poketype == []:
			print("The Pokemon type does not exist. Otherwise, check your spelling.")
		
		else:
			for pokemon in poketype:
				writer.writerow(pokemon)
			print()
			print("Your CSV has been exported!")

else:
	print('Wrong input! Please restart the program.')