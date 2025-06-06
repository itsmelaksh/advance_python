# Example file for Advanced Python by Joe Marini
# Manipulating string content


test_str = "The quick, brown fox jumps over the lazy dog."

# upper, lower, title
print(test_str.upper())
print(test_str.lower())
print(test_str.title())

# strip, lstrip, rstrip
test_str2 = "   This string has whitespace   "
print(test_str2.strip())
print(test_str2.lstrip())
print(test_str2.rstrip())

# split creates a sequence from a single string
words = test_str.split()
print(words)

# join concatenates an iterable into a single string
words = ["Hello", "world", "from", "Python"]
separator = " "
sentence = separator.join(words)
print(sentence)
