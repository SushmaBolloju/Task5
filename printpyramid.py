def print_pyramid(rows):
    num=1
    for i in range(1,rows+1):
        for j in range(1,rows-i+1):
            print("",end="")
        for j in range(1,i+1):
            print(num,end="")
            num=num+1
            if num>20:
                break
        print()
print_pyramid(6)

