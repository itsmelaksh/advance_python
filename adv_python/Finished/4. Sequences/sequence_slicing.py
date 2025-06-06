# Example file for Advanced Python by Joe Marini
# Sequences and slicing

from collections import deque

names = ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]

# a slice is a subset of a sequence. The form is [start:stop:step]
print(names[1:4])

# using a step 
print(names[0:7:2])

# shorthand
print(names[:3])
print(names[5:])

# reversing with step of -1
print(names[::-1])

newnames = ["Andy", "Stanley", "Angela"]
names[2:4] = newnames
print(names)

# the del operator works with slices
del names[0:2]
print(names)

# not all sequence types support slicing, however
deque_names = deque(["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"])
for name in deque_names:
    print(name, " ", end="")
print()
print(len(deque_names))
print(deque_names[1:4]) # TypeError!
