s1=input("enter the first string:")
s2=input("enter the second string:")
lcs_table=[[0]*(len(s2)+1) for i in range(len(s1)+1)]
max_length=0
ending_index=0

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            lcs_table[i][j]=lcs_table[i-1][j-1]+1
            if lcs_table[i][j]>max_length:
                max_length=lcs_table[i][j]
                ending_index=i
        else:
            lcs_table[i][j]=0
print("longest_common_substring:",s1[ending_index-max_length:ending_index])