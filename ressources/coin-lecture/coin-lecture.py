#!/usr/bin/env python
# -*- coding: utf-8 -*-

Nutrition = [
[ "http://www.amazon.fr/dp/2877240568/", "51B4J9RA5ZL.jpg", u"Le lait : une sacrée vacherie ?"                                                          , u"de Nicolas Le Berre  (Auteur)" ],
[ "http://www.amazon.fr/dp/2857421540/", "41T6NKQ74GL.jpg", u"La nutrithérapie : bases scientifiques et pratique médicale"                              , u"de Curtay (Auteur)" ],
[ "http://www.amazon.fr/dp/2868398871/", "41X4DR6C0SL.jpg", u"L'Alimentation, ou la troisième médecine"                                                 , u"de Jean Seignalet  (Auteur), Henri Joyeux (Préface)" ],
[ "http://www.amazon.fr/dp/2501046676/", "51y5F6pV4LL.jpg", u"L'index glycémique : un allié pour mieux manger"                                          , u"de Jennie Brand-Miller  (Auteur), Kaye Foster-Powell  (Auteur), Stephen Colagiuri (Auteur), Gérard Slama  (Auteur)" ],
[ "http://www.amazon.fr/dp/2290336335/", "51Isq9qY0TL.jpg", u"Je mange donc je maigris... et je reste mince !"                                          , u"de Michel Montignac  (Auteur)" ],
[ "http://www.amazon.fr/dp/2950902103/", "515jb0rpw+L.jpg", u"La santé vient en mangeant"                                                               , u"de Pierre-Henri Meunier  (Auteur)" ],
[ "http://www.amazon.fr/dp/2883431205/", "21531HNE1DL.jpg", u"Le régime crétois"                                                                        , u"de Docteur Jacques Gardan (Auteur)" ],
[ "http://www.amazon.fr/dp/2909757129/", "41CX1RN+6AL.jpg", u"Comment nourrir naturellement son enfant de 0 à 10 ans"                                   , u"de Lionel Clergeaud (Auteur), Chantal Clergeaud (Auteur)" ],
[ "http://www.amazon.fr/dp/2872110259/", "516HicXilYL.jpg", u"Pour en finir avec Pasteur : Un siècle de mystification scientifique"                     , u"de Docteur Éric Ancelet (Auteur)" ],
[ "http://www.amazon.fr/dp/2916878149/", "51r1RkyK-CL.jpg", u"Lait, mensonges et propagande"                                                            , u"de Thierry Souccar  (Auteur)" ],
[ "http://www.amazon.fr/dp/2804152359/", "51DnXHvQe4L.jpg", u"Micronutrition, santé et performance : Comprendre ce qu'est vraiment la micronutrition"   , u"de Denis Riché  (Auteur), Didier Chos  (Auteur)" ],
[ "http://www.amazon.fr/dp/2883533210/", "51hcyuI787L.jpg", u"L'énergie du cru : Mettez 75 % de cru dans votre assiette et de la vie dans votre corps !", u"de Leslie Kenton  (Auteur), Susannah Kenton (Auteur), Karen Vago (Traduction)" ],
[ "http://www.amazon.fr/dp/2883539464/", "41KRg9WGi3L.jpg", u"Les incroyables vertus des smoothies verts"                                               , u"de Colette Pairain (Auteur), Nadège Pairain (Auteur)" ],
[ "http://www.amazon.fr/dp/2253131504/", "51BHl8OgsBL.jpg", u"Les aliments contre le cancer : La prévention du cancer par l'alimentation"               , u"de Richard Beliveau (Auteur)" ],
[ "http://www.amazon.fr/dp/2916878173/", "5168cEiwy7L.jpg", u"Cholestérol, mensonges et propagande"                                                     , u"de Michel de Lorgeril  (Auteur)" ],
[ "http://www.amazon.fr/dp/2874610526/", "51xcMoqFU6L.jpg", u"Nutrithérapie : Bases scientifiques et pratique médicale"                                 , u"de Jean-Paul Curtay  (Auteur)" ],
[ "http://www.amazon.fr/dp/287211078X/", "51d9nPHw9AL.jpg", u"Ecosystème intestinal et santé optimale : Nouvelle approche diagnostique et thérapeutique", u"de Georges Mouton  (Auteur)" ],
[ "http://www.amazon.fr/dp/2916878483/", "51Xox7RB3UL.jpg", u"Le régime hormone"                                                                        , u"de Thierry Hertoghe  (Auteur), Margherita Enrico  (Auteur)" ],
[ "http://www.amazon.fr/dp/2253085073/", "414CJchKiYL.jpg", u"Guide familial des aliments soigneurs"                                                    , u"de Jean-Paul Curtay (Docteur) (Auteur)" ],
[ "http://www.amazon.fr/dp/2954103205/", "51PO+KJEM8L.jpg", u"TIME Nutrition “Faites de l'aliment votre médicament”"                                    , u"de Jean-René MESTRE (Auteur), Jean-Robert RAPIN (Auteur)" ]
]

