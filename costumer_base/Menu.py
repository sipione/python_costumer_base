from exceptions import Menu_error


class Menu:
    def __init__(self, title, txt: list):
        self.title = Title_format(title)
        self.txt =txt


    def show_options(self):
        self.title.show_title()
        print(f'Choose an option below typing a number from {0} to {len(self.txt) -1}')
        for i, e in enumerate(self.txt):
            print(f'{i} -> {e}')

    def option_check(self, answer):
        if not str(answer).isnumeric():
            raise Menu_error('Only numeric answer is available')
        if int(answer) < 0 or int(answer) > len(self.txt)-1:
            raise Menu_error(f'Choose out of range, please choose a number between 1 and '
                             f'{len(self.txt)}')
        else:
            return True


class Title_format:
    def __init__(self, title):
        self.title = title

    def show_title(self):
        size = len(self.title) + 4
        print(f'{"-" * size:^30}')
        print(f'{self.title:^30}')
        print(f'{"-" * size:^30}')

