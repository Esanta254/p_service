

from flask import Blueprint, request, jsonify
from datetime import datetime
from app.models.database import get_db_connection
from app.middleware import login_required
import africastalking
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Africa's Talking API (Ensure the sandbox username and API key are correct)
africastalking.initialize(username="sandbox", api_key="atsk_dbe5f06626f2f7515a1e98e6db38d6020a15a2ed1f8b0a63c1e7dd7bac582e5876bd3b6e")
sms = africastalking.SMS

# Define the Blueprint
orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['POST'])
@login_required
def add_order(user=None):
    """
    Endpoint to add an order for a specific customer.
    """
    data = request.get_json()
    customer_id = data.get('customer_id')
    item = data.get('item')
    amount = data.get('amount')
    time = datetime.now()

    if not customer_id or not item or not amount:
        return jsonify({"error": "customer_id, item, and amount are required fields"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Verify customer existence
        cursor.execute("SELECT COUNT(*) FROM Customers WHERE Id = ?", (customer_id,))
        if cursor.fetchone()[0] == 0:
            logging.error(f"Customer with ID {customer_id} does not exist")
            return jsonify({"error": f"Customer with ID {customer_id} does not exist"}), 400

        # Insert order into the database
        cursor.execute(
            "INSERT INTO Orders (CustomerId, Item, Amount, Time) VALUES (?, ?, ?, ?)",
            (customer_id, item, amount, time)
        )
        conn.commit()

        # Fetch the customer's phone number
        cursor.execute("SELECT Phone FROM Customers WHERE Id = ?", (customer_id,))
        customer_phone = cursor.fetchone()[0]
        conn.close()

        # Send SMS to the customer
        sms_response = None
        if customer_phone:
            try:
                message = f"Dear Customer, your order for {item} has been successfully placed. Amount: {amount}."
                sms_response = sms.send(message, [customer_phone])
                logging.info(f"SMS sent to {customer_phone}: {sms_response}")
            except Exception as sms_error:
                logging.error(f"Error sending SMS: {sms_error}")

        response_payload = {
            "message": "Order added successfully.",
            "sms_response": sms_response or "No SMS sent"
        }
        return jsonify(response_payload), 201

    except Exception as e:
        logging.error(f"Unhandled Exception: {e}")
        return jsonify({"error": "An error occurred while processing the order."}), 500
