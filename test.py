#user enter the first name
def searchname_input(fn):
    name= []
    name_letter = input("Enter a the first letter of the name: ")
    name_a = [element for element in open(fn, 'r') if element.startswith(name_letter)]
    name.append(name_letter)
    print(name)
    
searchname_input("names.txt")