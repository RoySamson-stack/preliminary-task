import re

def searchname():
    infile = open("names.txt", "r")
    for s in infile:
        if re.search(r'\b[A]\w+', s):
            print(s)
    
def search_name_from_user():
    infile = open("names.txt", "r")
    user_input = str(input('Enter the letter that you want the name to start with: '))
    result =  [name for name in infile if name.startswith((user_input))]
    print(result)

def searchage():
    infile = open("names.txt", "r")
    for s in infile:
        if re.search('[5]', s):
            print(s)

def searchage_user():
    infile = open("names.txt", "r")
    user_input_age = int(input('Enter the age at which you want to search the users with: '))
    for s in infile:
        if re.search(rf'[{user_input_age}]', s):
            print(s)

if __name__ == "__main__":
    user_choice = input("enter a choice you would like: ")
    if user_choice == '1':
        print(search_name_from_user())
    elif user_choice == '2':
        print(searchage_user)
    elif user_choice == '3':
        searchname()
    elif user_choice == '4':
        searchage()
    else:
        print('Select an input between 1 and 2 for searching through \n file for name or age')
    