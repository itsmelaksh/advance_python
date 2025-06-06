# Example file for Advanced Python by Joe Marini


import itertools

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

# the enumerate function
for i, m in enumerate(days, start=1):
    print(i, m)

# use zip to combine sequences
for m in zip(days, daysFr):
    print(m)

# use enumerate and zip together
for i, m in enumerate(zip(days, daysFr), start=1):
    print(i, m[0], "=", m[1], "in French")

# use zip_longest
seq1 = ["A","B","C","D","E","F"]
seq2 = [1, 2, 3, 4]
seq3 = "xyz"
result = itertools.zip_longest(seq1, seq2, seq3, fillvalue="-")
print("Result: ")
for item in result:
    print(item)
    