# Thème Hugo CNL Spirit

Le thème CNL Spirit a été développé à l’origine à partir du thème Spirit8. Il constitue désormais un thème propre au site du CNL.

## Dépendances attendues

Le site consommateur fournit :

- `params.brand`, `params.description`, `params.keywords`, `params.author` et `params.favicon` ;
- un menu Hugo `main` dont les URL ciblent les sections de la page d’accueil ;
- un fichier `data/home.yaml` contenant `hero`, `about`, `sections`, `quote`, `testimonials`, `contact` et `notFound` ;
- les sections de contenu `therapeutes`, `therapies`, `ressources` et `articles`, avec les paramètres historiques `infos` et `thumbnail` ;
- les images de fond et l’icône dans `static/img/`.

Le fichier `data/home.yaml` du site CNL constitue l’exemple complet du schéma attendu.

## Ressources du thème

Les feuilles de style, scripts et polices sont livrés dans `static/`. Les images éditoriales et de marque restent hors du thème afin qu’un autre site puisse fournir les siennes sans modifier le thème.
