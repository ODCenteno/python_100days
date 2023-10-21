'''Python 100 days, Workout tracker project'''
import datetime as dt
from settings import BASE_URL
from settings import EXERCISE_ENDPOINT, EXERCISE_PAYLOAD, TRACKAPI_HEADERS
from settings import SHEETY_URL, SHEETY_HEADERS
import requests



sheety_payload = {
    "workout": {
    }
}

def post_request(endpoint, headers, payload):
    '''Make post request -> post_request(endpoint, headers, payload)'''
    return requests.post(endpoint, headers=headers, json=payload, timeout=5)


def run():
    '''Main fuction'''
    EXERCISE_PAYLOAD['query'] = input('¿Qué ejercicio realizaste hoy? ')
    track_api_response = post_request(f'{BASE_URL}{EXERCISE_ENDPOINT}', TRACKAPI_HEADERS, EXERCISE_PAYLOAD)
    res_json = track_api_response.json()
    print(res_json['exercises'])

    now = dt.datetime.now()

    for ex in res_json['exercises']:
        date = now.strftime('%x')
        time = now.strftime('%X')
        exercise_type = ex['user_input']
        exercise_duration = ex['duration_min']
        calories_burned = ex['nf_calories']

        sheety_payload['workout']['date'] = date
        sheety_payload['workout']['time'] = time
        sheety_payload['workout']['exercise'] = exercise_type.title()
        sheety_payload['workout']['duration'] = exercise_duration
        sheety_payload['workout']['calories'] = calories_burned

        print(sheety_payload)

        sheety_res = post_request(SHEETY_URL, headers=SHEETY_HEADERS, payload=sheety_payload)
        print(sheety_res.status_code)
        sheety_json = sheety_res.json()
        print(sheety_json)

if __name__ == '__main__':
    run()
