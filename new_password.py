def newPassword(a, b):
    res = []
    # Alterna os caracteres das duas strings
    for first, second in zip(a, b):
        res.append(first)
        res.append(second)
    
    # Adiciona o restante dos caracteres da string maior
    if len(a) > len(b):
        res.extend(a[len(b):])
    elif len(b) > len(a):
        res.extend(b[len(a):])
    
    return ''.join(res)
