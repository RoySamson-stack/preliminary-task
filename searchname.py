import re

def searchname():
  infile = open("names.txt", "r")
  return ([word for word in infile.split() if (word.startswith('A'))])
  print(word)
  
# def searchname():
#   infile = open("names.txt", "r")
#   for line in infile.readlines():
#     print(name[:-1])    