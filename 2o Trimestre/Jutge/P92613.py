x=float(input())
y=int(x)
z=x-y
if z>=0.5:
    print(int(x),int(x)+1,int(x)+1)
elif z==0:
    print(int(x),int(x),int(x))
else:
    print(int(x),int(x)+1,int(x))
    