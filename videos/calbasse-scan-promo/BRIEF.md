---
workflow: general-video
flow: automation
storyboard: no
message: "Photographie ton plat ouest-africain, Calbasse compte les calories"
destination: tiktok
aspect: 1080x1920
language: fr
length: 30s
angle: demo-rapide
---

## Intent

Transformer une capture d'écran brute de l'app Calbasse en une démo produit
nerveuse et lisible pour TikTok / Reels / Shorts. Calbasse scanne une photo de
plat et renvoie les calories et les macros — avec une table de composition
d'Afrique de l'Ouest, donc elle reconnaît le poulet braisé, l'alloco et l'igname
frite, que les apps génériques ratent.

Ton : net, rapide, confiant. Le produit fait la démonstration, le texte ne fait
que pointer. Pas de slogan publicitaire gonflé.

## Assets

- assets/calbasse-screen.mp4 — la capture d'écran Android nettoyée (barres
  système retirées). Source unique de tous les plans.

## Customizations

- Gabarit TikTok : tout le texte tient dans x 60→840 / y 180→1440, hors des
  zones couvertes par la légende, le pseudo, la barre de navigation et le rail
  d'actions. Vérifié par mesure de pixels sur chaque plan, pas à l'œil.
- L'écran de l'app est montré comme une fenêtre panoramiquée (780×860) dont le
  cadrage change à chaque plan, plutôt que comme un téléphone entier rétréci :
  à cette taille de boîte, l'appareil complet serait illisible.
- Coupe des 18 s de défilement de galerie (12 s → 32 s dans la source), y compris
  la tentative ratée et son toast d'erreur « La photo n'a pas pu être lue depuis
  la galerie ».
- Arc en bascule chiffrée : 3 460 kcal restantes (état vide) → scan → 784,5 kcal
  restantes. C'est la colonne vertébrale du montage.
- Compteur animé sur le total 2 675,5 kcal et sur les macros.
- Punch-ins sur les chiffres clés ; le reste reste au repos.
- Bande sonore ajoutée de zéro : la source est totalement muette (-inf dB).
- Sound design final : 9 marqueurs, pas de lit musical. Décision confirmée par
  l'auteur après l'échec de la génération locale, pas un défaut de livraison.

## Notes

- Ne jamais afficher le toast d'erreur ni l'avertissement « hors ligne » : ce
  sont des bugs de la session d'enregistrement, pas le produit.
- Les valeurs à l'écran sont celles de l'app, étiquetées « à confirmer » par
  elle-même. Ne pas les présenter comme des mesures exactes.
- Horloge du téléphone à 7:09 et « 30 scans » visibles : acceptable, c'est une
  vraie session.
