#!/usr/bin/python3

# To run the script just use this:
# python3 /path/to/script.py 122.226.181.165

import requests
import json
import sys
import os

# Replace this with your actual APIVOID API key
apivoid_key = "e685adda693a0289b0e8111ea49b3b335a4f7ca6"

try:
   ip = sys.argv[1]
except IndexError:
   print("Usage: " + os.path.basename(__file__) + " <ip_address>")
   sys.exit(1)

def apivoid_iprep(key, ip):
   try:
      # Make the API request to the APIVOID IP Reputation API
      r = requests.get(url='https://endpoint.apivoid.com/iprep/v1/pay-as-you-go/?key='+key+'&ip='+ip)
      return json.loads(r.content.decode())
   except Exception as e:
      print(f"Error during API request: {e}")
      return None

data = apivoid_iprep(apivoid_key, ip)

def get_detection_engines(engines):
   engine_list = ""
   for key, value in engines.items():
      if bool(value['detected']):
         engine_list += str(value['engine']) + ", "
   return engine_list.rstrip(", ")

if data:
   if data.get('error'):
      print("Error: " + data['error'])
   else:
      # Print the IP reputation details
      print("IP: " + data['data']['report']['ip'])
      print("Hostname: " + data['data']['report']['information']['reverse_dns'])
      print("---")
      print("Detections Count: " + str(data['data']['report']['blacklists']['detections']))
      print("Detected By: " + get_detection_engines(data['data']['report']['blacklists']['engines']))
      print("---")
      print("Country: " + data['data']['report']['information']['country_code'] + " (" + data['data']['report']['information']['country_name'] + ")")
      print("Continent: " + data['data']['report']['information']['continent_code'] + " (" + data['data']['report']['information']['continent_name'] + ")")
      print("Region: " + data['data']['report']['information']['region_name'])
      print("City: " + data['data']['report']['information']['city_name'])
      print("Latitude: " + str(data['data']['report']['information']['latitude']))
      print("Longitude: " + str(data['data']['report']['information']['longitude']))
      print("ISP: " + data['data']['report']['information']['isp'])
      print("---")
      print("Is Proxy: " + str(data['data']['report']['anonymity']['is_proxy']))
      print("Is Web Proxy: " + str(data['data']['report']['anonymity']['is_webproxy']))
      print("Is VPN: " + str(data['data']['report']['anonymity']['is_vpn']))
      print("Is Hosting: " + str(data['data']['report']['anonymity']['is_hosting']))
      print("Is Tor: " + str(data['data']['report']['anonymity']['is_tor']))
else:
   print("Error: Request failed")
