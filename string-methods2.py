# .isalpha()  returns true if the string is made up of only alphabets and not whitesapces

greetings = "Goodmorning"

print(greetings.isalpha())

# .isalnum()        returns true if the string is made up of only alphabets and numbers and not whitesapces

words = "hi45"

print(words.isalnum())

# .istitle()        returns true if the string is intitle format thus with the first letters in capitals

example_of_title = "My Pet Is Cool"

print(example_of_title.istitle())

# .isspace()        returns true if the string is made up of whitesapces, newlines, and tabs
empty_1 = "   "
empty_1 = "\n"
empty_3 = "\t"

print(empty_1.isspace())
print(empty_2.isspace())
print(empty_3.isspace())

# .isdecimal()      returns true if the string is made up of only numbers regarded as decimals
decimal = "4557"

print(decimal.isdecimal())

# .isnumeric()      returns true if the string is made up of numbers, subscript, superscripts, roman numbers which are in unicode format
v = "\u2161"
print(v.isnumeric())

# .isdigit()        returns true if the string is made numbers, subscript, and superscripts which is in unicode format
numbers = "4478"

unicodes = "\u2070"
print(unicodes.isdigit())


