nums=input()
num=nums.split()
if len(num)==1:
    nums=input()
    num.append(nums)
tot=int(num[0])+int(num[1])
print(tot)