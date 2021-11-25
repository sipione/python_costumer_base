import exceptions
from Menu import *
from execution_comand import *


menu1 = Menu('Menu principal', ['new costumer', 'consult costumer base', 'edit costumer',
             'delete costumer', 'exit'])

while True:
    menu1.show_options()
    answer = input('Whats your choose? ').strip()
    try:
        menu1.option_check(answer)
    except Exception as error:
        exceptions.raise_error(error)
        continue

    if answer == '0':
        play_option_0()

    elif answer == '1':
        play_option_1()

    elif answer == '2':
        play_option_2()

    elif answer == '3':
        play_option_3()

    elif answer == '4':
        break





