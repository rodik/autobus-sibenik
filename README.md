# autobus-sibenik

Smisleni red vožnje gradskih autobusnih linija.

## Problem
Postojeći [raspored](https://www.gradski-parking.hr/stranice/javni-gradski-prijevoz/86.html) gradskih i prigradskih autobusnih linija prikazuje polaske i broj minuta između pojedinih stanica. Ako se u npr. želite na stanici **Križ** ukrcati na autobusnu liniju 2 (*Šubićevac - Ražine*) i doći do **TLM-a**, morate zbrajati sva vremena između prethodnih stanica `2 + 1 + 1 + 5 + 1 + 1 + 3 + 1 + 2 = 17`, zatim tih 17 minuta dodati na vrijeme polaska (npr. `10:20`) i doći do zaključka da vam bus staje na stanici Križ u `10:37`.

## Rješenje
[Tablični prikaz](https://rodik.github.io/autobus-sibenik/) vremena po svim stanicama.

## Izmjene voznog reda
Podatke je dovoljno osvježiti u odgovarajućem JSON fajlu (npr. [B__brodarica__ak](./linije/gradske/04_ak_brodarica/B__brodarica__ak.json) i napraviti Pull Request u `main` branch. Stranica s tablicom će se automatski osvježiti i prikazivati novi raspored.

Izmjenu možete [napraviti sami](CONTRIBUTING.md). Ako ne znate sami, napravite novi [issue](https://github.com/rodik/autobus-sibenik/issues) s kratkim opisom izmjene voznog reda. 