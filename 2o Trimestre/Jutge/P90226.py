pals=input()
pal=pals.split()
if pal[0]>pal[1]:
    print(f"{pal[0]} > {pal[1]}")
elif pal[0] < pal[1]:
    print(f"{pal[0]} < {pal[1]}")
else:
    print(f"{pal[0]} = {pal[1]}")