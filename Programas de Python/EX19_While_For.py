while True:
    a = []
    c = int(input("digite um numeiro"))
    res = input("quer continuar: ")
    if res in "Ss" or c == 0:
        break
    else:
        a.append(c)
        continue

print("a soma de todos numeiro: ",sum(a))
print("digitados: ",len(a))
print("a media de numerios: ",sum(a)/len(a))
print("a menor: ",max(a))
print("a maior: ",min(a))
print("a soma de todos numeiro: ",sum(a/2))