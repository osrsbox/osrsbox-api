"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Using the PyPi osrsbox package, insert data into osrsbox-api-mongo.

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
import itertools

import pymongo
from osrsbox import items_api
from osrsbox import monsters_api
from osrsbox import prayers_api

from connection_properties import ConnectionProperties
cp = ConnectionProperties()

client = pymongo.MongoClient(f"mongodb://{cp.username}:{cp.password}@localhost:{cp.port}/{cp.db_name}")
db = client[cp.db_name]


def insert_api_data(db_type: str):
    print(f">>> Inserting {db_type} data...")

    # Insert database contents using osrsbox-api
    if db_type == "items" or db_type == "icons_items":
        all_db_entries = items_api.load()
    elif db_type == "monsters":
        all_db_entries = monsters_api.load()
    elif db_type == "prayers" or db_type == "icons_prayers":
        all_db_entries = prayers_api.load()

    all_entries = list()
    bulk_entries = list()

    for entry in all_db_entries:
        # Check if we are processing icons, and strip to id, name
        if "icons" in db_type:
            new_entry = dict()
            new_entry["id"] = entry.id
            new_entry["icon"] = entry.icon
            entry = new_entry.copy()
        # Append to a list of all entries
        all_entries.append(entry)

    for db_entries in itertools.zip_longest(*[iter(all_entries)] * 50):
        # Remove None entries from the list
        db_entries = filter(None, db_entries)
        # Cast from filter object to list
        db_entries = list(db_entries)
        # Append to list of bulk entries
        bulk_entries.append(db_entries)

    for i, block in enumerate(bulk_entries):
        print(f"  > Processed: {i*50}")
        to_insert = list()
        for entry in block:
            # Make a dictionary from the *Properties object
            if not isinstance(entry, dict):
                entry = entry.construct_json()
                # Convert item ID to string for lookup
                entry["id"] = str(entry["id"])
            # Append to the to_insert list
            to_insert.append(entry)

        # Insert into MongoDB
        collection = db[db_type]
        collection.insert_many(to_insert)


if __name__ == "__main__":
    # Loop three database types
    dbs = ["items", "monsters", "prayers", "icons_items", "icons_prayers"]
    for db_type in dbs:
        insert_api_data(db_type)
        collection = db[db_type]
        print(">>> Indexing...")
        collection.create_index("_id")
