import requests


class SuperHero():
    """
    Класс супергероев!
    """

    # получаем список словарей супергероев по апи
    def __get_all_superhero(self):
        url = 'https://akabab.github.io/superhero-api/api'
        path = '/all.json'

        full_path = f'{url}{path}'
        
        response = requests.get(url=full_path)

        return response.json()
    
    # получаем ID супергероя по его имени
    def __get_id_superhero(self):
        all_superhero_list = self.__get_all_superhero()

        for superhero_dict in all_superhero_list:
            if superhero_dict['name'] == self.name:
                return superhero_dict['id']
        return None
    
    # получаем словарь с характеристиками супергероя по ID 
    def __get_powerstats_superhero(self):
        url = 'https://akabab.github.io/superhero-api/api'
        path = f'/powerstats/{self.id}.json'

        full_path = f'{url}{path}'

        response = requests.get(url=full_path)

        return response.json()
        
    def __init__(self, name) -> None:
        self.name = name
        self.id = self.__get_id_superhero()
        self.powerstats = self.__get_powerstats_superhero()
        self.intelligence = self.powerstats['intelligence']

    def __str__(self):
        return f'Имя: {self.name}\nID: {self.id}'

Hulk = SuperHero('Hulk')
Captain_America = SuperHero('Captain America')
Thanos = SuperHero('Thanos')

the_cleverest = max(Hulk, Captain_America, Thanos, key=lambda x: x.intelligence)  # определяем самого умного супергероя по характеристике "intelligence"

print(f'{the_cleverest.name} - cамый умный среди супергероев {Hulk.name}, {Captain_America.name}, {Thanos.name}')
