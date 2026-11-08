import streamlit as st
import unicodedata

BASE_DE_DONNEES = {
    "paludisme": {
        "nom": "Paludisme",
        "description": "Maladie infectieuse grave due à un parasite (Plasmodium), transmise par la piqûre de moustiques femelles Anophèles infectés. Elle est particulièrement fréquente en zone tropicale.",
        "symptomes": "Fièvre élevée et soudaine, frissons intenses, maux de tête violents, courbatures, fatigue intense, nausées et vomissements.",
        "prevention": "Utilisation systématique de moustiquaires imprégnées d'insecticide, prise d'un traitement préventif si conseillé, et élimination des gîtes larvaires (eaux stagnantes) autour du domicile."
    },
    "diabete": {
        "nom": "Diabète",
        "description": "Maladie chronique caractérisée par un taux excessif de sucre dans le sang (hyperglycémie), liée à une mauvaise production ou utilisation de l'insuline par l'organisme.",
        "symptomes": "Soif excessive et inhabituelle, envies très fréquentes d'uriner, fatigue chronique, perte de poids inexpliquée malgré un appétit normal, et parfois vision trouble.",
        "prevention": "Adoption d'une alimentation saine et équilibrée pauvre en sucres rapides, pratique régulière d'une activité physique, maintien d'un poids stable et contrôles médicaux réguliers."
    },
    "hypertension": {
        "nom": "Hypertension Artérielle",
        "description": "Pathologie chronique caractérisée par une pression anormalement élevée du sang dans les artères, ce qui fatigue le cœur et endommage les vaisseaux sanguins.",
        "symptomes": "Maux de tête fréquents (surtout au réveil), vertiges, bourdonnements d'oreilles, palpitations cardiaques, fatigue inhabituelle ou essoufflement à l'effort.",
        "prevention": "Réduction de la consommation de sel, limitation de l'alcool et du tabac, gestion efficace du stress, pratique d'un sport régulier et alimentation riche en fruits et légumes."
    },
    "insuffisance renale": {
        "nom": "Insuffisance Rénale",
        "description": "Altération progressive et durable de la fonction des reins, qui perdent peu à peu leur capacité à filtrer les déchets du sang et à réguler l'équilibre du corps.",
        "symptomes": "Fatigue persistante liée à l'anémie, gonflements (œdèmes) au niveau des jambes, des chevilles ou des paupières, modifications des urines, et démangeaisons cutanées.",
        "prevention": "Boire de l'eau en quantité suffisante chaque jour, contrôler rigoureusement sa tension artérielle et sa glycémie, et éviter l'abus d'automédication (notamment certains anti-inflammatoires)."
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

def nettoyer(texte):
    return ''.join(c for c in unicodedata.normalize('NFD', texte) if unicodedata.category(c) != 'Mn').lower().strip()

if choix == "1":
    st.write("Sur quelle maladie souhaitez-vous des informations ? (Paludisme, Diabète, Hypertension, Insuffisance rénale)")
    saisie = st.text_input("Votre réponse :", key="s_1")
    if saisie:
        st.session_state.historique.append(f"Choix 1 - Info : {saisie}")
        sc = nettoyer(saisie)
        trouve = False
        for k, v in BASE_DE_DONNEES.items():
            if nettoyer(k) in sc:
                st.success(f"**{v['nom']}**\n\n{v['description']}")
                trouve = True
                break
        if not trouve:
            st.warning("Je ne suis pas habilité à répondre à cette question ou elle est hors de mon domaine. Veuillez consulter un médecin.")

elif choix == "2":
    st.write("Sur quel(s) symptôme(s) souhaitez-vous avoir des informations ? (Paludisme, Diabète, Hypertension, Insuffisance rénale)")
    saisie = st.text_input("Votre réponse :", key="s_2")
    if saisie:
        st.session_state.historique.append(f"Choix 2 - Symptômes : {saisie}")
        sc = nettoyer(saisie)
        trouve = False
        for k, v in BASE_DE_DONNEES.items():
            if nettoyer(k) in sc:
                st.info(f"**Symptômes associés au {v['nom']}** :\n\n{v['symptomes']}\n\n*Attention : Je n'établis pas de diagnostic. Veuillez consulter un médecin.*")
                trouve = True
                break
        if not trouve:
            st.warning("Je ne suis pas habilité à répondre à cette question ou elle est hors de mon domaine. Veuillez consulter un médecin.")

elif choix == "3":
    st.write("Sur quoi souhaitez-vous avoir des conseils de prévention ? (Paludisme, Diabète, Hypertension, Insuffisance rénale)")
    saisie = st.text_input("Votre réponse :", key="s_3")
    if saisie:
        st.session_state.historique.append(f"Choix 3 - Prévention : {saisie}")
        sc = nettoyer(saisie)
        trouve = False
        for k, v in BASE_DE_DONNEES.items():
            if nettoyer(k) in sc:
                st.success(f"**Conseils de prévention ({v['nom']})** :\n\n{v['prevention']}")
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
        st.write(f"- {h}")
