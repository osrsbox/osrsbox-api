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

from eve import Eve
from eve_swagger import swagger

# Bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'

app = Eve()
app.register_blueprint(swagger)

# required. See http://swagger.io/specification/#infoObject for details.
app.config["SWAGGER_INFO"] = {
    "title": "osrsbox-api",
    "version": "1.0",
    "description": "An open, free, complete and up-to-date RESTful API for Old School RuneScape (OSRS) items, monsters and grand exchange data",
    "termsOfService": "TODO: Terms of Service",
    "contact": {
        "name": "PH01L",
        "url": "https://www.osrsbox.com"
    },
    "license": {
        "name": "GNU General Public License v3.0",
        "url": "https://github.com/osrsbox/osrsbox-api/blob/master/LICENSE",
    }
}

app.config['SWAGGER_HOST'] = host


if __name__ == "__main__":
    app.run(host=host, port=port)

