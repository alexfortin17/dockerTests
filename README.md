Docker Dump

Exemple comment runner docker comme environnemnt en faisant un mount d'un bout de code:

D'abord, je me cree une image baser sur ubuntu et jajoute seulement python et python3
Jappelle cette image python:ubuntu

Je cd jusque dans le directory qui continent mon script python et je lance:

docker run --rm -v "$(pwd)":/app -w /app python:ubuntu sh -c 'python runbaby.py'

--rm indique a docker de detruire le container aussitot lexecution de la commande termine
-v "$(pwd)"/app indique de mounter le presently working directory sur le root du container sous /app
-w /app indique a Docker que son working directory doit etre /app
sh -c est une shell command et on lance le script avec la commande python
