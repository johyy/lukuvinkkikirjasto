<h1>Loppuraportti – Lukuvinkkikirjasto</h1>

<i>Katja Kerkkänen, Tuukka Puonti, Noora Matilainen, Mingchen Li, Jonna Hyypiä</i>

<h2>Sprintti 1<h2>

Aloitustapaamisen jälkeen ensimmäiseen sprinttiin lähdettiin innolla. Tarkoituksenamme oli tehdä lukuvinkkikirjasto, jossa datan talletus ja haku hoidettaisiin Postgre-SQL -tietokannassa ja itse applikaation toteutus vietäisiin lopulta Herokuun, jossa se olisi vapaasti kenen tahansa nähtävissä ja käytettävissä. Sovimme, että ensin hoidettaisiin tarvittavien elementtien konfiguraatiot sekä toteutuksen pohja GitHubiin ja vasta sitten rupeaisimme tekemään varsinaisia toiminnallisuuksia. 

Alkuun kaikki näyttikin sujuvan suunnitelman mukaisesti ja varsin näppärästi, kunnes sprintin puolessa välissä alkoi ongelmia kasaantua. Tietokannan konfigurointi ei käynytkään niin helposti kuin olimme ajatelleet. Toisin kuin tietokantasovellus-kurssilla, tietokannan kanssa työskenteleviä henkilöitä oli useita ja tietokannan lokaali osoite piti jokaisen vaihtaa itselleen oikeaksi jokaisen git pullin yhteydessä. Tietokannan testaaminen Postgre-SQL:n kanssa ei myöskään ollut ihan triviaalia. Kun tietokantatestejä viimein saatiin lokaalisti toimimaan, ei jatkuvan integraation automaatiotestaus GitHubissa enää toiminut, sillä etärepositiolla ei ollut omaa tietokantaansa, jota testata.

Merge-konfliktit tulivat kaikille tutuiksi, kun tietokantojen osoitteita vaihdettiin jokaisella työskentelykerralla. Konflikteja aiheutti lisäksi user storyjen taskien hieman epäselvä jakaminen. Koska taskit oli jaettu tyylillä “yksi toiminnallisuuden kerros per tekijä”, johti tämä siihen, että päällekkäisiä asioita tehtiin eri henkilöiden toimesta eri kerroksissa ja vähän eri tyyleillä. Varsinkin jos samoja asioita tehtiin eri ihmisten toimesta samaan aikaan, saattoi pakka olla täysin sekaisin kun tuli repositorioon pushaamisen aika. Kommunikointi ryhmän Discord-kanavalla oli vilkasta, mutta aiheutti myös sekaannuksia. Samat sanat tarkoittivat eri asioita kullekin lukijalle. 

Ongelmia tuotti myös se, että sovelluksen rakenteesta ei oltu alussa käyty tarkkaa keskustelua, vaan se oli jokaisen ajatuksissa hieman erilainen. Tämän näyttäytyi circular import error:ina ja johtui siis siitä, että luokkia yritettiin importata kehämuodostelmassa, mikä ei tietenkään ole mahdollista.

Vaikka sprintti oli haasteellinen, oli se myös todella opettavainen. Teknisten merge-konfliktien ja automaatiotestausten lisäksi tuli kantapään kautta koettua se, miten tärkeää on heti alusta lähtien tehdä yksi pieni asia kerrallaan ja varmistaa että kyseinen asia toimii varmasti kaikilla mittareilla, ennen kuin edes miettii jatkamista seuraavaan asiaan. Sprintin tärkeä oppi oli myös se, miten asiat edistyvät huomattavasti mukavammin pari/ryhmäkoodaussessiossa verrattuna siihen, että jokainen tahollaan hakkaa päätänsä seinään samojen pulmien takia.

Vaikka stressitasot ehtivätkin nousta ensimmäisen sprintin aikana itse kullakin, oli ryhmässä kuitenkin toisia kunnioittava ja ennen kaikkea motivoitunut fiilis koko sprintin ajan. Apua uskallettiin kysyä ja omia ehdotuksia heittää ilmaan. Haasteista ei lannistuttu, vaan ratkaisuja etsittiin aktiivisesti.

<h2>Sprintti 2</h2>

