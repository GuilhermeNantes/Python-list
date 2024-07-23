a = []
d = []
c = []
for i in range(20):
    o = int(input("digite um numeiro: "))
    if o % 2 == 0:
        a.append(o)
    elif o % 2 == 1:
        d.append(o)
    else:
        c.append(o)

print("par",a)
print("impar",d)
print("os numeiro digitados",c)
             