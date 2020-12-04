# Manually printig out hello welcome without the use of a function
print("hello welcome")
print("hello welcome")
print("hello welcome")
print("hello welcome")
print("hello welcome")

def print_welcome_messsage():   #definig a function to print out the welcome message 5 times
    print("Hello welcome\n"*5)

def ask_name():
    print("whats your name?")
print_welcome_messsage()    #calling the function
ask_name()                  #calling the function

# Built-in functions
print(), str(), abs()

# lambda functions
out = lambda message : message*5  #writting the lambda function form of our previouse written function
print(out("hello welcome\n"))

# User defined functions

def ask_name(person):       #creating your own function thus user defined functions
    print("Welcome " + person)
    print("whats your name?" + person)

# Arguments & Parameters
ask_name("Janet")
ask_name("Joe")
ask_name("Kevin")
ask_name("Josh")    #calling each function and passing in an argument

# return values and return statement

def ask_name(age):
    new_age = age * 10
    age2 = new_age + 100
    if new_age > 50:
        return "Welcome Granny"
    elif new_age <= 40:
        return "hi you are welcomed"
    else:
        return "You are a youth"

print(ask_name(80))
print(ask_name(10))
print(ask_name(8))
print(ask_name(4))

# local scopes and Global scopes
a = 45

def ask_age(age):
# Global statement. This helps declare a local variable as a global variable which then can be used outside of functions and in other functions
    global new_age
    global age2

    new_age = age * a
    age2 = new_age + a
    print(new_age)
    print(age2)

def greet(name):
    print("Hello " + name)
    print(new_age)
    print(age2)


ask_age(5)
greet("Sam")

print(new_age)
print(age2)


