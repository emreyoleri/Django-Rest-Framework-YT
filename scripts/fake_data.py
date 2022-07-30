import os
import random
from urllib import request
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_market.settings')

import django
django.setup()

from django.contrib.auth.models import User

from faker import Faker
import requests


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
    

from pprint import pprint
def search_book():
    url = "http://openlibrary.org/search.json"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        pprint(data)
