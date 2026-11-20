from django.shortcuts import render

def book_detail(request):
    book = {
        'title': 'Мастер и Маргарита',
        'author': 'Михаил Булгаков',
        'year': 1967,
        'pages': 480,
        'description': 'Роман о добре и зле.',
        'is_available': True,
    }
    return render(request, 'catalog/book_detail.html', {'book': book})

def home(request):
    books = [
        {'title': 'Мастер и Маргарита', 'author': 'Михаил Булгаков'},
        {'title': 'Преступление и наказание', 'author': 'Федор Достоевский'},
        {'title': 'Война и мир', 'author': 'Лев Толстой'},
    ]
    return render(request, 'catalog/home.html', {'books': books})
