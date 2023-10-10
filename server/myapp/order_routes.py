from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from myapp.models import Order
from myapp import db

# Create a blueprint for orders
order_bp = Blueprint('orders', __name__)

# Update the status of an order
@order_bp.route('/orders/<int:order_id>/status', methods=['PUT'])
@jwt_required()
def update_order_status(order_id):
    # Get the current user
    current_user = get_jwt_identity()

    # Find the order by ID
    order = Order.query.filter_by(order_id).first()

    if not order:
        return jsonify({"message": "Order not found"}), 404

    # Check if the user is the owner of the order
    if order.user.username != current_user:
        return jsonify({"message": "Unauthorized"}), 403

    data = request.get_json()
    new_status = data.get('status')

    if not new_status:
        return jsonify({"message": "Missing status in request data"}), 400

    # Update the order status
    order.status = new_status
    db.session.commit()

    return jsonify({"message": "Order status updated successfully"}), 200

@order_bp.route('/orders', methods=['POST'])
@jwt_required()
def place_order():
    try:
        # Get the current user
        current_user = get_jwt_identity()

        # Parse order data from the request JSON
        data = request.get_json()
        # Assuming you have fields like 'menu_item_id', 'quantity', and 'address' in the request JSON
        menu_item_id = data.get('menu_item_id')
        quantity = data.get('quantity')
     

        # You can perform validation on the received data here

        # Create a new order
        new_order = Order(
            user_id=current_user,  # Set the user ID to the current user
            menu_item_id=menu_item_id,
            quantity=quantity,
            status='Pending'  # You can set an initial status here
        )

        # Add the order to the database
        db.session.add(new_order)
        db.session.commit()

        return jsonify({"message": "Order placed successfully"}), 201

    except Exception as e:
        # Handle any errors or validation failures here
        return jsonify({"message": "Failed to place order", "error": str(e)}), 400