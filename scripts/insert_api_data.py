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

import requests
from osrsbox import items_api
from osrsbox import monsters_api
from pymongo import MongoClient

# Specify the items API endpoint
API_ENDPOINT = "http://127.0.0.1:5000/api/v1"

# Specify the JSON content type for HTTP POSTS
HEADERS = {'Content-type': 'application/json'}

# Insert item database using osrsbox-api
all_db_items = items_api.load()
for item in all_db_items:
    # Make a dictionary from the ItemProperties object
    item_dict = item.construct_json()

    if int(item_dict["id"]) < 9764:
        continue

    # Dump dictionary to JSON for API parameter
    item_json = json.dumps(item_dict)


    # Send POST request
    r = requests.post(url=API_ENDPOINT + "/items",
                      data=item_json,
                      headers=HEADERS)

    # Parse response to a dictionary
    r = json.loads(r.text)
    print(r)

    # If error, send PUT request
    if r["_status"] == "ERR":
        print("PUT")
        testapi = API_ENDPOINT + f"/items/{item_dict['id']}"
        print(testapi)
        r = requests.put(url=testapi,
                           data=item_json,
                           headers=HEADERS)

        # Parse response to a dictionary
        r = json.loads(r.text)

    if r["_status"] == "ERR":
        print(">>> Data insertion error... Exiting.")
        print(r)
        quit()
    else:
        print(item_dict["id"], r["_updated"], r["_status"])

# Insert monster database using osrsbox-api
all_db_monsters = monsters_api.load()
for monster in all_db_monsters:
    # Make a dictionary from the MonsterProperties object
    monster_dict = monster.construct_json()

    # Dump dictionary to JSON for API parameter
    monster_json = json.dumps(monster_dict)

    # Send POST request
    r = requests.post(url=API_ENDPOINT + "/monsters",
                      data=monster_json,
                      headers=HEADERS)

    # Parse response to a dictionary
    r = json.loads(r.text)

    # If error, send PUT request
    if r["_status"] == "ERR":
        r = requests.put(url=API_ENDPOINT + "/monsters",
                           data=item_json,
                           headers=HEADERS)

        # Parse response to a dictionary
        r = json.loads(r.text)

    if r["_status"] == "ERR":
        print(">>> Data insertion error... Exiting.")
    else:
        print(item_dict["id"], r["_updated"], r["_status"])

# Establish a MongoDB connection
username = "someusername"
password = "somepassword"
client = MongoClient(f"mongodb://{username}:{password}@localhost:27017/?authSource=osrsbox-db")

# create a new database instance
db = client["osrsbox-db"]

# Select items collection and index
print(">>> Creating items index...")
col = db.items
col.create_index("id")

# Select monsters collection and index
print(">>> Creating monsters index...")
col = db.monsters
col.create_index("id")
