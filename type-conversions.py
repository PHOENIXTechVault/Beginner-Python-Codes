#str()              #This built-in function converts the value which is passed in to a string
print("Today is "+str(28)) #converting the 28 to a string value before you concatenate
a = str(5)          #converting the 5 to a string
b = "I am "

print(b  + a + " feet tall")

#float()            #This built-in function converts the value which is passed in to a float
a = 5
b = float(a)  #converting the value of variable a to a float
print(type(b)) #printing out the type after converting
print(type(a))  #printing out the type of the initial value

c = "123"
r = float(c)  #converting the value of variable a to a float
print(type(c))      #printing out the type of the initial value
print(r)
print(type(r))  #printing out the type after converting

y = "cat"       #this will give an error since the string is not numbers
print(float(y)) #an error will be given

#int()              #This built-in function converts the value which is passed in to an integer
fraction = 123.56
a = int(fraction)       #converting the the float value to an integer
print(type(fraction))       #printing out the type of the initial value
print(type(a))      #printing out the type after converting

word = "645"
new = int(word)     #converting the value of variable to an integer
print(type(word))   #printing out the type of the initial value
print(type(new))    #printing out the type after converting

print("Type your age ")     #asking the user to input a value
age = input()               #storing the value from the user into a variable age
age_plus10 = float(age)+10  #converting the value inside the age variable to a float and then adding 10 to it
print(type(age_plus10))     #printing out the type of the converted value

#bool()     #This data type only have true or false

print(bool(0))      #the output will be False, and apart from 0 any value you pass inside will give you a True answer
print(bool("yryryy"))       #the output will be False