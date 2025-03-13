# Linux Exam B2

## Exercices à faire en cours
* Faire un dossier par exercice avec script + fichier d'outputs + screenshots.
* Pensez à commit + push à la fin de l'examen.

___
0. Generals
    - Quelle différence entre GNU et Linux ?
    - Qui est l'inventeur de Linux ? Citez un autre programme célèbre dont il est à l'origine.

1. FileSystem
    - Créer un dossier "assets" à la racine du dossier d'exam
    - Dans ce dossier, créer 10 fichiers "img_1.png", "img_2.png" ...
    - Dans ce même dossier, créer un fichier "du_texte.txt" contenant "Hello, world".  
    - Renommer tous les fichiers .png du dossier en "img_1.jpeg", "img_2.jpeg" ...
    - Créer un dossier "medias" dans le dossier "assets", déplacez y tous les fichiez .jpeg du dossier "assets".
    - A quoi servent les formats de fichiers (.png, .txt, .jpeg) ?
    - Créer un fichier "script" (toujours dans le dossier) qui affiche "Hello world", ajoutez #!/usr/bin/bash 
    - A quoi sert la ligne #!/usr/bin/bash ? Quelles différences avec le lancement du script via "bash script" ?

2. Commandes
    - Créer un dossier "commandes"
    - Créer un fichier "too_long" contenant 100 lignes : "Ligne 1", "Ligne 2", "Ligne 3" ...
    - Affichier les 5 premières lignes.
    - Afficher les 7 dernières lignes.
    - Afficher les 3 lignes avec les nombres les plus élevés mais en utilisant head + sort
    - Afficher uniquement la ligne "Ligne 42".
    - Remplacer le ligne "Ligne 42" par "The Ultimate Question of Life, the Universe and Everything"
    - Créer un script "script" qui :
	1. Lit tous les arguments passés au script.
	2. Passe le premier argument à une fonction "check_argv", cette fonction doit retourner 1 si l'argument n'est pas vide et 0 s'il n'y a pas d'arguments.
	3. Récupérez la valeur retournée par la fonction et affichez la.
    - En quelques mots, quelle est la différence entre un if/else et un switch.
    - Dans le fichier "script", ajouter un switch qui check si le 2ieme argument passé au programme est "hello", "toto" ou autre chose.

3. Users
    - Lister les utilisateurs actuellement sur votre machine.
    - Créer un nouvel utilisateur "Toto" avec un groupe du même nom.
    - Lister les groupes auquels fait parti ce nouvel utilisateur.
    - Créer un groupe "shared" avec votre utilisateur classique + Toto
    - Expliquer brièvement à quoi sert de préfixer une commande par le mot "sudo".
    - Tous les utilisateurs peuvent ils utiliser ce mot clé ?
    - Comment donner à Toto le droit d'utiliser "sudo" pour une commande spécifique telle que "apt install"?
    - Comment donner à Toto le droit d'utiliser "sudo" en permanence ?
    - Pourquoi ne pas tout faire avec l'utilisateur root ?
    - Comment faire pour qu'à chaque fois que toto démarre un shell, un message "bienvenue toto" s'affiche ?

4. Permissions
    - Créer un dossier "shared" à la racine du dossier de l'examen.
    - Mettez "Toto" en tant que propriétaire du dossier "shared".
    - Dans ce dossier, créer un fichier "owned_by_toto" contenant "echo toto".
    - "Toto" doit être également propriétaire du fichier.
    - Rendez ce fichier executable avec bash (#!/usr/bin/bash).
    - Donnez à "Toto" le droit d'executer ce script.
    - Que fait le commande "sudo chmod g+x owned_by_toto" ?
    - Que fait la commande "sudo chown root:root owned_by_toto" ?

5. Environnement
    - Créer un dossier "environ"
    - Créer un script qui permette à l'utilisateur de choisir la valeur d'une variable d'environnement "ENVIRON" : les choix sont "dev", "prod", et "test".
    - Lorsque l'utilisateur change la variable "ENVIRON", affichez un message de confirmation.
    - Dans ce dossiez, créer un environnement virtuel python "pythonvenv". Activez le, installez la librairie flask et mettez le résultat de la commande "pip freeze" dans un fichier "requirements.txt".
    - A quoi sert cette dernière opération ?
    - Ajouter un fichier .gitignore, ajoutez y "pythonvenv/".
    - A quoi sert cette dernère opération ?
    - Quels autres fichiers ou dossiers serait il approprié d'ajouter dans le .gitignore ? Pourquoi ?
    - A quoi servent les commandes "apt update", "apt upgrade" ?
    - Quelles différence entre les commandes "apt autoclean", "apt clean", "apt autoremove" et "apt purge"?

6. Systemctl
    - Quelle est la commande pour prendre en compte les changements dans la configuration des services ?
    - Comment démarrer et stopper un service ?
    - A quoi sert l'option "restart" ? Quelles différences avec "start" ?

7. Cron
    - Quelle est la commande pour lister les taches cron ?
    - Comment créer une tache cron qui lance le script "owned_by_toto" avec l'utilisateur Toto à 1h30 du matin, tous les mercredis du mois.
    - Expliquez brièvement à quoi servent les dossiers cron.weekly, cron.hourly et cron.monthly

8. Logs
    - Quels sont les différents niveaux de logs ?
    - Créer un script "logger" qui, quand il est lancé, ajoute dans un fichier "logs" une ligne avec l'utilisateur actuel ainsi que l'heure à laquelle le programme est lancé.
    - Comment limiter la taille des fichiers de log du journal (journalctl) à 200Mo ?
    - Comment configurer les logs de l'application "nginx" (situés dans /var/log/nginx.log) pour que des rotations soient effectuées tous les mois en conservant les 12 derniers mois de logs, compressant les plus ancients, et en créant un nouveau fichier avec un mod "644 root root"
    - Dans la pratique, pourquoi créer des règles de rotation de log ?

9. Web
    - Quelle est la différence entre http et https ?
    - Donnez le nom de 2 programmes qui permettent de faire des requetes http.
    - Par convention, à quoi sont reservés les ports 80, 22 et 443 ?
    - Comment activer et désactiver le pare feu par défaut ? Comment lister les règles entrantes et sortantes ?
    - A quoi sert le programme Nginx ?
    - A quoi correspondent les initiales MVC ? Quel avantage offre cette architecture d'application ?
    - A quoi correspondent les initiales CRUD ?


## Projets
Prennez le temps de bien faire je ne suis pas au jour près.

1. Suivre un des tutos au choix sur la mise en production d'une application Flask.
    - Vous pouvez le faire dans une VM.
    - Prennez des screenshots de votre avancement peut suffire.
    - Si vous utilisez une instance AWS ou un service équivelent c'est encore mieux.

___

### Tips
* Lisez la documentation
* C'est ok d'utiliser ChatGPT ou d'autres LLM à condition de le faire intelligement
    - Ne lui demandez pas d'être logique !! Il ne fait que recracher ce qu'il a en base de données.
    - Ok pour des questions de syntaxe
    - Toujours le "challenger", essayez par exemple de lui faire dire l'inverse de ce qu'il vient de dire.
* Testez votre code petit à petit : Bien organiser le code en fichiers, fonctions etc vous aidera à tester.
* Prendre le temps de bien nommer les choses !
    - On évite par exemple les noms de variables type "x" ou "truc".
    - Un bon nom de variable décrit précisement l'objet sans pour autant être trop long.
* Eviter les commentaires "inutiles", le code s'explique de lui même.

