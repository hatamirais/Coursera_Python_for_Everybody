#Prompt user to input hours and rate to compute gross pay
#Rate for the hours up to 40 (<40) and 1.5 times hours rate if 
#all hours worked above 40 (>40)

#45 hours and rate 10.50 per hour to test program 
#output should be 498.75

#input both float() and int()

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
r = float(rate)

try:
	pay = 0
	if h > 40:
		pay = (h * r) + ((h-40)*r*0.5)
	elif h <= 40:
		pay = (h * 1) * r
except:
	print("Wrong Input!")

print(pay)

####--------------OR----------------#####

#sh = input("Enter Hours: ")
#sr = input("Enter Rate:")
#fh = float(sh)
#fr = float(sr)
#print(fh,fr)
#if fh > 40:
#	regular = fr * fh
#	otp =(fh - 40.0) * (fr * 0.5)
#	xp = regular+otp
#else:
#	#print regular
#	xp = fh * fr
#print("Pay:",xp)