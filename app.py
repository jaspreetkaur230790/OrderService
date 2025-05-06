from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import random

def mock_payment_gateway(amount):
    return random.choice([True, False])  # Simulates success or failure randomly

import app




app = Flask(__name__)

# Payment service URL
PAYMENT_SERVICE_URL = "https://book-store-6uww.onrender.com/api/payment"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/payment', methods=['POST'])
def create_payment():
    # Get data from the order request
    data = request.json
    amount = data.get('amount')
    item_name = data.get('itemName')

    # Send POST request to payment service
    response = requests.post(PAYMENT_SERVICE_URL, json={"amount": amount, "itemName": item_name})
    if response.status_code == 200:
        return redirect(url_for('payment_gateway'))
    else:
        return jsonify({"error": "Payment initiation failed"}), 400

@app.route('/api/payment-info', methods=['GET'])
def payment_info():
    # Get payment info (order details)
    return jsonify({
        "itemName": "Order 1",
        "amount": 2.00
    })

@app.route('/api/processPayment', methods=['POST'])
def process_payment():
    # Process payment based on card details received
    card_info = request.json
    # In real life, you'd validate the card and process the payment here
    payment_successful = True  # Mocking success here

    if payment_successful:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failure"}), 400

@app.route('/api/order/complete')
def order_complete():
    # Simulate order completion
    status = request.args.get('status')
    return render_template('order_complete.html', status=status)

@app.route('/api/paymentGateway')
def payment_gateway():
    # Payment gateway page where users enter card details
    return render_template('payment_gateway.html')

if __name__ == "__main__":
    app.run(debug=True)