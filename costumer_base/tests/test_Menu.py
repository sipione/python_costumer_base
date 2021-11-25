import pytest
from Menu import *

@pytest.fixture
def menu1():
    return Menu('Menu principal', 'inicio', 'aula01', 'aula02', 'recreio')

def test_register_all_options_as_txt(menu1):
    assert len(menu1.txt) == 4

def test_raise_error_answer_out_of_range_higher(menu1):
    with pytest.raises(Menu_error):
         answer = '5'
         menu1.option_check(answer)
def test_raise_error_answer_lower_than_range_options(menu1):
    with pytest.raises(Menu_error):
        answer = '0'
        menu1.option_check(answer)
def test_raise_error_answer_is_not_numeric(menu1):
    with pytest.raises(Menu_error):
        answer = 'test'
        menu1.option_check(answer)
