alte = str(input("digite o nome do atleta: "))
pla = []
a = []
for I in range(7):
    jur = float(input("digite a nota do atleta: "))
    if jur >= 0 or jur <= 10.0:
        a.append(jur)
        continue
    else:
        print("NUMEIRO INVALIDO: ")
        break

print("atleta: ",alte)
print("melhor nota: ",max(a))
print("melhor pior nota: ",min(a))
print("a media foi: ",sum(a)/7)