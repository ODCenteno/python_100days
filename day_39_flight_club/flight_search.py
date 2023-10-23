from pprint import pprint
from flight_data import FlightParams, FlightData
from settings import FLIGHT_BASE_URL, FLIGHT_SEARCH_HEADER
import requests
from datetime import datetime

class FlightSearch:
    '''
    class is responsible for talking to the Flight Search API.
        Methods:
            - search_flight(fly_from, date_from, date_to)
    '''

    def __init__(self) -> None:
        self.flight_params = FlightParams().get_flight_params()

    def search_flight(self, fly_from, fly_to):
        '''
        Params:
            - fly_from: IATA Code, example: LAX
                Accepts country, city or airport code
                - 'fly_from=city:DUS' will match all airports in "DUS", "MGL" and "NRN" (all in the city of Duesseldorf)
                - 'fly_from=airport:DUS' will only match airport "DUS"
            - date_from: departure date (dd/mm/yyyy). Example : 03/04/2021
            - date_to: departure date (dd/mm/yyyy). Example : 03/04/2021
                Use parameters date_from and date_to to define the range for the outbound flight departure.

            DEFAULT:
            "curr": "MXN",
            "selected_cabins": "M" (economy)
        '''

        self.flight_params['fly_from'] = fly_from
        self.flight_params['fly_to'] = fly_to

        res = requests.get(
            url=f'{FLIGHT_BASE_URL}/search',
            headers=FLIGHT_SEARCH_HEADER,
            params=self.flight_params,
            timeout=15
            )

        try:
            data = res.json()["data"][0]
        except IndexError:
            print(f"No flights found for {fly_to}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        # print(f"{flight_data.flight_info['destination_city']}: £{flight_data.flight_info['price']}")
        return flight_data.flight_info

    def get_destination_code_by_city(self, city_name):
        location_endpoint = f"{FLIGHT_BASE_URL}/locations/query"
        headers = FLIGHT_SEARCH_HEADER
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query, timeout=10)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code


# searcher = FlightSearch()
# pprint(searcher.flight_params)
# result = searcher.search_flight(fly_from='MEX', fly_to='LIS')
# pprint(result)
