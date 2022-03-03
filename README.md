# Lukuvinkkikirjasto

![GitHub Actions](https://github.com/johyy/lukuvinkkikirjasto/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/johyy/lukuvinkkikirjasto/branch/main/graph/badge.svg?token=TVM08LCTBS)](https://codecov.io/gh/johyy/lukuvinkkikirjasto)

## Backlog

[Projektin backlog](https://docs.google.com/spreadsheets/d/1Ku5KeGKPKRg1Zwu5qJ2XgSO0A5ig9_967XB01-ox_BI/edit#gid=792830139)

[Testikattavuusraportti](https://github.com/johyy/lukuvinkkikirjasto/dokumentaatio/testikattavuus.md)

## Asennus

Aseta riippuvuudet komennolla:

```
poetry install
```

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```
poetry run flask run
```

## Definition of Done

User Story katsotaan valmistuneeksi, kun:

- User Storylle kirjatut taskit on tehty
- Testikattavuus on yli 80 %
- Kaikki testit menevät läpi
- Koodin staattinen analyysi on kunnossa, Pylint arvo > 8
- Robot frameworkia on käytetty
- Koodi on puskettu tuotantoympäristöön
- Koodi on integroitu aikaisempaan työhön ja kokonaisuus on toimiva
