intervalos=input()
inters=intervalos.split()
max=""
min=""
if inters[0]<inters[2]:
    max=inters[2]
else:
    max=inters[0]
if inters[1]<inters[3]:
    min=inters[1]
else:
    min=inters[3]
if inters[0]==inters[2] and inters[1]==inters[3]:
    print(f"= , [{inters[0]},{inters[1]}]")
elif inters[2]<=inters[0] and  inters[1]<=inters[3]:
    print(f"1 , [{inters[0]},{inters[1]}]")
elif inters[0]<=inters[2] and inters[3]<=inters[1]:
    print(f"2 , [{inters[2]},{inters[3]}]")
elif max>min:
    print("? , []")
else:
    print(f"? , [{max},{min}]")
