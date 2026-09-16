# RPI-webrover

Un projet de robot autonome contrôlable via une interface web, basé sur une Raspberry Pi. Le robot offre deux modes : un **mode jeu** et un **mode libre** pour l'exploration et le contrôle manuel.

## 📋 Description du Projet

**Robot Game** est une plateforme robotique interactive permettant de contrôler et d'explorer avec un robot équipé d'une caméra embarquée. Le système combine une architecture matérielle complète avec une interface web intuitive.

## 🤖 Architecture Matérielle

### Composants Principaux

- **Contrôleur Principal** : Raspberry Pi (gestionnaire de système)
- **Système de Locomotion**
  - 4 roues en propulsion (motorisées)
  - Servo-moteur de direction
  - Contrôle PCA9685 (PWM pour moteurs)
  
- **Système de Vision**
  - Caméra (interface CameraV2)
  - 2 servo-moteurs pour le suivi de caméra (axe X et Y)
  
- **Capteurs & Périphériques**
  - Différents capteurs (type à définir selon les besoins)
  - Système LED indicateurs

### Pins GPIO Raspberry Pi (Exemple)

```
Motor_A_EN = GPIO 4
Motor_B_EN = GPIO 17
Motor_A_Pin1 = GPIO 14
Motor_A_Pin2 = GPIO 15
Motor_B_Pin1 = GPIO 27
Motor_B_Pin2 = GPIO 18
```

## 📁 Structure du Projet

```
Robot_game/
├── Main.py                    # Point d'entrée principal
├── Camera/                    # Module gestion caméra
│   ├── CameraV2.py           # Interface caméra
│   └── region/               # Détection de régions
├── Moteur/                   # Moteur et contrôle des mouvements
│   ├── __init__.py
│   ├── MCam.py              # Contrôle caméra moteur
│   ├── Roue.py              # Contrôle roues/direction
│   └── Maintest.py          # Tests moteur
├── Serveur/                 # Serveur web Flask
│   ├── __init__.py
│   ├── Routeur.py           # Routes Flask
│   ├── socket.py            # Communication WebSocket
│   └── Web/
│       ├── Static/          # Fichiers statiques
│       │   ├── CSS/         # Feuilles de styles
│       │   ├── JS/          # Scripts JavaScript
│       │   └── Ressource/   # Images, assets
│       └── Template/        # Templates HTML
│           ├── index.html   # Page d'accueil
│           ├── acceuil.html # Accueil alternatif
│           └── game.html    # Interface du jeu
└── README.md
```

## 🎮 Modes de Fonctionnement

### Mode Jeu
**Objectif** : Scanner un nombre défini de QR codes dans un temps imparti ⏱️

Le joueur doit naviguer le robot à travers l'environnement et utiliser la caméra pour scanner les QR codes disséminés. Le système :
- Compte les QR codes scannés avec succès
- Affiche un chronomètre pour suivre le temps restant
- Valide chaque code scanné automatiquement
- Affiche un score final et le résultat (réussi/échoué)

### Mode Libre
Contrôle manuel complet du robot. L'utilisateur peut :
- Diriger les mouvements via l'interface web
- Voir le flux caméra en temps réel
- Contrôler l'orientation de la caméra
- Tester les capteurs
- Activer le mode suivie de couleur sur la caméra
- detection et lecture de QR code en temps réel

## 🌐 Interface Web

**Technologie Stack** :
- **Backend** : Python Flask (routeur, WebSocket)
- **Frontend** : HTML5, CSS3, JavaScript
- **Communication** : HTTP, WebSocket

### Pages Disponibles
- `index.html` - Page d'accueil/sélection de mode
- `game.html` - Interface mode jeu
- `acceuil.html` - Écran d'accueil alternatif

### Fonctionnalités Web
- **manette.js** - Contrôle manette
- **fonction.js** - Fonctionnalités principales
- **acceuil.js** - Gestion accueil

## 🚀 Démarrage Rapide

### Prérequis
- Raspberry Pi (avec Raspbian)
- Python 3.x
- Bibliothèques requises :
  - Flask
  - RPi.GPIO
  - Adafruit PCA9685
  - OpenCV (caméra)

### Installation
```bash
# Installer les dépendances
pip install flask RPi.GPIO adafruit-pca9685 adafruit-motor opencv-python
```

### Lancement
```bash
python Main.py <IP_RaspberryPi>
```

### utilisation
- Accéder à l'interface web via `http://<IP_RaspberryPi>:5000`
- Choisir le mode souhaité (Jeu ou Libre)
- Contrôler le robot via une manette (clavier non fonctionnel)

## 📡 Architecture Système

1. **Main.py** - Initialise la caméra et démarre le serveur
2. **Serveur** - Gère l'interface web et la communication
3. **Moteur** - Contrôle les mouvements (roues, servo-moteurs)
4. **Camera** - Capture et traite les images

## 🔧 Configuration

Voir les fichiers de configuration dans chaque module :
- `Moteur/Roue.py` - Configuration GPIO et servo-moteurs
- `Camera/CameraV2.py` - Paramètres caméra
- `Serveur/Routeur.py` - Routes Flask

## 📝 Notes de Développement

- Système modulaire permettant des ajouts futurs
- Communication WebSocket pour mise à jour en temps réel

## 🛠️ Améliorations Futures

- [ ] Enregistrement des sessions
- [ ] Système de batterie/charge
- [ ] Modes de détection d'objets
