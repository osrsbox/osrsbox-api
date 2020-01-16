# osrsbox-api

An open, free, complete and up-to-date RESTful API for Old School RuneScape (OSRS) items, monsters and grand exchange data

This repository hosts the source code for the `osrsbox-api`, the RESTful API for the [`osrsbox-db` project](https://github.com/osrsbox/osrsbox-db). The project is not yet live, but check back soon... as a release date is immanent! Regardless, you can setup your own local environment using this repository.

## Setup Instructions

You can setup your own local API using the following instructions. These instructions are for Ubuntu 18.04, and have not been tested on other environments. But they are pretty generic.

### Clone this Repository

Start by cloning tise repository:

```
git clone --recursive https://github.com:osrsbox/osrsbox-api.git
```

### Install and Configure Docker

Install required packages for Docker:

```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

Add Docker GPG key, then add the repository to APT sources lists:

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
```

Update package repositories:

```
sudo apt update
```

Set Docker repo instead of default Ubuntu repo:

```
apt-cache policy docker-ce
```

Install Docker:

```
sudo apt install docker-ce
```

Check status:

```
sudo systemctl status docker
```

Add current user to `docker` group to allow user to run Docker"

```
sudo usermod -aG docker ${USER}
```

Install the `docker-compose` tool:

```
sudo curl -L https://github.com/docker/compose/releases/download/1.25.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
```

Set executable permissions for the `docker-compose` tool:

```
sudo chmod +x /usr/local/bin/docker-compose
```

Build and activate the Docker container:

```
docker-compose up --build
```

If you have finish and want to clean your Docker environment, the following commands will help:

```
docker-compose down
docker volume rm osrsbox-api_appdata
docker volume rm osrsbox-api_mongodata
docker volume rm osrsbox-api_nginxdata
```

### Load Data into the API

Change to the `scripts` directory:

```
cd scripts
```

Load all requirements using `python3-venv`:

```
python3 -m venv data
source data/bin/activate
pip3 install -r requirements.txt
```

Then load the data:

```
python insert_api_data.py
```

With the data loaded, you can access various API endpoints:

- `items`
- `equipment`
- `weapons`
- `monsters`

To access all items you can use the following URL:

```
0.0.0.0/api/items
```

Or access a specific item, using the ID number (in this case the item ID 0):

```
0.0.0.0/api/items/0
```

You can view the Swagger JSON at:

```
0.0.0.0/api-docs
```

And access the Swagger UI at (this is great for testing the API):

```
0.0.0.0/api/docs
```
