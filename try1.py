from pywebio.output import *
from pywebio.input import *


from pywebio import start_server



from functools import partial
import random
computer = random.randint(1,3)
def rps():
    put_text('this game is rock paper scissor\n rock =1 \n paper =2 \n scissor =3 \n')
    put_table([
        ['your choice', ' number'],
        ['rock', '1'],
        ['paper', '2'],
        ['scissor', '3']
    ])

    while True:

        number = radio("Choose one", options=[1, 2, 3])
        choice = ['rock', 'paper', 'scissor']
        ans = radio(f'you choose {number}which is{choice[int(number) - 1]}', options=['firm', 'le me chos again'])

        if ans == 'le me chos again':
            continue
        computer = random.randint(1, 3)

        your_choice = choice[int(number) - 1]
        computer_choice = choice[int(computer) - 1]
        put_text(f'computer chooes {computer_choice}\n')
        put_text(f'{your_choice} vs {computer_choice}')



        number = int(number)
        computer = int(computer)
        con1 = number == 1 and computer == 3
        con2 = number == 2 and computer == 1
        con3 = number == 3 and computer == 2

        if number == computer:
            x = 'its a tie'
        elif con1 or con2 or con3:
            x = 'you win'
        else:
            x = 'computer win'

        put_button("reults ", onclick=lambda: toast(x), color='success', outline=True)




        break
if __name__ == '__main__' :
    start_server(rps,port=8080,debug=False)
