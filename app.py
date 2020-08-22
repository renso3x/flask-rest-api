import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from security import authenticate, identity
from resources.item import Item, ItemList
from resources.user import UserRegister, UserLogin, TokenRefresh
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTION'] = True
app.config['JWT_SECRET_KEY'] = 'thisshouldbesecret'
api = Api(app)

jwt = JWTManager(app)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/token-refresh')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
