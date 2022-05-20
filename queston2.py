import re

# #names starting with an A
def printall():
    for line in open("names.txt", "r"):
        print(line)
        
printall()        
        
def searchname():
    name= []
    name_a = [element for element in open("names.txt", 'r') if element.startswith("A")]
    name.append(name_a)
    print(name)
searchname()

# #user enter the first name
def search_name():
    name=input("enter the letter (s): ")
    valid_names=[]
    for line in open("names.txt", 'r'):
        if line.startswith(name):
            words=line.split()
            valid_names.append(words)
            
    print(valid_names)
search_name()
# #if the program stops at the enter you first name kindly comment it out 

#searching age of the person
def searchage():
    age = []
    for line in open("names.txt", 'r'):
        if re.search(str(5), line):
            ages=line.split()
            age.append(ages)
    print(age)
searchage()   

#searching the age of the person using user input 
def searchage():
    age = []
    age_enter = input("Enter the age:")
    for line in open("names.txt", 'r'):
        if re.search(str(age_enter), line):
            ages=line.split()
            age.append(ages)
    print(age)
searchage()   

#main funtion
def main():
    ans = input("Kindly choose 1 to seach name and 2 to search by age:")
    if ans == 1:
        searchname()
    elif ans == 2:
        searchname() 
    else:
        print("You entered an invalid option")
        raise SystemExit
    
if __name__ == "__main__":
    main()    
    