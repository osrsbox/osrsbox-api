"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Connect to MongoDB container, create accounts database and populate.

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
import base64
import hashlib

from pymongo import MongoClient

# Set MongoDB connection configuration
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_DBNAME = "osrsbox-db"
PROJECT_USERNAME = os.getenv("PROJECT_USERNAME")
PROJECT_PASSWORD = os.getenv("PROJECT_PASSWORD")
PROJECT_SALT = os.getenv("PROJECT_SALT")


def main():
    # Start by generating scrypt hash
    password = PROJECT_PASSWORD.encode("utf-8")
    salt = PROJECT_SALT.encode("utf-8")
    password_hashed = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1)
    password_base64 = base64.b64encode(password_hashed)
    password_base64 = password_base64.decode()

    # Initialize MongoDB connection
    print(">>> Connecting to MongoDB....")
    client = MongoClient(f"mongodb://{PROJECT_USERNAME}:{PROJECT_PASSWORD}@mongo:{MONGO_PORT}/{MONGO_DBNAME}")

    # Load database
    db = client[MONGO_DBNAME]

    # Load collections
    coll = db["accounts"]

    # Initialize user properties
    admin_user = {
        "username": PROJECT_USERNAME,
        "password": password_base64
    }

    print("  > Creating account...")
    coll.insert_one(admin_user)


if __name__ == "__main__":
    main()
