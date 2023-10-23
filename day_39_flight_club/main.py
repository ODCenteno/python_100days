from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

def run():
    data_manager = DataManager()
    sheet_destinies = data_manager.get_flight_destinies()
    flight_search = FlightSearch()
    pprint(sheet_destinies)

    ORIGIN_CITY_IATA = 'SJD'

    for destination in sheet_destinies:
        flight = flight_search.search_flight(ORIGIN_CITY_IATA, destination["iataCode"])
        pprint(flight)





if __name__ == '__main__':
    run()
