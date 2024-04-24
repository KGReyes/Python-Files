# TODO
import sys
import csv
import sqlite3

if len(sys.argv) != 2:
    print("Incorrect number of command line arguments")
    sys.exit(1)

file = sys.argv[1]
db = sqlite3.connect('students.db')


with open(file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        names = row['name'].split(' ')
        first = names[0]
        middle = None
        last = names[1]
        if len(names) == 3:
            middle = names[1]
            last = names[2]

        db.execute('INSERT INTO students (first, middle, last, house, birth)VALUES (?, ?, ?, ?, ?)',(first, middle, last, row['house'], row['birth']))

db.commit()
db.close()