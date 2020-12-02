#################   LOOPS ###########################
# for loops
for i in range(10):     #Will print all number between 0 to 20( 20 is excluded )
    print(i)

for b in range(0, 20, 2):   #Will print all number between 0 to 20( 20 is excluded ) with interval diffrence of two
    print(b)

for n in range(20, 0, -2):  #Will print all number in a descending order starting from 20
    print(n)

# Suming up all the numbers within the range of 20 (0 - 19) using for loop
total = 0
for p in range(20):
    total = total + p
print(total)

# while loops

a = 0
while a < 5:    #all numbers between 0 to 5 thus 5 excluded
    print(a)
    a = a + 1   #will increase the value stored in the ariable by one

#break
while a < 5:
    print( str(a) + "is still less than 5")
    a = a + 1
    if a == 3:
        break   #iteration stops when a is equal to 3 because of the break keyword
print("We've reached 3")
print(a)

# continue

while a < 5:
    print(a)
    a = a + 1
    if a == 3:
        continue   #iteration skips over 3 because of the continue keyword
                    #3 won't be printed out at the end

# pass
while a < 5:
    a = a + 1
    if a == 3:
        pass    #the pass keyword does nothing to the loop
    print(a)    #it mostly used to creat empty functions

def listout():  #example of an empty function using the pass keyword
    pass

