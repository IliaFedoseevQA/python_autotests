import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '637f30ab0a0e598d2930520ce57d9fe4'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "amberuniverse1@gmail.com",
    "password": "Autotest123"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Титан",
    "photo_id": 6
}

body_catch = {
    "pokemon_id": "121752"
}

body_changename = {
    "pokemon_id": "121751",
    "name": "Луна",
    "photo_id": 6
}

response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print (response_confirmation.text)

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)

message= response_create.json()['message']
print (message)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print (response_catch.text)

response_changename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_changename)
print (response_changename.text)