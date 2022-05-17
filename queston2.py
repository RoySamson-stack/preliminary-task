import re

# #names starting with an A
def searchname(fn):
    name= []
    name_a = [element for element in open(fn, 'r') if element.startswith("A")]
    name.append(name_a)
    print(mylist)
searchname("names.txt")

# #user enter the first name
def searchname(fn):
    name= []
    name_letter = input("Enter a the first letter of the name: ")
    name_a = [element for element in open(fn, 'r') if element.startswith(name_letter)]
    name.append(name_a)
    print(mylist)
searchname("names.txt")

#searching age of the person
def searchage(fn):
    age = []
    for line in open(fn, 'r'):
        if re.search(str(5), line):
            words=line.split()
            age.append(words)
    print(age)
searchage("names.txt")   

#searchingthe age of the person using user input 
def searchage(fn):
    age = []
    age_enter = input("Enter the age:")
    for line in open(fn, 'r'):
        if re.search(str(age_enter), line):
            words=line.split()
            age.append(words)
    print(age)
searchage("names.txt")   