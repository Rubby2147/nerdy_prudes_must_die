atk = int(input('quantos ataques diferentes uns dos outros vai fazer:'))
ac=int(input('qual ac quer acertar:'))
     
    dado= int(input('quantos dados vai rolar:'))
    ataques= int(input('quantos ataques iguais vai fazer:'))
    bonus= int(input('qual seu bonus para acertar:'))
    dano=int(input('dano por cada ataque:'))
    crit =int(input('dano em um critico:'))
    hc = (1-pow(((ac-bonus)/20),dado))
    ataque1 =(ataques*(hc*(dano))+(dado/20)*crit)
fatores = list (dado, ataques,bonus,dano,crit,hc, ataque)
for atk in fatores:
