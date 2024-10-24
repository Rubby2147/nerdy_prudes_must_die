quer=input('quer calcular (s/n):')
while quer=='s' or quer== '1':
    print('='*50)
    atk = int(input('quantas vezes vai calcular:'))
    print('='*50)
    resultados= []
    for x in (range(atk)):
        ac=int(input('qual ac quer acertar:'))
        ataques= int(input('quantos ataques iguais vai fazer:'))
        dado = int(input('quantos dados vai rolar:')) 
        bonus= float(input('qual seu bonus para acertar:'))
        dano=float(input('dano por cada ataque:'))
        crit =float(input('dano em um critico:'))
        cc=int(input('quantas faces do dado que dá critco:'))
        wm= input('qual sua weapon mastery:')
        pam=int(input('vai fazer um ataque com dano diferente(s/n):'))
        if pam == 's':
            pamy=input('quanto dano da esse ataque:')
            cpamy=input('quanto dano da esse critco:')
            pbonus=input('qual o bonus desse ataque')
        else:
            pamy=0 
            cpamy=0
            pbonus=0
        sm= input('você tem mestre de escudo (s/n):')
        kye= input('você ganha vantagem se errar (s/n):')
        dano_em_um_atk= float(input('dano em um ataque só:'))
        print('='*50)

        hc=(1-pow(((ac-bonus)/20),dado))
        ataque=float(ataques*(hc*dano+((dado*(cc/20))*crit)))
        
        dano_uma_vez= dano_em_um_atk*(pow(hc,ataques)) 

        if wm == 'vex' and dado<2:
             wmd = float((ataques-1)*(1-pow(hc,2))*dano)*pow(hc,(ataques))
        elif wm == 'topple'and dado<2:
         wmd = float((ataques-1)*(1-pow(hc,2))*dano*pow(hc,(ataques)))*0.4
        elif wm =='graze':
            dg=int(input('dano do graze:'))
            print('='*50)
            wmd = ((1-hc)*dg)*ataques
        else:
             wmd = 0

        if kye == "s" and dado<2:
            dkye=float((ataques-1)*(1-pow(hc,2))*dano)*pow(1-hc,(ataques))
        else:
            dkye=0

        if sm == "s" and dado <1 and not wm =='vex':
            dsm=float((ataques-1)*(1-pow(hc,2))*pow(hc,(ataques)*dano))*0.4
        else:
            dsm=0

        phc=(1-pow(((ac-pbonus)/20),dado))
        pamd=ataque=float(phc*pamy+((dado*(cc/20))*cpamy))

        resultado = [ataque+wmd+dano_uma_vez+dkye+dsm+pamd]
        resultados.append(resultado)
    total_de_dano =  resultados

    print('='*50)
    print ('seu dano medio por turno é:',total_de_dano)
    print('='*50)
    quer=input('quer calcular (s/n):')

if quer == 'n' or '0':
    print('fim')
else:
    print ('error')