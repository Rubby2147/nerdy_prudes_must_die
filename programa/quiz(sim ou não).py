print ('ola vamos começar (reponda 1 para sim e 2 não)')
print ('primeira pergunta')
primeira= int(input ('você acha certo bater em criança pra deducar:'))
print ('segunda pergunta')
segunda = int(input ('você acha que outros merecem menos que você:'))
print ('terceira pergunta')
terceira = int(input ('o captalismo é bom:'))
print ('quarta pergunta')
quarta = int(input ('você sente que na vida é cada um por si:'))
print ('quinta pergunta')
quinta = int(input ('a lei é mais importante que o bem estar alheio:'))

soma = primeira + segunda + terceira + quarta + quinta
if soma <=5:
    print ('você não é bom')
elif soma >=6 and soma <10:
    print (' você é uma boa pessoa')
else: soma >= 10
print ('você é uma otima pessoa') 