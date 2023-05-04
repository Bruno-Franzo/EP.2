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

#exercício 4 

def posiciona_frota(frota):
    grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    for coordenadas_barco in frota.values():
        for posicoes in coordenadas_barco:
            for x,y in posicoes:
                grid[x][y] = 1 


    return grid

#exercicio 5

def afundados(frota,tabuleiro):
    
    afundados = 0
    
    for barco in frota.values():
        for coordenadas in barco:
            acertos = 0
            for x,y in coordenadas:
                if tabuleiro[x][y] == 'X':
                    acertos+=1
                if acertos == len(coordenadas):
                    afundados +=1

    return afundados

#exercício 6 

def posicao_valida(navios,lin,col,ori,tam):
    posicoes=define_posicoes(lin,col,ori,tam)
    validado=True
    for i in posicoes:
        for j in navios.values():
            for k in j:
                for l in k:
                    if l==i:
                        validado=False
        if i[0]>9 or i[0]<0 or i[1]>9 or i[1]<0:
            validado=False
    return validado