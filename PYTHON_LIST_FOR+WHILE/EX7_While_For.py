for i in range(10):
    a = []
    m = []
    t = []
    o = float(input("qual sau nota: "))
    if o > 7:
        a.append(o)
        t.append(o)
    else:
        t.append(o)
        m.append(o)

print("a nota maior que 7.0",a)
print("a nota todas",sum(t) / 10)
print("a maior ",max(a))