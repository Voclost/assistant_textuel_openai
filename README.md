🧠 Assistant Textuel OpenAI

Un assistant IA conversationnel développé avec Streamlit & OpenAI, configuré pour le Vibe Coding Framework.

🚀 À propos

L’Assistant Textuel OpenAI est une application Streamlit qui permet de discuter avec un modèle GPT (jusqu’à GPT-5) dans une interface simple et personnalisable.
Le projet illustre comment intégrer l’intelligence artificielle dans un workflow de développement et de gestion de projet.

🔹 Interface Web : Streamlit
🔹 Moteur IA : OpenAI API (GPT-4o, GPT-5, GPT-5-mini)
🔹 Mode de lancement : launch.exe ou exécution Python directe
🔹 Conçu et configuré par Zied Douraï

🧩 Fonctionnalités principales

✅ Discussion en temps réel avec OpenAI GPT-5
✅ Saisie libre des prompts système et personnalisés
✅ Historique contextuel conservé
✅ Sélecteur de modèle (GPT-4o, GPT-5, GPT-5-mini, etc.)
✅ Interface légère & responsive via Streamlit
✅ Fichier .env pour la configuration de la clé API
✅ Mode “Launch” via exécutable ou terminal

⚙️ Installation & Exécution
1️⃣ Cloner le dépôt
bash
git clone https://github.com/Voclost/assistant-textuel-openai.git
cd assistant-textuel-openai

2️⃣ Créer et activer un environnement virtuel
bash
py -3.12 -m venv .venv
.\.venv\Scripts\activate

3️⃣ Installer les dépendances
bash
pip install --upgrade pip
pip install -r requirements.txt

4️⃣ Ajouter la clé OpenAI
Créer un fichier .env à la racine :
ini
OPENAI_API_KEY=sk-xxxxxx

5️⃣ Lancer l’application
bash
streamlit run assistant_textuel_openai.py

💻 Lancer via l’exécutable (facultatif)
Un exécutable Windows (launch.exe) est disponible dans la section : https://drive.google.com/file/d/1vAmIjmE2gzz7LkOaHJM1oJoOlYgPK6Vg/view?usp=sharing

📂 Structure du projet
assistant-textuel-openai/
│
├── assistant_textuel_openai.py   # Application Streamlit principale
├── launch.py                     # Lanceur local (vers streamlit run)
├── requirements.txt               # Dépendances Python
├── .env.example                   # Exemple de configuration API
├── README.md                      # Ce fichier :)
└── .gitignore                     # Exclusions (env, dist, exe, etc.)

🧠 Technologies & IA utilisées
Domaine	:           Outil / API
Interface :	        Streamlit
IA :	              OpenAI GPT-4o / GPT-5
Générateurs d’aide: GitHub Copilot, Google Gemini
Langages :	        Python 3.12
Automatisation :	  PyInstaller, dotenv
Style	:             Vibe Coding – Modern-Tech Design ⚡
