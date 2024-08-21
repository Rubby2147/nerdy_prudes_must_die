
ac=int(input('qual ac quer acertar:'))

dado= int(input('quantos dados vai rolar:'))
ataques= int(input('quantos ataques iguais vai fazer:'))
bonus= int(input('qual seu bonus para acertar:'))
dano=int(input('dano por cada ataque:'))
crit =int(input('dano em um critico:'))
hc = (1-pow(((ac-bonus)/20),dado))
ataque1 =(ataques*(hc*(dano))+(dado/20)*crit)

uma_vez= pow((hc),ataques+dado)
dano_uma_vez = int(input('dano em um ataque só:'))

tipos_de_ataques= int(input('quantos ataques diferentes um dos outros vai fazer:'))
if tipos_de_ataques >2:
    dano_por_round = ataque1+dano_uma_vez
elif tipos_de_ataques == 2:
    dado2= int(input('quantos dados vai rolar:'))
    ataques2= int(input('quantos ataques iguais vai fazer:'))
    bonus2= int(input('qual seu bonus para acertar:'))
    dano2=int(input('dano por cada ataque:'))
    crit2 =int(input('dano em um critico:'))
    hc2 = (1-pow(((ac-bonus2)/20),dado2))
    ataque2 =(ataques2*(hc2*(dano2))+(dado2/20)*crit2)
    dano_por_round = ataque1+ataque2+dano_uma_vez
else: tipos_de_ataques >= 3
dado3= int(input('quantos dados vai rolar:'))
ataques3= int(input('quantos ataques iguais vai fazer:'))
bonus3= int(input('qual seu bonus para acertar:'))
dano3=int(input('dano por cada ataque:'))
crit3 =int(input('dano em um critico:'))
hc3 = (1-pow(((ac-bonus3)/20),dado3))
ataque3 =(ataques3*(hc3*(dano3))+(dado3/20)*crit3)
dano_por_round = ataque1+ataque2+ataque3+dano_uma_vez

print(dano_por_round)