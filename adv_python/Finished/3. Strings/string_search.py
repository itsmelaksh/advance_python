# Example file for Advanced Python by Joe Marini


sample_text = "The quick brown fox jumps over the lazy dog."

tempstr = sample_text.lower()

# Using find() to find the first occurrence of a substring
print("First occurrence of 'the':", tempstr.find("the"))

# Example with optional start and end parameters
print("First occurrence of 'the' after index 5:", tempstr.find("the", 5, 36))

# Using index() to find the first occurrence of a substring (raises ValueError if not found)
try:
    print("First occurrence of 'fox':", sample_text.index("fax"))
except ValueError:
    print("Not found")

# The 'in' operator can be used for Boolean testing:
print("Is 'fox' present:", "fox" in sample_text)

# Using rfind() to find the last occurrence of a substring
print("Last occurrence of 'a':", sample_text.rfind("the"))

# Using rindex() to find the last occurrence of a substring (raises ValueError if not found)
print("Last occurrence of 'jump':", sample_text.rindex("jump"))

# The replace() function will find content in the string and replace it
result = sample_text.replace("lazy","tired")
print(result)
result = tempstr.replace("the","THE")
print(result)
