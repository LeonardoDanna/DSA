def lucas(nome):
    nome = "Lucas Donofrio"

    nome_lista = list(nome)

    for i in range(len(nome_lista)-1):
        if nome_lista[i].isalpha() and nome_lista[i+1].isalpha():
            nome_lista[i], nome_lista[i+1] = nome_lista[i+1], nome_lista[i]
            print(''.join(nome_lista))
            
def lucasAoContrario(nome):
    
    nome_invertido = nome[::-1]
    print(nome_invertido)
    
lucasAoContrario("Hello")