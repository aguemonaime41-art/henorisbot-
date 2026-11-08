import streamlit as st

# Base de données pour les 4 maladies
BASE_DE_DONNEES = {
    "paludisme": {"nom": "Paludisme", "description": "Maladie parasitaire transmise par les moustiques."},
    "diabete": {"nom": "Diabète", "description": "Trouble métabolique lié au taux de sucre dans le sang."},
    "hypertension": {"nom": "Hypertension Artérielle", "description": "Élévation anormale de la pression artérielle."},
    "insuffisance renale": {"nom": "Insuffisance Rénale", "description": "Diminution de la capacité des reins à filtrer les déchets."}
}

# Initialisation de l'historique pour le web
if "historique" not in st.session_state:
    st.session_state.historique = []

st.title("Bienvenue sur MediBot")
st.write("Votre assistant d'information en santé.")
st.write("Comment puis-je vous aider ?")

st.markdown("### ===== MEDIBOT =====")
choix = st.selectbox("Que souhaitez-vous faire ?", [
    "1. Informations sur les maladies",
    "2. Comprendre les symptômes",
    "3. Conseils de prévention",
    "4. Voir mon historique",
    "5. Quitter"
])

if "1." in choix:
    st.write("Sur quelle maladie souhaitez-vous des informations ? *(Note : Seules les informations sur le paludisme, le diabète, l'hypertension et l'insuffisance rénale sont disponibles).*")
    saisie = st.text_input("Votre réponse :", key="saisie_1")
    if saisie:
        st.session_state.historique.append(f"Option 1 - Recherche : {saisie}")
        saisie_clean = saisie.lower().strip()
        trouve = False
        for cle, info in BASE_DE_DONNEES.items():
            if cle in saisie_clean:
                st.success(f"**{info['nom']}** : {info['description']}")
                trouve = True
                break
        if not trouve:
            st.warning("Je ne suis pas habilité à répondre à cette question ou elle est hors de mon domaine d'action. Veuillez consulter un médecin.")

elif "2." in choix:
    st.write("Quels symptômes souhaitez-vous comprendre ou avoir d'information ? *(Attention : je n'établis pas de diagnostic).*")
    saisie = st.text_input("Votre réponse :", key="saisie_2")
    if saisie:
        st.session_state.historique.append(f"Option 2 - Symptômes : {saisie}")
        saisie_clean = saisie.lower().strip()
        trouve = any(cle in saisie_clean for cle in BASE_DE_DONNEES.keys())
        if trouve:
            st.info("Ceci est une information indicative. Attention : je n'établis pas de diagnostic. Veuillez consulter un médecin.")
        else:
            st.warning("Je ne suis pas habilité à répondre à cette question ou elle est hors de mon domaine d'action. Veuillez consulter un médecin.")

elif "3." in choix:
    st.write("Sur quoi voulez-vous des conseils de prévention ?")
    saisie = st.text_input("Votre réponse :", key="saisie_3")
    if saisie:
        st.session_state.historique.append(f"Option 3 - Prévention : {saisie}")
        saisie_clean = saisie.lower().strip()
        trouve = any(cle in saisie_clean for cle in BASE_DE_DONNEES.keys())
        if trouve:
            st.success("Conseil général : Adoptez un mode de vie sain et consultez régulièrement un professionnel de santé.")
        else:
            st.warning("Je ne suis pas habilité à répondre à cette question ou elle est hors de mon domaine d'action. Veuillez consulter un médecin.")

elif "4." in choix:
    st.write("### Votre historique :")
    if st.session_state.historique:
        for item in st.session_state.historique:
            st.write(f"- {item}")
    else:
        st.write("Votre historique est vide pour le moment.")

elif "5." in choix:
    st.write("Merci d'avoir utilisé MediBot !")
