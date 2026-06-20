# date/ — cheltuieli-2026.csv (execuție bugetară Nordica, fictiv)

Registru de cheltuieli **fictiv** al firmei Nordica, ianuarie–august 2026 (55 de linii). Folosit la **Cursul 6**
(financiar): analiză și grafic din date reale dintr-un fișier.

## Coloane

| coloană | ce conține |
|---------|-----------|
| `data` | data cheltuielii, format `YYYY-MM-DD` |
| `categorie` | una din: Marketing, Salarii, Software, Birou, Deplasări, Servicii |
| `furnizor` | numele furnizorului (fictiv) |
| `descriere` | scurtă descriere a cheltuielii |
| `suma_lei` | suma în lei (număr întreg) |

Notă pentru trainer: totalul pe categoria **Marketing** (ian–aug) este **exact 52.340 lei** — aceasta e cifra
reală care **corectează** estimarea „din memorie" de ~38.000 lei din `folder-haos-admin/Copy of Copy of raport
ciorna.md` (capcana L4 → L6). Suma se obține filtrând rândurile cu `categorie = Marketing` și adunând `suma_lei`.
