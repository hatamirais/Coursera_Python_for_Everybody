"""
fruit = 'ayaya'
index = 0
while index < len(fruit):
    x = fruit[index]
    print(index, x)
    index = index + 1



fruit = 'banana'
for x in fruit:
    print(x)


fruit = 'ayaya'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    letter = index + 1


word = "ayaya"
count = 0
for x in word:
    if x == 'a':
        count = count + 1
print(count)


"""

if word == 'banana':
    print('Alright bananas.')

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Yout wiord' + word + ', comes after banana.')
else:
    print('allright')