# MODULES
def add(a=0,b=0):
    return a + b

def mul(a=0,b=0):
    return a * b

def div(a=0,b=0):
    return a / b


class Bio:
    def __init__(self,fname,lname,age,sex,location,occupation,married="single"):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.sex = sex
        self.location = location
        self.occupation = occupation
        self.married = married

    def fullname(self):
        return "This is your fullname: {} {}".format(self.fname, self.lname)

    def emailaddress(self):
        return "This is your email: {}{}@gmail.com".format(self.fname.lower()[0],self.lname.lower())


    def wholebio(self):
        return """Your first name is {} and your last name is {}.\
You are {} years of age and also a {}. You are in {} and your marital status is {}.\
You are currently working as {}.""".format(self.fname,self.lname,self.age,self.sex,self.location,self.married,self.occupation)


