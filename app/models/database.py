import pyodbc

DB_CONFIG = {
    'server': 'SANTHAMO\\SQLEXPRESS',
    'database': 'Products',
    'username': 'sa',  # Replace with your username
    'password': 'pass123',  # Replace with your password
}

CONNECTION_STRING = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={DB_CONFIG['server']};"
    f"DATABASE={DB_CONFIG['database']};"
    f"UID={DB_CONFIG['username']};"
    f"PWD={DB_CONFIG['password']}"
)

def get_db_connection():
    return pyodbc.connect(CONNECTION_STRING)
