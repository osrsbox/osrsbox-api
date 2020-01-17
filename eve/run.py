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
import hashlib

from eve import Eve
from eve.auth import BasicAuth
from eve.io.mongo import Validator
from eve_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint


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
        accounts = app.data.driver.db['accounts']
        account = accounts.find_one({'username': username})
        password = password.encode('utf-8')
        pwdhash = hashlib.scrypt(password)
        return account and \
            bcrypt.hashpw(password, account['password']) == account['password']


# Start by configuring environment (production/development)
environment = "dev"

if "APP_ENV" in os.environ:
    environment = os.environ["APP_ENV"]

if environment == "prod":
    host = "api.osrsbox.com"
    port = 5000
    API_URL = f"https://{host}/api-docs"
else:
    host = "127.0.0.1"
    port = 5000
    API_URL = f"http://{host}:{port}/api-docs"

# Set Swagger UI configuration
SWAGGER_CONFIG = {
    "title": "osrsbox-api",
    "version": "1.0",
    "description": "An open, free, complete and up-to-date RESTful API for Old School RuneScape (OSRS) items, monsters and grand exchange data",
    "termsOfService": "Terms of Service",
    "contact": {
        "name": "PH01L",
        "url": "https://www.osrsbox.com"
    },
    "license": {
        "name": "GNU General Public License v3.0",
        "url": "https://github.com/osrsbox/osrsbox-api/blob/master/LICENSE",
    },
    "schemes": ["https"],
}

if environment != "prod":
    SWAGGER_CONFIG["schemes"] = ["http"]

# Set URL for Swagger UI
SWAGGER_URL = "/swagger"

# Using flask_swagger_ui, create Swagger UI blueprint
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL,
                                              API_URL,
                                              config=SWAGGER_CONFIG,
                                              )

# Initialize Eve app, and attach modified Validator
# app = Eve(validator=MyValidator,
#           auth=SCryptAuth)

app = Eve(validator=MyValidator)

# Using eve-swagger, generate /api-docs and JSON for Swagger UI
app.register_blueprint(swagger)

# Using flask_swagger_ui, generate Swagger UI web interface
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Set Swagger UI information to the specific configuration
app.config["SWAGGER_INFO"] = SWAGGER_CONFIG

# Set the Swagger host, to enable running of Swagger UI API calls
if environment == "prod":
    app.config["SWAGGER_HOST"] = f"{host}"
else:
    app.config["SWAGGER_HOST"] = f"{host}:{port}"


if __name__ == "__main__":
    app.run(host=host, port=port)
