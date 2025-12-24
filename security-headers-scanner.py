#!/usr/bin/env python3
# ☝️ SHEBANG: Dit au système d'utiliser Python3 pour exécuter ce fichier
# Permet de lancer le script avec ./security_scanner.py au lieu de python security_scanner.py
# Pour l'activer sur Mac: chmod +x security_scanner.py

"""
Security Headers Scanner
Vérifie les headers de sécurité d'un site web
"""
#  pour importer les outils dont on a besoin
import requests  # Pour faire des requêtes HTTP (va chercher le site web)
import sys       # Pour récupérer les arguments de la ligne de commande

def scanner_site(url):
    """
    Cette fonction scanne un site web pour vérifier ses headers de sécurité
    """

     # Étape 1: Préparer l'URL
    # Si l'utilisateur n'a pas mis https://, on l'ajoute
    if not url.startswith('http'):
        url = 'https://' + url
    