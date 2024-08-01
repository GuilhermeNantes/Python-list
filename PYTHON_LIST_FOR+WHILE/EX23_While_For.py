print("academiaBemforte")
j = 2 ## limite
q = w = e = c = cm= 0
a =[]
g =[]
for i in range(j):
    idade = int(input("digite sua idade: "))
    sexo = input("digite seu genero: ")
    altura = float(input("digite seu altura "))
    peso = float(input("digite seu peso "))
    
    if sexo in "man":
        c += 1
    elif sexo in "she":
        cm += 1
    elif idade > q :
        q = idade
    else:
        a.append(q)
    if altura > w :
        w = altura
    else:
        g.append(w)
    if peso > e:
        e = peso
    
                
somam = c / i
somas = cm / i

print("a idade da pessoa mais velha: ",q)
print("a idade da pessoa mais nova: ",min(a))
print("altura da pessoa mais alta: ",w)
print("altura da pessoa mais baixa: ",min(g))
print("o maior peso: ",e)
print("porcentagem de Sexo Masculino",somam)
print("porcentagem de Sexo Feminino",somas)
