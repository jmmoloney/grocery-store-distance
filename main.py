import googlemaps
from config import Config
from testing import load_neighbourhood_data

def main():
	return 7

if __name__ == '__main__':
	config = Config().config
	filepath = config["NEIGHBOURHOOD DATA"]["FILEPATH"]
	key = config["MAIN"]["API_KEY"]

	df = load_neighbourhood_data(filepath)

	area = 'Waterfront Communities-The Island (77)'
	lat_long = df.query("AREA_NAME == '{}'".format(area))
	lat, long = lat_long.LATITUDE.values, lat_long.LONGITUDE.values
	location= (lat, long)

	# inputtype="textquery"
	keyword = "Grocery Store"

	radius = 2000 # in metres
	rank_by='prominence' #distance # cannot have radius when rankby is prominence

	gmaps = googlemaps.Client(key=key)
	result = gmaps.places_nearby(location=location, radius=radius, keyword=keyword,
								 rank_by=rank_by)
	print(result)

	# location=None,
    # radius=None,
    # keyword=None,
    # language=None,
    # min_price=None,
    # max_price=None,
    # name=None,
    # open_now=False,
    # rank_by=None,
    # type=None,
    # page_token=None,
