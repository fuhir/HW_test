import pytest
import configparser

from yandexAPI import make_folder, delete_folder

config = configparser.ConfigParser()
config.read("../autorization.ini")
token = config['YANDEX_TOKEN']['token']

fixture = [
    ('Test_folder', token, 201),
    (1, token, 201),
    ('Folder_1', token, 201),
]

fail_fixture = [
    ('Test_folder', token, 409),
    (1, token, 409),
    ('Test_folder', 1, 409),
]


@pytest.fixture
def teardown(file_path, token):
    yield
    delete_folder(file_path, token)


@pytest.mark.parametrize('file_path, token, result', fixture)
def test_make_folder(file_path, token, result, teardown):
    test_result = make_folder(file_path, token)
    assert test_result == result


@pytest.mark.parametrize('file_path, token, result', fail_fixture)
@pytest.mark.xfail
def test_make_folder_fails(file_path, token, result, teardown):
    test_result = make_folder(file_path, token)
    assert test_result == result
