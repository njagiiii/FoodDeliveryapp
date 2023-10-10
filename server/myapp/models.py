from datetime import datetime
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import BLOB
from myapp import db

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules=('-order.user', '-order.restaurant.order_item1',)

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique=True, nullable = False)
    email = db.Column(db.String(120), nullable=False, unique = True)
    password= db.Column(db.String(60), nullable=False)
    order = db.relationship('Order', back_populates ='user')
   
    def __repr__(self):
        return f"User( '{self.username}', '{self.email}', '{self.image_file}')"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    
class Order(db.Model,SerializerMixin):
    __tablename__ = "orders" 

    serialize_rules=('-user.order', '-restaurant.orders.menus', '-order_item1.menu_items.order1')

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    status = db.Column(db.String(50), nullable=False, default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', back_populates='order')

    restaurant = db.relationship('Restaurant', back_populates ='orders')

    order_item1 = db.relationship('OrderItem',back_populates='order1')

    def __repr__(self):
        return f"Order('{self.id}')"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_rules = ('-orders.restaurant', '-menus.restaurants')

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique=True, nullable = False)
    cuisine_type = db.Column(db.String,  nullable = False)

    orders = db.relationship('Order', back_populates ='restaurant')

    menus = db.relationship('Menu', back_populates ='restaurants')

    def __repr__(self):
        return f"Restaurant('{self.name}', {self.cuisine_type}')"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    


class Menu(db.Model, SerializerMixin):
    __tablename__ = 'menus'

    serialize_rules = ('-restaurants.menus', '-order_items.menu_items',
                        {'name': '-menu_association.order_items.order_item_association', 'overlaps': 'menu_items,order_items'},

                       )

    id = db.Column(db.Integer, primary_key = True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String(255))
    price = db.Column(db.Integer)
    image_url = db.Column(db.String)

    restaurants = db.relationship('Restaurant', back_populates='menus')

    order_items = db.relationship('OrderItem', secondary='menu_order_item_association', back_populates='menu_items')

    def __str__(self):
        return self.name
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    


class OrderItem(db.Model, SerializerMixin):
    __tablename__ = 'order_items'

    serialize_rules =('-menu_items.order_items', '-order1.order_item1',{'name': '-order_item_association.menu.menu_association', 'overlaps': 'menu_items,order_items'})

    id = db.Column(db.Integer, primary_key = True)
    order_id= db.Column(db.Integer, db.ForeignKey('orders.id'))
    menu_id= db.Column(db.Integer, db.ForeignKey('menus.id'))
    quantity = db.Column(db.Integer, nullable=False)

    menu_items = db.relationship('Menu', secondary='menu_order_item_association', back_populates='order_items')
    order1 = db.relationship('Order', back_populates='order_item1')

    def __str__(self):
        return f"OrderItem #{self.id} - Menu Item {self.menu_items.name}, Quantity{self.quantity}"
    

class MenuOrderItemAssociation(db.Model):
    __tablename__ = 'menu_order_item_association'

    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), primary_key=True)
    order_item_id = db.Column(db.Integer, db.ForeignKey('order_items.id'), primary_key=True)

    menu = db.relationship('Menu', backref='menu_association')
    order_item = db.relationship('OrderItem', backref='order_item_association')

serialize_rules = (
        '-menu.menu_association.order_items.order_item_association',  
        '-order_item.order_item_association.menu.menu_association',
        {'name': '-order_item_association.menu.menu_association', 'overlaps': 'menu_items,order_items'}  
    )


# keep track of our accesstokens blocklist
class TokenBlocklist(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        jti = db.Column(db.String(), nullable=True)
        created_at = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)


        def __repr__(self):
             return f"<Token('{self.jti})>"
        
        def save(self):
             db.session.add(self)
             db.session.commit()











