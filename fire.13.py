a=[]
for i in open('file.txt'):
  x=i.split()
  for e in x:
    if 'c' in e or 'C' in e:
      a.append(e)
      print(a)
