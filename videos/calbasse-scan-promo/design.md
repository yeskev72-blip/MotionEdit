# design.md — Calbasse · démo scan (1080×1920)

## Angle

Un plat ouest-africain chaud et généreux passé au compteur froid d'un
instrument de mesure. Toute la direction artistique tient dans ce frottement :
**l'assiette parle fort, la machine répond en chiffres.**

## Palette — relevée dans le produit, pas inventée

| Token             | Valeur    | Origine                                   |
| ----------------- | --------- | ----------------------------------------- |
| `--brand`         | `#9C4818` | terracotta : anneau du logo, FAB, arc     |
| `--brand-bright`  | `#C7531D` | orange de la barre d'état de l'app        |
| `--gold`          | `#D8A860` | remplissage du bol dans le logo           |
| `--cream`         | `#FCF8F2` | fond de page de l'app                     |
| `--ink`           | `#1B191A` | texte principal de l'app                  |
| `--prot`          | `#CC3C3C` | jauge protéines                           |
| `--gluc`          | `#E49C0C` | jauge glucides                            |
| `--lip`           | `#246CD8` | jauge lipides                             |
| `--bg-0`          | `#1C0E07` | fond de scène (hors produit)              |
| `--bg-1`          | `#4A2010` | halo radial derrière l'appareil           |

Le fond de scène est **sombre et chaud** : l'écran de l'app est crème, il
devient donc la source de lumière du cadre. Aucune couleur hors de cette liste.

## Typographie

Deux voix, pas une hiérarchie :

- **Archivo Black** (400 uniquement — ne jamais demander 700/900) — *la voix
  de l'assiette.* Affirmations, accroche, carton de fin. Grasse, frontale,
  appétissante.
- **IBM Plex Mono** (400 / 700) — *la voix de l'instrument.* Tous les nombres,
  étiquettes, numéros d'étape, unités. Chiffres tabulaires, capitales
  interlettrées.

La tension est explicite : le display porte ce qu'on mange, le mono porte ce
que ça coûte. Les deux familles sont pré-embarquées par le compilateur, donc
aucun fetch réseau au rendu.

Tailles (plein écran vertical) : accroche 112px · titre 76px · nombre héros
150px · corps 38px · étiquette mono 30px, `letter-spacing: .18em`.

## Scène

L'écran de l'app n'est **jamais rogné** : la source 1080×2182 est posée en
entier dans un cadre d'appareil.

- Cadre au repos : 880 × 1778, centré, `border-radius: 44px`, filet
  `rgba(255,255,255,.14)`, ombre portée chaude.
- Les cartons de texte flottent au-dessus de l'écran sur un voile dégradé —
  jamais à côté, pour garder l'écran grand.
- Quand une carte large entre, l'appareil descend à `scale .88` et remonte de
  60px : la bande libérée en bas accueille la carte. Il revient à 1.0 à la
  sortie. C'est la seule chorégraphie de caméra globale.
- Punch-ins ponctuels : `scale 1.0 → 1.22` recentré sur le nombre visé, 0.5 s,
  `power3.out`. Uniquement sur 2 675,5 kcal et sur 784,5 kcal.

## Arc narratif — la bascule chiffrée

L'ossature du montage est un seul chiffre qui se vide :

**3 460 kcal restantes** (état vide, rien de mangé) → le scan → **784,5 kcal
restantes** (2 675,5 mangées). Le spectateur voit un budget se faire entamer
par une assiette. Tout le reste sert cette bascule.

## Plan de montage (source = assets/calbasse-screen.mp4, nettoyée)

Toutes les bornes ci-dessous ont été vérifiées image par image sur le master
recadré, pas estimées.

| # | t comp | durée | src in | vitesse | Écran                              | Surcouche                                              |
| - | ------ | ----- | ------ | ------- | ---------------------------------- | ------------------------------------------------------ |
| 1 | 0.00   | 2.60  | 0.45   | 1.0     | photo du plat, **plein cadre**     | accroche « Combien de calories ? »                     |
| 2 | 2.60   | 1.40  | 7.00   | 1.0     | splash, bol → lockup CALBASSE      | « l'app qui connaît nos plats »                        |
| 3 | 4.00   | 1.30  | 11.65  | 0.35    | journal vide, 3 460 kcal           | « Rien de mangé. Tout à dépenser. »                    |
| 4 | 5.30   | 1.60  | 12.35  | 0.55    | caméra « Cadre tout le plat »      | pastille « 01 · CADRE LE PLAT »                        |
| 5 | 6.90   | 1.40  | 32.20  | 1.0     | aperçu photo + bouton Analyser     | pastille « 02 · ANALYSE » + pulsation sur le bouton    |
| 6 | 8.30   | 3.20  | 33.70  | 1.55    | les 4 étapes d'analyse             | pastille « 03 · ÇA TRAVAILLE », rail de progression    |
| 7 | 11.50  | 4.80  | 38.90  | 1.0     | résultat 2 675,5 + macros          | compteur héros 2 675,5 kcal, puis 3 pastilles macros   |
| 8 | 16.30  | 2.60  | 43.70  | 1.0     | aliments détectés + type de repas  | « Pas de saisie. Pas de recherche. »                   |
| 9 | 18.90  | 3.70  | 47.80  | 1.0     | journal final 784,5                | compteur 3 460 → 784,5                                 |
| 10| 22.60  | 3.60  | —      | —       | carton de fin sur fond de marque   | logo + CALBASSE + accroche                             |

