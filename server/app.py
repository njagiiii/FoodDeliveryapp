
from myapp import app,models,jwt,db
from flask import jsonify
from myapp.auth import auth_bp
from myapp.user_account import user_bp
from myapp.restaurant_routes import restaurant_bp
from myapp.menu_routes import menu_bp
from myapp.order_routes import order_bp
from myapp.association_routes import associate_bp
from myapp.models import TokenBlocklist



# register blueprint for auth
app.register_blueprint(auth_bp, url_prefix='/auth')

# register blueprint for user
app.register_blueprint(user_bp, url_prefix='/users')

# register blueprint for restaurant
app.register_blueprint(restaurant_bp, url_prefix='/restaurants')

# register blueprint for menu
app.register_blueprint(menu_bp, url_prefix='/menus')

# register blueprint for order
app.register_blueprint(order_bp, url_prefix='/orders')

# register blueprint for association
app.register_blueprint(associate_bp, url_prefix='/association')



@jwt.token_in_blocklist_loader
def token_in_blocklist_callback(jwt_header, jwt_data):
        jti = jwt_data['jti']

        token =db.session.query(TokenBlocklist).filter(TokenBlocklist.jti == jti).scalar()
        
        return token is not None

@jwt.expired_token_loader
def expired_token(jwt_header, jwt_data):
    return jsonify({"message":"Expired token"}), 401

@jwt.invalid_token_loader
def invalid_token(error):
    return jsonify({"message":"signature verification failed", "error":"invalid token"}), 401

@jwt.unauthorized_loader
def missing_token(error):
    return jsonify({"message":"missing token"}), 401



if __name__ == '__main__':
    app.run(debug=True)

 