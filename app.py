import streamlit as st

# Base de données pour les maladies
BASE_DE_DONNEES = {
    "paludisme": {"nom": "Paludisme", "description": "Maladie parasitaire transmise par les moustiques."},
    "diabete": {"nom": "Diabète", "description": "Trouble métabolique lié au taux de sucre dans le sang."},
    "hypertension": {"nom": "Hypertension Artérielle", "description": "Élévation anormale de la pression artérielle."},
    "insuffisance renale": {"nom": "Insuffisance Rénale", "description": "Diminution de la capacité des reins à filtrer les déchets."}
}

# Initialisation de l'historique
if "historique" not in st.session_state:
    st.session_state.historique = []

st.title("Bienvenue sur Hénorisbot")
st.write("Votre assistant d'information en santé.")

# Affichage du menu principal sous forme de texte
st.markdown("### ===== HÉNORISBOT =====")
st.write("1. Informations sur les maladies")
st.write("2. Comprendre les symptômes")
st.write("3. Conseils de prévention")
st.write("4. Quitter")

# L'utilisateur tape son choix (1, 2, 3 ou 4)
choix = st.text_input("Votre choix (tapez 1, 2, 3 ou 4) :", key="menu_choix")

if choix == "1":
    st.write("Sur quelle maladie souhaitez-vous des informations ? *(Paludisme, Diabète, Hypertension, Insuffisance rénale)*")
    saisie = st.text_input("Votre réponse :", key="saisie_1")
    if saisie:
        st.session_state.historique.append(f"Choix 1 - Recherche : {saisie}")
        saisie_clean = saisie.lower().strip()
        trouve = False
        for cle, info in BASE_DE_DONNEES.items():
            if cle in saisie_clean:
                st.success(f"**{info['nom']}** : {info['description']}")
                trouve = True
                break
        if not trouve:
            st.warning("Je ne suis pas habilité à répondre à cette question. Veuillez consulter un médecin.")

elif choix == "2":
    st.write("Sur quels symptômes souhaitez-vous avoir des informations ou comprendre ?")
    saisie = st.text_input("Votre réponse :", key="saisie_2")
    if saisie:
        st.session_state.historique.append(f"Choix 2 - Symptômes : {saisie}")
        saisie_clean = saisie.lower().strip()
        trouve = any(cle in saisie_clean for cle in BASE_DE_DONNEES.keys())
        if trouve:
            st.info("Ceci est une information indicative. Attention : je n'établis pas de diagnostic. Veuillez consulter un médecin.")
        else:
            st.warning("Je ne suis pas habilité à répondre à cette question. Veuillez consulter un médecin.")

elif choix == "3":
    st.write("Sur quoi souhaitez-vous avoir des conseils de prévention ?")
    saisie = st.text_input("Votre réponse :", key="saisie_3")
    if saisie:
        st.session_state.historique.append(f"Choix 3 - Prévention : {saisie}")
        saisie_clean = saisie.lower().strip()
        trouve = any(cle in saisie_clean for cle in BASE_DE_DONNEES.keys())
        if trouve:
            st.success("Conseil général : Adoptez un mode de vie sain et consultez régulièrement un professionnel de santé.")
        else:
            st.warning("Je ne suis pas habilité à répondre à cette question. Veuillez consulter un médecin.")

elif choix == "4":
    st.write("Merci d'avoir utilisé Hénorisbot !")

elif choix != "":
    st.write("Merci d'avoir utilisé Hénorisbot")

# Affichage de l'historique en bas pour le suivi
if st.session_state.historique:
    st.markdown("---")
    st.write("**Votre historique de navigation :**")
    for item in st.session_state.historique:
        st.write(f"- {item}")
