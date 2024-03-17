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
if max>min:
    print("[]")
else:
    print(f"[{max},{min}]")
