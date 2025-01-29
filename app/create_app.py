# from flask import Flask
# from app.models.tables import create_tables
# from app.routes.customers import customers_bp
# from app.routes.orders import orders_bp

# def create_app():
#     app = Flask(__name__)

#     # Register blueprints
#     app.register_blueprint(customers_bp)
#     app.register_blueprint(orders_bp)

#     # Create tables at startup
#     with app.app_context():
#         create_tables()

#     return app













from flask import Flask
from app.models.tables import create_tables
from app.routes.customers import customers_bp
from app.routes.orders import orders_bp
from config import Config  # Import your Config class

def create_app():
    app = Flask(__name__)

    # Load configuration from the Config class
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(customers_bp)
    app.register_blueprint(orders_bp)

    # Create tables at startup
    with app.app_context():
        create_tables()

    return app
