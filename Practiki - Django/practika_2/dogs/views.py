


import requests
from django.shortcuts import render


def get_breeds():
    """Получает список всех пород собак из Dog CEO API."""
    url = 'https://dog.ceo/api/breeds/list/all'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    breeds = []

    for breed in data['message']:
        breeds.append(breed)

    return breeds


def get_dog_images(breed):
    """Получает список фотографий собак указанной породы."""
    url = f'https://dog.ceo/api/breed/{breed}/images'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if data['status'] == 'success':
        return data['message']

    return []


def index(request):
    """Обрабатывает запросы пользователя и отображает страницу с породами и фотографиями."""
    breeds = get_breeds()
    images = []
    errors = []

    if request.method == 'POST':
        entered_breeds = request.POST.get('breeds', '')
        selected_breeds = entered_breeds.lower().split(',')

        for breed in selected_breeds:
            breed = breed.strip()

            if breed:
                if breed in breeds:
                    dog_images = get_dog_images(breed)
                    images.extend(dog_images)
                else:
                    errors.append(breed)

    return render(request, 'dogs/index.html', {
        'breeds': breeds,
        'images': images,
        'errors': errors
    })
