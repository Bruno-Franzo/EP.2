#exercicio 1
def define_posicoes(l,c,ori,tam):
    orientacao=ori
    posi0=[l,c]

    posicoes=[]
    posicoes.append(posi0)
    if orientacao=='horizontal':
        for i in range(1,tam):
            c+=1
            posi0=[l,c]
            posicoes.append(posi0)
    elif orientacao=='vertical':
                for i in range(1,tam):
                    l+=1
                    posi0=[l,c]
                    posicoes.append(posi0)
    return posicoes

#exercicio 2
def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    x = define_posicoes(linha,coluna,orientacao,tamanho)
    if navio not in frota:
        frota[navio] = [x]
    else:
        frota[navio].append(x)
    
    return frota

#exercicio 3
def faz_jogada(tabuleiro, linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    
    return tabuleiro