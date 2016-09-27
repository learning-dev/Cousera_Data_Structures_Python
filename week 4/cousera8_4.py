fname = raw_input("Enter file name: ")
fh = open(fname,'r')
lst = list()

for line in fh:
   if line in lst : continue 
   lst.append(line.split())
tmp=[]  # you can len() function to find the length of list.
tmp=lst[0]+lst[1]+lst[2]+lst[3]
tmp.sort()
lst=[]
for x in tmp:
 if x not in lst:
    lst.append(x)
lst.sort()
print lst

