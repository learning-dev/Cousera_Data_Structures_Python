name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

avg=dict()
for lines in handle:
    if not lines.startswith ('From '):continue
    list=lines.split()
    list=list[1]
    avg[list]=avg.get(list,0)+1
 
ind=None
val=None
for key,value in avg.items():
  if ind == None or value > val:
        ind=key
        val=value
print ind,val