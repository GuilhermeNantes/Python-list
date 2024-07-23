def caculadora(a,s,b):
    s = str(s)
    if s == "+":
       c =  a + b
       print(f"a resutador foi {c}")
    elif s == "*":
       c =  a * b
       print(f"a resutador foi {c}")
    elif s == "/":
       c =  a / b
       print(f"a resutador foi {c}")
    elif s == "**":
       c =  a ** b
       print(f"a resutador foi {c}")
    else:
       c =  a - b
       print(f"a resutador foi {c}")

    
caculadora(6,"**",2)