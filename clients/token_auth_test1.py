import requests
from pprint import pprint

# {'key': '22bac4e4e7a62453814e4bd0f6b68910e87408d7'}


def client():
    credentials = {
        "username": "admin",
        "password": "123"
    }

    res = requests.post(
        url="http://127.0.0.1:8000/dj-rest-auth/login/",
        data=credentials
    )

    print("Status Code: ", res.status_code)

    res_data = res.json()

    pprint(res_data)


if __name__ == "__main__":
    client()
