def maximumLenghtSubstring(self, s: str) -> int:
    l, r = 0, 0  # Ponteiros da janela
    _max = 1  # Comprimento máximo da substring
    counter = {}  # Dicionário para contar frequências
    counter[s[0]] = 1  # Inicializa o primeiro caractere

    while r < len(s) - 1:
        r += 1  # Expande a janela para a direita
        if counter.get(s[r]):
            counter[s[r]] += 1  # Incrementa a frequência do caractere
        else:
            counter[s[r]] = 1  # Adiciona o caractere ao dicionário

        # Reduz a janela se um caractere aparecer 3 vezes
        while counter[s[r]] == 3:
            counter[s[l]] -= 1  # Decrementa a frequência do caractere à esquerda
            l += 1  # Move o ponteiro à esquerda

        # Atualiza o comprimento máximo
        _max = max(_max, r - l + 1)

    return _max  # Retorna o comprimento máximo