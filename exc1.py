def define_posicoes(l,c,ori,tam):
    orientacao=ori
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