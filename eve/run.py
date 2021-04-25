"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
The osrsbox-api main program to run the Python Eve API.

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

from eve import Eve
from eve.auth import BasicAuth
from eve.io.mongo import Validator
from eve_swagger import get_swagger_blueprint
from eve_swagger import add_documentation
from flask import jsonify


class MyValidator(Validator):
    def _validate_description(self, description, field, value):
        """ {'type': 'string'} """
        # Accept description attribute, used for swagger doc generation
        pass

    def _validate_example(self, description, field, value):
        """ {'type': 'string'} """
        # Accept an example attribute, used for swagger doc generation
        pass


class SCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # Specify accounts collection
        accounts = app.data.driver.db["accounts"]

        # Query accounts collection to see if account exists
        account = accounts.find_one({"username": username})
        if not account:
            return False

        # Get salt from query
        salt = account["salt"]

        # Convert user supplied password to bytes
        password = password.encode()

        # Hash pass/salt using scrypt
        password_hashed = hashlib.scrypt(password,
                                         salt=salt,
                                         n=2**14, r=8, p=1)

        # Convert hashed pass to base64, then convert to string
        password_base64 = base64.b64encode(password_hashed)
        password_base64 = password_base64.decode()

        # Check hashes match
        return password_base64 == account["password"]


# Initialize Eve app, and attach modified validator and auth
app = Eve(validator=MyValidator,
          auth=SCryptAuth)

# Configure environment (production/development)
environment = os.environ["APP_ENV"]
if environment == "prod":
    host = "https://api.osrsbox.com"
    port = 5000
if environment == "dev":
    host = "http://127.0.0.1"
    port = 5000

# Set Swagger configuration
SWAGGER_CONFIG = {
    "title": "osrsbox-api",
    "version": "1.0",
    "description": "An open, free, complete and up-to-date RESTful API for Old School RuneScape (OSRS) items, monsters and prayers.",
    "contact": {
        "name": "osrsbox-api",
        "url": "https://api.osrsbox.com"
    },
    "license": {
        "name": "GNU General Public License v3.0",
        "url": "https://github.com/osrsbox/osrsbox-api/blob/master/LICENSE",
    },
    "schemes": ["https"],
}

# If dev environment, use HTTP for swagger
if environment == "dev":
    SWAGGER_CONFIG["schemes"] = ["http"]

swagger = get_swagger_blueprint()

# Update documentation: Fix invalid warnings
add_documentation(swagger, {"components": {"parameters": {
                  "Item_id": {"schema": {"type": "string"}}}}})
add_documentation(swagger, {"components": {"parameters": {
                  "Equipment_id": {"schema": {"type": "string"}}}}})
add_documentation(swagger, {"components": {"parameters": {
                  "Weapon_id": {"schema": {"type": "string"}}}}})
add_documentation(swagger, {"components": {"parameters": {
                  "Monster_id": {"schema": {"type": "string"}}}}})
add_documentation(swagger, {"components": {"parameters": {
                  "Prayer_id": {"schema": {"type": "string"}}}}})
add_documentation(swagger, {"components": {"parameters": {
                  "Icons_item_id": {"schema": {"type": "string"}}}}})
add_documentation(swagger, {"components": {"parameters": {
                  "Icons_prayer_id": {"schema": {"type": "string"}}}}})

app.register_blueprint(swagger)

# Set Swagger UI information to the specific configuration
app.config["SWAGGER_INFO"] = SWAGGER_CONFIG

# Set the Swagger host, to enable running of Swagger UI API calls
app.config["SWAGGER_HOST"] = f"{host}"


@app.errorhandler(Exception)
def handle_exception(e):
    rdict = {
        "_status": "ERR",
        "_error": {
            "code": 500,
            "message": str(e)
        }
    }

    return jsonify(rdict), 500


if __name__ == "__main__":
    app.run(host=host, port=port)
