def ArrayChallenge(arr):
  target=0
  result=[]
  if (arr):
    target = arr[0]
    for i in range(1,len(arr)):
      for j in range(i+1, len(arr)):
        if arr[i]+arr[j]==target:
          result.append(str(arr[i])+','+str(arr[j]))
  if (result):
    return(' '.join(result))
  else:
    return -1


    
# keep this function call here 
print(ArrayChallenge(input()))