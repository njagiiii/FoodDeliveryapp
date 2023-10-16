from flask import request,jsonify,Blueprint,flash
from myapp import bcrypt
from myapp.models import User,TokenBlocklist
from flask_jwt_extended import (create_access_token,create_refresh_token,
                                jwt_required,
                                get_jwt_identity,
                                get_jwt)
from flask_cors import cross_origin

# create blueprints for authentication
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
@cross_origin(origin='http://localhost:5173', supports_credentials=True)

def register_user():
    data =request.get_json()
    # extract necessary data nneeded
    username = data['username']
    email= data['email']
    password= data['password']

    # check input fields are not empty
    if 'username' not in data or 'email' not in  data or 'password' not in data:
        return jsonify({"message":"input fields requred"}), 400
    
    # check if username exists
    user = User.query.filter_by(username=username).first()

    if user:
        return jsonify({"msg":"User alredy exists"}), 400
    
    # hash password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user=User(username=username, email=email, password=hashed_password)
    new_user.save()

    flash(f'Your account has been created! Proceed to login', 'success')

    return jsonify({"message":"user created"})


@auth_bp.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if user:
        user.delete()
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404




@auth_bp.route('/login', methods=['GET', 'POST'])
@cross_origin(origin='http://localhost:5173', supports_credentials=True)
def login():
     if request.is_json:
            try:
                # Parse JSON data from the request body
                data = request.get_json()
                username = data.get("username")
                password = data.get("password")

                if not username or not password:
                    return {"message": "Missing required fields."}

                # Query the database for the user by username
                user = User.query.filter_by(username=username).first()

                if not user:
                    return {"message": "User not found!"}, 404

                # Check if the provided password matches the hashed password
                if bcrypt.check_password_hash(user.password, password):
                    # Create access and refresh tokens for the user
                    access_token = create_access_token(identity=user.id)
                    refresh_token = create_refresh_token(identity=user.id)

                    return {
                        "message": "Login Successful",
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    }, 200
                else:
                    return {"message": "Invalid Login!"}, 401
            except Exception as e:
                return {"message": str(e)}, 500
     else:
         return {"message": "Request Content-Type must be 'application/json'"}, 400


@auth_bp.route('/refresh', methods=['GET'])
@jwt_required(refresh=True)
def refresh_access():
    identity = get_jwt_identity()

    
    # create a new access token
    new_access_token = create_access_token(identity=identity)

    return jsonify({"access": new_access_token}),200

# log out scenario
@auth_bp.route('/logout', methods=['POST'])
@jwt_required(verify_type=False)
@cross_origin(origin='http://localhost:5173', supports_credentials=True)

def logout():
    jtw = get_jwt()
    jti = jtw['jti']
    token_type = jtw['type']

    token_revoked = TokenBlocklist(jti=jti)
    token_revoked.save()

    return jsonify({"message":f"{token_type}token revoked successfully"}), 200






            


