# fast_api_pokemon

Bienvenue dans le projet Pokémon API ! Cette API fournit des fonctionnalités pour gérer des informations sur les Pokémon, leurs compétences, et leurs types.

## Installation

1. Clonez ce depot sur votre machine locale via commande git :
  
```bash
git clone  https://github.com/romain-pons/fast_api_pokemon.git
```

Ou en téléchargeant le zip du projet puis en le dezippant en local sur votre pc via le bouton Donwload zip

![image](https://github.com/romain-pons/fast_api_pokemon/assets/75258269/f49f9614-ae42-4286-925e-62f98f18baee)

2. Assurez vous d'avoir python d'installé sur votre machine
   
```bash
python --version
```

ou

```bash
python -V
```

Dans le cas contraire installé le via [Python donwload](https://www.python.org/downloads/)

Deplacez vous jusqu'au projet, aller a l'origine du projet : fast_api_pokemon

3. Créez un environnement de travail virtuel

```bash
python -m venv api-venv
```

Et activez le via 

```bash
api-venv\Script\Activate
```

Téléchargez les dépendances nécessaires via 

```bash
pip install -r requirements.txt
```

4. Mise en place de la base de données

Si vous avez télécharger la base de données, vous n'avez pas besoin de créer une base de données, elle est déjà créée, au contraire si vous ne l'avez pas téléchargé ou que vous voulez exécuter le script, supprimez le fichier 'pokemon.db'
Par la suite dans votre terminal

```bash
cd bdd
py pokemon_bdd.py
```

Ce qui va exécuter le script afin de créer la base de données

## Utilisation

Une fois la base de données créée, il faut aller dans le dossier api

```bash
cd ../api
```

Une fois dans ce dossier, vouz pouvez lancer l'application FsatAPI

```bash
uvicorn main:app --reload
```

L'application étant lancée, vous pouvez dès a présent consulter les différnents endpoint proposés
Consultez la documentation générée automatiquement pour plus d'informations sur les endpoints et les modèles de données : http://127.0.0.1:8000/docs#/ 
Ou les différents endpoints mis en commentaires dans le fichier main.py
