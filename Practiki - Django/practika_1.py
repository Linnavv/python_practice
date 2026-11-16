"""
Программа для получения информации о покемонах через PokéAPI.
Выводит список первых 20 покемонов и характеристики выбранного:
имя, тип, вес, рост и способности.
"""

import requests

url = 'https://pokeapi.co/api/v2/pokemon?limit=20'
response = requests.get(url)
data = response.json()

for pokemon in data['results']:
    print(pokemon['name'])

name = input('Имя покемона: ')

pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{name}'
pokemon_response = requests.get(pokemon_url)

if pokemon_response.status_code == 200:
    pokemon_data = pokemon_response.json()

    print('\nИнформация о покемоне:')
    print('Имя:', pokemon_data['name'])

    print('Типы:')
    for pokemon_type in pokemon_data['types']:
        print('-', pokemon_type['type']['name'])

    print('Вес:', pokemon_data['weight'])
    print('Рост:', pokemon_data['height'])

    print('Способности:')
    for ability in pokemon_data['abilities']:
        print('-', ability['ability']['name'])
else:
    print('Покемон не найден!')

