c = int(input("digite seu numeiro"))
a = int(input("digite seu numeiro"))
s=[]
f = a - c
for i in  range(f):
    if i % 2 != 0:
        s.append(i)
print(s)