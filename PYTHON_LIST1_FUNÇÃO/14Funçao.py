import random 
def aleot(par:str):
    c = []
    for i in par:
        c.append(i)
    for u in c:
        print(random.choice(c),end="")    

aleot('ERTYUIO')