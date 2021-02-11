import random

def roll_dice(amount=1, value=20, mod=0):
    result = 0
    history = []

    if value not in [2, 4, 6, 8, 10, 12, 20, 100]:
        return (-1,['Invalid Dice Type'])
    elif amount < 1:
        return (-1, ['Invalid Dice Amount'])
    else:
        while amount > 0:
            roll = random.randint(1,value)
            history.append(roll)
            result += roll
            amount -= 1
    
    result += mod
    return (result, history)
