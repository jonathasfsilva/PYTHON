while True:
    b_originais, pessoas = [int(x) for x in input().split()]
    
    if b_originais == pessoas == 0:
        break
    
    originais = []
    falsos = []
    n_bilhetes = [int(x) for x in input().split()]
    n_bilhetes = n_bilhetes[0:pessoas]
    
    for n in n_bilhetes:
        if n not in originais:
            originais.append(n)
        elif n not in falsos:
            falsos.append(n)

    print(len(falsos))
            
