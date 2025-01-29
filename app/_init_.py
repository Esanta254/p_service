# app/__init__.py

# This can be left empty if you don't need to expose anything globally.
# Alternatively, you can import the create_app function here for convenience.
from .create_app import create_app

__all__ = ['create_app']
