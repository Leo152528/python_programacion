nums=input()
num=nums.split()
if len(num)==1:
    nums=input()
    num.append(nums)
if int(num[0])<int(num[1]):
    print(num[1])
else:
    print(num[0])