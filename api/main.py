import sqlite3
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Pokemon(BaseModel):
    id: int
    nom: str
    taille: float
    poids: float
    statistique: float
    image_url: str
    type_id: int

class PokemonCreateUpdate(BaseModel):
    nom: str
    taille: float
    poids: float
    statistique: float
    image_url: str
    type_id: int

class Type(BaseModel):
    id: int
    nom: str

class TypeCreateUpdate(BaseModel):
    nom: str

class Competence(BaseModel):
    id: int
    nom: str
    description: str
    puissance: int
    precision: int
    pp_max: int
    type_id: int

class CompetenceCreateUpdate(BaseModel):
    nom: str
    description: str
    puissance: int
    precision: int
    pp_max: int
    type_id: int



# Endpoint pour récupérer la liste de tous les pokémons
@app.get('/api/pokemons', response_model=dict)
def get_all_pokemons():
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Sélection de tous les pokémons
    cursor.execute("SELECT * FROM pokemon")
    pokemons = cursor.fetchall()

    conn.close()

    # Conversion des résultats en format JSON
    pokemon_list = []
    for pokemon in pokemons:
        pokemon_dict = {
            'id': pokemon[0],
            'nom': pokemon[1],
            'taille': pokemon[2],
            'poids': pokemon[3],
            'statistique': pokemon[4],
            'image_url': pokemon[5],
            'type_id': pokemon[6]
        }
        pokemon_list.append(pokemon_dict)

    return JSONResponse(content={'pokemons': pokemon_list})




# Endpoint pour récupérer les détails d'un Pokémon par ID
@app.get('/api/pokemons/{pokemon_id}', response_model=Pokemon)
def get_pokemon_by_id(pokemon_id: int):
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Sélection du Pokémon par ID
    cursor.execute("SELECT * FROM pokemon WHERE id=?", (pokemon_id,))
    pokemon = cursor.fetchone()

    conn.close()

    if not pokemon:
        raise HTTPException(status_code=404, detail='Pokemon non trouvé')


    pokemon = {
            'id': pokemon[0],
            'nom': pokemon[1],
            'taille': pokemon[2],
            'poids': pokemon[3],
            'statistique': pokemon[4],
            'image_url': pokemon[5],
            'type_id': pokemon[6]
        }
    return JSONResponse(content={'pokemon': pokemon})




# Endpoint pour récupérer la liste de tous les types
@app.get('/api/types', response_model=list[Type])
def get_all_types():
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Sélection de tous les types
    cursor.execute("SELECT * FROM type")
    types = cursor.fetchall()

    conn.close()

    # Conversion des résultats en format JSON
    type_list = []
    for type_result in types:
        type_dict = {
            'id': type_result[0],
            'nom': type_result[1]
        }
        type_list.append(type_dict)

    return type_list




# Endpoint pour récupérer les détails d'un Type par ID
@app.get('/api/types/{type_id}', response_model=Type)
def get_type_by_id(type_id: int):
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Sélection du Type par ID
    cursor.execute("SELECT * FROM type WHERE id=?", (type_id,))
    type_result = cursor.fetchone()

    conn.close()

    if not type_result:
        raise HTTPException(status_code=404, detail='Type non trouvé')

    return Type(**{
        'id': type_result[0],
        'nom': type_result[1]
    })




# Endpoint pour récupérer la liste de toutes les compétences
@app.get('/api/competences', response_model=list[Competence])
def get_all_abilities():
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Sélection de toutes les compétences
    cursor.execute("SELECT * FROM competence")
    competences = cursor.fetchall()

    conn.close()

    # Conversion des résultats en format JSON
    competence_list = []
    for competence_result in competences:
        competence_dict = {
            'id': competence_result[0],
            'nom': competence_result[1],
            'description': competence_result[2],
            'puissance': competence_result[3],
            'precision': competence_result[4],
            'pp_max': competence_result[5],
            'type_id': competence_result[6]
        }
        competence_list.append(competence_dict)

    return JSONResponse(content={'competences': competence_list})




# Endpoint pour récupérer les détails d'une Compétence par ID
@app.get('/api/competences/{ability_id}', response_model=Competence)
def get_ability_by_id(ability_id: int):
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Sélection de la Compétence par ID
    cursor.execute("SELECT * FROM competence WHERE id=?", (ability_id,))
    ability_result = cursor.fetchone()

    conn.close()

    if not ability_result:
        raise HTTPException(status_code=404, detail='Compétence non trouvée')

    return Competence(**{
        'id': ability_result[0],
        'nom': ability_result[1],
        'description': ability_result[2],
        'puissance': ability_result[3],
        'precision': ability_result[4],
        'pp_max': ability_result[5],
        'type_id': ability_result[6]
    })



