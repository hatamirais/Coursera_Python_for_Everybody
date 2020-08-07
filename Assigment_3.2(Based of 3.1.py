sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
	fh = float(sh)
	fr = float(sr)
except:
	print("Wrong input, chief!")
	quit()

print(fh,fr)
if fh > 40:
	regular = fr * fh
	otp =(fh - 40.0) * (fr * 0.5)
	xp = regular+otp
else:
	#print regular
	xp = fh * fr
print("Pay:",xp)