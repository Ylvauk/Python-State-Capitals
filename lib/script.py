from capitals import states
import random

def state_capitals():
    random.shuffle(states)

    print("Welcome to the State Capital Game!")

    right=0
    wrong=0
    for i in range(0, len(states)):
        Input=input(f"Enter the capital of {states[i]['name']}: ")

        if Input == states[i]['capital']:
            right+=1
            print(f'Good job, you have {right} right')
        else:
            wrong+=1
            print(f'Oops, you have {wrong} wrong')

    print(f"Right: {right}")
    print(f"wrong: {wrong}")

    game_over=input(f"Would you like to play again?: ")
    if game_over=='yes':
        return state_capitals()
    else:
        print('Game Over')
        
state_capitals()