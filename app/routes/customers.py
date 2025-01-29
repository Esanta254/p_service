
# from flask import Blueprint, request, jsonify, session
# from app.models.database import get_db_connection
# from app.middleware import login_required  # Ensure this is correctly implemented in your project

# customers_bp = Blueprint('customers', __name__)

# @customers_bp.route('/customers', methods=['POST'])
# @login_required  # Protect the endpoint with authentication
# def add_customer(user):  # Accept the user parameter here
#     data = request.get_json()
#     name = data.get('name')
#     code = data.get('code')

#     if not name or not code:
#         return jsonify({"error": "Both 'name' and 'code' are required fields"}), 400

#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()

#         cursor.execute("INSERT INTO Customers (Name, Code) VALUES (?, ?)", (name, code))
#         conn.commit()
#         conn.close()

#         return jsonify({"message": "Customer added successfully"}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500














from flask import Blueprint, request, jsonify, session
from app.models.database import get_db_connection
from app.middleware import login_required 

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/customers', methods=['POST'])
@login_required  # Protect the endpoint with authentication
def add_customer(user):  # Accept the user parameter here
    data = request.get_json()
    name = data.get('name')
    code = data.get('code')
    phone = data.get('phone')  # Accept phone number

    if not name or not code or not phone:
        return jsonify({"error": "Both 'name', 'code', and 'phone' are required fields"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert the customer including the phone number
        cursor.execute("INSERT INTO Customers (Name, Code, Phone) VALUES (?, ?, ?)", (name, code, phone))
        conn.commit()
        conn.close()

        return jsonify({"message": "Customer added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
