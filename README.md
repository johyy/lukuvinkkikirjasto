# Lukuvinkkikirjasto

![GitHub Actions](https://github.com/johyy/lukuvinkkikirjasto/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/johyy/lukuvinkkikirjasto/branch/main/graph/badge.svg?token=TVM08LCTBS)](https://codecov.io/gh/johyy/lukuvinkkikirjasto)

## Backlog, testikattavuusraportti ja release

[Projektin backlog](https://docs.google.com/spreadsheets/d/1Ku5KeGKPKRg1Zwu5qJ2XgSO0A5ig9_967XB01-ox_BI/edit#gid=792830139)

[Testikattavuusraportti](https://github.com/johyy/lukuvinkkikirjasto/blob/main/dokumentaatio/testikattavuus.md)

[Release](https://github.com/johyy/lukuvinkkikirjasto/releases/tag/sprint2)

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

Testit suoritetaan juurikansiossa komennoilla:

```
poetry shell
```

```
pytest
```

## Definition of Done

User Story katsotaan valmistuneeksi, kun:

- User Storylle kirjatut taskit on tehty
- Testikattavuus on yli 80 %
- Kaikki testit menevät läpi
- Koodin staattinen analyysi on kunnossa, Pylint arvo > 8
- Koodi on puskettu tuotantoympäristöön
- Koodi on integroitu aikaisempaan työhön ja kokonaisuus on toimiva
