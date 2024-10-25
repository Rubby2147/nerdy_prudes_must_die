import random
while True:
    func=input('what do you wanna do? (choose_dice or add_dice):')

    if func == 'choose_dice':
        avg=int(input('how many diferente rolls are you gonna make:'))
        dsize=int(input('what is the dice size:'))
        bonus=int(input('input the bonus to the roll'))
        solv=[random.randint(1,dsize) for x in range(avg)]
        print(max(solv)+bonus)
    
    elif func =='add_dice':
        dice=int(input('how many diferente rolls are you gonna make:'))
        dsize=int(input('what is the dice size:'))
        avg=int(input('how many rolls are you making:'))    
        bonus=int(input('what is your bonus to the roll:'))
        for i in range(dice):
            solv=[random.randint(1,dsize) for x in range(avg)]
            print(solv,'+',bonus,"=",(sum(solv)+bonus))
    else:
        print('error')
    print('='*50)