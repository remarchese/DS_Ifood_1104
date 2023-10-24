def funcao_fatorial(num):
    fatorial = 1
    if num < 0:
        return print("Não existe fatorial de número negativo")
    elif num == 0:
        return print("O fatorial de 0 é 1")
    else:
        for c in range(num,0,-1):
            fatorial = fatorial * c # 5*1 => 4 * 5 => 3 * 4*5 => 2*3*4*5 => 1*2*3*4*5
        return print(f"O fatorial de {num} é {fatorial}")