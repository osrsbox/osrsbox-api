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
from pymongo import MongoClient

# Set MongoDB connection configuration
ip_address = "0.0.0.0"
port = 27017
username = "someusername"
password = "somepassword"
db_name = "osrsbox-db"

# Initialize MongoDB connection
print(">>> Connecting to MongoDB....")
client = MongoClient(f"mongodb://{username}:{password}@{ip_address}:{port}/")

# Load database
db = client[db_name]

collection_names = [
    "items",
    "monsters",
    "prayers"
]

# Index each collection
for collection_name in collection_names:
    print("  > Indexing:", collection_name)
    coll = db[collection_name]
    coll.create_index("id")
