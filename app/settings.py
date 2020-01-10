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

# # Set API version
# API_VERSION = "v1"

# Set id to the primary field
ID_FIELD = "id"

# Set renderer to JSON for API output
RENDERERS = ["eve.render.JSONRenderer", ]

# Enable GET, POST, and DELETE for collections
RESOURCE_METHODS = ["GET", "POST", "DELETE"]

# Enable GET, PUT and DELETE for items in collections
ITEM_METHODS = ["GET", "PUT", "DELETE"]

# Enable standard client cache directive for all resources
CACHE_CONTROL = "max-age=20"
CACHE_EXPIRES = 20

# Load osrsbox-db schema-items.json file, and get the properties key
schema_file_path = "schemas/schema-items.json"
with open(schema_file_path) as f:
    item_schema_data = json.load(f)

# Load osrsbox-db schema-monsters.json file, and get the properties key
schema_file_path = "schemas/schema-monsters.json"
with open(schema_file_path) as f:
    monster_schema_data = json.load(f)

# Define item resource
items = {
    # Provide additional item.id lookup
    "additional_lookup": {
        # Allow any 5 digit number
        "url": 'regex("[0-9]{1,5}")',
        "field": "id"
    },

    # Specify schema
    "schema": item_schema_data,
}

weapons = {
    # Specify schema
    "schema": item_schema_data,

    # Specify items database collection as datasource
    "datasource": {
        "source": "items",
        "filter": {"equipable_weapon": True}
    },
}

equipment = {
    # Specify schema
    "schema": item_schema_data,

    # Specify items database collection as datasource
    "datasource": {
        "source": "items",
        "filter": {"equipable_by_player": True}
    },
}

# Define monsters resource
monsters = {
    # Provide additional monster.id lookup
    "additional_lookup": {
        # Allow any 5 digit number
        "url": 'regex("[0-9]{1,5}")',
        "field": "id"
    },

    # Specify schema
    "schema": monster_schema_data,
}

DOMAIN = {
    "items": items,
    "weapons": weapons,
    "equipment": equipment,
    "monsters": monsters,
}
