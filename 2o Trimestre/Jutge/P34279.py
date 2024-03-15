tiempo=input()
hms=tiempo.split()
h=int(hms[0])
m=int(hms[1])
s=int(hms[2])
se=int(s)+1
if h==23 and m==59 and s==59:
    print("00:00:00")
elif se==60:
    se="00"
    mi=int(m)+1
    if mi==60:
        mi="00"
        ho=int(h)+1
        if ho<10:
            print(f"0{ho}:{mi}:{se}")
        else:
            print(f"{ho}:{mi}:{se}")
    else:
        if mi<10:
            if h<10:
                print(f"0{h}:0{mi}:{se}")
            else:
                print(f"{h}:0{mi}:{se}")
        elif h<10:
                print(f"0{h}:{mi}:{se}")
        else:
            print(f"{h}:{mi}:{se}")
else:
    if se<10:
        if m<10:
            if h<10:
                print(f"0{h}:0{m}:0{se}")
            else:
                print(f"{h}:0{m}:0{se}")
        elif h<10:
            print(f"0{h}:{m}:0{se}")
        else:
            print(f"{h}:{m}:0{se}")
    elif m<10:
        if h<10:
                print(f"0{h}:0{m}:{se}")
        else:
            print(f"{h}:0{m}:{se}")
    elif h<10:
        print(f"0{h}:{m}:{se}")
    else:
        print(f"{h}:{m}:{se}")