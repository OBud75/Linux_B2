from flask import Flask, render_template

# La boucle infinie est gérée par Flask
# Flask se charge aussi de gérer les
# requêtes HTTP : on se retrouve avec un
# objet request qui contient les informations
# de la requête HTTP (avec les infos de
# l'utilisateur), et un objet response.
app = Flask(import_name=__name__)

@app.route(rule="/")
def index():
    # Flask s'occupe de générer le HTML à
    # partir des templates + données passées
    # en paramètre (context de la request)
    return render_template(
        template_name_or_list="index.html",
        title="Home",
        content="This is the index page!"
    )
