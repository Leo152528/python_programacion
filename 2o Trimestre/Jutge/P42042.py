let=input()
if let.isupper():
    print("uppercase")
else:
    print("lowercase")
x=let.casefold()
if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
    print("vowel")
else:
     print("consonant")