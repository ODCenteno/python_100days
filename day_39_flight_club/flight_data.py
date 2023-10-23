import datetime
from pprint import pprint

class FlightParams:
    '''
    Responsible for structuring the flight data.
    '''
    flight_params = {
            "fly_from": 'LAP',
            "fly_to": 'MEX',
            "date_from": '',
            "date_to": '',
            "curr": "MXN",
            "selected_cabins": "M",
            "flight_type": "round",
            "max_stopovers": 3,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
        }

    def __init__(self) -> None:
        self.flight_params["date_from"] = self.get_formatted_date(1)
        self.flight_params["date_to"] = self.get_formatted_date(180)

    def get_formatted_date(self, days):
        raw_date = datetime.datetime.now() + datetime.timedelta(days=float(days))
        formatted_date = raw_date.strftime("%d/%m/%Y")
        return formatted_date

    def get_flight_params(self):
        return self.flight_params

    def set_new_flight_param(self, param):
        self.flight_params[param] = param
        return self.flight_params[param]

# data = FlightParams('LAX', 'SFO')
# result = data.get_flight_params()
# pprint(result)

class FlightData:
    flight_info = {}

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.flight_info["price"] = price
        self.flight_info["origin_city"] = origin_city
        self.flight_info["origin_airport"] = origin_airport
        self.flight_info["destination_city"] = destination_city
        self.flight_info["destination_airport"] = destination_airport
        self.flight_info["out_date"] = out_date
        self.flight_info["return_date"] = return_date


