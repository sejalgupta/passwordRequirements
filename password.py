import re
import string

def StringChallenge(str):
  if (Length(str) == "false"):
    return false
  if (Numbers(str) == "false"):
    return false
  if (Punctuation(str) == "false"):
    return false
  if (noPass(str) == "false"):
    return false
  if (Capital(str) == "false"):
    return false
  return true
  
#checks condition 5
def Length(str):
  try:
    if (len(str) >= 31): #returns false if 31 or more characters
      return "false"
    if (len(str) <= 7): #returns false if 7 or less characters
      return "false"
  except:
    return "false"
  return "true"

#checks condition 2
def Numbers(str):
  try: 
    if(re.search("\d", str) is None): #searches for a digit in the password
      return "false"
  except:
    return "false"
  return "true"

#checks condition 3
def Punctuation(str):
  try: #searches for punctuation and returns false if there is none
    for a in str:
      for b in string.punctuation:
        if (a == b):
          return "true"
    return "false"
  except:
    return "false"

#checks condition 4
def noPass(str):
  try: 
    if(re.search("password", str, re.I) is None): #searches for the word password (case insensitive)
      return "true"
  except:
    return "false"
  return "false"
  
#checks condition 1
def Capital(str):
  try: 
    if(re.search("[A-Z]", str) is None): #searches for capital letter
      return "false"
  except:
    return "false"
  return "true"
  
#call function
print StringChallenge(raw_input())
