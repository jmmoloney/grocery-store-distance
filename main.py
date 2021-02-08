import json
import requests
import urllib
from config import Config

def main():
	return 4


if __name__ == '__main__':
	config = Config().config
	filepath = config["NEIGHBOURHOOD DATA"]["FILEPATH"]
	from testing import load_neighbourhood_data
	# load acceptable grocery stores
	# grocery_store_names.txt
	# parse geojson instead?

	df = load_neighbourhood_data(filepath)
	# print(df["AREA_NAME"].unique().tolist())
	# cycle through for each latitude and longitude
	# lat = df.query("AREA_NAME == 'Kensington-Chinatown (78)'").LATITUDE.values
	# long = df.query("AREA_NAME == 'Kensington-Chinatown (78)'").LONGITUDE.values
	area = 'Waterfront Communities-The Island (77)'
	lat = df.query("AREA_NAME == '{}'".format(area)).LATITUDE.values
	long = df.query("AREA_NAME == '{}'".format(area)).LONGITUDE.values


	output = "json"
	key = config["MAIN"]["API_KEY"]
	inputtype="textquery"
	keyword = "Grocery Store".replace(' ', '%20')

	radius = 2000 # in metres
	location=f"{lat[0]},{long[0]}"
	rankby='distance'
	# query = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/{output}?key={key}&inputtype={inputtype}&input={text}&locationbias={locationbias}"
	query = f"https://maps.googleapis.com/maps/api/place/nearbysearch/{output}?key={key}&location={location}&keyword={keyword}&rankby={rankby}"
	# resp = requests.get(query)
	# if resp.status_code == requests.codes.ok:
		# with open("waterfront_response.json", "w") as f:
			# f.write(resp.text)
	# rankby distance, could also do prominence
	with open("waterfront_response.json", 'r') as f:
		file = json.load(f)
	results=file["results"]
	sample = results[0]
	# print(sample)
	# print(sample.keys())
	location_name = sample['name']
	# distance_from_nb = sample[]
	location_lat = sample["geometry"]["location"]["lat"]
	location_long = sample["geometry"]["location"]["lng"]
	address = sample["vicinity"]
	# TODO: use the requests library to format the request
