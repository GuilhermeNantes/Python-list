s = []
a = str(input("digite sua palavra: "))
for i in a:
    
    if i in "Aa":
        s.append(i)
    elif i in "Ee":
        s.append(i)
    elif i in "Ii":
        s.append(i)
    elif i in "Oo":
        s.append(i)
    elif i in "Uu":
        s.append(i)
    else:
         continue

print(s)