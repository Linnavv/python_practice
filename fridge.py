import datetime
from decimal import Decimal 

DATE_FORMAT = '%Y-%m-%d'
goods = {
    'Молоко': [
                {'amount': Decimal('1'), 'expiration_date':
                 datetime.date(2026, 10, 9)}
            ],
            'Яйца': [
                {'amount': Decimal('10'), 'expiration_date':
                 datetime.date(2026,10, 12)}
    
            ],
            'Вода': [
                {'amount': Decimal('1.5'), 'expiration_date':
                 None}
            ]

}

def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []
    if expiration_date != None:
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    items[title].append({
        'amount': amount, 
        'expiration_date': expiration_date
        })

def add_by_note(items, note):
    parts = note.split()
    if len(parts[-1].split('-')) == 3:
        expiration_date = parts[-1]
        amount = Decimal(parts[-2])
        title = ' '.join(parts[:-2])
        add(items, title, amount, expiration_date)
    else:
        expiration_date = None
        amount = Decimal(parts[-1])
        title = ' '.join(parts[:-1])
        add(items, title, amount, expiration_date)

def find(items, needle):
    result = []
    for title in items.keys():
        if needle.lower() in title.lower():
            result.append(title)
    return result

def amount(items,needle):
    found = find(items, needle)
    total = Decimal('0')
    for title in found:
        for item in items[title]:
            total += item['amount']
    return total


        