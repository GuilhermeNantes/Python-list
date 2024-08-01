import random
def sortearalunos(n):
    a = []
    for i in range(n):
        w = str(input("Digite o nome do aluno: "))
        a.append(w)

    print("o Primeiro aluno(a) a se apresentar: ",random.choice(a))
sortearalunos(3)