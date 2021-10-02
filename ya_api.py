import requests


with open('token.txt', 'r', encoding='utf-8') as file:
    token = file.read()
url_path = 'https://cloud-api.yandex.net:443/v1/disk/resources'


def ya_api_create(path):
    params = {'path': path}
    headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth ' + token}
    create_dir = requests.api.put(url_path, headers=headers, params=params)
    print(create_dir.status_code)
    return create_dir.status_code


def ya_api_read(path):
    params = {'path': path}
    headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth ' + token}
    get_dir = requests.api.get(url_path, headers=headers, params=params)
    print(get_dir.status_code)
    return get_dir.status_code


def ya_api_delete(path):
    params = {'path': path}
    headers = {'Content-Type': 'application/json','Authorization': 'OAuth ' + token}
    delete_dir = requests.api.delete(url_path, headers=headers, params=params)
    print(delete_dir.status_code)
    return delete_dir.status_code


if __name__ == '__main__':
    ya_api_create('test')
    ya_api_delete('test')
