from flask import Blueprint

mensagens_routes = Blueprint(
    "mensagens",
    __name__,
    url_prefix="/mensagens"
)

@mensagens_routes.route("")
def getGrupos():
    return "Lista de Mensagens"