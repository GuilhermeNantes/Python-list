def pot(a,b):
    for i in range(1,b+1,1):
        soma = a ** i
        print(f"{a} ** {i} = {soma}")

pot(2,3) 