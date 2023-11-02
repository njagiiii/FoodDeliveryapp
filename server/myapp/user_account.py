from flask import jsonify,request,Blueprint
from server.myapp.models import User,Order
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_cors import cross_origin

# create a blueprint for user
user_bp= Blueprint('users', __name__)

# user related activities

@user_bp.route('/users', methods=['GET'])
@jwt_required()
@cross_origin(origin='http://localhost:5173', supports_credentials=True)
def get_all_users():
    try:
        users = User.query.all()
        user_list = []

        for user in users:
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                # Include other user attributes as needed
            }
            user_list.append(user_data)

        return jsonify(user_list), 200

    except Exception as e:
        return {"error": str(e)}, 500

# user to see their profile only
@user_bp.route('/account', methods=['GET'])
@jwt_required()
@cross_origin(origin='http://localhost:5173', supports_credentials=True)
def user_account():
    try:
        current_user_id = get_jwt_identity()
        user = User.query.filter_by(id=current_user_id).first()

        if not user:
            return {"message": "User not found"}, 404

        # Serialize the user data using the SerializerMixin
        user_data = user.to_dict()

        return user_data, 200

    except Exception as e:
        return {"error": str(e)}, 500



@user_bp.route('/orders', methods=['GET'])
@jwt_required()
def get_order():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()

    if user:
        orders = Order.query.filter_by(user_id=user.id).all()
        # serialize the data
        seriaized_data=[]
        for order in orders:
            order_data ={
                "restaurant":order.restaurant.name,
                "status":order.status,
                "created_at":order.created_at.strftime("%Y-%m-%d %H:%M:%S")

            }
            seriaized_data.append(order_data)
            return jsonify(seriaized_data), 200
        else:
            return jsonify({"message":'user not found', "error":"order not found"}), 404

    
@user_bp.route('/edit', methods=['PATCH'])
@jwt_required()
def edit_profile():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()

    # check if user exists
    if not user:
        return jsonify({"message":"User not found"})
    
    data = request.get_json()

    # see if username or email exists
    if 'username' in data:
        user.username = data['username']

    if 'email' in data:
        user.email = data['email']

    user.save()

    return jsonify({"message":"profile updated successfully"}), 200