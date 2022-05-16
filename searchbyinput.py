def searchname():
    infile = open("names.txt", "r")
    first_letter = input("Enter the search letter: ")
    for s in infile:
        if s[0].lower() == first_letter.upper():
            print(s)