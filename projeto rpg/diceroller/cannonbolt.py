import random
while True:
    dice=int(input('how many dice are you gonna roll:'))
    dsize=int(input('what is the dice size:'))
    bonus=int(input('what is your bonus to the roll:'))
    for i in range(dice):    
        solv=random.randint(1,dsize)
        print('your roll is:',solv+bonus)