# grocery-store-distance

Utilizes the Google Places API to determine the closest/most prominent stores
per Toronto neighbourhood.

API documentation  
https://developers.google.com/places/web-service/details  

Next Steps/To dos:
- instead of blanket distance from average lat/long, customize sliding distance calculations across areas in neighbourhood
- UI embeded to switch queries -- whether interested in closest, applying custom
prominence filter, just prominence, etc. (median, average distance?)
- Change distance calculation from haversine formula to (manhattan approx?) and
then finally call the google distance matrix api on them
- change options of search criteria (strictly nearest) (not prominence or radius), and then be
able to filter based on a list/categorization of chain/independent/large chain vs small chain, how
expensive the stores are -- more thoughts on this...

- find the densest populated areas (maybe do a distance from these points) to nearest store? -- this answers how far most people might have to travel to get to groceries (getting population density data)

Map visuals
- add closest store name etc
- add points for reference point and the nearest store on the maps



What questions might you want to look into?:
- what do grocery stores look like for a certain neighbourhood (more dense vs others?,areas with higher household income for e.g) # of grocery stores in an area, average $$$$$?, types - indep or mostly chain
-
