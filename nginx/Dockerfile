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
FROM alpine:latest
LABEL MAINTAINER="PH01L <phoil@osrsbox.com>"

# Install nginx
RUN apk --update add nginx

# Remove cache to reclaim some space
RUN rm -rf /var/cache/apk/*

# Link log files to stdout/err to forward to Docker logs
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

# Make needed directories
RUN mkdir /etc/nginx/sites-enabled/
RUN mkdir -p /run/nginx

# Remove the default configuration
RUN rm -rf /etc/nginx/conf.d/default.conf

# Copy the project configuration file
COPY conf.d/app.conf /etc/nginx/conf.d/app.conf
# COPY conf.d/app.dev.conf /etc/nginx/conf.d/app.dev.conf

# Expose ports 80/443 to outside
EXPOSE 80 443

# Run nginx
CMD ["nginx", "-g", "daemon off;"]
