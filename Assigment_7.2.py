# Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:
#
# X-DSPAM-Confidence:    0.8475
#
# Count these lines and extract
# the floating point values from
# each of the lines and
# compute the average of those values and
# produce an output as shown below.
# Do not use the sum() function
# or a variable named sum in your solution.
#
# You can download the sample data at 
# http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt
# as the file name.

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
count = 0
average = 0
for line in fh:
	#if the program dont find "X_DSPAM"
	#it re loop from (for line in fh)
    if not line.startswith("X-DSPAM-Confidence:") :
    	continue
    #+= is like c+=a is same with c = c+a
    #so 'average' below is a variable that
    #has the value where X-DSPAM is found,
    #strip it from whitespace, and store it
    average += float(line[19:].strip())
    count = count + 1
    
print("Average spam confidence:", (average/count))


"""
fname = input("Enter file name: ")
count = 0
total = 0
try:
	fh = open(fname)
except:
	print(fname,"nowhere found")
	quit()
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
    	count = count+1
    	n = line.find(":")
    	convt = float(line[n+1:])
    	avg = total / count
print("Average spam confidence:", avg)
"""