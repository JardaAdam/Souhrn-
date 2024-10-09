import requests

# Napis skript, ktory vrati zoznam vsetkych mien rezidentov planety Tatooine,
# ktora je na 'https://swapi.dev/api/planets/1/'
class NotFoundExeption(Exception):
    pass


def get_residents(planet_url):
    response = requests.get(planet_url)
    if response.status_code == 404:
            raise NotFoundExeption("Planet not found")

    data = response.json()
    result_resident_names = []
    for resident_url in data['residents']:
        resident_response = requests.get(resident_url)
        data = resident_response.json()
        result_resident_names.append(data['name'])

    return result_resident_names


url = 'https://swapi.dev/api/planets/1/'
print(get_residents(url))

# TODO pridat timerit kolik casu to zabere