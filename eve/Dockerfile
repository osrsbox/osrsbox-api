# Author:  PH01L
# Email:   phoil@osrsbox.com
# Website: https://www.osrsbox.com
#
# Description:
# Dockerfile for Python Eve
#
# Copyright (c) 2020, PH01L
# 
###############################################################################
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
FROM python:3.7-alpine
LABEL MAINTAINER="PH01L <phoil@osrsbox.com>"

# Set PYTHONPATH environment variable
ENV PYTHONPATH "${PYTHONPATH}:/var/www/eve/"

# Set working directory to www and app data
WORKDIR /var/www/eve/

# Install API requirements and gunicorn
ADD ./requirements.txt /var/www/eve/requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Add the www user, run as root (temporarily)
USER root
RUN addgroup -g 1000 www; exit 0
RUN adduser -D -u 1000 -G www www -s /bin/sh; exit 0

# Run as the www user
USER www

# Expose port 5000 and run the app
EXPOSE 5000
CMD [ "gunicorn", "--workers", "3", "--worker-connections", "1024", "--log-file", "-", "--bind", "0.0.0.0:5000", "run:app"]
