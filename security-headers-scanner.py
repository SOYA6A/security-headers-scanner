#!/usr/bin/env python3
"""
Security Headers Scanner - Version avec Score
Auteur: SOYA
Description: Vérifie les headers de sécurité d'un site web et attribue un score
"""

import requests
import sys

def scanner_site(url):
    if not url.startswith('http'):
        url = 'https://' + url
    
    print(f"\n🔍 Analyse de: {url}\n")
    
    try:
        reponse = requests.get(url, timeout=10)
        headers = reponse.headers
        
        print("📋 Headers de sécurité trouvés:\n")
        print("-" * 50)
        
        score = 0
        total_headers = 4
        
        if 'Strict-Transport-Security' in headers:
            print("✅ HSTS présent - Le site force HTTPS")
            score += 1
        else:
            print("❌ HSTS manquant - Le site devrait forcer HTTPS")
        
        if 'X-Frame-Options' in headers:
            print("✅ X-Frame-Options présent - Protégé contre clickjacking")
            score += 1
        else:
            print("❌ X-Frame-Options manquant - Vulnérable au clickjacking")
        
        if 'X-Content-Type-Options' in headers:
            print("✅ X-Content-Type-Options présent - Protégé MIME sniffing")
            score += 1
        else:
            print("❌ X-Content-Type-Options manquant")
        
        if 'Content-Security-Policy' in headers:
            print("✅ CSP présent - Protégé contre les injections XSS")
            score += 1
        else:
            print("❌ CSP manquant - Vulnérable aux attaques XSS")
        
        print("-" * 50)
        
        pourcentage = (score / total_headers) * 100
        
        print(f"\n📊 SCORE DE SÉCURITÉ: {score}/{total_headers} ({pourcentage:.0f}%)")
        print("-" * 50)
        
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
        print(f"❌ Erreur: {erreur}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\n📖 Comment utiliser ce script:")
        print("   python3 security_scanner.py <url>")
        print("\n💡 Exemple:")
        print("   python3 security_scanner.py google.com\n")
        sys.exit(1)
    
    url_a_scanner = sys.argv[1]
    scanner_site(url_a_scanner)
