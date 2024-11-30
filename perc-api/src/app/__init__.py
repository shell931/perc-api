# imports
from flask import Flask
from flask_cors import CORS

# Here we're gonna import the blueprints
from src.api.v1.auth import auth_bp
from src.api.v1.perc_service import perc_service_bp

# function than create a flask app with CORS
def create_app():
    app = Flask(__name__)
    #CORS(app)
    CORS(app, resources={r"*": {"origins": "*"}})

    # Here we're gonna register the blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(perc_service_bp)
    
    return app
