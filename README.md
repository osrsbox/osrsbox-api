# osrsbox-api

An open, free, complete and up-to-date RESTful API for Old School RuneScape (OSRS) items, monsters and prayer data. This repository hosts the source code for the `osrsbox-api`, the RESTful API for the [`osrsbox-db` project](https://github.com/osrsbox/osrsbox-db). The official `osrsbox-api` project is available from:

- [https://api.osrsbox.com](https://api.osrsbox.com)

## Using the osrsbox API

This section documents the API structure and provides some guidance on usage:

### API Endpoints

The API currently has a total of 5 API endpoints, which you can query and get data. The following list documents the endpoints and associated URL:

- Items: [https://api.osrsbox.com/items](https://api.osrsbox.com/items)
- Equipment: [https://api.osrsbox.com/equipment](https://api.osrsbox.com/equipment)
- Weapons: [https://api.osrsbox.com/weapons](https://api.osrsbox.com/weapons)
- Monsters: [https://api.osrsbox.com/monsters](https://api.osrsbox.com/monsters)
- Prayers: [https://api.osrsbox.com/prayers](https://api.osrsbox.com/prayers)

### Swagger UI

For those new to REST APIs, Swagger is a set of rules (a specification) for describing API structure. Have a read of [What is Swagger?](https://swagger.io/docs/specification/2-0/what-is-swagger/), if you are interested. The osrsbox API provides Swagger documentation, available from:

- [https://api.osrsbox.com/api-docs](https://api.osrsbox.com/api-docs)

More interestingly, you can try out specific API endpoints using the Swagger UI, available from:

- [https://api.osrsbox.com/swaggerui](https://api.osrsbox.com/swaggerui)

In this interface, you can _Try out_ different API endpoints. For example, try the following:

- Browse to: [https://api.osrsbox.com/swaggerui](https://api.osrsbox.com/swaggerui)
- Click on the _GET /items_ button, which will expand
- Click on the _Try it out_ button
- Click on the _Execute_ button
- Browse the _Response_ section and you will find:
    - A curl command, which documents your API request
     - A request URL, which documents the API URL used
     - A response body, which documents the data you got back from the API

In the Swagger UI, there is a _Models_ section at the bottom of the page. If you review this section you will see the different properties available for the different API endpoints.

### Example API URLs

I always like examples to help learn how projects or resources are used. This section documents some useful examples for the osrsbox API. The API is most useful when integrating with an application, for example, a web application. But you can also query the API and view the results in a web browser to see the raw data.

#### Access All OSRS Items

To access all items you can use the following URL:

- [https://api.osrsbox.com/items](https://api.osrsbox.com/items)

If you were interested in monsters, just replace the `items` endpoint, with `monsters` (the same is true for `equipment`, `weapons` or `prayers`):

- [https://api.osrsbox.com/monsters](https://api.osrsbox.com/monsters)

This query will return the first 25 items, out of approximately 23,000 available items. From here you can continue the query using pagination. The returned JSON from the first query will have a `_links` key, with a nested `next` key and also a nested `last` key. Below is an example:

```
 "_links": {
 "parent": {
 "title": "home",
 "href": "/"
 },
 "self": {
 "title": "items",
 "href": "items"
 },
 "next": {
 "title": "next page",
 "href": "items?page=2"
 },
 "last": {
 "title": "last page",
 "href": "items?page=897"
 }
 },
```

You can see that the next page is accessible using the `?page=2` parameter, and there are pages available up to `?page=897`. You could make a loop to query all the pages from page 2 to page 897. A full URL example to fetch the second page would be:

- [https://api.osrsbox.com/items?page=2](https://api.osrsbox.com/items?page=2)

#### Access a Specific OSRS Item

There are multiple ways to access a specific OSRS item (weapon, equipment, monster or prayer). Firstly, you can query a specific API endpoint and include the ID number. For example, to access the _Abyssal whip_ you could use the ID number `4151`, and use the following URL:

- [https://api.osrsbox.com/items/4151](https://api.osrsbox.com/items/4151)

If you want to know a specific item or monster URL, you could use the following tools:

- [https://www.osrsbox.com/tools/item-search/](https://www.osrsbox.com/tools/item-search/)
- [https://www.osrsbox.com/tools/npc-search/](https://www.osrsbox.com/tools/npc-search/)

The second method to find a specific item would be to write a query for the API. Take the following example of finding the _Abyssal whip_ item. The following query would find any item by matching the item name:

- [https://api.osrsbox.com/items?where={"name":"Abyssal%20whip"}](https://api.osrsbox.com/items?where={"name":"Abyssal%20whip"})

A couple of notes about this:

- OSRS item names always start with a capital letter
- No other capital letters occur in any OSRS name
- The `%20` indicates a space character

When you run this query, you will get a response containing 5 items. In OSRS, there may be items that have multiple occurrences, as duplicate items might be used in quests, minigames or have some other use. You can add query parameters to find the item you desire. Some useful API query parameters include:

- `duplicate`: A boolean indicating if the item is a duplicate
- `equipable_by_player`: A boolean indicating if the item is equipable (so not a placeholder or noted item)
- `equipable_weapon`: A boolean indicating if the item is a weapon

Using these properties, you could entend the initial query. For example:

- [https://api.osrsbox.com/items?where={"name":"Abyssal%20whip","duplicate":false,"equipable_weapon":true}](https://api.osrsbox.com/items?where={"name":"Abyssal%20whip","duplicate":false,"equipable_weapon":true})

## Setup Instructions

You can set up your local API using the following instructions. These instructions are for Ubuntu 18.04 and have not been tested on other environments. But they are pretty generic.

### Clone this Repository

Start by cloning this repository:

```
git clone --recursive https://github.com:osrsbox/osrsbox-api.git
```

### Install and Configure Docker

The following instructions are for Ubuntu 18.04. Install the required packages for Docker:

```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

Add Docker GPG key, then add the repository to APT sources lists:

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
```

Update package repositories, and set Docker repo instead of default Ubuntu repo:

```
sudo apt update
apt-cache policy docker-ce
```

Install Docker:

```
sudo apt install docker-ce
```

Add current user to `docker` group to allow a user to run Docker:

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

### Load Data into the API

From the host system, you can run various scripts that are located in the `eve` folder and `osrsbox-api-eve` container. There are three scripts in the `eve/scripts` folder:

1. To set up user accounts (to allow POST/PUT requests)
1. To insert data from the `osrsbox` Python package into the API
1. To create an index (of `id` property) in MongoDB

The scripts can be called with `docker exec` as displayed below:

```
docker exec -it osrsbox-api-eve python3 /var/www/scripts/mongo_create_accounts.py
docker exec -it osrsbox-api-eve python3 /var/www/scripts/api_insert_data.py
docker exec -it osrsbox-api-eve python3 /var/www/scripts/mongo_create_indicies.py
```

Done.
