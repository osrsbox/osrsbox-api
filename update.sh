#!/bin/bash
: '
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Update the API after a osrsbox package update

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
'
# Dump docker nginx logs
docker logs osrsbox-api-nginx >> /tmp/nginx.log

# Keep local changes
git stash
git pull
git submodule update --remote --merge

# Clean the docker environment
./clean.sh

# Add existing changes (username/password)
git stash pop

# Build and run docker environment, as a background process
docker-compose up -d --build
