import random
l = []
def sorteia():
    for i in range(5):
        a = random.randint(1,100)
        return l.append(a)
    
def somapar():
    p = 0
    for i in l:
        p += i
        print(p)

sorteia()
somapar()