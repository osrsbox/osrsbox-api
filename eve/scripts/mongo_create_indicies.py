"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Connect to MongoDB container, index the osrsbox-db database collections.

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
import os

from pymongo import MongoClient

# Set MongoDB connection configuration
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_DBNAME = "osrsbox-db"
PROJECT_USERNAME = os.getenv("PROJECT_USERNAME")
PROJECT_PASSWORD = os.getenv("PROJECT_PASSWORD")


def main():
    # Initialize MongoDB connection
    print(">>> Connecting to MongoDB....")
    client = MongoClient(f"mongodb://{PROJECT_USERNAME}:{PROJECT_PASSWORD}@mongo:{MONGO_PORT}/{MONGO_DBNAME}")

    # Load database
    db = client[MONGO_DBNAME]

    collection_names = [
        "items",
        "monsters",
        "prayers",
        "icons_items",
        "icons_prayers"
    ]

    # Index each collection
    for collection_name in collection_names:
        print("  > Indexing:", collection_name)
        coll = db[collection_name]
        coll.create_index("id")


if __name__ == "__main__":
    main()
