# 🎁 Gemini Gift AI – Le Générateur de Cadeaux Intelligent

**Gemini Gift AI** est une application web moderne qui utilise l'intelligence artificielle (Google Gemini 1.5 Flash) pour vous aider à trouver le cadeau parfait en quelques secondes. Que ce soit pour un anniversaire, une fête ou un plaisir d'offrir, notre IA analyse le profil du destinataire pour proposer 5 idées sur-mesure.

---

### 🚀 Fonctionnalités Clés / Key Features

- **Génération IA Personnalisée** : Basée sur l'âge, le sexe, les centres d'intérêt et le budget. (AI-Powered Recommendations)
- **Support Multilingue** : Disponible en Français, Anglais et Arabe. (Multilingual Support: FR, EN, AR)
- **Système d'Authentification** : Créez un compte pour sauvegarder vos idées favorites. (User Auth & Profile)
- **Dashboard Favoris** : Retrouvez facilement toutes les meilleures idées que vous avez générées. (Favorites Management)
- **Interface Premium** : Design responsive avec mode sombre (Dark) et clair (Light). (Sleek Dark/Light Mode UI)

---

### 🛠️ Technologies / Stack

- **Backend** : Flask (Python 3.x)
- **IA** : Google Gemini API (Modèle `gemini-flash-latest`)
- **Base de données** : SQLite (persistance locale)
- **Frontend** : HTML5, CSS3 (Vanilla design, glassmorphism vibes)

---

### 📦 Installation & Setup

1. **Cloner le projet :**
   ```bash
   git clone https://github.com/Chaimae-aamymi/kado.git
   cd kado
   ```

2. **Installer les dépendances :**
   ```bash
   pip install flask python-dotenv google-generativeai
   ```

3. **Configurer les variables d'environnement :**
   Créez un fichier `.env` à la racine :
   ```env
   GEMINI_API_KEY=VOTRE_CLE_API_ICI
   SECRET_KEY=votre_secret_key_aléatoire
   ```

4. **Lancer l'application :**
   ```bash
   python app.py
   ```
   L'application sera disponible sur `http://localhost:3000`.

---

### ⚖️ Licence
Ce projet est sous licence MIT. Libre à vous de l'utiliser et de le modifier !
