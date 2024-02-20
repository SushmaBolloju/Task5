count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
input_string='Guvi geeks Network private limited'
string = input_string.lower()
for char in string:
    if char=='a':
        count_a+=1
    elif char=='e':
        count_e+=1
    elif char=='i':
        count_i+=1
    elif char=='o':
        count_o+=1
    elif char=='u':
        count_u+=1
print('total_vowels:',count_a+count_e+count_i+count_o+count_u)
print('count of a is:',count_a)
print('count of e is:',count_e)
print('count of i is:',count_i)
print('count of o is:',count_o)
print('count of u is:',count_u)
