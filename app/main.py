from flask import Flask, request, jsonify
from app.models import PricingRequest
from app.pricing import calculate_price

app = Flask(__name__)

@app.route("/price", methods=["POST"])
def get_price():
    try:
        data = request.get_json()

        pricing_request = PricingRequest(
            base_price=data["base_price"],
            demand=data["demand"],
            availability=data["availability"]
        )

        pricing_request.validate()

        final_price = calculate_price(
            pricing_request.base_price,
            pricing_request.demand,
            pricing_request.availability
        )

        return jsonify({"final_price": final_price}), 200

    except (KeyError, TypeError):
        return jsonify({"error": "Invalid request format"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
