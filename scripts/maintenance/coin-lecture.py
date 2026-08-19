#!/usr/bin/env python3

from html import escape
from pathlib import Path

NUTRITION = [
[ "https://www.amazon.fr/dp/2877240568/", "51B4J9RA5ZL.jpg", "Le lait : une sacrée vacherie ?"                                                          , "de Nicolas Le Berre (Auteur)" ],
[ "https://www.amazon.fr/dp/2857421540/", "41T6NKQ74GL.jpg", "La nutrithérapie : bases scientifiques et pratique médicale"                              , "de Curtay (Auteur)" ],
[ "https://www.amazon.fr/dp/2868398871/", "41X4DR6C0SL.jpg", "L’Alimentation, ou la troisième médecine"                                                 , "de Jean Seignalet (Auteur), Henri Joyeux (Préface)" ],
[ "https://www.amazon.fr/dp/2501046676/", "51y5F6pV4LL.jpg", "L’index glycémique : un allié pour mieux manger"                                          , "de Jennie Brand-Miller (Auteur), Kaye Foster-Powell (Auteur), Stephen Colagiuri (Auteur), Gérard Slama (Auteur)" ],
[ "https://www.amazon.fr/dp/2290336335/", "51Isq9qY0TL.jpg", "Je mange donc je maigris... et je reste mince !"                                          , "de Michel Montignac (Auteur)" ],
[ "https://www.amazon.fr/dp/2950902103/", "515jb0rpw+L.jpg", "La santé vient en mangeant"                                                               , "de Pierre-Henri Meunier (Auteur)" ],
[ "https://www.amazon.fr/dp/2883431205/", "21531HNE1DL.jpg", "Le régime crétois"                                                                        , "de Docteur Jacques Gardan (Auteur)" ],
[ "https://www.amazon.fr/dp/2909757129/", "41CX1RN+6AL.jpg", "Comment nourrir naturellement son enfant de 0 à 10 ans"                                   , "de Lionel Clergeaud (Auteur), Chantal Clergeaud (Auteur)" ],
[ "https://www.amazon.fr/dp/2872110259/", "516HicXilYL.jpg", "Pour en finir avec Pasteur : Un siècle de mystification scientifique"                     , "de Docteur Éric Ancelet (Auteur)" ],
[ "https://www.amazon.fr/dp/2916878149/", "51r1RkyK-CL.jpg", "Lait, mensonges et propagande"                                                            , "de Thierry Souccar (Auteur)" ],
[ "https://www.amazon.fr/dp/2804152359/", "51DnXHvQe4L.jpg", "Micronutrition, santé et performance : Comprendre ce qu’est vraiment la micronutrition"   , "de Denis Riché (Auteur), Didier Chos (Auteur)" ],
[ "https://www.amazon.fr/dp/2883533210/", "51hcyuI787L.jpg", "L’énergie du cru : Mettez 75 % de cru dans votre assiette et de la vie dans votre corps !", "de Leslie Kenton (Auteur), Susannah Kenton (Auteur), Karen Vago (Traduction)" ],
[ "https://www.amazon.fr/dp/2883539464/", "41KRg9WGi3L.jpg", "Les incroyables vertus des smoothies verts"                                               , "de Colette Pairain (Auteur), Nadège Pairain (Auteur)" ],
[ "https://www.amazon.fr/dp/2253131504/", "51BHl8OgsBL.jpg", "Les aliments contre le cancer : La prévention du cancer par l’alimentation"               , "de Richard Beliveau (Auteur)" ],
[ "https://www.amazon.fr/dp/2916878173/", "5168cEiwy7L.jpg", "Cholestérol, mensonges et propagande"                                                     , "de Michel de Lorgeril (Auteur)" ],
[ "https://www.amazon.fr/dp/2874610526/", "51xcMoqFU6L.jpg", "Nutrithérapie : Bases scientifiques et pratique médicale"                                 , "de Jean-Paul Curtay (Auteur)" ],
[ "https://www.amazon.fr/dp/287211078X/", "51d9nPHw9AL.jpg", "Écosystème intestinal et santé optimale : Nouvelle approche diagnostique et thérapeutique", "de Georges Mouton (Auteur)" ],
[ "https://www.amazon.fr/dp/2916878483/", "51Xox7RB3UL.jpg", "Le régime hormone"                                                                        , "de Thierry Hertoghe (Auteur), Margherita Enrico (Auteur)" ],
[ "https://www.amazon.fr/dp/2253085073/", "414CJchKiYL.jpg", "Guide familial des aliments soigneurs"                                                    , "de Jean-Paul Curtay (Docteur) (Auteur)" ],
[ "https://www.amazon.fr/dp/2954103205/", "51PO+KJEM8L.jpg", "TIME Nutrition “Faites de l’aliment votre médicament”"                                    , "de Jean-René MESTRE (Auteur), Jean-Robert RAPIN (Auteur)" ]
]

