# SurahDB

## FRANÇAIS

Ce projet est né d'un intérêt intellectuel pour le Coran. Des scripts à la
racine du dépôt communiquent avec une base de données rassemblant des
informations sur les 114 sourates du livre sacré de l'islam.

### Connexion à un serveur MySQL

Tous les scripts se connectent à un serveur MySQL pour accéder à la base de
données. L'utilisateur doit leur fournir en argument le chemin d'un fichier
JSON configurant cette connexion. Le fichier de configuration doit correspondre
à [ce schéma](src/database/db_config_schema.json).

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

### Ordre des sourates

L'ordre des sourates dans le Coran (l'ordre traditionnel) ne correspond pas à
l'ordre chronologique de leur révélation. Lorsqu'on extrait les données des
sourates, on peut les ordonner traditionnellement ou chronologiquement.

### Propriétés des sourates

`id`: numéro dans l'ordre traditionnel et identifiant.

`chronology`: position dans l'ordre chronologique.

`titlefr`: titre en français.

`titleen`: titre en anglais.

`period`: période mecquoise (0) ou médinoise (1).

`nbverses`: nombre de versets.

### Fichiers de données

Certains scripts utilisent des fichiers CSV contenant les données des sourates.
Des points-virgules (`;`) séparent les valeurs. Tout fichier de données doit
avoir les colonnes suivantes, qui correspondent aux propriétés des sourates.

```
id;chronology;titlefr;titleen;period;nbverses
```

Le fichier de données [surahs.csv](surahs.csv), à la racine du dépôt, permet
d'initialiser la base de données.

### Dépendances

La commande suivante installe les dépendances de ce dépôt.
```
pip install -r requirements.txt
```

### Scripts

Les exemples d'exécution supposent l'existence de `db_config.json`, un fichier
de configration pour la connexion à la base de données, à la racine du dépôt
local de l'utilisateur. Ce fichier n'existe pas dans le dépôt distant;
l'utilisateur doit le créer.

Le drapeau `-c` fait ordonner à certains scripts les sourates chronologiquement
plutôt que traditionnellement.

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
python plot_surah_length.py -d db_config.json -l fr -c
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
python plot_progression_in_reading.py -d db_config.json -l fr -c
```

## ENGLISH

This project is the result of an intellectual interest in the Quran. Scripts at
the repository's root communicate with a database containing information about
the 114 surahs of Islam's sacred book.

### Connection to a MySQL server

All scripts connect to a MySQL server to access the database. The user must
provide as an argument the path to a JSON file that configures the connection.
The connection configuration file must match
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

### Order of the surahs

The surahs' order in the Quran (the traditional order) does not match the
chronological order of their revelation. When the surahs' data is extracted, it
can be ordered traditonnally or chronologically.

### Properties of the surahs

`id`: number in the traditional order and identifier.

`chronology`: position in the chronological order.

`titlefr`: title in French.

`titleen`: title in English.

`period`: Meccan (0) or Medinan (1).

`nbverses`: number of verses.

### Data files

Certain sripts use CSV files that store data about the surahs. Semicolons (`;`)
separate the values. Any data file must have the following columns, which
correspond to the surahs' properties.

```
id;chronology;titlefr;titleen;period;nbverses
```

Data file [surahs.csv](surahs.csv), at the repository's root, allows to
initialize the database.

### Dependencies

The following command installs this repository's dependencies.
```
pip install -r requirements.txt
```

### Scripts

The execution examples suppose that `db_config.json`, a configuration file for
the connection to the database, exists at the user's local repository's root.
This file does not exist in the remote repository; the user must create it.

Flag `-c` makes certain scripts order the surahs chronologically rather than
traditionnally.

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
python plot_surah_length.py -d db_config.json -l en -c
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
python plot_progression_in_reading.py -d db_config.json -l en -c
```
