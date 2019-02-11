from flask import Flask, Blueprint
from app.api.v1.routes.officeroutes import endpoint as officeblueprint
from app.api.v1.routes.partyroutes import endpoint as partyblueprint


def createapp():
    app = Flask(__name__)
    app.register_blueprint(partyblueprint)
    app.register_blueprint(officeblueprint)
    return app


