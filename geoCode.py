#! /usr/bin/python
import urllib2
import json
import argparse
from tqdm import tqdm
import csv
import re
from time import sleep

def main(args):
	f= open(args.input,'r')
	rows = csv.reader(f, delimiter=',', quotechar='"')
	report = {"success":0,"Fail":0}
	o = open(args.output, 'w')
	for row in tqdm(rows):

		for i in range(len(row)):
			row[i] = re.sub("\n","",row[i])
		key = args.key
		baseurl = 'https://maps.googleapis.com/maps/api/geocode/json?address='

		baseAddress = "+".join([row[0],row[1]])
		address = "Barclays+" + baseAddress
#		address = baseAddress
		address = address.replace(" ","+")
		address = address.replace("\W","+")
		address = address.replace("++","+")
		url = baseurl + address + "&key=" + key
		print url
		try:
			response = urllib2.urlopen(url).read()
		except:
			print "\nERROR:Can't connect to the internet"
			quit()
		res = json.loads(response)
		if (len(res['results'])!=0):
			try:
				town_idx = map(lambda x: x["types"][0], res['results'][0]['address_components']).index('postal_town')
				town = res['results'][0]['address_components'][town_idx]["short_name"]
			except:
				town="NA"
			lat = res['results'][0]['geometry']['location']['lat']
			lng = res['results'][0]['geometry']['location']['lng']
			string = "%s\t%s\t%s\t%s\n" % (baseAddress,lat,lng,town)
			row.append(str(lat))
			row.append(str(lng))
			row.append(town)
			report["success"] += 1
		else:
			address = baseAddress
			address = address.replace(" ","+")
			address = address.replace("\W","+")
			address = address.replace("++","+")
			url = baseurl + address + "&key=" + key
			print url
			try:
				response = urllib2.urlopen(url).read()
			except:
				print "\nERROR:Can't connect to the internet"
				quit()
			res = json.loads(response)
			if (len(res['results'])!=0):
				try:
					town_idx = map(lambda x: x["types"][0], res['results'][0]['address_components']).index('postal_town')
					town = res['results'][0]['address_components'][town_idx]["short_name"]
				except:
					town="NA"
				lat = res['results'][0]['geometry']['location']['lat']
				lng = res['results'][0]['geometry']['location']['lng']
				string = "%s\t%s\t%s\t%s\n" % (baseAddress,lat,lng,town)
				row.append(str(lat))
				row.append(str(lng))
				row.append(town)
				report["success"] += 1
			else:
				string = "%s\tNA\tNA\tNA\n" % baseAddress
				report["Fail"] += 1
		o.write(string)

	succRate = float(report["success"])/(float(report["success"])+float(report["Fail"])) * 100
	print "-"*80
	print "Finished!"
	print "Success rate: %s%%" % succRate
	print "-"*80


parser = argparse.ArgumentParser(description='Geocode adresses to Lat Lng',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
subparsers = parser.add_subparsers(help="Task to perform")

parser_pca = subparsers.add_parser('geocode', help='Geocode adresses to Lat Lng', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser_pca.add_argument('input',help='File with one address per line')
parser_pca.add_argument('key',help='googleapis key')
parser_pca.add_argument('output',help='Output file name')
parser_pca.set_defaults(func=main)

args = parser.parse_args()
args.func(args)
