#  Kado – Le Générateur de Cadeaux Intelligent

**Kado** est une application web moderne qui utilise l'intelligence artificielle (Google Gemini 1.5 Flash) pour vous aider à trouver le cadeau parfait en quelques secondes. Que ce soit pour un anniversaire, une fête ou un plaisir d'offrir, notre IA analyse le profil du destinataire pour proposer 5 idées sur-mesure.

---

###  Fonctionnalités Clés

- **Génération IA Personnalisée** : Basée sur l'âge, le sexe, les centres d'intérêt et le budget.
- **Support Multilingue** : Disponible en Français, Anglais et Arabe..
- **Système d'Authentification** : Créez un compte pour sauvegarder vos idées favorites.
- **Dashboard Favoris** : Retrouvez facilement toutes les meilleures idées que vous avez générées.
- **Interface Premium** : Design responsive avec mode sombre (Dark) et clair (Light).

---

###  Key Features (English)

- **AI-Powered Recommendations**: Real-time generation based on age, gender, interests, and budget.
- **Multilingual Support**: Fully localized in French, English, and Arabic.
- **User Authentication**: Secure login/registration system to personalize your experience.
- **Favorites System**: Save and manage your favorite gift ideas for later.
- **Premium UI**: Sleek, responsive design featuring both Dark and Light modes.

---

###  Technologies / Stack

- **Backend** : Flask (Python 3.x)
- **IA** : Google Gemini API (Modèle `gemini-flash-latest`)
- **Base de données** : SQLite (persistance locale)
- **Frontend** : HTML5, CSS3 (Modern design, glassmorphism)

---

###  Installation & Setup

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

###  Licence
Ce projet est sous licence MIT.
