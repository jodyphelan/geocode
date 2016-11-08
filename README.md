# geocode

Use google maps api to Geocode addresses to GPS

**Input:** CSV file with "," as delimeter and double quotes to encapsulate text fields<br>
**Output:** Three column CSV file with Town, Lat, Lng

usage: geoCode.py geocode [-h] input key output

positional arguments:
  input       File with one address per line
  key         googleapis key
  output      Output file name

optional arguments:
  -h, --help  show this help message and exit
