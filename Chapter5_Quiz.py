"""
n = 5
while n > 0 :
    print(n)
    break
print('All done')

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)




#Hint: This is a trick question
#and most would say this code has a bug - so read carefully

#Answer:
#all number in the_num are greater than -1


n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')



tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

"""