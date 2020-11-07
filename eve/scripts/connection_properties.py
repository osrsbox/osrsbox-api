"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Database class for MongoDB data properties.

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


class ConnectionProperties():
    def __init__(self):
        self.username = os.getenv("PROJECT_USERNAME")
        self.password = os.getenv("PROJECT_PASSWORD")
        self.port = os.getenv("MONGO_PORT")
        self.db_name = os.getenv("DATABASE_NAME")
