def main():
  #search by name
  def searchname():
    infile = open("names.txt", "r")
    first_letter = input("Enter the search letter: ")
    for s in infile:
        if s[0].lower() == first_letter.lower():
            print(s)
            
  searchname()            