
<h1>ClusterProg : Cluster editing problem</h1>

<b>Auteurs :</b> MiaouLelion & nael93260 (<a href="https://github.com/nael93260">Github</a>)

Le programme "ClusterProg" permet de créer une union de cliques à partir d'un Graph quelconque.

L'exécution du programme se fait grâce à la commande suivante :
<i>cat file.gr | python3 ClusterProg.py > Solution.txt</i>

Le fichier texte envoyé au programme (file.gr ici) doit répondre à un certain format. 
Chaque ligne doit correspondre à une arrête particulière, les sommets étant séparés d'un espace.
Des instances d'essais sont disponibles dans le dossier "instances".

<b>Exemple</b> : <br>
2 3<br>
2 4<br>
1 3<br>
4 1<br>

"Le sommet 2 est lié au sommet 3"...

Le fichier "Solution.txt" contiendra toutes les éditions (suppressions) d'arrêtes nécessaires à l'obtention d'une union de cliques.
