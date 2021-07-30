li=[int(i) for i in input('enter numbers:').split()]
print (*li)

def remove_duplicates(duplist):
  newli = []
  for ele in duplist:
    if ele not in newli:
      newli.append(ele)
  return newli

print (remove_duplicates(li))
