text = input("Input your text: ")

let = len([c for c in text if c.isalpha() or c.isdigit()])
wor = len(text.split())
sen = text.count('.') + text.count('!') + text.count('?')

L = (let / wor) * 100
S = (sen / wor) * 100

  
i = 0.0588 * L - 0.296 * S - 15.8

  
if i < 1:
  print()
  print("Before Grade 1")
elif i >= 16:
  print()
  print("Grade 16+")
else:
  print()
  print(f"Grade {round(i)}")