### La règle de caméra

Un seul principe gouverne les mouvements d'appareil, et il est tenu partout :

- **Pastille en haut → l'appareil reste au repos** (plans 4, 5, 6).
- **Carton en bas → l'appareil recule et se soulève**, ouvrant une bande propre
  sous lui (plans 3, 7, 8, 9).

Les valeurs de `scale` / `y` ne sont pas réglées à l'œil : la boîte de
l'appareil fait 880 × 1778 à `top: 71`, donc chaque recul est calculé pour
poser le bas de l'écran juste au-dessus du haut du carton.

### Ce que les surcouches ne font pas

Deux cartons ont été réécrits en cours de route parce qu'ils **répétaient** ce
que l'app affichait déjà :

- Plan 3 : le « 3 460 » géant doublait celui de l'app. Remplacé par une phrase.
  La seule reformulation d'un chiffre est gardée pour le plan 9, où le compte à
  rebours fait un travail que l'écran ne fait pas.
- Plan 8 : la liste des 4 plats doublait la liste à l'écran. Remplacée par ce
  que cette liste prouve — aucune saisie manuelle.

**Durée totale : 26.20 s.**

## Ce qui est coupé, et pourquoi

- **12.0 s → 32.0 s de la source (20 s)** : défilement de galerie, première
  tentative échouée, et le toast rouge « La photo n'a pas pu être lue depuis la
  galerie ». C'est un incident de session, pas le produit.
- **46.1 s → 47.9 s** : bandeau « 1 repas en attente de synchronisation (hors
  ligne) ». Même raison.

## Son

La source est **entièrement muette** (-inf dB) : toute la bande-son est ajoutée.

**9 marqueurs**, tirés de la bibliothèque SFX locale de `media-use` (licence
Pixabay, usage commercial libre) — un par chose que le spectateur voit atterrir,
jamais plus :

| t      | effet            | ce qu'il souligne                 |
| ------ | ---------------- | --------------------------------- |
| 0.42   | impact-bass-1    | l'accroche qui claque             |
| 2.56   | whoosh           | coupe vers le produit             |
| 7.50   | click            | l'appui sur « Analyser »          |
| 8.45   | glitch-3         | texture de traitement             |
| 12.98  | impact-bass-2    | l'atterrissage du 2 675,5         |
| 13.24… | pop × 3          | les 3 pastilles macros            |
| 18.86  | whoosh-short     | coupe vers le journal final       |
| 20.46  | chime            | le budget restant se pose         |
| 22.74  | sparkle          | le logo du carton de fin          |

Chaque effet a une enveloppe de volume qui retombe à 0 avant la fin de son clip,
donc aucune coupure nette ne claque.

**Lit musical** : absent de la version livrée. `assets/bgm/generate.py` est prêt
(prompt afrobeat, graine torch fixée pour une piste reproductible) mais
`huggingface.co` est refusé par la politique réseau de l'environnement — les
poids de `facebook/musicgen-small` sont inatteignables. torch s'installe bien
depuis PyPI, le modèle non. Débloquer `huggingface.co` dans les réglages de
l'environnement suffit à relancer le script tel quel.

Rien n'a été substitué à la place : sur 26 secondes, un ersatz de musique
synthétisé à la main s'entendrait et desservirait la vidéo plus qu'un silence
assumé sous les marqueurs.

## Garde-fous

- Les valeurs affichées sont celles de l'app, qui les étiquette elle-même
  « à confirmer ». Aucune surcouche ne les présente comme exactes.
- Aucune surcouche n'imite l'interface de l'app : Archivo Black / Plex Mono sur
  voile sombre, jamais les cartes blanches du produit. Le spectateur doit
  toujours distinguer le produit du commentaire.
