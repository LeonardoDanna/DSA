def firstUniqChar(self, s: str) -> int: #Problema com HashMap
    d = {}  # Dicionário para armazenar informações sobre cada caractere 

    # Primeiro loop: Contagem de caracteres
    for idx, ch in enumerate(s):
        if not d.get(ch):
            d[ch] = [idx, 1]  # Adiciona o caractere ao dicionário
        else:
            d[ch][1] += 1  # Incrementa a contagem do caractere

    # Segundo loop: Encontrando o primeiro caractere único
    for ch, val in d.items():
        if val[1] == 1:  # Verifica se a contagem é 1
            return val[0]  # Retorna o índice da primeira ocorrência

    return -1  # Retorna -1 se nenhum caractere único for encontrado