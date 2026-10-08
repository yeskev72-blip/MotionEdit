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

## Scène — construite autour du gabarit TikTok

La vidéo est destinée à TikTok, où l'interface recouvre une grande partie du
cadre. **Tout le texte vit dans une boîte de sécurité ; rien n'en sort.**

TikTok ne publie pas de cote unique : sa doc dit que la zone dépend du format
et de la longueur de la légende, et les guides tiers se contredisent (bas de
320 à 484 px, droite de 64 à 280 px). Le gabarit retenu est l'extrémité
prudente de cette fourchette, pour un post **organique** où le rail d'actions
(avatar, cœur, commentaire, partage, disque) est plus large que dans les
modèles publicitaires :

| Côté   | À laisser libre | Raison                                      |
| ------ | --------------- | ------------------------------------------- |
| Haut   | 180 px          | barre d'état + onglets « Abonnements / Pour toi » |
| Bas    | 480 px          | pseudo, légende, ticker musical, barre de navigation |
| Gauche | 60 px           | marge                                       |
| Droite | 240 px          | rail d'actions                              |

**Zone d'écriture : x 60 → 840, y 180 → 1440.**

Le *footage* peut déborder de cette boîte — un spectateur accepte que l'image
continue sous l'interface. Le texte, jamais.

### La fenêtre, et pourquoi ce n'est plus un téléphone entier

Un écran 1080 × 2182 ne rentre pas dans une boîte de 780 × 1260 sans devenir
illisible. La composition montre donc **une fenêtre panoramiquée** dans
l'enregistrement plutôt que l'appareil entier :

- Fenêtre fixe : `x 60, y 180, 780 × 860`, coins arrondis, filet clair.
- La vidéo y est rendue à `780 × 1576` (échelle 0,72222), donc la fenêtre
  découpe une tranche de 1191 px de la source.
- **Chaque plan porte son propre décalage vertical**, qui amène son contenu
  utile dans la tranche. C'est ce qui remplace le rétrécissement : au lieu de
  réduire tout l'écran, le film montre la partie qui compte.

| Plan | Décalage source | Ce que la fenêtre cadre                       |
| ---- | --------------- | --------------------------------------------- |
| 2    | 560             | le lockup CALBASSE                            |
| 3    | 60              | la carte 3 460 et la rangée de macros         |
| 4    | 60              | le viseur et « Cadre tout le plat »           |
| 5    | 500             | la photo cadrée et le bouton Analyser         |
| 6    | 700             | les quatre étapes d'analyse                   |
| 7    | 450             | le total 2 675,5, les macros, « Aliments détectés » |
| 8    | 150             | la liste des plats reconnus                   |
| 9    | 60              | la carte 784,5 et les anneaux de macros       |

### Une seule bande de texte

Sous la fenêtre, entre `y 1090` et `y 1430`, une bande unique porte **tout**
le texte de tous les plans. Les pastilles d'étape qui flottaient en haut du
cadre ont été supprimées : elles créaient un second point d'ancrage pour
l'œil et laissaient la bande vide sur les plans 4 à 6. Le regard ne bouge
plus.

Les plans 4, 5 et 6 forment désormais un triptyque de verbes courts —
**« Tu photographies. » / « Tu appuies. » / « Elle compte. »** — qui dit qui
fait quoi, sans répéter le texte affiché par l'app.

### L'accroche

Seule exception au cadrage en fenêtre : le plan 1 joue la photo en plein
cadre. Aucune lecture n'y est requise, donc le débordement est sans
conséquence — et l'assiette doit posséder l'image avant que le produit
n'arrive. Son texte, lui, reste dans la boîte.

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

### Le mouvement

La fenêtre et la bande étant fixes, plus rien n'a besoin de s'écarter pour
laisser passer un carton. Il ne reste que deux mouvements, tous deux motivés :
la poussée lente sur l'assiette pendant l'accroche, et une impulsion de 3,5 %
sur la fenêtre au moment où le verdict tombe.

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

**Pas de lit musical — choix assumé, pas un repli.** La piste a été tentée
(MusicGen hors-ligne) puis abandonnée : `huggingface.co` est refusé par la
politique réseau de l'environnement, donc les poids de `facebook/musicgen-small`
sont inatteignables. Mis devant le choix, l'auteur a tranché pour les marqueurs
seuls.

Ce que ça implique pour le mixage : entre les marqueurs, c'est le silence, et
le plus long intervalle fait 4,4 s (entre la coupe vers le produit à 3,13 s et
le clic sur « Analyser » à 7,50 s). Si le silence venait à s'entendre comme une
coupure de son plutôt que comme une intention, un fond de salle très discret ou
un tic régulier sous les plans 4 à 6 suffirait à le combler, sans ajouter de
musique.

Le script de génération a été retiré du projet une fois la décision prise ; il
reste récupérable dans l'historique git (commit bd1f49d).

## Garde-fous

- Les valeurs affichées sont celles de l'app, qui les étiquette elle-même
  « à confirmer ». Aucune surcouche ne les présente comme exactes.
- Aucune surcouche n'imite l'interface de l'app : Archivo Black / Plex Mono sur
  voile sombre, jamais les cartes blanches du produit. Le spectateur doit
  toujours distinguer le produit du commentaire.
