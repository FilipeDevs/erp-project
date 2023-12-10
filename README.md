# ERP - Book Sales Module

The goal of this project was to develop a book sales module in ODOO along with a Django interface to also interact with it.

## Features

## ODOO

* View/Add/Delete/Edit Books
* Consult the authors of the books and classify them by number of books written
* User can like books
* Integration of inventory and sales management for the books

## Django interface

* Configure an ODOO connection
* Search books based on the name
  

## Usage

### ODOO (Docker environement)

#### Prerequisites

- Docker installed on your machine.

#### Create the necessary containers

All commands should be run in the root of the repository

**First usage**

For the database (POSTGRES 13) :

```
docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:13
```

For Odoo (ODOO 14) :

```
docker run --mount type=bind,source="$(pwd)"/extra-addons,target=/mnt/extra-addons/ -p 8069:8069 --name odoo --link db:db -t odoo:14
```

**Following usages**

```
docker start db
docker start odoo
docker logs -f odoo
```

Once it's done you can connect to [localhost:8069](http://localhost:8069/) and setup Odoo.

You can then install the module `esi_lecture` and start using it by accesing the menu `ESI LECTURE`.

#### DJANGO interface (Virtual environement)

#### Prerequisites

- Atleast Python 3.10 

#### Setup

From the root navigate to  `django_interface/` :

```
cd django_interface/
```

Create virtual environement:







