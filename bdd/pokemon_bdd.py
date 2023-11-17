import sqlite3

# Connexion à la base de données (si elle n'existe pas, elle sera créée)
conn = sqlite3.connect('pokemon.db')

# Création d'un objet curseur pour exécuter les requêtes SQL
cursor = conn.cursor()

# Création de la table 'type'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS type (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL
    )
''')

# Création de la table 'competence'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS competence (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        description TEXT,
        puissance INTEGER,
        precision INTEGER,
        pp_max INTEGER,
        type_id INTEGER,
        FOREIGN KEY (type_id) REFERENCES type (id)
    )
''')

# Création de la table 'pokemon'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        taille REAL,
        poids REAL,
        statistique REAL,
        image_url TEXT,
        type_id INTEGER,
        FOREIGN KEY (type_id) REFERENCES type (id)
    )
''')

# Création de la table de jointure 'pokemon_competence'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pokemon_competence (
        id INTEGER PRIMARY KEY,
        pokemon_id INTEGER,
        competence_id INTEGER,
        FOREIGN KEY (pokemon_id) REFERENCES pokemon (id),
        FOREIGN KEY (competence_id) REFERENCES competence (id)
    )
''')


# Ajout des types 
cursor.execute("INSERT INTO type (nom) VALUES ('Feu')")
cursor.execute("INSERT INTO type (nom) VALUES ('Eau')")
cursor.execute("INSERT INTO type (nom) VALUES ('Normal')")
cursor.execute("INSERT INTO type (nom) VALUES ('Plante')")
cursor.execute("INSERT INTO type (nom) VALUES ('Poison')")
cursor.execute("INSERT INTO type (nom) VALUES ('Vol')")
cursor.execute("INSERT INTO type (nom) VALUES ('Electricite')")

# Ajout de competences
cursor.execute("INSERT INTO competence (nom, description, puissance, precision, pp_max, type_id) VALUES ('Vampigraine', 'Attaque qui plante des graines vampiriques', 50, 100, 10, 5)")
cursor.execute("INSERT INTO competence (nom, description, puissance, precision, pp_max, type_id) VALUES ('Fouet lianes', 'Attaque avec des lianes', 45, 95, 15, 4)")
cursor.execute("INSERT INTO competence (nom, description, puissance, precision, pp_max, type_id) VALUES ('Lance-flammes', 'Attaque avec des flammes intenses', 90, 85, 10, 1)")
cursor.execute("INSERT INTO competence (nom, description, puissance, precision, pp_max, type_id) VALUES ('Pistolet à O', 'Attaque eau en forme de pistolet', 70, 95, 15, 2)")
cursor.execute("INSERT INTO competence (nom, description, puissance, precision, pp_max, type_id) VALUES ('Carapace dure', 'Utilise sa carapace pour se protéger', 0, 100, 20, 2)")
cursor.execute("INSERT INTO competence (nom, description, puissance, precision, pp_max, type_id) VALUES ('Tornade', 'Crée une tornade pour attaquer', 60, 90, 15, 6)")
cursor.execute("INSERT INTO competence (nom, description, puissance, precision, pp_max, type_id) VALUES ('Picpic', 'Attaque avec son bec pointu', 40, 100, 20, 'Normal')")
cursor.execute("INSERT INTO competence (nom, description, puissance, precision, pp_max, type_id) VALUES ('Charge', 'Charge l ennemi pour l attaquer', 50, 100, 15, 3)")
cursor.execute("INSERT INTO competence (nom, description, puissance, precision, pp_max, type_id) VALUES ('Morsure', 'Attaque en mordant l ennemi', 40, 95, 20, 3)")
cursor.execute("INSERT INTO competence (nom, description, puissance, precision, pp_max, type_id) VALUES ('Croc poison', 'Attaque avec des crocs empoisonnés', 55, 90, 15, 5)")
cursor.execute("INSERT INTO competence (nom, description, puissance, precision, pp_max, type_id) VALUES ('Éclair', 'Une attaque électrique rapide', 70, 90, 15, 7)")
cursor.execute("INSERT INTO competence (nom, description, puissance, precision, pp_max, type_id) VALUES ('Queue de fer', 'Attaque avec la queue de fer', 75, 95, 10, 7)")

