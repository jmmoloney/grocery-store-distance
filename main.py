from config import Config
import googlemaps
import json
from math import pi, sin, cos, asin, sqrt, radians
import pandas as pd
import string
from testing import load_neighbourhood_data

def get_closest_result(results_json):
	try:
		return results_json["results"][0]
	except IndexError:
		return {}

def calculate_distance(lat_lon1, lat_lon2):
	R = 6371  #Earth's Radius in KMs
	lat1, lon1 = lat_lon1
	lat2, lon2 = lat_lon2
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = (sin(radians(dlat)/2))**2 + cos(radians(lat1))*cos(radians(lat2))*\
		(sin(radians(dlon)/2))**2
	c = 2*asin(sqrt(a)) #inverse haversine
	distance = R*c
	return distance

if __name__ == '__main__':
	config = Config().config
	filepath = config["NEIGHBOURHOOD DATA"]["FILEPATH"]
	key = config["MAIN"]["API_KEY"]

	keyword = "Grocery Store"
	radius = 2000 # in metres
	rank_by='prominence' #distance # cannot have radius when rankby is prominence

	df = load_neighbourhood_data(filepath)
	distinct_areas = df["AREA_NAME"].unique()
	gmaps = googlemaps.Client(key=key)
	final_results = []
	areas_done = 0
	for area in distinct_areas:
		areas_done += 1
		print(area, areas_done)
		scrubbed_name = area.translate(str.maketrans('', '', string.punctuation))
		calculated_result = {}
		calculated_result["area_name"] = area
		lat_long = df.query('AREA_NAME == "{}"'.format(area))
		calculated_result["reference_point"] = lat_long.LATITUDE.values.item(), lat_long.LONGITUDE.values.item()

		result = gmaps.places_nearby(location=calculated_result["reference_point"], radius=radius, keyword=keyword,
									 rank_by=rank_by)
		with open(f"/Users/jessicamoloney/Documents/Projects/grocery-store-distance/data/{scrubbed_name}_response_{rank_by}.json", "w") as f:
			json.dump(result, f)
		# with open("waterfront_response.json", 'r') as f:
		# 	result = json.load(f)
		closest_store = get_closest_result(result)
		calculated_result["closest_store"] = closest_store.get("name", "")
		calculated_result["address"] = closest_store.get("vicinity", "")
		lat_long = closest_store.get("geometry", {}).get("location", "")
		calculated_result["location"] = lat_long.get("lat", ""), lat_long.get("lng", "")
		calculated_result["distance"] = \
			calculate_distance(calculated_result.get("reference_point", ""),
							   calculated_result.get("location", ""))
		final_results.append(calculated_result)
	final_frame = pd.DataFrame.from_records(final_results)
	print(final_frame)
	final_frame.to_csv('/Users/jessicamoloney/Documents/Projects/grocery-store-distance/data/results_frame.csv', index=False)
