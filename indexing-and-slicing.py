word = "hello there"

# h = 0 ==> first index which always starts at 0
# e = 1 ==> secod index
# l = 2 ==> third index
# l = 3 ==> fourth index
# o = 4 ==> fifth index

# using negative indexing
# -1 = e
# -2 = r
# -3 = e
# -4 = h
# -5 = t
# -6 = " ' ==> whitespace
# -7 = o
# -8 = l
# -9 = l
# -10 = e
# -11 = h

# Grabing the characters using their positional index(also known as slicing)
#
print(word[0:8])

print(word[4:10])

print(word[:])

print(word[:8])

find = word.index("h")

find = word.index("t")

find = word.index("l",1,4)
print(find)

print(word[-11])
