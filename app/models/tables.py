# from .database import get_db_connection

# def create_tables():
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()

#         # Create Customers table if it doesn't exist
#         cursor.execute("""
#             IF OBJECT_ID('Customers', 'U') IS NULL
#             CREATE TABLE Customers (
#                 Id INT IDENTITY(1,1) PRIMARY KEY,
#                 Name NVARCHAR(100) NOT NULL,
#                 Code NVARCHAR(50) NOT NULL
#             )
#         """)

#         # Create Orders table if it doesn't exist
#         cursor.execute("""
#             IF OBJECT_ID('Orders', 'U') IS NULL
#             CREATE TABLE Orders (
#                 Id INT IDENTITY(1,1) PRIMARY KEY,
#                 CustomerId INT NOT NULL,
#                 Item NVARCHAR(100) NOT NULL,
#                 Amount DECIMAL(10, 2) NOT NULL,
#                 Time DATETIME NOT NULL,
#                 FOREIGN KEY (CustomerId) REFERENCES Customers(Id)
#             )
#         """)

#         conn.commit()
#         conn.close()
#     except Exception as e:
#         print(f"Error creating tables: {e}")












from .database import get_db_connection

def create_tables():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Create Customers table if it doesn't exist
        cursor.execute("""
            IF OBJECT_ID('Customers', 'U') IS NULL
            CREATE TABLE Customers (
                Id INT IDENTITY(1,1) PRIMARY KEY,
                Name NVARCHAR(100) NOT NULL,
                Code NVARCHAR(50) NOT NULL,
                Phone NVARCHAR(15) NULL  -- Add Phone column, adjust size as necessary
            )
        """)

        # Create Orders table if it doesn't exist
        cursor.execute("""
            IF OBJECT_ID('Orders', 'U') IS NULL
            CREATE TABLE Orders (
                Id INT IDENTITY(1,1) PRIMARY KEY,
                CustomerId INT NOT NULL,
                Item NVARCHAR(100) NOT NULL,
                Amount DECIMAL(10, 2) NOT NULL,
                Time DATETIME NOT NULL,
                FOREIGN KEY (CustomerId) REFERENCES Customers(Id)
            )
        """)

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error creating tables: {e}")
