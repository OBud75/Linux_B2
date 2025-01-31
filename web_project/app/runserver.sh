#!usr/bin/bash


handle_request() {
    local request=$1
    echo "Requête reçue : $request"
    response=$(python3 $APP_DIR/request_handler.py "$request")
    echo "Réponse envoyée : $response"
    echo -en "$response"
}

while true; do
    # Ecoute les connexions entrantes sur le port 8080.
    # Netcat reçoit des données, les capture et les
    # passe à la commande dans laquelle il est utilisé.
    request=$(nc -l -k -p 8080 -q 1)
    echo "Connexion reçue"
    handle_request "$request"
done
