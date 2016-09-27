text = "X-DSPAM-Confidence:    0.8475";
pos=text.find('0');
x=text[pos:];  # starting from 0 to end
x=float(x);
print x;
