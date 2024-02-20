str=input('Enter a string')
vowels = 'aeiouAEIOU'
print('Input string',str)
for char in str:
    if char in vowels:
        str=str.replace(char,'')
print('New string with vowels removed:',str)