num = 0
tot = 0.0
while True:
	sval = input("Enter a number: ")
	if sval == "done":
		break
	#add try if the code has porblem with the input
	try:
		fval = float(sval)
	except:
		print("Invalid Input!")
		continue
	print(fval)
	num = num + 1
	tot = tot + fval

print('all done')
print(tot, num, tot/num)