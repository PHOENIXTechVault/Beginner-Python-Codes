#creating dictionaries {} dict()

# contact = {}
# contact = dict()
# print(type(contact))

# creating dictionaries with value in them

emp = {'name':'Sam', 'age':35, 'location':'Hilltoop road', 'pragramLang':'Python'}
# print(emp)
# print(emp['age'])
# print(emp['name'])

# creating dictionaries with multiple datatypes
emp2 = {1:"Josh", 2:45, 'courses':['Arts', 'Physics', 'Programming']}
# print(emp2)
# print(emp2[1])
# print(emp2['courses'])

# creating dictionaries with nested dictionaries

emp3 = {'name':'Angela', 'age':22, 'courses': {'Arts': 'BA', 'Programming':'Masters', 'Physics':'Dr.'}}
# print(emp3)

#adding new entries in dictionaries
emp['sex'] = 'Male'
# print(emp)

#adding multple new entries in dictionaries
# .update method

emp.update({'name':'Samuel', 'salary':1000, 'location':'Estate'})
# print(emp)

emp = {'name':'Sam', 'age':35, 'location':'Hilltoop road', 'pragramLang':'Python'}


# .delete method

# del(emp['name'])
# print(emp)

# .pop method

# a = emp.pop('age')
# print(emp)
# print(a)

# .len method
# print(len(emp))

# .keys method
# print(emp.keys())

# .values metthod
# print(emp.values())

# .items method
# print(emp.items())

# looping through dictionaries

# for i,k in emp.items():
#     print(i,k)

emp = {'name':'Sam', 'age':35, 'location':'Hilltoop road', 'pragramLang':'Python'}

# .get method
# print(emp.get('sex', 'Key not found'))

# .clear method
# emp.clear()
# print(emp)

# .copy method

# copy_emp = emp.copy()
# print(copy_emp)
# print(emp)

# set default method

# if 'sex' not in emp:
#     emp['sex'] = 'Male'

emp.setdefault('name', 'male')

print(emp)
