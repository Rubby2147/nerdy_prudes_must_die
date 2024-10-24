import random
while True:
    dice=int(input('how many times are you gonna roll:'))
    dsize=int(input('what is the dice size:'))
    avg=int(input('how many rolls are you choosing from'))
    reroll=[(input('do you reroll in which numbers'))]
    for i in range(dice):    
        solv=[random.randint(1,dsize) for x in range(avg)]
        while solv==reroll:
            solv=[random.randint(1,dsize) for x in range(avg)]
        print(solv)
        