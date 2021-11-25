from Client import *
from datetime import date
import pytest

@pytest.fixture
def client1():
    return Client('Ricardo', '25/01/1995')

def test_raise_error_if_contain_no_str_in_the_name(client1):
    with pytest.raises(Client_error):
        client1.name = 'R1cardo'

def test_match_correct_birth_date_with_re_pattern(client1):

    assert client1.birth_date == '25/01/1995'

def test_raise_error_if_birth_dathe_out_of_pattern(client1):
    with pytest.raises(Client_error):
        client1.birth_date = '32/1/1995'

def test_age_complete_current_year(client1):

    assert client1.age == date.today().year - 1995

def test_age_incomplete_current_year_birthday_in_months(client1):
    client1.birth_date = f'25/{date.today().month +1}/1995'
    assert client1.age == date.today().year - 1995 -1

def test_age_incomplete_current_year_birthday_in_days(client1):
    client1.birth_date = f'{date.today().day+1}/{date.today().month}/1995'
    assert client1.age == date.today().year - 1995 -1

