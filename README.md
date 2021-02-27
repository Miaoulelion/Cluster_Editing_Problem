
@uteurs : MiaouLelion & nael93260

Le programme "ClusterProg" permet de créer une union de cliques à partir d'un Graph quelconque.

L'exécution du programme se fait grâce à la commande suivante :
cat file.gr | python3 ClusterProg.py > Solution

Le fichier texte envoyé au programme doit répondre à un certain format. 
Chaque ligne doit correspondre à une arrête particulière, les sommets étant séparés d'un espace.

<b>Exemple</b> : <br>
2 3<br>
2 4<br>
1 3<br>
4 1<br>

"Le sommet 2 est lié au sommet 3"...

Le fichier "Solution" contiendra toutes les éditions (ajouts et suppressions) d'arrêtes nécessaires à l'obtention d'une union de cliques.
