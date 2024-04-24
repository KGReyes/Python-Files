# TODO
import sys
import sqlite3


if len(sys.argv) != 2:
    print("Incorrect number of command line arguments")
    sys.exit(1)


db = sqlite3.connect('students.db')
cursor = db.cursor()
cursor.execute('SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first ',(sys.argv[1],))

for row in cursor:
    fullname = ' '.join(name for name in row[:3] if name is not None)
    print(f"{fullname}, born {row[3]}")


db.close()