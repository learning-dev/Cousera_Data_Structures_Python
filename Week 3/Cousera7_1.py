# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
imp=fh.read()
imp=imp.upper()
imp=imp.strip()
print imp

