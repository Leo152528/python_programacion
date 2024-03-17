year=input()
nums=year[0]+year[1]
noms=year[2]+year[3]
x=int(year)%4
if x==0:
    if noms=="00":
        if int(nums)%4==0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
else:
    print("NO")
