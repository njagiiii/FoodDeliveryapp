from flask import Flask, request, jsonify,Blueprint



# create blueprints
associate_bp = Blueprint('association', __name__)

# Dummy data to simulate the database
menu_order_item_association_data = []

@associate_bp.route('/associate_menu_order_item', methods=['POST'])
def associate_menu_order_item():
    data = request.get_json()
    menu_id = data.get('menu_id')
    order_item_id = data.get('order_item_id')
    
    if menu_id is None or order_item_id is None:
        return jsonify({"message": "Invalid input"}), 400

    # Check if the association already exists
    for association in menu_order_item_association_data:
        if association['menu_id'] == menu_id and association['order_item_id'] == order_item_id:
            return jsonify({"message": "Association already exists"}), 400

    # Create the association and add it to the data
    new_association = {"menu_id": menu_id, "order_item_id": order_item_id}
    menu_order_item_association_data.append(new_association)

    return jsonify({"message": "Association created successfully"}), 201

@associate_bp.route('/remove_association', methods=['DELETE'])
def remove_association():
    data = request.get_json()
    menu_id = data.get('menu_id')
    order_item_id = data.get('order_item_id')

    if menu_id is None or order_item_id is None:
        return jsonify({"message": "Invalid input"}), 400

    # Find and remove the association
    removed = False
    for association in menu_order_item_association_data:
        if association['menu_id'] == menu_id and association['order_item_id'] == order_item_id:
            menu_order_item_association_data.remove(association)
            removed = True
            break

    if not removed:
        return jsonify({"message": "Association not found"}), 404

    return jsonify({"message": "Association removed successfully"}), 200