PHYTOTHERAPIE_AROMATHERAPIE = [
[ "https://www.amazon.fr/dp/2857079192/", "41GXCZCYZVL.jpg", "Aromathérapie essentielle : Huiles essentielles et parfums pour le corps et l’âme"        , "de Jean-Louis Abrassart (Auteur)" ],
[ "https://www.amazon.fr/dp/2035071259/", "514WFVSEJ9L.jpg", "Encyclopédie des plantes médicinales : Identification, préparations, soins"               , "de Paul Iserin (Préface), Collectif (Auteur)" ],
[ "https://www.amazon.fr/dp/2035822246/", "51Q02ieAFZL.jpg", "Le guide de l’aromathérapie"                                                              , "de Denise Whichello Brown (Auteur), Marie-Noëlle Pichard (Traduction)" ]
]

THERAPIES_COMPLEMENTAIRES = [
[ "https://www.amazon.fr/dp/284899357X/", "51X2bPANO-L.jpg", "Homéopathie guide pratique"                                                               , "de Albert-Claude Quemoun (Auteur)" ],
[ "https://www.amazon.fr/dp/2212548036/", "51LFouB2ysL.jpg", "Le grand livre de la naturopathie"                                                        , "de Christian Brun (Auteur)" ],
[ "https://www.amazon.fr/dp/2290348279/", "51ybjuwGB2L.jpg", "Médecin des trois corps"                                                                  , "de Janine Fontaine (Auteur)" ],
[ "https://www.amazon.fr/dp/2883530300/", "51P799WWJXL.jpg", "Les 5 piliers de la santé : Au-delà de la Méthode..."                                     , "de Philippe-Gaston Besson (Auteur), Alain Docteur Bondil (Auteur), André Docteur Denjean (Auteur), Philip Kéros (Auteur)" ],
[ "https://www.amazon.fr/dp/2850000051/", "41stgJvxpwL.jpg", "De nombreuses demeures"                                                                   , "de Gina Cerminara (Auteur)" ],
[ "https://www.amazon.fr/dp/2916878432/", "51kTX5nRBvL.jpg", "Vaccins, mensonges et propagande"                                                         , "de Sylvie Simon (Auteur)" ],
[ "https://www.amazon.fr/dp/2813200956/", "41LgNMekZGL.jpg", "Quand la couleur guérit : Psychologie et chromothératie"                                  , "de Michèle Delmas (Auteur)" ],
[ "https://www.amazon.fr/dp/2221048415/", "41kTWbTptCL.jpg", "Le massage"                                                                               , "de Lucinda Lidell (Auteur)" ],
[ "https://www.amazon.fr/dp/2221097629/", "31Fp-9KdF5L.jpg", "Guérir, le stress, l’anxiété, la dépression sans médicament ni psychanalyse"              , "de David Servan-Schreiber (Auteur)" ],
[ "https://www.amazon.fr/dp/2872110291/", "21DW6RBEACL.jpg", "Psycho-neuro immunologie"                                                                 , "de Francesco Bottaccioli (Auteur)" ],
[ "https://www.amazon.fr/dp/2922969045/", "41Ovvn9e48L.jpg", "L’adrénaline : Trop c’est trop ! Le syndrome du stress du 21e siècle"                     , "de James Wilson (Auteur), Collectif (Auteur), Jonathan V. Wright (Préface)" ]
]

