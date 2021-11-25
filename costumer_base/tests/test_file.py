import pytest

@pytest.fixture
def file_txt():
    return 'clients.txt'

@pytest.fixture
def file_json():
    return 'clients.json'

def test_write_txt_file(file_txt):
    file = open(file_txt, 'wt')
    assert file.writable() == True


