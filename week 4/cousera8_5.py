
fname = raw_input("Enter file name: ")
fh = open(fname)
 
 
count=0
for lines in fh:
	if lines.startswith('From '):
	    count +=1
	    ln=lines.split()
	    print ln[1]
	 
    
 
 
print "There were", count, "lines in the file with From as the first word"
