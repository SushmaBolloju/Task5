a = input('Enter first string :')
b = input('Enter second string :')
count = 0
for i in a:
    if i in b:
        count = count + 1
if count == len(b):
    print('anagram')
else:
    print("not an anagram")

