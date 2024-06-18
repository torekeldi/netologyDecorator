import requests
import time
from task_2 import logger


@logger('my_log.log')
def find_uk_city(coordinates: list) -> str:
    uk_cities = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
    api_key = '65c6e0e0d7799358363770ekx24b5ed'
    url = 'https://geocode.maps.co/reverse'
    for lat, long in coordinates:
        key_str = f'?lat={lat}&lon={long}&api_key={api_key}'
        time.sleep(2)
        geo_data = requests.get(url+key_str).json()
        city_name = geo_data.get('address', {}).get('city')
        if city_name in uk_cities:
            return city_name
        else:
            continue


location1 = [('55.7514952', '37.618153095505875'), ('52.3727598', '4.8936041'), ('53.4071991', '-2.99168')]

find_uk_city(location1)
