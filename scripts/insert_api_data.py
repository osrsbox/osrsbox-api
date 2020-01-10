"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Using the PyPi osrsbox package, insert data into the osrsbox-api.

Copyright (c) 2020, PH01L

###############################################################################
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
"""
import json
from typing import Dict
from typing import Tuple

import requests
from osrsbox import items_api
from osrsbox import monsters_api
from osrsbox import prayers_api

# Specify the items API endpoint
API_ENDPOINT = "http://0.0.0.0/api"

# Specify the JSON content type for HTTP POSTS
HEADERS = {'Content-type': 'application/json'}


def perform_api_post(api_endpoint: str, data: Dict) -> Tuple:
    # Perform post request
    r = requests.post(url=api_endpoint,
                      data=data,
                      headers=HEADERS)

    # Determine HTTP response status
    status = r.status_code
    # Extract API response as a dict
    response = json.loads(r.text)

    return status, response


def perform_api_put(api_endpoint: str, data: Dict) -> Tuple:
    # Perform put request
    r = requests.post(url=api_endpoint,
                      data=data,
                      headers=HEADERS)

    # Determine HTTP response status
    status = r.status_code
    # Extract API response as a dict
    response = json.loads(r.text)

    return status, response


def insert_api_data(db_type: str):
    # Insert database contents using osrsbox-api
    if db_type == "items":
        all_db_entries = items_api.load()
    elif db_type == "monsters":
        all_db_entries = monsters_api.load()
    elif db_type == "prayers":
        all_db_entries = prayers_api.load()

    count = 0
    print(f">>> Inserting {db_type} data...")
    for entry in all_db_entries:
        # Make a dictionary from the ItemProperties object
        entry_dict = entry.construct_json()

        # Dump dictionary to JSON for API parameter
        entry_json = json.dumps(entry_dict)

        # Send POST request
        status, response = perform_api_post(API_ENDPOINT + f"/{db_type}",
                                            entry_json)

        if response["_status"] == "ERR":
            status, response = perform_api_put(API_ENDPOINT + f"/{db_type}",
                                               entry_json)

        if response["_status"] == "ERR":
            print(response)
            print(">>> Data insertion error... Exiting.")
            quit()

        count += 1
        print(f"  > Processed: {count:05} of {len(all_db_entries)}", end="\r", flush=True)


if __name__ == "__main__":
    # Loop three database types
    dbs = ["items", "monsters", "prayers"]
    for db_type in dbs:
        # if db_type == "items":
        #     continue
        # if db_type == "monsters":
        #     continue
        # if db_type == "prayers":
        #     continue
        insert_api_data(db_type)
