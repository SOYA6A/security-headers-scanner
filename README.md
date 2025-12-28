# 🔒 Security Headers Scanner
Un outil simple pour analyser les headers de sécurité HTTP d'un site web.
### 📋 Description

Ce script Python vérifie la présence des headers de sécurité essentiels sur un site web :

- HSTS (Strict-Transport-Security): Force l'utilisation de HTTPS
- X-Frame-Options: Protection contre le clickjacking
- X-Content-Type-Options: Protection contre le MIME sniffing
- Content-Security-Policy: Protection contre les attaques XSS

🚀 Installation

1. Cloner le repository :
```bash
 git clone https://github.com/ton-username/security-headers-scanner.git
cd security-headers-scanner
```
2. Installer les dépendances
```bash
p install -r requirements.txt
```
🛠️ Technologie utilisées 

- Python 3
- Bibliothèque requests pour les requêtes HTTP

🎯 Objectifs du projet
