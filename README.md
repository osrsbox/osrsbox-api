# osrsbox-api

An open, free, complete and up-to-date RESTful API for Old School RuneScape (OSRS) items, monsters and grand exchange data

This repository hosts the source code for the `osrsbox-api`, the RESTful API for the [`osrsbox-db` project](https://github.com/osrsbox/osrsbox-db). The project is not yet live, but check back soon... as a release date is immanent!

## Setup Instructions

These instructions are for Ubuntu 18.04. Basically, you just need Docker. Install required packages for Docker:

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
sudo systemtctl status docker
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

Access the API at (but there will be no data... yet):

```
127.0.0.1:5000/api/items
127.0.0.1:5000/api/monsters
127.0.0.1:5000/api-docs
```
