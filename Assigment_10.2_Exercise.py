name = input("Enter file:")
if len(name) < 1 :
	name = "mbox-short.txt"

handle = open(name)


'''
Create list to store the "string" from 
the text after slicing the space
'''

lst = list()

for line in handle:
	if not line.startswith('From:'):
		continue
	line = line.split()
	lst.append(line[1])

'''
create dictionary called counts
which read the lst value
and add it to the counts dict
as well as adding if its exist
ex: 

for word in lst:
	counts[word] = counts.get(word,0) + 1

the code found 'from', then > {'from:1'}
then found 'bad', then > {'from:1', 'bad:1'}
then found 'from', then > {'from:2', 'bad:1'}
as reference its from minute 3.47
'''

counts = dict()
for word in lst:
	counts[word] = counts.get(word,0) + 1


'''
find the most frequent word which represent
as big_count to return as how many
and big_word as what word
'''

big_count = None
big_word = None


'''
word = key
count = value
example if the dict() counts has:

{'ayaya:3', 'weeb:1', 'yolo:2'}

then the word will read the 'ayaya', 'weeb' and yolo
and the count will read the '3', '1', '2'

look for 9.3 at 7.43

'''


for word,count in counts.items():
	if big_count is None or count > big_count:
		big_count = count
		big_word = word

print(big_word, big_count)