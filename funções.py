#exercicio 1
def define_posicoes(l,c,orientacao,tam):
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


#Exercício 7 

PA=0
NT=0
CT=0
SM=0

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
while PA<1:
    print('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')
    linha=int(input('linha: '))
    coluna=int(input('coluna: '))
    orientacao=input('[1] Vertical [2] Horizontal > ')
    if orientacao == '1':
        orientacao = 'vertical'
    elif orientacao == '2':
        orientacao = 'horizontal'
    posicao = posicao_valida(frota,linha,coluna,orientacao,4)
    if posicao==True:
        PA+=1
        frota=preenche_frota(frota,'porta-aviões',linha,coluna,orientacao,4)
    else:
        print('Esta posição não está válida!')
while NT<2:
    print('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')
    linha=int(input('linha: '))
    coluna=int(input('coluna: '))
    orientacao=input('[1] Vertical [2] Horizontal > ')
    if orientacao == '1':
        orientacao = 'vertical'
    elif orientacao == '2':
        orientacao = 'horizontal'
    posicao = posicao_valida(frota,linha,coluna,orientacao,3)
    if posicao==True:
        NT+=1
        frota=preenche_frota(frota,'navio-tanque',linha,coluna,orientacao,3)
    else:
        print('Esta posição não está válida!')
while CT<3:
    print('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')
    linha=int(input('linha: '))
    coluna=int(input('coluna: '))
    orientacao=input('[1] Vertical [2] Horizontal > ')
    if orientacao == '1':
        orientacao = 'vertical'
    elif orientacao == '2':
        orientacao = 'horizontal'
    posicao = posicao_valida(frota,linha,coluna,orientacao,2)
    if posicao==True:
        CT+=1
        frota=preenche_frota(frota,'contratorpedeiro',linha,coluna,orientacao,2)
    else:
        print('Esta posição não está válida!')
while SM<4:
    print('Insira as informações referentes ao navio submarino que possui tamanho 1')
    linha=int(input('linha: '))
    coluna=int(input('coluna: '))
    posicao = posicao_valida(frota,linha,coluna,orientacao,1)
    if posicao==True:
        SM+=1
        frota=preenche_frota(frota,'submarino',linha,coluna,orientacao,1)
    else:
        print('Esta posição não está válida!')
print(frota)