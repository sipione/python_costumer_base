from time import sleep


class Client_error(Exception):
    pass

class Menu_error(Exception):
    pass

def raise_error(error):
    sleep(1)
    print('*' * 30)
    print('Invalid information')
    print(error)
    print('Try again please')
    print('*' * 30)
    sleep(1)
    print('Returning...')
    sleep(2)