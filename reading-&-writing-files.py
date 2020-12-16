# # open
myFile = open('example.txt', 'r') #read 'r', write 'w', append 'a', read&write 'r+'
print(myFile.read())
myFile.close()

# # using the with clause [prefered]
with open('example.txt', 'r') as myFile:
    # print(myFile.read())
    # print(myFile.mode)
    print(myFile.name)

text = "My name is PHOENIXTech.Vault.\n Welcome once again to this tutorial"

with open('example3.txt', 'w') as myFile:
    myFile.write(text)

with open('example4.txt', 'a') as myFile:
    myFile.write(text)

with open('example4.txt', 'r+') as myFile:
    myFile.write(text)


#copying files to another file

with open('example.txt', 'r') as parentFile:
    with open('example_copy.txt', 'a') as copiedFile:
        for words in parentFile:
            copiedFile.write(words)

# WORKING WITH CSV FILES
import csv
with open('mycsv.csv', 'w') as f:
    filewrite = csv.writer(f, delimiter=',')
    filewrite.writerow(['dog', 'bag', 'cow'])
    filewrite.writerow(['a', 'toys', 'cars'])
    filewrite.writerow(['twenty', '4', '56'])

with open('mycsv.csv', 'r') as readfile:
    # print(readfile)
    for a in readfile:
        print(''.join(a))
