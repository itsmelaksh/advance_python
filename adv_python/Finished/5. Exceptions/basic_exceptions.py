# Example file for Advanced Python by Joe Marini
# Working with basic exception handling

# Try to execute some code that might cause an exception:

try:
    num = input("Enter the first number: ")
    denom = input("Enter the second numnber: ")
    n = int(num)
    d = int(denom)
    result = n/d
except ZeroDivisionError as e:
    print("You can't divide by zero!")
    print(e)
except ValueError as e:
    print("You didn't give me a valid number!")
    print(e)
else:
    print(result)
finally:
    print("Thanks for playing!")
