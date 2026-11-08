import streamlit as st

BASE_DE_DONNEES = {
    "paludisme": {
        "nom": "Paludisme",
        "description": "Maladie parasitaire transmise par les moustiques Anophèles.",
        "symptomes": "Fièvre élevée, frissons, maux de tête, fatigue, courbatures.",
        "prevention": "Utiliser des moustiquaires impregnées, prendre un traitement préventif si besoin."
    },
    "diabete": {
        "nom": "Diabète",
        "description": "Trouble métabolique caractérisé par un excès de sucre dans le sang (hyperglycémie).",
        "symptomes": "Soif intense, envies fréquentes d'uriner, fatigue, perte de poids inexpliquée.",
        "prevention": "Avoir une alimentation équilibrée, pratiquer une activité physique régulière, éviter les excès de sucre."
    },
    "hypertension": {
        "nom": "Hypertension Artérielle",
        "description": "Élévation chronique de la pression du sang dans les artères.",
        "symptomes": "Maux de tête matinaux, vertiges, palpitations, fatigue.",
        "prevention": "Réduire la consommation de sel, faire du sport, limiter le stress et l'alcool."
    },
    "insuffisance renale": {
        "nom": "Insuffisance Rénale",
        "description": "Incapacité progressive des reins à filtrer correctement les déchets du sang.",
        "symptomes": "Fatigue, gonflements des jambes ou des paupières, mictions modifiées.",
        "prevention": "Boire suffisamment d'eau, surveiller sa tension et sa glycémie, éviter l'abus de certains médicaments."
    }
}

if "historique" not in st.session_state:
    st.session_state.historique = []

st.title("Bienvenue sur Hénorisbot")
st.write("Votre assistant d'information en santé.")

st.markdown("### ===== HÉNORISBOT =====")
st.write("1. Informations sur les maladies")
st.write("2. Comprendre les symptômes")
st.write("3. Conseils de prévention")
st.write("4. Quitter")

choix = st.text_input("Votre choix (tapez 1, 2, 3 ou 4) :")

if choix == "1":
    st.write("Sur quelle maladie souhaitez-vous des informations ? (Paludisme, Diabète, Hypertension, Insuffisance rénale)")
    saisie = st.text_input("Votre réponse :", key="s_1")
    if saisie:
        st.session_state.historique.append(f"Choix 1 - Info : {saisie}")
        sc = saisie.lower().strip()
        trouve = False
        for k, v in BASE_DE_DONNEES.items():
            if k in sc:
                st.success(f"**{v['nom']}** : {v['description']}")
                trouve = True
                break
        if not trouve:
            st.warning("Je ne suis pas habilité à répondre à cette question ou elle est hors de mon domaine. Veuillez consulter un médecin.")

elif choix == "2":
    st.write("Sur quel(s) symptôme(s) souhaitez-vous avoir des informations ? (Paludisme, Diabète, Hypertension, Insuffisance rénale)")
    saisie = st.text_input("Votre réponse :", key="s_2")
    if saisie:
        st.session_state.historique.append(f"Choix 2 - Symptômes : {saisie}")
        sc = saisie.lower().strip()
        trouve = False
        for k, v in BASE_DE_DONNEES.items():
            if k in sc:
                st.info(f"**Symptômes ({v['nom']})** : {v['symptomres'] if 'symptomres' in v else v['symptomes']}\n\n*Attention : Je n'établis pas de diagnostic. Veuillez consulter un médecin.*")
                trouve = True
                break
        if not trouve:
            st.warning("Je ne suis pas habilité à répondre à cette question ou elle est hors de mon domaine. Veuillez consulter un médecin.")

elif choix == "3":
    st.write("Sur quoi souhaitez-vous avoir des conseils de prévention ? (Paludisme, Diabète, Hypertension, Insuffisance rénale)")
    saisie = st.text_input("Votre réponse :", key="s_3")
    if saisie:
        st.session_state.historique.append(f"Choix 3 - Prévention : {saisie}")
        sc = saisie.lower().strip()
        trouve = False
        for k, v in BASE_DE_DONNEES.items():
            if k in sc:
                st.success(f"**Prévention ({v['nom']})** : {v['prevention']}")
                trouve = True
                break
        if not trouve:
            st.warning("Je ne suis pas habilité à répondre à cette question ou elle est hors de mon domaine. Veuillez consulter un médecin.")

elif choix == "4":
    st.write("Merci d'avoir utilisé Hénorisbot !")

elif choix != "":
    st.write("Merci d'avoir utilisé Hénorisbot")

if st.session_state.historique:
    st.markdown("---")
    st.write("**Votre historique de navigation :**")
    for h in st.session_state.historique:
        st.write(- f"{h}")
