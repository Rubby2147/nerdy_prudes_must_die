print ('ola vamos começar')

sim = 1
não = 2

print ('primeira pergunta')
primeira= (input ('você acha certo bater em criança pra deducar:'))
print ('segunda pergunta')
segunda = (input ('você acha que outros merecem menos que você:'))
print ('terceira pergunta')
terceira = (input ('o captalismo é bom:'))
print ('quarta pergunta')
quarta = (input ('você sente que na vida é cada um por si:'))
print ('quinta pergunta')
quinta = (input ('a lei é mais importante que o bem estar alheio:'))

soma = primeira + segunda + terceira + quarta + quinta
if soma <=5:
    print ('você não é bom')
elif soma >=6 and soma <10:
    print (' você é uma boa pessoa')
else: soma >= 10
print ('você é uma otima pessoa') 