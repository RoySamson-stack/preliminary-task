def searchname():
  infile = open("names.txt", "r")
  for name in infile.readlines():
    if name.startswith("A"):
      print(name)
    
  
def searchname():
  infile = open("names.txt", "r")
  for line in infile.readlines():
    if name.startswith("A"):
      print(name[:-1])    