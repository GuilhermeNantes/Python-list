v = 6
while True:
    i = int(input("Adiviem qual o numeiro: "))
    if i+4 == v and i-4 ==v:
        print("errou longe. ")
        continue
    elif i == v:
        print("parabems")
        break
    else:
        print("errou ta quase lá. ")
        continue