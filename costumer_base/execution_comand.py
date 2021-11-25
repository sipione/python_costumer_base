from time import sleep
from exceptions import *
from Client import Client
from Menu import *


def play_option_0():
    while True:
        Title_format('New costumer registration system').show_title()
        name = input("What's your name: ").strip().title()
        birth_date = input("What's the birthdate (dd/mm/yyyy): ")
        try:
            client = Client(name, birth_date)
        except Exception as error:
            raise_error(error)
        else:
            while True:
                if __ask_to(f"Would you like to register {client.name}, {client.age} years old, "
                      f"who was born in {client.birth_date}? "):
                    try:
                        client.register()
                    except Exception as error:
                        raise_error(error)
                    else:
                        print(f'{name} was registrad with sucess')
                        break
                else:
                    print(f'ok, {name} WAS NOT registrated....')
                    sleep(2)
                    break

            if __ask_to('Would you like to keep registring? '):
                continue
            else:
                break


def play_option_1():
    list = __show_costumer_base()
    list_name = [item[0] for item in list]
    play_1_menu = Menu("Below are all costumer's name and cod", list_name)
    play_1_menu.show_options()
    if not __ask_to("Would you like to consult a costumer information? "):
        sleep(0.5)
        print('*'*30)
        print('returning to main menu...')
        print('*'*30)
        sleep(1.5)
    else:
        while True:
            cod = int(input('Type the costumer cod: '))
            try:
                play_1_menu.option_check(cod)
            except Exception as error:
                raise_error(error)
            else:
                print(f"{'name':^20}{' birthdate':^10}{'age':>13}")
                print(f"{list[cod][0]:.<20}{list[cod][1]:.^10}{list[cod][2]:.>10}")

            if __ask_to("Would you like to choose another costumer[Y/N]? "):
                play_1_menu.show_options()
                pass
            else:
                list.clear()
                break


def play_option_2():
    while True:
        list = __show_costumer_base()
        play_2_menu = Menu("editing costumer sistem", list)
        play_2_menu.show_options()
        client_edit = int(input("What's the costumer's cod which you would like to edit the "
                                "informations? "
                                "").strip())
        try:
            play_2_menu.option_check(client_edit)
        except Exception as error:
            raise_error(error)
        else:
            with open('clients.txt', 'r') as f:
                file_content = f.readlines()
                f.close()
            info = file_content[client_edit].split(",")
            if __ask_to(f"Are you sure want to edit the {info[0]} informations? "):
                try:
                    file_content.remove(file_content[client_edit])
                    with open('clients.txt', 'w') as g:
                        new_contents = "".join(file_content)
                        g.write(new_contents)
                        g.close()
                    sleep(1)
                    print(f"Ok... now is time to rewrite the costumer informations!")
                    sleep(1)
                    play_option_0()
                except Exception as error:
                    print('*' * 30)
                    print(error)
                    print('*' * 30)
            else:
                print(f"Ok! {info[0]} keep registered in the sistem, WAS NOT edited.")
                sleep(1.5)
            if __ask_to("Would you like to edit another costumers' informations? "):
                continue
            else:
                sleep(0.5)
                print(f"Ok! returning to main menu...")
                sleep(1)
                break


def play_option_3():
    while True:
        list = __show_costumer_base()
        play_3_menu = Menu("Exclusion costumer sistem", list)
        play_3_menu.show_options()
        client_deleted = int(input("What's the costumer's cod which you would like to delete? "
                                   "").strip())
        try:
            play_3_menu.option_check(client_deleted)
        except Exception as error:
            raise_error(error)
        else:
            with open('clients.txt', 'r') as f:
                file_content = f.readlines()
                f.close()
            info = file_content[client_deleted].split(",")
            if __ask_to(f"Are you sure want to delete the {info[0]} informations? "):
                try:
                    file_content.remove(file_content[client_deleted])
                    with open('clients.txt', 'w') as g:
                        new_contents = "".join(file_content)
                        g.write(new_contents)
                        g.close()
                except Exception as error:
                    print('*' * 30)
                    print(error)
                    print('*' * 30)
                else:
                    sleep(0.5)
                    print(f"ok! deleting {info[0]} informations")
                    sleep(1.5)
            else:
                print(f"Ok! {info[0]} keep registered in the sistem, WAS NOT deleted.")
                sleep(1.5)

            if __ask_to("Would you like to delete another costumer? "):
                continue
            else:
                sleep(0.5)
                print(f"Ok! returning to main menu...")
                sleep(1)
                break


def __show_costumer_base():
    list = []
    with open('clients.txt', 'r') as f:
        for pos, line in enumerate(f.readlines()):
            info = line.replace("\n", "").split(',')
            list.append(info)
        f.close()
    return list


def __ask_to(txt):
    while True:
        keep = input(txt).strip(
        ).lower()[0]
        if 'n' in keep:
            return False
        elif 'y' in keep:
            return True
        else:
            sleep(1)
            print('*'*30)
            print('invalid answer, please, type only "Y/N".')
            print('*'*30)
            sleep(1)