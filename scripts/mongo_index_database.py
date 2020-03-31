"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Connect to MongoDB, index the osrsbox-db database collections.

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
import pymongo

from connection_properties import ConnectionProperties
cp = ConnectionProperties()

# Initialize MongoDB connection
client = pymongo.MongoClient(f"mongodb://{cp.username}:{cp.password}@localhost:{cp.port}/{cp.db_name}")
db = client[cp.db_name]


def main():
    # Set names of collections to index
    collection_names = [
        "items",
        "monsters",
        "prayers",
        "icons_items",
        "icons_prayers"
    ]

    # Index each collection by ID property
    for collection_name in collection_names:
        print("  > Indexing:", collection_name)
        collection = db[collection_name]
        collection.create_index("id")


if __name__ == "__main__":
    main()
