# Author:  PH01L
# Email:   phoil@osrsbox.com
# Website: https://www.osrsbox.com
#
# Description:
# Dockerfile for osrsbox-api
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

FROM python:3.7-slim-buster
MAINTAINER PH01L <phoil@osrsbox.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY ./app/ /usr/src/app/

EXPOSE 5000
CMD ["python", "run.py"]
