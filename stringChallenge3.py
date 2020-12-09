import re

def StringChallenge(strParam):

  # code goes here
  password = strParam.lower()
  f = 'false'
  t = 'true'
  regex = re.compile('[+-=*/!]') 
  #check if string password is in
  if 'password' in password:
    return f
  #checks for length
  if len(strParam)<=7 or len(strParam)>=31:
    return f
  #checks for special characters
  if(re.search(regex, strParam)==None): 
    return f
  #checks for digits for all
  if ((any(char.isdigit() for char in strParam))==False):
    return f
  #checks for upper case for everything
  if ((any(char.isupper() for char in strParam))==False):
    return f
  
  return t

# keep this function call here 
print(StringChallenge(input()))