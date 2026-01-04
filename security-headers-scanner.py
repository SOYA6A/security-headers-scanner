#!/usr/bin/env python3
# ☝️ SHEBANG: Dit au système d'utiliser Python3 pour exécuter ce fichier
# Permet de lancer le script avec ./security_scanner.py au lieu de python security_scanner.py
# Pour l'activer sur Mac: chmod +x security_scanner.py

"""
Security Headers Scanner - Version Débutant
Description: Vérifie si un site web a les headers de sécurité importants
"""

# importer les outils dont on a besoin
import requests  # Pour faire des requêtes HTTP (va chercher le site web)
import sys       # Pour récupérer les arguments de la ligne de commande

def scanner_site(url):
    """
    Cette fonction scanne un site web pour vérifier ses headers de sécurité
    """
    
    # first 1: Préparer l'URL
    # Si l'utilisateur n'a pas mis https://, on l'ajoute
    if not url.startswith('http'):
        url = 'https://' + url
    
    print(f"\n🔍 Analyse de: {url}\n")
    
    try:
        # Étape 2: chercher le site web
        # C'est comme ouvrir une page dans ton navigateur
        reponse = requests.get(url, timeout=10)
        
        # Étape 3:  récupèrer les headers (en-têtes HTTP)
        # Les headers sont des infos que le serveur nous envoie
        headers = reponse.headers
        
        print("📋 Headers de sécurité trouvés:\n")
        print("-" * 50)

        # Variable pour compter les headers présents
        score = 0
        total_headers = 4  # On vérifie 4 headers au total
        
        # Étape 4: On vérifie chaque header de sécurité un par un
        
        # Header 1: HSTS (force HTTPS)
        if 'Strict-Transport-Security' in headers:
            print("✅ HSTS présent - Le site force HTTPS")
            score += 1
        else:
            print("❌ HSTS manquant - Le site devrait forcer HTTPS")
        
        # Header 2: Protection contre le clickjacking
        if 'X-Frame-Options' in headers:
            print("✅ X-Frame-Options présent - Protégé contre clickjacking")
            score += 1
        else:
            print("❌ X-Frame-Options manquant - Vulnérable au clickjacking")
        
        # Header 3: Protection MIME sniffing
        if 'X-Content-Type-Options' in headers:
            print("✅ X-Content-Type-Options présent - Protégé MIME sniffing")
           score += 1
        else:
            print("❌ X-Content-Type-Options manquant")
        
        # Header 4: Protection XSS (attaques de script)
        if 'Content-Security-Policy' in headers:
            print("✅ CSP présent - Protégé contre les injections XSS")
           score += 1
        else:
            print("❌ CSP manquant - Vulnérable aux attaques XSS")
        
        print("-" * 50)
        # calcule et affiche le score
        pourcentage = (score / total_headers) * 100

        print(f"\n📊 SCORE DE SECURITE: {score}/{total_headers} ({pourcentage:.0f}%)")
        print("-"* 50)
    #Message selon le niveau de sécurité
    if pourcentage == 100:
        print("\n✨ Scan terminé !\n")


# Message selon le niveau de sécurité
        if pourcentage == 100:
            print("🟢 Excellent ! Tous les headers de sécurité sont présents.")
        elif pourcentage >= 75:
            print("🟡 Bon niveau de sécurité, mais quelques améliorations possibles.")
        elif pourcentage >= 50:
            print("🟠 Sécurité moyenne - Des headers importants manquent.")
        else:
            print("🔴 Sécurité faible - Action urgente requise !")
        
      






        print("\n✨ Scan terminé !\n")
        
    except Exception as erreur:
        # Si quelque chose ne marche pas,  afficher l'erreur
        print(f"❌ Erreur: {erreur}")

# Programme principal
if __name__ == "__main__":
    # vérifier que l'utilisateur a donné une URL
    if len(sys.argv) < 2:
        print("\n📖 Comment utiliser ce script:")
        print("   python security_scanner.py <url>")
        print("\n💡 Exemple:")
        print("   python security_scanner.py google.com\n")
        sys.exit(1)
    
    #  récupèrer l'URL donnée par l'utilisateur
    url_a_scanner = sys.argv[1]
    
    #  lancer le scan !
    scanner_site(url_a_scanner)
