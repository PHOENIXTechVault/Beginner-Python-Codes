# in & not in operator always returm a boolean value True or False depending on the condition

name = "My name is King"

print('Simon' in name)      #this will return to False since the name Simon is not in the string in the variable

print('Simon' not  in name)     # this will return True because Simon is not in the string

#practical example
ans = "Tiger or Lion"          #The answer we're expecting the user to enter

print("What is the answer?")    #Asking the user to enter his or her answer

res = input()       #storing the users input in a variable res

if res in ans:      #checking whether the input of the user is in the answer we're expecting
    print("You had it correct")     #if it evaluates to true then this print statement will execute
else:
    print("Oh no, try again later")     #if it's not in, thus False this print statement will execute
