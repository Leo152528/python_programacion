intervalos=input()
inters=intervalos.split()
if inters[0]==inters[2] and inters[1]==inters[3]:
    print("=")
elif inters[2]<=inters[0] and  inters[1]<=inters[3]:
    print("1")
elif inters[0]<=inters[2] and  inters[3]<=inters[1]:
    print("2")
else:
    print("?")
