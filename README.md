# Lukuvinkkikirjasto

![GitHub Actions](https://github.com/johyy/lukuvinkkikirjasto/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/johyy/lukuvinkkikirjasto/branch/main/graph/badge.svg?token=TVM08LCTBS)](https://codecov.io/gh/johyy/lukuvinkkikirjasto)

## Backlog, testikattavuusraportti, release ja lisenssi

[Projektin backlog](https://docs.google.com/spreadsheets/d/1Ku5KeGKPKRg1Zwu5qJ2XgSO0A5ig9_967XB01-ox_BI/edit#gid=792830139)

[Testikattavuusraportti](https://github.com/johyy/lukuvinkkikirjasto/blob/main/dokumentaatio/testikattavuus.md)

[Release](https://github.com/johyy/lukuvinkkikirjasto/releases/tag/sprint3)

[Lisenssi](https://github.com/johyy/lukuvinkkikirjasto/blob/main/LICENSE)

## Asennus

Aseta riippuvuudet komennolla:

```
poetry install
```

### .env-tiedoston lisäys

Ohjelma tarvitsee .env-tiedoston, jossa on määriteltynä tietokannan osoite ja SECRET_KEY. 

Luo .env-tiedoston ensin komennolla
```
touch .env
```

Avaa .env-tiedosto tekstinmuokkausohjelmalla ja lisää siihen nämä rivit.
```
DATABASE_FILENAME='database.db'
SECRET_KEY=TÄHÄN OMA AVAIN
```
Muista lisätä oma avain kohtaan "SECRET_KEY"

### Ohjelman suorittaminen

Siirry kansion ```src``` sisälle.
Ohjelman pystyy suorittamaan komennoilla:
```
poetry shell
```

```
poetry run flask run
```

Ohjelman suoritus alkaa osoitteessa:

```
http://127.0.0.1:5000/
```

### Testien suorittaminen

Kaikki testit ja tyylitarkistus suoritetaan juurikansiossa komennoilla:

```
poetry shell
```

```
invoke test
```

Pelkät yksikkötestit, Robot Framework -testit tai Pylint-tyylitarkastus suoritetaan juurikansiossa komennoilla:

```
pytest
```
```
invoke robot
```
```
invoke lint
```

Testikattavuuden saa ajamalla komennon:

```
invoke coverage-report
```

## Definition of Done

User Story katsotaan valmistuneeksi, kun:

- User Storylle kirjatut taskit on tehty
- Testikattavuus on yli 80 %
- Kaikki testit menevät läpi
- Koodin staattinen analyysi on kunnossa, Pylint arvo > 8
- Koodi on puskettu tuotantoympäristöön
- Koodi on integroitu aikaisempaan työhön ja kokonaisuus on toimiva
