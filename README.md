
# Lang2Code

## Description
Lang2Code est une application conçue pour transformer du langage humain en code Python. L'application utilise l'API d'OpenAI pour générer du code à partir de prompts en langage naturel et offre une interface utilisateur intuitive pour interagir avec la fonctionnalité de génération de code. L'application est destinée à être utilisée localement.

## Installation

### Création et activation de l'environnement virtuel

- **Sous Windows**
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```

- **Sous Linux**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### Installation des dépendances
Avec l'environnement virtuel activé, naviguez vers le répertoire de l'application et installez les dépendances en utilisant le fichier `requirements.txt` :
   ```bash
   pip install -r requirements.txt
   ```

### Configuration de l'API OpenAI
Placez votre clé API d'OpenAI dans le fichier `config/.env`.

## Utilisation
1. Naviguez vers le répertoire de l'application via la ligne de commande ou un terminal.
2. Exécutez l'application en utilisant la commande `streamlit run app.py`.
3. L'application devrait être accessible via un navigateur web à une adresse locale telle que `localhost:8501`.