# Endpoint pour ajouter un nouveau Pokémon
@app.post('/api/pokemons', response_model=Pokemon)
def add_pokemon(pokemon: PokemonCreateUpdate):
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Insertion du nouveau Pokémon dans la base de données
    cursor.execute("""
        INSERT INTO pokemon (nom, taille, poids, statistique, image_url, type_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        pokemon.nom,
        pokemon.taille,
        pokemon.poids,
        pokemon.statistique,
        pokemon.image_url,
        pokemon.type_id
    ))

    new_pokemon_id = cursor.lastrowid

    conn.commit()
    conn.close()

    # Retourner les détails du nouveau Pokémon
    return {**pokemon.dict(), 'id': new_pokemon_id}



# Endpoint pour ajouter un nouveau Type
@app.post('/api/types', response_model=Type)
def add_type(type_create: TypeCreateUpdate):
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Insertion du nouveau Type dans la base de données
    cursor.execute("INSERT INTO type (nom) VALUES (?)", (type_create.nom,))

    conn.commit()

    # Obtenez l'ID auto-incrémenté du nouveau Type
    new_type_id = cursor.lastrowid

    # Sélectionnez le Type avec l'ID généré pour le renvoyer en réponse
    cursor.execute("SELECT * FROM type WHERE id=?", (new_type_id,))
    new_type = cursor.fetchone()

    conn.close()

    return Type(**{
        'id': new_type[0],
        'nom': new_type[1],
    })




# Endpoint pour modifier un Pokémon par ID
@app.put('/api/pokemons/{pokemon_id}', response_model=Pokemon)
def update_pokemon(pokemon_id: int, pokemon_update: PokemonCreateUpdate):
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()


    # Vérifier si le Pokémon existe
    cursor.execute("SELECT * FROM pokemon WHERE id=?", (pokemon_id,))
    existing_pokemon = cursor.fetchone()

    if not existing_pokemon:
        conn.close()
        raise HTTPException(status_code=404, detail='Pokémon non trouvé')

    # Mettre à jour les détails du Pokémon dans la base de données
    cursor.execute("""
        UPDATE pokemon
        SET nom=?, taille=?, poids=?, statistique=?, image_url=?, type_id=?
        WHERE id=?
    """, (
        pokemon_update.nom,
        pokemon_update.taille,
        pokemon_update.poids,
        pokemon_update.statistique,
        pokemon_update.image_url,
        pokemon_update.type_id,
        pokemon_id
    ))

    conn.commit()

    # Récupérer les détails mis à jour du Pokémon
    cursor.execute("SELECT * FROM pokemon WHERE id=?", (pokemon_id,))
    updated_pokemon = cursor.fetchone()

    conn.close()

    return Pokemon(**{
        'id': updated_pokemon[0],
        'nom': updated_pokemon[1],
        'taille': updated_pokemon[2],
        'poids': updated_pokemon[3],
        'statistique': updated_pokemon[4],
        'image_url': updated_pokemon[5],
        'type_id': updated_pokemon[6]
    })




# Endpoint pour ajouter une nouvelle Compétence
@app.post('/api/competences', response_model=Competence)
def add_ability(ability_create: CompetenceCreateUpdate):
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Insertion de la nouvelle Compétence dans la base de données
    cursor.execute("""
        INSERT INTO competence (nom, description, puissance, precision, pp_max, type_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        ability_create.nom,
        ability_create.description,
        ability_create.puissance,
        ability_create.precision,
        ability_create.pp_max,
        ability_create.type_id
    ))

    conn.commit()

    # Obtenez l'ID auto-incrémenté de la nouvelle Compétence
    new_ability_id = cursor.lastrowid

    # Sélectionnez la Compétence avec l'ID généré pour la renvoyer en réponse
    cursor.execute("SELECT * FROM competence WHERE id=?", (new_ability_id,))
    new_ability = cursor.fetchone()

    conn.close()

    return Competence(**{
        'id': new_ability[0],
        'nom': new_ability[1],
        'description': new_ability[2],
        'puissance': new_ability[3],
        'precision': new_ability[4],
        'pp_max': new_ability[5],
        'type_id': new_ability[6]
    })



