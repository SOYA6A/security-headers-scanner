# 🔒 Security Headers Scanner
Un outil simple pour analyser les headers de sécurité HTTP d'un site web.

### 🔄 Prochaines fonctionnalités
- ⏳ Système de score de sécurité (0-100%)
- ⏳ Niveaux d'alerte selon le score

  ### 📋 Description

Ce script Python vérifie la présence des headers de sécurité essentiels sur un site web :

- HSTS (Strict-Transport-Security): Force l'utilisation de HTTPS
- X-Frame-Options: Protection contre le clickjacking
- X-Content-Type-Options: Protection contre le MIME sniffing
- Content-Security-Policy: Protection contre les attaques XSS

### 🚀 Installation

1. Cloner le repository :
```bash
 git clone https://github.com/SOYA6A/security-headers-scanner.git
cd security-headers-scanner
```
2. Installer les dépendances
```bash
p install -r requirements.txt
```
### 🛠️ Technologie utilisées 

- Python 3
- Bibliothèque requests pour les requêtes HTTP

### 🎯 Objectifs du projet
- Comprendre les headers de sécurité HTTP
- Pratiquer 
- Sensibiliser à la sécurité web
## 📊 Exemples d'utilisation
- GitHub.com - Score : 100% 🟢
```bash
python3 security-headers-scanner.py github.com
```
<img width="2508" height="738" alt="image" src="https://github.com/user-attachments/assets/599abae6-b82d-43d9-9569-5a976cc3ae6b" />


- Google.com - Score : 25% 🔴

<img width="2598" height="762" alt="image" src="https://github.com/user-attachments/assets/92368d52-ff44-44b1-9de9-92b19bf1d50a" />


- Netflix.com - Score : 75% 🟡
  
<img width="1828" height="764" alt="image" src="https://github.com/user-attachments/assets/81557307-7525-4512-b129-b3e8a161630e" />



<img width="1692" height="770" alt="image" src="https://github.com/user-attachments/assets/e409c3a4-6b9d-4cd7-a66d-b80463ed4053" />