DEVELOPPEMENT_PERSONNEL = [
[ "https://www.amazon.fr/dp/2896260307/", "51FJyH-ko3L.jpg", "La Divine Matrice"                                                                        , "de Gregg Braden (Auteur)" ],
[ "https://www.amazon.fr/dp/2980084352/", "41MQS4J4J8L.jpg", "La liberté d’être ou la voie de la plénitude"                                             , "de Annie Marquier (Auteur)" ],
[ "https://www.amazon.fr/dp/2951846304/", "51Sba-YEOEL.jpg", "Racines familiales de la “mal a dit”"                                                     , "de Gérard Athias (Auteur)" ],
[ "https://www.amazon.fr/dp/2951846312/", "41jlZ6slKFL.jpg", "La suite... Racines familiales de la “mal a dit”"                                         , "de Gérard Athias (Auteur)" ],
[ "https://www.amazon.fr/dp/271030385X/", "41Ce2AETjEL.jpg", "L’audace de vivre"                                                                        , "de Véronique Loiseleur (Auteur), Arnaud Desjardins (Auteur)" ],
[ "https://www.amazon.fr/dp/2826700286/", "51sMQt5m8CL.jpg", "La puissance de votre subconscient"                                                       , "de MURPHY Joseph Dr (Auteur)" ],
[ "https://www.amazon.fr/dp/2890444864/", "51QBmSrnlzL.jpg", "L’éveil de votre puissance intérieure"                                                    , "de Anthony Robbins (Auteur)" ],
[ "https://www.amazon.fr/dp/2920932187/", "519bu0V8XbL.jpg", "Les cinq blessures qui empêchent d’être soi-même"                                         , "de Lise Bourbeau (Auteur)" ],
[ "https://www.amazon.fr/dp/2970063883/", "41OOzDFyh2L.jpg", "Le grand livre de la vie"                                                                 , "de Stéphane Bruchez (Auteur)" ],
[ "https://www.amazon.fr/dp/2970063816/", "51PK6JE4-aL.jpg", "Ouvriers du ciel (les) - au-delà des apparences"                                          , "de Stéphane Bruchez (Auteur)" ],
[ "https://www.amazon.fr/dp/2710305933/", "41AEPQtvklL.jpg", "Le livre tibétain de la vie et de la mort"                                                , "de Dalaï-Lama (Préface), Sogyal Rinpoché (Auteur)" ],
[ "https://www.amazon.fr/dp/2916878874/", "41dEsrLxbgL.jpg", "Les 3 émotions qui guérissent"                                                            , "de Emmanuel Pascal (Auteur), David O’Hare (Préface)" ]
]

PHILOSOPHIE = [
[ "https://www.amazon.fr/dp/2253942200/", "41COJ+cDCyL.jpg", "Le Sacrifice interdit : Freud et la Bible"                                                , "de Marie Balmary (Auteur)" ]
]

CATEGORIES = [
    ("Nutrition", NUTRITION),
    ("Phytothérapie & Aromathérapie", PHYTOTHERAPIE_AROMATHERAPIE),
    ("Thérapies complémentaires", THERAPIES_COMPLEMENTAIRES),
    ("Développement personnel", DEVELOPPEMENT_PERSONNEL),
    ("Philosophie", PHILOSOPHIE),
]

HEADER = """---
title: Coin lecture
author: nico
date: 2016-01-10
weight: 3
thumbnail:
    desc: Coin lecture
    image: feature.jpg
---
"""

OUTPUT_FILE = (
    Path(__file__).resolve().parents[2]
    / "content"
    / "ressources"
    / "coin-lecture"
    / "index.md"
)


def create_html_string(books):
    lines = ['<div class="row">']
    for url, image, title, author in books:
        title_attribute = escape(title, quote=True)
        title_text = escape(title, quote=False)
        author_text = escape(author, quote=False)
        url_attribute = escape(url, quote=True)
        image_attribute = escape(image, quote=True)
        lines.extend(
            [
                '<div class="col-xs-6 col-sm-4 col-md-3">',
                '    <div class="portfolio-item">',
                '        <div class="hover-bg">',
                f'            <a title="{title_attribute}" href="{url_attribute}">',
                '                <div class="hover-text">',
                f'                    <h3>{title_text}</h3>',
                f'                    <small>{author_text}</small>',
                '                    <div class="clearfix"></div>',
                '                    <i class="fa fa-plus"></i>',
                '                </div>',
                f'                <img src="./images/{image_attribute}" class="img-responsive" alt="{title_attribute}">',
                '            </a>',
                '        </div>',
                '    </div>',
                '</div>',
            ]
        )
    lines.append('</div>')
    return "\n".join(lines) + "\n"


def main():
    sections = [HEADER]
    for heading, books in CATEGORIES:
        sections.append(f"<h2>{escape(heading)}</h2>\n")
        sections.append(create_html_string(books))

    OUTPUT_FILE.write_text("".join(sections), encoding="utf-8")


if __name__ == '__main__':
    main()
