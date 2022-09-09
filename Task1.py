import requests
from datetime import datetime

with open('Token.txt') as file:
    TOKEN = file.read()

list = [
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain%America',
]

def requests_get(url_list):
    r = (requests.get(url) for url in url_list)
    return r

def search_intelligence():
    super_man = []
    for item in requests_get(list):
        intelligence = item.json()
        try:
            for power_stats in intelligence['results']:
                super_man.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })
        except KeyError:
            print(f"Неверная ссылка: {list}")

    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in super_man:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый умный герой {name}, его интелект: {intelligence_super_hero}")


if __name__ == "__main__":
    search_intelligence()