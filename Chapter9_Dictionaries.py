''''
List
-  A Linear collection of values that stay in order

Dictionary
- A "bag" of values, each with its own label
'''

"""
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
#print(purse)
#print(purse['candy'])
purse['candy'] = purse['candy']
"""
"""
ayaya = dict()
ayaya['money'] = 12
ayaya['candy'] = 3

#print(ayaya)
print(ayaya['money']+ayaya['candy'])
"""

"""

COUNTING WITH DICTIONARIES

"""

"""
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
	if name not in counts:
		counts[name] = 1
	else :
		counts[name] = counts[name] + 1
print(counts)
"""

"""
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
	counts[name] = counts.get(name, 0)  + 1
print(counts)

"""

"""

DICTIONARIES AND FILES


"""

"""
counts = dict()
print('Type in the text: ')
#input the text from user
line = input('')

#assign those input in words and split it
#from space
words = line.split()

print('Words:', words)

print('COUNTING...')
for word in words:
	counts[word] = counts.get(word,0) + 1
print('Counts', counts)

"""

