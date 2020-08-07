#Write a program to prompt the user for hours
#and rate per hour using input to compute gross pay.
#
#Pay should be the normal rate for hours up to 40
#and time-and-a-half for the hourly rate for all
#hours worked above 40 hours.
#
#Put the logic to do the computation of pay
#in a function called computepay() and
#use the function to do the computation.
#
#The function should return a value.
#Use 45 hours and a rate of 10.50 per hour
#to test the program (the pay should be 498.75).
#You should use input to read a string and
#float() to convert the string to a number.


#Do not worry about error checking the user input
#unless you want to - you can assume the user types numbers
#properly.
#Do not name your variable sum or use the sum() function. 

#define fucntion computepay with h and r as parameter
hrs = input("Enter Hours : ")
rate = input("Enter rate : ")

Fhours =  float(hrs)
Frate = float(rate)

def computepay(Fhours,Frate):
    if Fhours <= 40 :
        p=Fhours*Frate
    else:
        p=((40 * Frate) + ((Fhours - 40) * (Frate * 1.5)))
    return p

p = computepay(Fhours,Frate)
print("Pay",p)

#####----------------OR-------------####

#def computepay(h,r):
#    if h > 40: #if over-time
#    	p =  (40 * r) + ((h - 40) * (r * 1.5))
#    	return p
#    else: #normal pay
#    	p = h * r
#
#hrs = input("Enter Hours:")
#hr = float(hrs) #take input and translate it to float
#rphr = input("Enter Rate per Hours:")
#rph = float(rphr) #take input and translate it to float
#
#p = computepay(hr,rph)
#
#print("Pay",p)