# Ajout de pokemons
cursor.execute("INSERT INTO Pokemon (nom, taille, poids, statistique, image_url, type_id) VALUES ('Bulbizarre', 0.7, 6.9, 318, 'https://img.pokemondb.net/artwork/avif/bulbasaur.avif', 4)")
cursor.execute("INSERT INTO Pokemon (nom, taille, poids, statistique, image_url, type_id) VALUES ('Salameche', 0.6, 8.5, 309, 'https://img.pokemondb.net/artwork/avif/charmander.avif', 1)")
cursor.execute("INSERT INTO Pokemon (nom, taille, poids, statistique, image_url, type_id) VALUES ('Carapuce', 0.5, 9, 314, 'https://img.pokemondb.net/artwork/avif/squirtle.avif', 2)")
cursor.execute("INSERT INTO Pokemon (nom, taille, poids, statistique, image_url, type_id) VALUES ('Roucool', 0.3, 1.8, 251, 'https://img.pokemondb.net/artwork/avif/pidgey.avif', 6)")
cursor.execute("INSERT INTO Pokemon (nom, taille, poids, statistique, image_url, type_id) VALUES ('Rattata', 0.3, 3.5, 253, 'https://img.pokemondb.net/artwork/avif/rattata.avif', 3)")
cursor.execute("INSERT INTO Pokemon (nom, taille, poids, statistique, image_url, type_id) VALUES ('Abo', 2, 6.9, 288, 'https://img.pokemondb.net/artwork/avif/ekans.avif', 5)")
cursor.execute("INSERT INTO Pokemon (nom, taille, poids, statistique, image_url, type_id) VALUES ('Pikachu', 0.4, 6, 320, 'https://img.pokemondb.net/artwork/avif/pikachu.avif', 7)")


# Ajout dans la table de jointure
cursor.execute("INSERT INTO pokemon_competence (pokemon_id, competence_id) VALUES (1, 1)")
cursor.execute("INSERT INTO pokemon_competence (pokemon_id, competence_id) VALUES (1, 2)")
cursor.execute("INSERT INTO pokemon_competence (pokemon_id, competence_id) VALUES (2, 3)")
cursor.execute("INSERT INTO pokemon_competence (pokemon_id, competence_id) VALUES (3, 4)")
cursor.execute("INSERT INTO pokemon_competence (pokemon_id, competence_id) VALUES (3, 5)")
cursor.execute("INSERT INTO pokemon_competence (pokemon_id, competence_id) VALUES (4, 6)")
cursor.execute("INSERT INTO pokemon_competence (pokemon_id, competence_id) VALUES (4, 7)")
cursor.execute("INSERT INTO pokemon_competence (pokemon_id, competence_id) VALUES (5, 8)")
cursor.execute("INSERT INTO pokemon_competence (pokemon_id, competence_id) VALUES (5, 9)")
cursor.execute("INSERT INTO pokemon_competence (pokemon_id, competence_id) VALUES (6, 10)")
cursor.execute("INSERT INTO pokemon_competence (pokemon_id, competence_id) VALUES (7, 11)")
cursor.execute("INSERT INTO pokemon_competence (pokemon_id, competence_id) VALUES (7, 12)")


cursor.execute("SELECT * FROM pokemon")
rows = cursor.fetchall()

# Affichage des pokemons
print('Pokemon')
for row in rows:
    print(row)


cursor.execute("SELECT * FROM type")
rows = cursor.fetchall()

# Affichage des types
print('\nType')
for row in rows:
    print(row)

cursor.execute("SELECT * FROM competence")
rows = cursor.fetchall()

# Affichage des competences
print('\nCompetence')
for row in rows:
    print(row)


cursor.execute("SELECT * FROM Pokemon_Competence")
rows = cursor.fetchall()

# Affichage des pokemon/competences
print('\nPokemon_Competence')
for row in rows:
    print(row)


# Commit des changements et fermeture de la connexion
conn.commit()
conn.close()