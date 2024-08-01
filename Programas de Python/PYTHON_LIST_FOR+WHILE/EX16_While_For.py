z = 1.20
c = 1.70
for i in range(9):

    if z > c:
        print(f"{z} anos {i} , {c} anos {i}")
        break
    else:
        z += 5
        c += 2