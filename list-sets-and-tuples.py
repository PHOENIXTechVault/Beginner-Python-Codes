#List

my_list = ['pen', 'pencil', 'book']
# print(my_list)
# print(len(my_list))
# print(my_list[0])
# print(my_list[0:2])
# print(my_list[1:])

.append() method
my_list.append("eraser")
print(my_list)
.insert() method
my_list.insert(1, "bag")
print(my_list)

.extend() method

multiple_values = ['car', 'truck', 'train']
my_list.extend(multiple_values)
print(my_list)

.remove() method
my_list.remove('book')
print(my_list)
.pop() method
removed_value = my_list.pop()
print(my_list)
print(removed_value)
my_list = ['pen', 'pencil', 'book', 'eraser']
my_num_list = [9, 5, 3, 75, 98, 1]
.reverse() method
my_list.reverse()
print(my_list)
.sort() method
my_list.sort()
my_num_list.sort()
print(my_list)
print(my_num_list)

my_list.sort(reverse=True)
my_num_list.sort(reverse=True)
print(my_list)
print(my_num_list)

.index() method
print(my_list.index('pen'))

in
print('car' in my_list)
print('pen' in my_list)

looping through all the elements inside our list
for things in my_list:
    print(things)

for position, things in enumerate(my_list):
    # print(position, things)
    print(things + " is having a position of " + str(position))
# Changing strings to list
string_my_list = ", ".join(my_list)
string_my_list = " - ".join(my_list)

# print(string_my_list)
# words = "I am PHOENIX"
# words = "I program in Python"
# new_list = words.split()
# print(new_list)
# print(new_list[3])

#tuples
my_animal = ('cat', 'dog', 'cow', 'sheep')
for i in my_animal:
    print(i)
#sets
my_set = {'math', 'english', 'history', 'french'}
my_set2 = {'math','math','math','math','math','math'}
print(my_set2)
my_set3 = {'math', 'arts', 'history', 'physics'}

intersection method
print(my_set.intersection(my_set3))

difference method()
print(my_set.difference(my_set3))

empty_list = []
empty_list = list[]

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} #cannot do this since it will creat an empty dictionary
empty_set = set{}

