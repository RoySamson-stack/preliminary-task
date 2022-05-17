import re

# #names starting with an A
def searchname(fn):
    name= []
    name_a = [element for element in open(fn, 'r') if element.startswith("A")]
    name.append(name_a)
    print(name)
searchname("names.txt")

# #user enter the first name
def searchname_input(fn):
    name= []
    name_letter = input("Enter a the first letter of the name: ")
    name_a = [element for element in open(fn, 'r') if element.startswith(name_letter)]
    name.append(str(name_letter))
    print(name)
searchname_input("names.txt")
#if the program stops at the enter you first name kindly comment it out 

#searching age of the person
def searchage(fn):
    age = []
    for line in open(fn, 'r'):
        if re.search(str(5), line):
            ages=line.split()
            age.append(ages)
    print(age)
searchage("names.txt")   

#searching the age of the person using user input 
def searchage(fn):
    age = []
    age_enter = input("Enter the age:")
    for line in open(fn, 'r'):
        if re.search(str(age_enter), line):
            ages=line.split()
            age.append(ages)
    print(age)
searchage("names.txt")   

#main funtion
def main():
    ans = input("Kindly choose 1 to seach name and 2 to search by age:")
    if ans == 1:
        searchname("names.txt")
    elif ans == 2:
        searchname("names.txt") 
    else:
        print("You entered an invalid option")
        raise SystemExit
    
if __name__ == "__main__":
    main()    
    