import pandas as pd
import requests

def load_neighbourhood_data(filepath):
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError as e:
        print("FILE NOT FOUND: ", e)

def get_neighbourhood_data():
    return

# def get_neighbourhood_metadata():
#     # TODO: move this into a config?
# 	url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show"
#     params = { "id": "4def3f65-2a65-4a4f-83c4-b2a4aed72d46"}
#     package = requests.get(url, params = params).json()
#
#     for idx, resource in enumerate(package["result"]["resources"]):
#         if resource["datastore_active"]:
#             url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/datastore_search"
#             p = { "id": resource["id"] }
#             data = requests.get(url, params = p).json()
#             df = pd.DataFrame(data["result"]["records"])
#             break
