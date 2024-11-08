import requests
import pandas as pd
import csv
import time

# APIVOID API key (sign up and get your API key)
api_key = 'e685adda693a0289b0e8111ea49b3b335a4f7ca6'
api_url = 'https://endpoint.apivoid.com/iprep/v1/pay-as-you-go/?key=' + api_key

# Load the CSV with IP addresses
input_csv = 'ips_report.csv'
output_csv = 'ips_with_reputation.csv'

# Read the CSV file
df = pd.read_csv(input_csv)

# Prepare a list to hold the results
reputation_data = []

# Iterate through the rows and get the reputation for each IP
for index, row in df.iterrows():
    ip_address = row['IP']  # Adjust based on your column name in CSV

    # Make a request to the APIVOID API
    try:
        response = requests.get(f"{api_url}&ip={ip_address}")
        response.raise_for_status()  # This will raise an HTTPError for bad status codes
        data = response.json()

        # Check if the response contains the expected data
        reputation_info = {
            'IP': ip_address,
            'Reputation': data.get('data', {}).get('reputation', 'N/A'),
            'Risk': data.get('data', {}).get('risk', 'N/A'),
            'Country': data.get('data', {}).get('country', 'N/A'),
            'Abuse Confidence': data.get('data', {}).get('abuse_confidence', 'N/A')
        }
        reputation_data.append(reputation_info)

        # Delay to respect the 2 requests per second limit
        time.sleep(0.5)  # Half a second delay to stay within the limit

    except requests.exceptions.RequestException as e:
        print(f"Error with IP {ip_address}: {e}")
        continue

# Create a DataFrame from the reputation data
reputation_df = pd.DataFrame(reputation_data)

# Save the data to a new CSV file
reputation_df.to_csv(output_csv, index=False)

print(f"Reputation analysis complete. Results saved to {output_csv}")
