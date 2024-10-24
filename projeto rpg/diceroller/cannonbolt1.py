import random
while True:
    dice=int(input('how many times are you gonna roll:'))
    dsize=int(input('what is the dice size:'))
    bonus=int(input('what is your bonus to the roll:'))
    avg=int(input('how many rolls are you choosing from'))
    for i in range(dice):    
        solv=[random.randint(1,dsize) for x in range(avg)]
        print(solv)
        
