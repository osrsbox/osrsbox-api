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
DEBUG = False

# Set global MongoDB configuration
MONGO_HOST = os.getenv("MONGO_URI")
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_USERNAME = os.getenv("PROJECT_USERNAME")
MONGO_PASSWORD = os.getenv("PROJECT_PASSWORD")
MONGO_AUTH_SOURCE = os.getenv("DATABASE_NAME")
MONGO_DBNAME = os.getenv("DATABASE_NAME")

# Set root (/) as API endpoint
URL_PREFIX = ""

# Set renderer to JSON for API output
RENDERERS = ["eve.render.JSONRenderer", ]

# Enable GET, POST, and DELETE for collections
# RESOURCE_METHODS = ["GET", "POST"]
RESOURCE_METHODS = ["GET"]

# Enable GET, PUT and DELETE for items in collections
# ITEM_METHODS = ["GET", "PUT"]
ITEM_METHODS = ["GET"]

# Lock down all endpoints, apart from GET requests
PUBLIC_METHODS = ["GET"]
PUBLIC_ITEM_METHODS = ["GET"]

# Enable standard client cache directive for all resources
CACHE_CONTROL = "public, max-age=86400"
CACHE_EXPIRES = 86400

# ITEMS
schema_file_path = "schemas/schema-items.json"
with open(schema_file_path) as f:
    item_schema_data = json.load(f)
# Define item resource
items = {
    "item_lookup_field": "id",
    "item_url": 'regex("[0-9]{1,5}")',
    "schema": item_schema_data,
}
# Define weapon resource
weapons = {
    "item_lookup_field": "id",
    "item_url": 'regex("[0-9]{1,5}")',
    "schema": item_schema_data,
    # Specify items database collection as datasource
    "datasource": {
        "source": "items",
        "filter": {"equipable_weapon": True}
    },
}
# Define equipment resource
equipment = {
    "item_lookup_field": "id",
    "item_url": 'regex("[0-9]{1,5}")',
    "schema": item_schema_data,
    # Specify items database collection as datasource
    "datasource": {
        "source": "items",
        "filter": {"equipable_by_player": True}
    },
}

# MONSTERS
schema_file_path = "schemas/schema-monsters.json"
with open(schema_file_path) as f:
    monster_schema_data = json.load(f)
# Define monsters resource
monsters = {
    "item_lookup_field": "id",
    "item_url": 'regex("[0-9]{1,4}")',
    "schema": monster_schema_data,
}

# PRAYERS
schema_file_path = "schemas/schema-prayers.json"
with open(schema_file_path) as f:
    prayer_schema_data = json.load(f)
# Define prayers resource
prayers = {
    "item_lookup_field": "id",
    "item_url": 'regex("[0-9]{1,2}")',
    "schema": prayer_schema_data,
}

# ICONS ITEMS
schema_file_path = "schemas/schema-icons-items.json"
with open(schema_file_path) as f:
    icons_items_schema_data = json.load(f)
# Define icons_items resource
icons_items = {
    "item_lookup_field": "id",
    "item_url": 'regex("[0-9]{1,5}")',
    "schema": icons_items_schema_data,
}

# ICONS PRAYERS
schema_file_path = "schemas/schema-icons-prayers.json"
with open(schema_file_path) as f:
    icons_prayers_schema_data = json.load(f)
# Define icons_prayers resource
icons_prayers = {
    "item_lookup_field": "id",
    "item_url": 'regex("[0-9]{1,2}")',
    "schema": icons_prayers_schema_data,
}

# Set endpoints
DOMAIN = {
    "items": items,
    "weapons": weapons,
    "equipment": equipment,
    "monsters": monsters,
    "prayers": prayers,
    "icons_items": icons_items,
    "icons_prayers": icons_prayers,
}
