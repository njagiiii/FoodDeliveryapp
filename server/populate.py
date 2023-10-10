from myapp import db,app
from myapp.models import User, Restaurant, Menu, OrderItem,Order,MenuOrderItemAssociation

def populate_data():
    with app.app_context():
        db.session.query(User).delete()
        db.session.query(Restaurant).delete()
        db.session.query(Menu).delete()
        db.session.query(OrderItem).delete()
        db.session.query(Order).delete()
        db.session.query(MenuOrderItemAssociation).delete()

        db.session.commit()
        

        print('data deleted.')

if __name__ == '__main__':
    populate_data()