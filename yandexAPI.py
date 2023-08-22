import requests
import configparser


def make_folder(file_path: str, token: str) -> str:
    url_for_dir = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    params_for_dir = {'path': file_path}
    response_get_folder = requests.put(url=url_for_dir, headers=headers, params=params_for_dir)
    return response_get_folder.status_code

def delete_folder(file_path: str, token: str) -> int:
    url_for_dir = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    params_for_dir = {'path': file_path}
    response_del_folder = requests.delete(url=url_for_dir, headers=headers, params=params_for_dir)
    return response_del_folder.status_code

if __name__ == '__main__':
    disk_file_path = 'Test_folder'
    config = configparser.ConfigParser()
    config.read("autorization.ini")
    token_yd = config['YANDEX_TOKEN']['token']
    make_folder(disk_file_path, token_yd)

