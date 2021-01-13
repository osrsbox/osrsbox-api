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
# Get current date
date=$(date +'%m-%d-%Y')

# Dump docker nginx logs
docker logs osrsbox-api-nginx >> ~/nginx-$date.log 2>&1

# Clean docker environment
bash clean.sh

# Keep local changes
git stash

# Update repo from Git
git pull

# Update submodules (schemas) if needed (uncomment)
# git submodule update --remote --merge

# Add existing changes (username/password)
git stash pop

# Build and run docker environment, as a background process
docker-compose up -d --build

# Update osrsbox data
docker exec -t osrsbox-api-eve python3 /scripts/mongo_insert_osrsbox.py

# Clear cache after update
docker exec -t osrsbox-api-nginx rm -rf /etc/nginx/cache/*