# Endpoint pour modifier une compétence par ID
@app.put('/api/competences/{ability_id}', response_model=Competence)
def update_ability(ability_id: int, ability_update: CompetenceCreateUpdate):
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Vérifier si la compétence existe
    cursor.execute("SELECT * FROM competence WHERE id=?", (ability_id,))
    existing_ability = cursor.fetchone()

    if not existing_ability:
        conn.close()
        raise HTTPException(status_code=404, detail='Compétence non trouvée')

    # Mettre à jour les détails de la compétence dans la base de données
    cursor.execute("""
        UPDATE competence
        SET nom=?, description=?, puissance=?, precision=?, pp_max=?, type_id=?
        WHERE id=?
    """, (
        ability_update.nom,
        ability_update.description,
        ability_update.puissance,
        ability_update.precision,
        ability_update.pp_max,
        ability_update.type_id,
        ability_id
    ))

    conn.commit()

    # Récupérer les détails mis à jour de la compétence
    cursor.execute("SELECT * FROM competence WHERE id=?", (ability_id,))
    updated_ability = cursor.fetchone()

    conn.close()

    return Competence(**{
        'id': updated_ability[0],
        'nom': updated_ability[1],
        'description': updated_ability[2],
        'puissance': updated_ability[3],
        'precision': updated_ability[4],
        'pp_max': updated_ability[5],
        'type_id': updated_ability[6]
    })




# Endpoint pour modifier un type par ID
@app.put('/api/types/{type_id}', response_model=Type)
def update_type(type_id: int, type_update: TypeCreateUpdate):
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Vérifier si le type existe
    cursor.execute("SELECT * FROM type WHERE id=?", (type_id,))
    existing_type = cursor.fetchone()

    if not existing_type:
        conn.close()
        raise HTTPException(status_code=404, detail='Type non trouvé')

    # Mettre à jour les détails du type dans la base de données
    cursor.execute("""
        UPDATE type
        SET nom=?
        WHERE id=?
    """, (
        type_update.nom,
        type_id
    ))

    conn.commit()

    # Récupérer les détails mis à jour du type
    cursor.execute("SELECT * FROM type WHERE id=?", (type_id,))
    updated_type = cursor.fetchone()

    conn.close()

    return Type(**{
        'id': updated_type[0],
        'nom': updated_type[1],
    })



# Endpoint pour supprimer un Pokémon par ID
@app.delete('/api/pokemons/{pokemon_id}', response_model=dict)
def delete_pokemon(pokemon_id: int):
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Vérifier si le Pokémon existe
    cursor.execute("SELECT * FROM pokemon WHERE id=?", (pokemon_id,))
    existing_pokemon = cursor.fetchone()

    if not existing_pokemon:
        conn.close()
        raise HTTPException(status_code=404, detail='Pokémon non trouvé')

    # Supprimer le Pokémon de la base de données
    cursor.execute("DELETE FROM pokemon WHERE id=?", (pokemon_id,))
    conn.commit()

    conn.close()

    return {"message": "Pokémon supprimé avec succès"}




# Endpoint pour supprimer une compétence par ID
@app.delete('/api/competences/{ability_id}', response_model=dict)
def delete_ability(ability_id: int):
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Vérifier si la compétence existe
    cursor.execute("SELECT * FROM competence WHERE id=?", (ability_id,))
    existing_ability = cursor.fetchone()

    if not existing_ability:
        conn.close()
        raise HTTPException(status_code=404, detail='Compétence non trouvée')

    # Supprimer la compétence de la base de données
    cursor.execute("DELETE FROM competence WHERE id=?", (ability_id,))
    conn.commit()

    conn.close()

    return {"message": "Compétence supprimée avec succès"}



# Endpoint pour supprimer un type par ID
@app.delete('/api/types/{type_id}', response_model=dict)
def delete_type(type_id: int):
    conn = sqlite3.connect('../bdd/pokemon.db')
    cursor = conn.cursor()

    # Vérifier si le type existe
    cursor.execute("SELECT * FROM type WHERE id=?", (type_id,))
    existing_type = cursor.fetchone()

    if not existing_type:
        conn.close()
        raise HTTPException(status_code=404, detail='Type non trouvé')

    # Supprimer le type de la base de données
    cursor.execute("DELETE FROM type WHERE id=?", (type_id,))
    conn.commit()

    conn.close()

    return {"message": "Type supprimé avec succès"}