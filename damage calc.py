dado= int(input('quantos dados vai rolar:'))
ataques= int(input('quantos ataques iguais vai fazer:'))
bonus= int(input('qual seu bonus para acertar:'))
ac=int(input('qual ac quer acertar:'))
dano=int(input('dano por cada ataque:'))
dano_uma_vez = int(input('dano em um ataque só:'))
crit =int(input('dano em um critico:'))
hc = (1-pow(((ac-bonus)/20),dado))
uma_vez= pow((hc),ataques+dado)
dano_por_round =(ataques*(hc*(dano))+(dado/20)*crit)+uma_vez*dano_uma_vez
print(dano_por_round)
