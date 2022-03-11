#!/bin/bash

# käynnistetään Flask-palvelin taustalle
cd src
DATABASE_FILENAME=test-database.db SECRET_KEY=sk123 poetry run flask run &

# odetetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000/ping)" != "200" ]]; 
  do sleep 1; 
done

# suoritetaan testit
# poetry run robot tests
cd src
poetry run robot tests
status=$?

# pysäytetään Flask-palvelin portissa 5000
kill $(lsof -t -i:5000)

exit $status
