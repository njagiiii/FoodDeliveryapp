from flask import Blueprint, request,jsonify
from myapp.models import Menu
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_cors import cross_origin

# create blueprints
menu_bp = Blueprint('menus', __name__)


# add menu
@menu_bp.route('/add_menu', methods=['POST'])
def add_menu():
    data = request.get_json()

    name = data['name']
    description = data['description']
    price =data['price']
    restaurant_id = data['restaurant_id']
    image_url = data['image_url']

    # create a menu item
    new_menu = Menu(name=name, description=description, price=price, restaurant_id=restaurant_id, image_url=image_url)
    new_menu.save()

    return jsonify({"msg":"menu added successfully"}), 200


@menu_bp.route('/menus', methods=['GET'])
@jwt_required()
@cross_origin(origin='http://localhost:5173', supports_credentials=True)

def get_all_menus():
    menus = Menu.query.all()
    serialized_menus = [{
        "id": menu.id,
        "name": menu.name,
        "description": menu.description,
        "price": menu.price,
        "restaurant_id": menu.restaurant_id,
        "image_url": menu.image_url
    } for menu in menus]
    return jsonify(serialized_menus), 200


@menu_bp.route('/menus/<int:restaurant_id>', methods=['GET'])
@jwt_required()
@cross_origin(origin='http://localhost:5173', supports_credentials=True)

def get_menus_for_restaurant(restaurant_id):
    menus = Menu.query.filter_by(restaurant_id=restaurant_id).all()
    if not menus:
        return jsonify({"message": "No menus found for this restaurant"}), 404
    
    serialized_menus = [{
        "id": menu.id,
        "name": menu.name,
        "description": menu.description,
        "price": menu.price,
        "restaurant_id": menu.restaurant_id,
        "image_url": menu.image_url
    } for menu in menus]
    return jsonify(serialized_menus), 200
