def texto():
    listames = ["nao existe 00","janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"] 
    dia,mes,ano = input("digite o dia e mes e ano atual: ").split("/")
    mes = int(mes)
    print(dia,listames[mes],ano) 

texto()