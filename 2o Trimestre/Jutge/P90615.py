nums=input()
num=nums.split()
if int(num[0])>int(num[1]):
    if int(num[0])>int(num[2]):
        print(num[0])
    else:
        print(num[2])
else:
    if int(num[1])>int(num[2]):
        print(num[1])
    else:
        print(num[2])