import requests
from pprint import pprint


def client():
    token = "Token 22bac4e4e7a62453814e4bd0f6b68910e87408d7"

    headers = {"Authorization": token}

    res = requests.get(
        url="http://127.0.0.1:8000/api/user-profiles/",
        headers=headers
    )

    print("Status Code: ", res.status_code)

    res_data = res.json()

    pprint(res_data)


if __name__ == "__main__":
    client()
