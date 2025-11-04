import os
from dotenv import load_dotenv
import streamlit as st

# ---- Chargement des variables d'environnement ----
load_dotenv()
DEFAULT_API_KEY = os.getenv("", "")

# ---- UI : configuration de la page ----
st.set_page_config(page_title="Assistant IA – Vitrine", page_icon="🤖", layout="centered")

st.title("🤖 Assistant Textuel – OpenAI (Vitrine)")
st.caption("Prototype Streamlit • Chat avec mémoire • Système + Température • Upload contexte")

# ---- Sidebar : paramètres ----
with st.sidebar:
    st.header("⚙️ Paramètres")
    api_key = st.text_input(
        "OpenAI API Key",
        value=DEFAULT_API_KEY if DEFAULT_API_KEY else "",
        type="password",
        help="Stocke la clé en .env pour la retenir automatiquement."
    )

    # Choix du modèle : tu peux ajuster selon ton compte
    model = st.text_input(
    "Modèle",
    value="gpt-5",
    help="Modèles disponibles : gpt-5, gpt-5-mini, gpt-5-nano."
)

    temperature = st.slider("Température", 0.0, 1.0, 0.2, 0.05,
                            help="Plus haut = plus créatif, plus bas = plus factuel.")
    max_tokens = st.slider("Max tokens réponse", 256, 4096, 1024, 128)

    system_prompt = st.text_area(
        "Système (rôle de l'assistant)",
        value=(
            "Tu es un assistant utile, concis et orienté métier. "
            "Tu expliques clairement, donnes des étapes actionnables, et proposes des exemples."
        ),
        height=120
    )

    uploaded = st.file_uploader("📎 Contexte (txt/markdown)", type=["txt", "md"], help="Optionnel : ajouté au contexte.")
    add_reset = st.button("♻️ Réinitialiser la conversation")

# ---- Sécurité simple : clés manquantes ----
if not api_key:
    st.warning("⚠️ Renseigne une **OpenAI API Key** dans la sidebar pour démarrer.")
    st.stop()

# ---- OpenAI client (SDK v1.x) ----
try:
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
except Exception as e:
    st.error(f"Erreur import OpenAI SDK : {e}")
    st.stop()

# ---- Session state ----
if "messages" not in st.session_state or add_reset:
    st.session_state.messages = []

# On ajoute le contexte uploadé comme un 'system' additionnel (optionnel)
context_note = ""
if uploaded is not None:
    try:
        context_note = uploaded.read().decode("utf-8", errors="ignore")
    except Exception:
        context_note = ""
if context_note:
    # On (ré)injecte le contexte comme premier message système auxiliaire
    # (On évite les doublons si on reset pas)
    if not any(m.get("meta") == "ctx" for m in st.session_state.messages):
        st.session_state.messages.insert(0, {
            "role": "system",
            "content": f"Contexte fourni par l'utilisateur :\n{context_note}",
            "meta": "ctx"
        })

# ---- Affichage du fil de discussion ----
for m in st.session_state.messages:
    if m["role"] in ("user", "assistant"):
        with st.chat_message("user" if m["role"] == "user" else "assistant"):
            st.markdown(m["content"])

# ---- Chat input ----
user_input = st.chat_input("Écris ton message…")

def build_payload_messages():
    msgs = [{"role": "system", "content": system_prompt}]
    # Ajoute messages de l'historique (hors meta)
    for m in st.session_state.messages:
        if m["role"] in ("user", "assistant"):
            msgs.append({"role": m["role"], "content": m["content"]})
    # On ajoute le contexte uploadé côté système si présent
    if context_note:
        msgs.insert(1, {"role": "system", "content": f"Contexte : {context_note}"})
    return msgs

def chat_complete(prompt_text: str) -> str:
    """Appel simple au Chat Completions API (OpenAI SDK v1.x)."""
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=build_payload_messages() + [{"role": "user", "content": prompt_text}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"❌ Erreur API : {e}"

if user_input:
    # Affiche le message utilisateur
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Appel modèle + streaming simple (non token à token pour simplicité)
    with st.chat_message("assistant"):
        with st.spinner("Réflexion en cours…"):
            assistant_reply = chat_complete(user_input)
            st.markdown(assistant_reply)

    # Mémorise la réponse
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

# ---- Footer aide ----
st.markdown("---")
st.caption(
    "Astuce : ajuste le **Système**, la **Température** et **Max tokens** dans la sidebar pour façonner le style. "
    "Ajoute un fichier .txt/.md (ex: cahier des charges) pour guider les réponses."
)