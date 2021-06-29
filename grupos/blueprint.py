from flask import Blueprint

grupos_routes = Blueprint(
    "grupos",
    __name__,
    url_prefix="/grupos"
)

@grupos_routes.route("")
def getGrupos():
    return "Lista de Grupos"