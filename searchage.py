def searchname():
  infile = open("names.txt", "r")
  for s in infile:
    if name.startswith("A"):
      print(s)
    
  
def searchname():
  infile = open("names.txt", "r")
  for s in infile:
    if name.startswith("A"):
      print(s[:-1])    