# SurahDB

## FRANÇAIS

Ce projet est né d'un intérêt intellectuel envers le Coran. La base de données
rassemble des informations sur les 114 sourates du livre sacré de l'islam.

### Connexion à un serveur MySQL

Tous les scripts à la racine de ce dépôt se connectent à un serveur MySQL pour
accéder à la base de données. L'utilisateur doit leur fournir en argument un
fichier JSON configurant cette connexion. Le fichier de configuration doit
correspondre à
[ce schéma](src/database/db_config_schema.json).

Une configuration valide ressemble au modèle ci-dessous.
```
{
  "host": "host_name",
  "user": "username",
  "password": "password",
  "allow_local_infile": true
}
```

Chaque propriété de la configuration doit correspondre à un
[argument de connexion](https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html).
L'argument `allow_local_infile` est optionnel; sa valeur par défaut est vrai
(`true`). La configuration peut contenir des proprités autres que celles
indiquées ci-dessus.

### Dépendances

La commande suivante installe les dépendances de ce dépôt.
```
pip install -r requirements.txt
```

### Scripts

#### Ordre des sourates

L'ordre des sourates dans le Coran (l'ordre traditionnel) ne correspond pas à
l'ordre chronologique de leur révélation. Le drapeau `-c` fait ordonner à
certains scripts les sourates chronologiquement plutôt que traditionnellement.

#### Fichiers requis

Les exemples d'exécution supposent l'existence du fichier de configration
`db_config.json` et du fichier de données `surahs.csv` à la racine du dépôt
local de l'utilisateur. Ces fichiers n'existent pas dans le dépôt distant.

#### Création de la base de données

`load_surah_data.py` crée la base de données et charge les données des sourates
depuis un fichier CSV. L'utilisateur doit fournir le chemin de ce fichier comme
argument.

L'argument de connexion à un serveur MySQL `allow_local_infile` doit être vrai
(`true`) pour `load_surah_data.py`. Autrement, ce script sera incapable de
charger les données dpuis un fichier et il lèvera une exception.

Aide:
```
python load_surah_data.py -h
```

Exemple d'exécution:
```
python load_surah_data.py -d db_config.json -s surahs.csv
```

#### Suppression de la base de données

`delete_database.py` supprime la base de données.

Aide:
```
python delete_database.py -h
```

Exemple d'exécution:
```
python delete_database.py -d db_config.json
```

#### Écriture des données

`dump_surah_data.py` écrit les données sur les sourates dans un fichier CSV.

Aide:
```
python dump_surah_data.py -h
```

Exemple d'exécution:
```
python dump_surah_data.py -d db_config.json -s exemple.csv -c
```

#### Longueur des sourates

`plot_surah_length.py` produit un diagramme à bandes montrant la longueur des
sourates.

Aide:
```
python plot_surah_length.py -h
```

Exemple d'exécution:
```
python plot_surah_length.py -d db_config.json -c
```

#### Progression dans la lecture du Coran

`plot_progression_in_reading.py` produit un graphique montrant la progression
dans la lecture du Coran selon la dernière sourate entièrement lue.

Aide:
```
python plot_progression_in_reading.py -h
```

Exemple d'exécution:
```
python plot_progression_in_reading.py -d db_config.json -c
```

## ENGLISH

This project is the result of an intellectual interest for the Quran. The
database gathers information about the 114 surahs of islam's sacred book.

### Connection to a MySQL server

All scripts at this repository's root connect to a MySQL server to access the
database. The user must provide as an argument a JSON file that configures the
connection. The connection configuration file must match
[this schema](src/database/db_config_schema.json).

A valid configuration resembles the template below.
```
{
  "host": "host_name",
  "user": "username",
  "password": "password",
  "allow_local_infile": true
}
```

Each property must correspond to a
[connection argument](https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html).
Argument `allow_local_infile` is optional; its default value is `true`. The
configuration may contain other properties than those indicated above.

### Dependencies

The following command installs this repository's dependencies.
```
pip install -r requirements.txt
```

### Scripts

#### Surah order

The surahs' order in the Quran (the traditional order) does not match the
chronological order of their revelation. Flag `-c` makes certain scripts order
the surahs chronologically rather than traditionnally.

#### Required files

The execution examples suppose that configuration file `db_config.json` and
data file `surahs.csv` exist at the user's local repository's root. These files
do not exist in the remote repository.

#### Database creation

`load_surah_data.py` creates the database and loads the surahs' data from a CSV
file. The user must provide the path to this file as an argument.

MySQL connection argument `allow_local_infile` must be `true` for
`load_surah_data.py`. Otherwise, this script will be unable to load data from a
file and will raise an exception.

Help:
```
python load_surah_data.py -h
```

Execution example:
```
python load_surah_data.py -d db_config.json -s surahs.csv
```

#### Database deletion

`delete_database.py` does what its name says.

Help:
```
python delete_database.py -h
```

Execution example:
```
python delete_database.py -d db_config.json
```

#### Data writing

`dump_surah_data.py` writes the surahs' data in a CSV file.

Help:
```
python dump_surah_data.py -h
```

Execution example:
```
python dump_surah_data.py -d db_config.json -s example.csv -c
```

#### Surah length

`plot_surah_length.py` produces a bar diagram showing the surahs' length.

Help:
```
python plot_surah_length.py -h
```

Execution example:
```
python plot_surah_length.py -d db_config.json -c
```

#### Progression in reading the Quran

`plot_progression_in_reading.py` produces a graph showing the progression in
the Quran's reading based on the last surah entirely read.

Help:
```
python plot_progression_in_reading.py -h
```

Execution example:
```
python plot_progression_in_reading.py -d db_config.json -c
```
