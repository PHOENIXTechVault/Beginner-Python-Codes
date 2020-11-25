# AND
a = 5
b = 5
c = 7

print(a == b and c > b)     #return True since both conditions are True

print((a != b and c > b) and c > a)     #return False since one of the conditions is False

# OR
print(a == b or c > a)      #return True since both conditions are True

print(a != b or c > b)      #return True since one of the conditions is True

print(a == c or c < b)      #return False since both conditions are False


# NOT
a = False
b = not a             #will return the opposite value of False which is True
print(b)

c = True
d = not c             #will return the opposite value of True which is False
print(d)

sex = "male"

age = 18

if sex == "male" and age >= 18:
    print("You are allowed to come to the party")
else:
    print("You not allowed")


if sex == "male" or age >= 18:
    print("You are allowed to come to the party")
else:
    print("You not allowed")
