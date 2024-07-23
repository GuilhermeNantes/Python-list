while True:
    opi = int(input("digite uma opição ex(1 soma,2 sub,3 mutlp,4 div,5 saida)"))

    if opi < 0 and opi >= 6:
        print("ERRO: por favor umas opição de 1 a 5.")
        break
    elif opi == 1:
        soma1 = int(input("digite um numeiro: "))
        soma2 = int(input("digite um numeiro: "))
        resoma = soma1 + soma2
        print("resutado: ",resoma)
        continue
    elif opi == 2:
        sub1 = int(input("digite um numeiro: "))
        sub2 = int(input("digite um numeiro: "))
        resub = sub1 + sub2
        print("resutado: ",resub)
        continue
    elif opi == 3:
        mulp1 = int(input("digite um numeiro: "))
        mulp2 = int(input("digite um numeiro: "))
        remulp = mulp1 + mulp2
        print("resutado: ",remulp)
        continue
    elif opi == 4:
        div1 = int(input("digite um numeiro: "))
        div2 = int(input("digite um numeiro: "))
        rediv = div1 + div2
        print("resutado: ",rediv)
        continue
    else:
        print("saiando do programa...")
        break