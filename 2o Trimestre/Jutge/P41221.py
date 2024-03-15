nums=input()
num=nums.split()
while len(num)!=3:
    if len(num)==1:
        nums=input()
        if nums.isnumeric():
            num.append(nums)
    if len(num)==2:
        nums=input()
        if nums.isnumeric():
            num.append(nums)
tot=int(num[0])+int(num[1])+int(num[2])
print(tot)