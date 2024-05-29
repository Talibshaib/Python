import requests

URL = 'https://api.freeapi.app/api/v1/public/randomusers/user/random/'

def get_random_users():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None

def main():
    user = get_random_users()
    user_data = user['data']
    print(f"Name: {user_data['name']['first']} {user_data['name']['last']}")
    print(f"Email: {user_data['email']}")
    print(f"Phone: {user_data['phone']}")
    print(f"Country: {user_data['location']['country']}")
if __name__ == '__main__':
    main()