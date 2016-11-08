# geocode

Use google maps api to Geocode addresses to GPS

**Input:** CSV file with "," as delimeter and double quotes to encapsulate text fields<br>
**Output:** Three column CSV file with Town, Lat, Lng

##Usage
usage: geoCode.py geocode [-h] input key output

positional arguments:
  input       File with one address per line
  key         googleapis key
  output      Output file name

optional arguments:
  -h, --help  show this help message and exit


##Note

This implements the tqdm module - if for some reason you cant install just remove it from the two lines where it appears
