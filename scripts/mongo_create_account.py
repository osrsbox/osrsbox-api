"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Connect to MongoDB, create account for API.

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
import base64
import hashlib
import getpass
import secrets

import pymongo

from connection_properties import ConnectionProperties
cp = ConnectionProperties()

# Initialize MongoDB connection
client = pymongo.MongoClient(f"mongodb://{cp.username}:{cp.password}@localhost:{cp.port}/{cp.db_name}")
db = client[cp.db_name]


def main():
    # Get desired username and password from user
    print(">>> Enter new account details...")
    username = input("  > Enter username: ")
    password = getpass.getpass("  > Enter password: ")
    password = password.encode("utf-8")

    # Generate salt, and convert to base64
    salt = secrets.token_bytes(64)
    salt = base64.b64encode(salt)
    salt = salt.decode()
    salt = salt.encode("utf-8")

    # Hash new credentials using scrypt
    password_hashed = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1)
    password_base64 = base64.b64encode(password_hashed)
    password_base64 = password_base64.decode()

    # Load collections
    collection = db["accounts"]

    # Initialize user properties
    new_user = {
        "username": username,
        "password": password_base64,
        "salt": salt
    }

    print("  > Creating account...")
    collection.insert_one(new_user)


if __name__ == "__main__":
    main()
