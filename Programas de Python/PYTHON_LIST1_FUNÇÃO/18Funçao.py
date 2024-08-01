def pri(n:int):
    t = 0
    f = 6
    for i in range(100):
        if i % 2 == 1:
            print(" "*f,"*"*i) 
            t += 1
            f -= 1
        elif t == n:
            break

pri(6)