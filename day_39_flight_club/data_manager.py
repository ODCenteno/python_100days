'''
Data Manager allows to get the destinies information
   - get_flight_destinies() -> return a list of cities and maximum price
   - update_single_sheet_data(destiny_id, lowest_price) -> Update a value by ID
'''

from pprint import pprint
from settings import SHEETY_BASE_URL, HEADER
import requests

class DataManager:
    body = {}

    def __init__(self) -> None:
        self.sheet_data = self.get_flight_destinies()

    def get_flight_destinies(self):
        '''get_flight_destinies() -> return a list of dictionaries with the
        information of cities, IATA airport code, ID and, máximum price allowed per flight.
        Example:
            [
                {'city': 'Barcelona', 'iataCode': 'BCN', 'id': 2, 'lowestPrice': 54},
                ...
            }
        '''
        try:
            res = requests.get(url=SHEETY_BASE_URL, headers=HEADER, timeout=5)
            res_json = res.json()
            return res_json['prices']
        except Exception:
            print(f'Unable to get a response from: {SHEETY_BASE_URL}')

    def build_lowest_price_body(self, lowest_price):
        self.body = {
            "price": {
                "lowestPrice": lowest_price
                }
            }
        return self.body

    def update_single_lowestPrice_data(self, destiny_id: int, lowest_price=220):
        index_row = 0

        for row in self.sheet_data:
            if row['id'] == destiny_id:
                index_row = row['id'] - 1
                self.build_lowest_price_body(lowest_price)
                break

        try:
            res = requests.put(url=f'{SHEETY_BASE_URL}/{destiny_id}', headers=HEADER, json=self.body, timeout=5)
            city_updated = res.json()
            return city_updated
        except:
            print(f'Not posible to update the lowest price in index: {index_row},\
                city: {self.sheet_data[index_row]}')

    def find_id_by_city_name(self, city_name):
        for row in self.sheet_data:
            if row['city'].lower() == city_name.lower():
                return row['id']
        return 'City not finded'
