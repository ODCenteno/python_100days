import requests
from datetime import datetime
from api_keys import USERNAME, TOKEN

pixela_endpoint = "https://pixe.la/v1/users"
my_pixela_endpoint = "https://pixe.la/v1/users/odcenteno/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response)

graph_config = {
    "id": "graph2",
    "name": "practiceps",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=my_pixela_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph2_endpoint = "https://pixe.la/v1/users/odcenteno/graphs/graph2"

# Getting and formatting today's date
today = datetime.now().strftime("%Y%m%d")

post_pixel_params = {
    "date": today,
    "quantity": "5",
}

# Posting a new pixel https://docs.pixe.la/entry/post-pixel
# response = requests.put(url=graph2_endpoint, json=post_pixel_params, headers=headers)
# print(response.text)


update_config = {
    "quantity": "10",
}

# # Update a pixel
# response = requests.put(url=f"{graph2_endpoint}/{today}", json=update_config, headers=headers)
# print(response.text)


increment_params = {
    "X-USER-TOKEN": TOKEN,
    "Content-Length": "5",
}

# # Increment a pixel https://docs.pixe.la/entry/increment-pixel
# response = requests.put(url=f"{graph2_endpoint}/increment", json=post_pixel_params)
# print(response.text)