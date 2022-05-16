def main():
  #search by name
  def searchName():
    infile = open("names.txt",'r')
    for s in infile:
        if s.startswith('A'):
            print(s)    
    return
            
  searchname()            