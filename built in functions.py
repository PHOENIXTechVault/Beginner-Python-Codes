abs()   #returns the absolute value of a given number
print(abs(-100))    #will return the absolute value which will be positive 100

print(abs(0.123))   #will return the absolute value which will be 0.123

print()         #the print function evaluates the value inside the parentheses and output or display it to the user
print(5+5)      #this will evaluate the expression 5+5 and then print the final value which is 10

print("Hello welcome to PHOENIXTech.Vault")     #this will output Hello welcome to PHOENIXTech.Vault to the user

a = 123

b = 5**2

print("these are the value", a, b)      #it can also take in multiple values and evaluate them at the same time

help()      #the help function gives infomation or documentation on modules, keywords or any concept you do not know
help(modules)       #this will give you all the list of modules available in Python

len()           #gives you the integer value of a string or the number of characters in a string
                #NB that whitespaces are also included as characters
print(len("hello there"))  #this will evaluate to 11 characters including the whitespaces

words = "When ever coding make to sure to get a cup of coffee"

print(len(words)) #passing the variable words as argument inside the len function, this evaluate to 52 characters including whitespaces

input()     #this built-in function always receive innformation or always wait for the user to enter information before it moves to the next line of code

print("Enter your name here: ")
ans = input()           #storing the value the user entered inside a variable called ans

print("this is what you typed " +ans)       #the value stored in the variable then gets printed out together with some string