Ensimmäisen sprintin retrospektiivistä otettiin kaikki hyöty irti ja ongelmakohdat pyrittiin paikallistamaan. Nyt oli selvästi Stop & Fix:in aika, jotta tietokanta ja sen testaus saataisiin toimimaan ennen kuin toiminnallisuuksien tuottoa jatkettaisiin. Päätimme vaihtaa tietokantajärjestelmäksi SQLiten, jonka käyttö pitäisi olla yksinkertaisempaa kuin Postgre-SQL:n, jotta tietokannan toiminnan kanssa säätäminen ei veisi enempää aikaa pikkuruisesta projektista. Samalla päätimme, että sovellus jäisi työpöytäsovellukseksi, eikä sitä siirrettäisi Herokuun.

Tietokanta saatiin vaihdettua ja kun kaikki tietokantatestitkin saatiin toimimaan testitietokannan kanssa, näytti automaatiotestaus viimein vihreältä! Vaikka kaikki ongelmat tietokannan kanssa eivät suinkaan vielä olleet ohi, oli tästä hyvä jatkaa varsinaisten toiminnallisuuksien kanssa. Olimme edellisesta sprintistä viisastuneina jakaneet taskit suunnilleen yksi user story per tekijä, kaikkien kerrosten kuuluessa työnkuvaan. Tämä toimikin hienosti ja vielä kun päätimme pitää lyhyen palaverin lähes joka päivä, olivat kaikki paremmin kartalla siitä, mitä toiset olivat tekemässä.

Sprintin ongelmaksi voisi nimetä epäselvyydet luokkarakenteissa ja kerroksissa. Nämä johtivat juurensa alun luokkapohjien konfiguraatioihin ja epäselviin nimeämiskäytäntöihin, mutta olivat korjattavissa melko vaivattomasti.

Toisen sprintin alussa tajusimme, että sellaisia toiminnallisuuksia, jotka olisivat todennäköisesti vuorossa seuraavaksi, ei kannata tehdä etukäteen. Koska sovelluksen muoto muokkautuu koko ajan, voi olla että työ on turhaa tai se voi pahimmillaan aiheuttaa ohjelman hajoamista kun toiset toiminnallisuudet tai testit eivät vielä ole niin pitkällä. Oppia tuli myös Robot Frameworkin käytöstä, mock-testauksesta sekä Pytestin, Sqliten ja Flaskin yhdistämisestä ja debuggauksesta yksikkötesteissä. Tässä vaiheessa tuli myös totuttua siihen ajatukseen, että jokainen on vastuussa lähinnä omista taskeistaan ja vaikka joku niistä ei valmistuisikaan asiakastapaamiseen mennessä, ei se tarkoita, että työ olisi ollut turhaa.

<h2>Sprintti 3</h2>

Kolmannen sprintin aloitus tuntui sujuvan jo rutiinilla. Kommunikaatio ryhmässä oli hioutunut huippuunsa eivätkä tekemisen meininki tai ryhmähenki olleet missään vaiheessa hiipuneet. Varsinaisia ongelmia ei sprintissä enää ollut, vaikkakin testitietokanta tuotti edelleen omia haasteitaan. Tämä ei kuitenkaan estänyt toiminnallisuuksien ja muiden testien työstämistä, ja koska taskit oli edellisen sprintin tapaan jaettu user storyittain, ei päällekkäistä työtä syntynyt.

Sprinttien aikana opimme arvioimaan tehtäviin kuluvaa työaikaa. Tätä tietoutta voi varmasti käyttää hyväksi seuraavissa projekteissa. Meille jokaiselle ryhmätyö oli ensimmäinen laatuaan ohjelmistotuotannon parissa. Se varmasti edesauttoi alun ongelmien syntymistä, mutta toimi toisaalta loistavana oppina siitä, miten projektia ei ehkä kannata aloittaa. 

Kun demotilaisuuden aika koitti, toimivat kaikki toiminnallisuudet juuri niin kuin haluttiin ja ongelmat testitietokantojen kanssa oli selätetty. Testikattavuus nousi lopulta huimaan 96 %:iin ja Pylint-arvokin oli päälle yhdeksikön. Kaikki pyydetyt taskit oli hoidettu Definition of Done:n mukaisesti ja backlog oli ajantasalla. Tätä projektia oli ilo tehdä ja esitellä asiakkaalle.