Phytotherapie_aromatherapie = [
[ "http://www.amazon.fr/dp/2857079192/", "41GXCZCYZVL.jpg", u"Aromathérapie essentielle : Huiles essentielles et parfums pour le corps et l'âme"        , u"de Jean-Louis Abrassart  (Auteur)" ],
[ "http://www.amazon.fr/dp/2035071259/", "514WFVSEJ9L.jpg", u"Encyclopédie des plantes médicinales: Identification, préparations, soins"                , u"de Paul Iserin (Préface), Collectif (Auteur)" ],
[ "http://www.amazon.fr/dp/2035822246/", "51Q02ieAFZL.jpg", u"Le guide de l'aromathérapie"                                                              , u"de Denise Whichello Brown  (Auteur), Marie-Noëlle Pichard (Traduction)" ]
]

Therapies_complementaires = [
[ "http://www.amazon.fr/dp/284899357X/", "51X2bPANO-L.jpg", u"Homéopathie guide pratique"                                                               , u"de Albert-Claude Quemoun (Auteur)" ],
[ "http://www.amazon.fr/dp/2212548036/", "51LFouB2ysL.jpg", u"Le grand livre de la naturopathie"                                                        , u"de Christian Brun (Auteur)" ],
[ "http://www.amazon.fr/dp/2290348279/", "51ybjuwGB2L.jpg", u"Médecin des trois corps"                                                                  , u"de Janine Fontaine  (Auteur)" ],
[ "http://www.amazon.fr/dp/2883530300/", "51P799WWJXL.jpg", u"Les 5 piliers de la santé : Au-delà de la Méthode..."                                     , u"de Philippe-Gaston Besson (Auteur), Alain Docteur Bondil (Auteur), André Docteur Denjean (Auteur), Philip Kéros (Auteur)" ],
[ "http://www.amazon.fr/dp/2850000051/", "41stgJvxpwL.jpg", u"De nombreuses demeures"                                                                   , u"de Gina Cerminara  (Auteur)" ],
[ "http://www.amazon.fr/dp/2916878432/", "51kTX5nRBvL.jpg", u"Vaccins, mensonges et propagande"                                                         , u"de Sylvie Simon  (Auteur)" ],
[ "http://www.amazon.fr/dp/2813200956/", "41LgNMekZGL.jpg", u"Quand la couleur guérit : Psychologie et chromothératie"                                  , u"de Michèle Delmas  (Auteur)" ],
[ "http://www.amazon.fr/dp/2221048415/", "41kTWbTptCL.jpg", u"Le massage"                                                                               , u"de Lucinda Lidell (Auteur)" ],
[ "http://www.amazon.fr/dp/2221097629/", "31Fp-9KdF5L.jpg", u"Guérir, le stress, l'anxiété, la dépression sans médicament ni psychanalyse"              , u"de David Servan-Schreiber  (Auteur)" ],
[ "http://www.amazon.fr/dp/2872110291/", "21DW6RBEACL.jpg", u"Psycho-neuro immunologie"                                                                 , u"de Francesco Bottaccioli  (Auteur)" ],
[ "http://www.amazon.fr/dp/2922969045/", "41Ovvn9e48L.jpg", u"L'adrénaline : Trop c'est trop ! Le syndrome du stress du 21e siècle"                     , u"de James Wilson  (Auteur), Collectif (Auteur), Jonathan V. Wright (Préface)" ]
]

