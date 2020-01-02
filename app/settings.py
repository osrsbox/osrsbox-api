"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Python Eve API settings.

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
import json

# Set to True to enable debugging
DEBUG = True

# Set global MongoDB configuration
MONGO_HOST = os.getenv("MONGO_URI")
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_AUTH_SOURCE = "osrsbox-db"
MONGO_DBNAME = "osrsbox-db"

# Set api/ as API endpoint
URL_PREFIX = "api"

# Set ID in MongoDB
ID_FIELD = "id"

# Set API version
# API_VERSION = "v1"

# Set renderer to JSON for API output
RENDERERS = ["eve.render.JSONRenderer", ]

# Enable GET, POST, and DELETE for collections
RESOURCE_METHODS = ["GET", "POST", "DELETE"]

# Enable GET, PATCH, PUT and DELETE for items in collections
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]

# Enable standard client cache directive for all resources
CACHE_CONTROL = "max-age=20"
CACHE_EXPIRES = 20

# Load osrsbox-db schema-items.json file, and get the properties key
schema_file_path = "schema-items.json"
with open(schema_file_path) as f:
    item_schema_data = json.load(f)
item_schema_data = item_schema_data["properties"]
for k, v in item_schema_data.items():
    # Check schema for lists, and extract first entry
    if isinstance(v["type"], list):
        item_schema_data[k]["type"] = v["type"][0]

# Load osrsbox-db schema-monsters.json file, and get the properties key
schema_file_path = "schema-monsters.json"
with open(schema_file_path) as f:
    monster_schema_data = json.load(f)
monster_schema_data = monster_schema_data["properties"]
for k, v in monster_schema_data.items():
    # Check schema for lists, and extract first entry
    if isinstance(v["type"], list):
        monster_schema_data[k]["type"] = v["type"][0]

# Define item resource
items = {
    # Title tag
    "item_title": "items",

    # Provide addition item.name lookup
    "additional_lookup": {
        # Allow any character in an item name
        "url": 'regex("[ &\'()+\\-\\./0-9a-zA-Z]+")',
        "field": "name"
    },

    # Specify JSON schema
    "schema": item_schema_data,
}

# Define monsters resource
monsters = {
    # Title tag
    "item_title": "monsters",

    # Provide addition monster.name lookup
    "additional_lookup": {
        # Allow any character in a monster name
        "url": 'regex("[ \'()\\-\\.0-9a-zA-Z]+")',
        "field": "name"
    },

    # Specify JSON schema
    "schema": monster_schema_data,
}

DOMAIN = {
    "items": items,
    "monsters": monsters,
}
