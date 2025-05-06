from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/processPayment', methods=['POST'])
def process_payment():
    try:
        data = request.get_json()
        # Validate card info
        if not validate_card_info(data['card']):
            raise ValueError("Invalid card details")

        # Simulate payment processing
        if not process_payment_gateway(data['amount']):
            raise Exception("Payment gateway error")
        
        return jsonify({"status": "success", "message": "Payment processed successfully"})
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def validate_card_info(card):
    # Logic to validate card details (mocked)
    return True if card else False

def process_payment_gateway(amount):
    # Logic to simulate payment gateway processing (mocked)
    return True

if __name__ == '__main__':
    app.run(debug=True)