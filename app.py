import streamlit as st
import openai  # Assurez-vous que la bibliothèque OpenAI est installée et configurée
import sys
import os
from io import StringIO
from dotenv import load_dotenv

# Charger la clé API OpenAI à partir du fichier .env situé dans le répertoire config
load_dotenv(dotenv_path='../config/.env')
# Configuration de la clé d'API OpenAI
openai.api_key = os.getenv('OPENAI_KEY')


def python_openai_api(prompt_human: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Sans explication hors code, sans commentaire, traduire le texte suivant en code Python : {prompt_human}"}
        ],
        temperature=0.4,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['message']['content']


def main():
    st.title('Ecris moi des mots doux :blossom: :snake: ')

    # Création de deux colonnes
    col1, col2 = st.columns(2)

    with col1:
        st.header('Texte humanoïde')
        human_text = st.text_area('Entrez votre texte ici :', height=200)
        translate_button = st.button('Traduire en Python')

    with col2:
        st.header('Code Python généré')
        if translate_button and human_text:
            # Vous pouvez décommenter et utiliser cette ligne si vous avez les clés API d'OpenAI configurées.
            st.session_state.python_code = python_openai_api(human_text)
        # Ceci est une ligne temporaire.
        # st.session_state.python_code = 'Votre code traduit apparaîtra ici.'

        python_code = st.text_area('Votre code traduit sera affiché ici :',
                                   value=st.session_state.get('python_code', ''), height=200)

        execute_button = st.button('Exécuter le code')

    if execute_button and python_code:
        try:
            # Rediriger la sortie standard vers un tampon
            old_stdout = sys.stdout
            new_stdout = StringIO()
            sys.stdout = new_stdout

            exec(python_code)
            # Récupérer la sortie standard capturée
            output = new_stdout.getvalue()

            # Restaurer la sortie standard d'origine
            sys.stdout = old_stdout

            # Créer une zone pour afficher le résultat
            st.subheader("Résultat de l'exécution 😊")
            st.text(output)

            st.subheader("Code saisi 😊")
            st.code(python_code, language="python")
            st.success('Le code a été exécuté avec succès.')
        except Exception as e:
            st.error(f'Une erreur est survenue : {e}')
        finally:
            st.info("Merci d'avoir utilisé cette application !")

with st.sidebar.expander("🛠️ Setting and Historics :books:", expanded=False):

    page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

if __name__ == '__main__':
    main()