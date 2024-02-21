string=input("enter the string:")
char=input("enter the character to find the frequency:")
count=0
for i in string:
    if (i==char):
        count=count+1
print("the frequency of char in the string is:",count)