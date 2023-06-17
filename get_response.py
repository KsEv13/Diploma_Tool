import requests


def get_response(endpoint_url, return_json=True):
    TOKEN = ''
    API_URL = f'https://api.github.com'
    headers = {'Authorization': f'Token {TOKEN}'}

    if 'https' in endpoint_url:
        url = endpoint_url
    else:
        url = f'{API_URL}/{endpoint_url}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200 and return_json:
        response_json = response.json()
        return response_json
    elif response.status_code == 200:
        return response
    else:
        print(
            f"Не удалось получить информацию по ссылке: {endpoint_url}. Код ошибки: {response.status_code}")
        return None
