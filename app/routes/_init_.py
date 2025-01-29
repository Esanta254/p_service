
from .customers import customers_bp
from .orders import orders_bp
from .auth_routes import auth_bp

# Expose blueprints for easier imports
__all__ = ['customers_bp', 'orders_bp', 'auth_bp']









