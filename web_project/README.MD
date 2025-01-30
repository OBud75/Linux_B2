# Créer une page web d'authentification

# Login, create_user, delete_user, update_user
# Variables env : différencier dev de la prod
# -> logs (dev : erreurs sur la console, prod : dans un fichier + log les login d'utilisateurs)
# SQL -> dev sqlite3 | prod : postgres

# Créer des taches en background :
# Tache récurente 1*par semaine : envoyer les logs par email et supprimer le fichier
# cron, systemctl, supervisor