Developpement_personnel = [
[ "http://www.amazon.fr/dp/2896260307/", "51FJyH-ko3L.jpg", u"La Divine Matrice"                                                                        , u"de Gregg Braden (Auteur)" ],
[ "http://www.amazon.fr/dp/2980084352/", "41MQS4J4J8L.jpg", u"La liberté d'être ou la voie de la plénitude"                                             , u"de Annie Marquier  (Auteur)" ],
[ "http://www.amazon.fr/dp/2951846304/", "51Sba-YEOEL.jpg", u"Racines familiales de la “mal a dit”"                                                     , u"de Gérard Athias  (Auteur)" ],
[ "http://www.amazon.fr/dp/2951846312/", "41jlZ6slKFL.jpg", u"La suite... Racines familales de la “mal a dit”"                                          , u"de Gérard Athias  (Auteur)" ],
[ "http://www.amazon.fr/dp/271030385X/", "41Ce2AETjEL.jpg", u"L'audace de vivre"                                                                        , u"de Véronique Loiseleur  (Auteur), Arnaud Desjardins (Auteur)" ],
[ "http://www.amazon.fr/dp/2826700286/", "51sMQt5m8CL.jpg", u"La puissance de votre subconscient"                                                       , u"de MURPHY Joseph Dr (Auteur)" ],
[ "http://www.amazon.fr/dp/2890444864/", "51QBmSrnlzL.jpg", u"L'éveil de votre puissance intérieure"                                                    , u"de Anthony Robbins  (Auteur)" ],
[ "http://www.amazon.fr/dp/2920932187/", "519bu0V8XbL.jpg", u"Les cinq blessures qui empêchent d'être soi-même"                                         , u"de Lise Bourbeau  (Auteur)" ],
[ "http://www.amazon.fr/dp/2970063883/", "41OOzDFyh2L.jpg", u"Le grand livre de la vie"                                                                 , u"de Stéphane Bruchez  (Auteur)" ],
[ "http://www.amazon.fr/dp/2970063816/", "51PK6JE4-aL.jpg", u"Ouvriers du ciel (les) - au-delà des apparences"                                          , u"de Stéphane Bruchez  (Auteur)" ],
[ "http://www.amazon.fr/dp/2710305933/", "41AEPQtvklL.jpg", u"Le livre tibétain de la vie et de la mort"                                                , u"de Dalaï-Lama (Préface), Sogyal Rinpoché (Auteur)" ],
[ "http://www.amazon.fr/dp/2916878874/", "41dEsrLxbgL.jpg", u"Les 3 émotions qui guérissent"                                                            , u"de Emmanuel Pascal  (Auteur), David O'Hare (Préface)" ]
]

Philosophie = [
[ "http://www.amazon.fr/dp/2253942200/", "41COJ+cDCyL.jpg", u"Le Sacrifice interdit : Freud et la Bible"                                                , u"de Marie Balmary  (Auteur)" ]
]




def createHTMLString( HTMLArray ):
    htmlstring = ""
    htmlstring += '<div class="row">\n'
    for item in HTMLArray:
        htmlstring += '<div class="col-xs-6 col-sm-4 col-md-3">\n'
        htmlstring += '\t<div class="portfolio-item">\n'
        htmlstring += '\t\t<div class="hover-bg">\n'
        htmlstring += '\t\t\t<a title="%s" href="%s">\n' % ( item[ 2 ], item[ 0 ] )
        # htmlstring += '\t\t\t\t<div class="non-hover-text">\n'
        # htmlstring += '\t\t\t\t\t<h4><br/>%s...<br/></h4>\n' % ( item[ 2 ][ 0:16 ] )
        # htmlstring += '\t\t\t\t\t<small> </small>\n'
        # htmlstring += '\t\t\t\t</div>\n'
        htmlstring += '\t\t\t\t<div class="hover-text">\n'
        htmlstring += '\t\t\t\t\t<h4>%s</h4>\n' % ( item[ 2 ] )
        htmlstring += '\t\t\t\t\t<small> </small>\n'
        htmlstring += '\t\t\t\t\t<div class="clearfix"></div>\n'
        htmlstring += '\t\t\t\t\t<i class="fa fa-plus"></i>\n'
        htmlstring += '\t\t\t\t</div>\n'
        htmlstring += '\t\t\t\t<img src="./images/%s" culass="img-responsive" alt="..." />\n' % ( item[ 1 ] )
        htmlstring += '\t\t\t</a>\n'
        htmlstring += '\t\t</div>\n'
        htmlstring += '\t</div>\n'
        htmlstring += '</div>\n'
    htmlstring += '</div>\n'
    return htmlstring

def main():

    strheader = u"""---
title: Coin lecture
author: nico
date: 2016-01-10
weight: 3
thumbnail:
    desc: Coin lecture
    image: feature.jpg
---
"""

    indexfilename = "index.md"
    indexfile = open( indexfilename, 'w' )
    indexfile.write( strheader.encode( 'utf-8' ) )

    htmlstring = ""
    htmlstring += u"<h2>Nutrition</h2>\n"
    htmlstring += createHTMLString( Nutrition )
    htmlstring += u"<h2>Phytothérapie &amp; Aromathérapie</h2>\n"
    htmlstring += createHTMLString( Phytotherapie_aromatherapie )
    htmlstring += u"<h2>Thérapies complémentaires</h2>\n"
    htmlstring += createHTMLString( Therapies_complementaires )
    htmlstring += u"<h2>Développement personnel</h2>\n"
    htmlstring += createHTMLString( Developpement_personnel )
    htmlstring += u"<h2>Philosophie</h2>\n"
    htmlstring += createHTMLString( Philosophie )

    indexfile.write( htmlstring.encode( 'utf-8' ) )
    indexfile.close


if __name__ == '__main__':

    main()
