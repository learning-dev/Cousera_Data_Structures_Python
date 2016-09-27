fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
sum=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    pos=line.find(" ")
    num=line[pos:].rstrip()
    num = float(num)
    sum= sum + num
  
print "Average spam confidence:",sum/count
