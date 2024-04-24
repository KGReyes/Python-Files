import csv
from sys import argv

def main():

	if len(argv) != 3:
		print("Incorrect arguments")

	dbfile = open("./"+ argv[1])
	dnafile = open("./" + argv[2])

	dbreader = csv.DictReader(dbfile)
	i = dbreader.fieldnames[1:]

	dna = dnafile.read()
	dnafile.close()

	dnafp = {}
	for str in i:
		dnafp[str] = consec_repeats(str, dna)

	for row in dbreader:
		if match(i, dnafp, row):
			print(f"{row['name']}")
			dbfile.close()
			return

	print("No match")
	dbfile.close()


def consec_repeats(str, dna):
	i = 0
	while str*(i+1) in dna:
		i += 1
	return i


def match(i, dnafp, row):
	for str in i:
		if dnafp[str] != int(row[str]):
			return False
	return True


main()