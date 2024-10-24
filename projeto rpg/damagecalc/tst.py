ataques= int(input('quantos ataques iguais vai fazer:'))
dado = int(input('quantos dados vai rolar:')) 
bonus= float(input('qual seu bonus para acertar:'))
dano=float(input('dano por cada ataque:'))
cc=int(input('quantas faces do dado que dá critco:'))
crit =float(input('dano em um critico:'))
ac=int(input('qual ac quer acertar:'))

rest =[]
hc=(1-pow(((ac-bonus)/20),dado))
for x in range(ataques):
    wmd = float((ataques-x-1)*(1-pow(hc,2))*hc*(dano+0.1*crit))
rest.append(wmd)
print(rest)