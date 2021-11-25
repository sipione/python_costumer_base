from datetime import date, datetime
from exceptions import Client_error


class Client():
    def __init__(self, name, birth_date):
        self.__name = self._name_validator(name)
        self.__birth = self._birth_validator(birth_date)
        self.__age = self.age_generator(birth_date)

    def age_generator(self, birth_date):
        date_format = datetime.strptime(birth_date, '%d/%m/%Y')
        today = date.today()
        if date_format.month > today.month or \
                (date_format.month == today.month and date_format.day > today.day):
            return today.year - date_format.year - 1
        else:
            return today.year - date_format.year

    def _name_validator(self, name):
        sequence = "".join(name.split(" "))
        if sequence.isalpha():
            return name
        else:
            raise Client_error("name doesn't supposed to contain numbers")

    @property
    def name(self):
        return self.__name

    @property
    def birth_date(self):
        return self.__birth

    @property
    def age(self):
        return self.age_generator(self.__birth)

    def _birth_validator(self, birth_date):
        try:
            date_format = datetime.strptime(birth_date, '%d/%m/%Y')
        except:
            raise Client_error('The birth date must to follow the pattern dd/mm/yyyy')
        else:
            return datetime.strftime(date_format, '%d/%m/%Y')

    @birth_date.setter
    def birth_date(self, value):
        self.__birth = self._birth_validator(value)

    @name.setter
    def name(self, value):
        self.__name = self._name_validator(value)

    def __repr__(self):
        return f'{self.name,self.birth_date,self.age}\n'

    def __str__(self):
        return f'{self.__dict__}'

    def register(self):
        with open('clients.txt', 'a') as f:
            f.write(f'{self.name},{self.birth_date},{self.age}\n')
            f.close()

