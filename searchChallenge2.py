def SearchingChallenge(strParam):

  # code goes here
  total=0
  numchar=0
  for i in strParam:
    if i.isnumeric():
      total+=int(i)
    elif i.isalpha():
      numchar+=1
  return (round(total/numchar))


# keep this function call here 
print(SearchingChallenge(input()))