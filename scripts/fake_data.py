import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_market.settings')

import django
django.setup()

from django.contrib.auth.models import User

from faker import Faker

import requests 
from pprint import pprint

def set_user():
    fake = Faker(['en_US'])

    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f_name.lower() + '_' + l_name.lower()
    email = f'{u_name}@{fake.domain_name()}'

    user_check = User.objects.filter(username=u_name)

    while user_check.exists():
        u_name = f_name + '_' + l_name + str(random.randrange(1, 999))
        user_check = User.objects.filter(username=u_name)

    user = User(
        username=u_name,
        first_name=f_name,
        last_name=l_name,
        email=email,
        is_staff=fake.boolean(chance_of_getting_true=50)
    )

    user.set_password('testing123')
    user.save()

    user_check = User.objects.filter(username=u_name)[0]

def search_book(key_word):
    fake = Faker(['en_US'])
    url = "http://openlibrary.org/search.json"
    payload = {"q": key_word}
    res = requests.get(url, params=payload)
    if res.status_code != 200:
        print("Wrong request made", res.status_code)
        return
    json_data = res.json()
    books = json_data.get("docs")

    for book in books:
        pprint(book)
        data = dict(
            name=book.get("title"),
            author=book.get("publisher_facet")[0] if book.get(
                "publisher_facet") else "Emre Yoleri",
            description='-'.join(book.get("author_facet")) if book.get("author_facet")
            else "OL115220A Edmund O'Donovan",
            date_of_relase=fake.date_time_between()
        )

        pprint(data)
