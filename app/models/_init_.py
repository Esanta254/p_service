# app/models/__init__.py

# You can import database utilities or leave it empty.
from .database import get_db_connection
from .tables import create_tables

__all__ = ['get_db_connection', 'create_tables']
