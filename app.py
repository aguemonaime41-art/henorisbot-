import streamlit as st

# Base de données pour les 4 maladies demandées
BASE_DE_DONNEES = {
    "paludisme": {"nom": "Paludisme", "description": "Maladie parasitaire transmise par les moustiques."},
    "diabete": {"nom": "Diabète", "description": "Trouble métabolique lié au taux de sucre dans le sang."},
    "hypertension": {"nom": "Hypertension Artérielle", "description": "Élévation anormale de la pression artérielle."},
    "insuffisance renale": {"nom": "Insuffisance Rénale", "description": "Diminution de la capacité des reins à filtrer les déchets."}
}

st.title("Bienvenue sur MediBot")
st.write("Votre assistant d'information en santé.")
st.write("Comment puis-je vous aider ?")

st.markdown("### ===== MEDIBOT =====")
choix = st.selectbox("Que souhaitez-vous faire ?", [
    "1. Informations sur les maladies",
    "2. Comprendre les symptômes",
    "3. Conseils de prévention",
    "4. Quitter"
])

if "1." in choix:
    st.write("Sur quelle maladie souhaitez-vous des informations ? *(Note : Seules les informations sur le paludisme, le diabète, l'hypertension et l'insuffisance rénale sont disponibles).*")
    saisie = st.text_input("Votre réponse :")
    if saisie:
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
    st.write("Quels symptômes souhaitez-vous comprendre ou avoir d'information ? *(Attention : je n'établis pas de diagnostic, et je me limite à nos 4 maladies de référence).*")
    saisie = st.text_input("Votre réponse :")
    if saisie:
        saisie_clean = saisie.lower().strip()
        trouve = any(cle in saisie_clean for cle in BASE_DE_DONNEES.keys())
        if trouve:
            st.info("Ceci est une information indicative. Attention : je n'établis pas de diagnostic. Veuillez consulter un médecin.")
        else:
            st.warning("Je ne suis pas habilité à répondre à cette question ou elle est hors de mon domaine d'action. Veuillez consulter un médecin.")

elif "3." in choix:
    st.write("Sur quoi voulez-vous des conseils de prévention ? *(Rappel : mes conseils se concentrent exclusivement sur ces quelques pathologies).*")
    saisie = st.text_input("Votre réponse :")
    if saisie:
        saisie_clean = saisie.lower().strip()
        trouve = any(cle in saisie_clean for cle in BASE_DE_DONNEES.keys())
        if trouve:
            st.success("Conseil général : Adoptez un mode de vie sain et consultez régulièrement un professionnel de santé.")
        else:
            st.warning("Je ne suis pas habilité à répondre à cette question ou elle est hors de mon domaine d'action. Veuillez consulter un médecin.")

elif "4." in choix:
    st.write("Merci d'avoir utilisé Hénorisbot")
