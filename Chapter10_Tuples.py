"""

Tuples and List are similiar

Different is Tuples is non mutable, which
mean we cant change the value

List identifies with []
Tuples identifies with ()

Tuples cant:

sort()
append()
reverse()
etc look the library method

there are exception look
from min 9 foe sort, min 10 for reverse
and append,

Tuples are more efficient
"""

'''
(x, y) = (4, 'fred')
print(y)
'''

'''
(a, b) = (99, 98)
print(a)
'''

'''
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.(word, 0) + 1

lst = list()
for key, val in counts:
	newtup = (val, key)
	lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
	print(key, val)
'''

'''
c= {'a':10, 'b':1, 'c':22}
print(sorted( [(v,k) for k,v in c.items()]))

'''