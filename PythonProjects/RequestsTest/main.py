import requests

token = '705cb8f56db6e092c1d2a8c551d71614'
response = requests.post('https://pokemonbattle.me:9104/pokemons', 
headers = {'Content-Type': 'application/json', "trainer_token": token}, 
json = {"name": "Покемончик", "photo": "https://dolnikov.ru/pokemons/albums/001.png"})
print(response.text)

response = requests.put('https://pokemonbattle.me:9104/pokemons',
headers = {'Content-Type': 'application/json', "trainer_token": token},
json = {"pokemon_id": 6034, "name": "Marina", "photo": ""})
print(response.text)

response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball',
headers = {'Content-Type': 'application/json', "trainer_token": token},
json = {"pokemon_id": 6034})
print(response.text)