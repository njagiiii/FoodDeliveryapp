from myapp.models import Restaurant,Menu,User,Order,OrderItem
from myapp import db
from flask import jsonify,request,Blueprint,request
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_cors import cross_origin



# create a blueprint for restaurant
restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('/add', methods=['POST'])
def add_restaurant():
    data = request.get_json()

    # extract necessary data
    name = data['name']
    cuisine_type = data['cuisine_type']

    existing_restaurant = Restaurant.query.filter_by(name=name).first()

    if existing_restaurant:
        return jsonify({"message":"Restaurant already exists"}), 400
    
    new_restaurant = Restaurant(name=name, cuisine_type=cuisine_type)
    new_restaurant.save()
    
    return jsonify({"msg": "Restaurant added successfully"}), 200

# get all the restaurants
@restaurant_bp.route('/dashboard', methods=['GET'])
@jwt_required()
@cross_origin(origin='http://localhost:5173', supports_credentials=True)

def get_restaurant():
    restaurants = Restaurant.query.all()
    restaurant_list = [{'id':restaurant.id, "name":restaurant.name, "cuisine_type":restaurant.cuisine_type}for restaurant in restaurants]

    return jsonify(restaurant_list),200

# get the restaurants menu
@restaurant_bp.route('/restaurantss/<int:restaurant_id>/menu', methods=['GET'])
@jwt_required()
@cross_origin(origin='http://localhost:5173', supports_credentials=True)

def get_menu(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return jsonify({"message":"Restaurant not found"})
    
    menu = Menu.query.filter_by(restaurant_id=restaurant_id).all()
    serialized_menu = [{"id": item.id, "name": item.name, "description": item.description, "price": item.price, "image_url":item.image_url} for item in menu]

    return jsonify(serialized_menu), 200


@restaurant_bp.route('/checkout', methods=['POST'])
@jwt_required()
def checkout():
    current = get_jwt_identity()
    user = User.query.filter_by(username=current).first()

    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()

    restaurant_id = data.get('restaurant_id')# restaurant i want to place an order
    menu_items_id = data.get('menu_items_id') # items i want from this restaurant(so query the menu table)

    if not restaurant_id or not menu_items_id :
        return jsonify({"message":"Missing required id"}), 400
    
    # place new order
    new_order = Order(user_id=user.id, restaurant_id=restaurant_id)
    new_order.save()

    for menu_item_id in menu_items_id:
        menu_item = Menu.query.get(menu_item_id)
        if menu_item:
            quantity =1
            order_item = OrderItem(order_id=new_order.id, menu_id=menu_item_id, quantity=quantity)
            db.session.add(order_item)

    db.session.commit()

    return jsonify({"message": "Order placed successfully"}), 201
