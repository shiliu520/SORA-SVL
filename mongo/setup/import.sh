#! /bin/bash

mongoimport --host localhost --db WISE --collection global --mode=upsert --type json --jsonArray --file /docker-entrypoint-initdb.d/global.json
mongoimport --host localhost --db WISE --collection maps --mode=upsert --type json --jsonArray --file /docker-entrypoint-initdb.d/maps.json
mongoimport --host localhost --db WISE --collection plugins --mode=upsert --type json --jsonArray --file /docker-entrypoint-initdb.d/plugins.json
mongoimport --host localhost --db WISE --collection vehicles --mode=upsert --type json --jsonArray --file /docker-entrypoint-initdb.d/vehicles.json
mongoimport --host localhost --db WISE --collection hd_maps --mode=upsert --type json --jsonArray --file /docker-entrypoint-initdb.d/hd_maps.json
mongoimport --host localhost --db WISE --collection geojson --mode=upsert --type json --jsonArray --file /docker-entrypoint-initdb.d/geojson.json