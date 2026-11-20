import requests
from django.shortcuts import render, redirect
from .models import Pokemon


def get_pokemon(name):
    """Получает информацию о покемоне из PokéAPI."""
    url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None


def index(request):
    """Главная страница менеджера команды покемонов."""
    message = ''
    search_result = None
    search_error = ''

    if request.method == 'POST':
        name = request.POST.get('name', '').strip().lower()

        if name:
            if Pokemon.objects.filter(name=name).exists():
                message = 'Этот покемон уже есть в команде!'
            else:
                data = get_pokemon(name)

                if data:
                    pokemon = Pokemon(
                        name=data['name'],
                        pokemon_id=data['id'],
                        image=data['sprites']['front_default'] or '',
                        pokemon_type=data['types'][0]['type']['name'],
                        height=data['height'],
                        weight=data['weight'],
                        base_experience=data['base_experience'] or 0,
                        abilities=[
                            ability['ability']['name']
                            for ability in data['abilities']
                        ],
                        stats={
                            stat['stat']['name']: stat['base_stat']
                            for stat in data['stats']
                        }
                    )

                    pokemon.save()
                    message = f'{name.capitalize()} добавлен в команду!'
                else:
                    message = 'Покемон не найден!'

    if request.method == 'GET':
        search_name = request.GET.get('search', '').strip().lower()

        if search_name:
            search_result = get_pokemon(search_name)

            if not search_result:
                search_error = 'Покемон не найден!'

    team = Pokemon.objects.all()

    return render(request, 'pokemon/index.html', {
        'team': team,
        'message': message,
        'search_result': search_result,
        'search_error': search_error
    })


def delete_pokemon(request, pokemon_id):
    """Удаляет покемона из команды."""
    if request.method == 'POST':
        Pokemon.objects.filter(id=pokemon_id).delete()

    return redirect('index')


def battle(request):
    """Проводит тренировочный бой между двумя покемонами."""
    team = Pokemon.objects.all()
    result = None

    if request.method == 'POST':
        first_id = request.POST.get('first_pokemon')
        second_id = request.POST.get('second_pokemon')

        if first_id and second_id and first_id != second_id:
            first = Pokemon.objects.filter(id=first_id).first()
            second = Pokemon.objects.filter(id=second_id).first()

            if first and second:
                first_power = sum(first.stats.values())
                second_power = sum(second.stats.values())

                if first_power > second_power:
                    winner = first.name
                elif second_power > first_power:
                    winner = second.name
                else:
                    winner = 'Ничья'

                result = {
                    'first': first,
                    'second': second,
                    'first_power': first_power,
                    'second_power': second_power,
                    'winner': winner
                }

    return render(request, 'pokemon/battle.html', {
        'team': team,
        'result': result
    })
