import requests


def search_address(zipcode):
    response = requests.get(f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}')

    results = response.json()['results']

    prefecture_name = results[0]['address1']
    city_name = results[0]['address2']
    town_name = results[0]['address3']

    address = f'{prefecture_name}{city_name}{town_name}'
    return address