
import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import Registeruser
from resources.item import Item,ItemList
from resources.stores import stores,storelist
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL",'sqlite:///cola.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.secret_key="badguy"
api=Api(app)

jwt=JWT(app,authenticate,identity)


api.add_resource(stores,"/store/<string:name>")
api.add_resource(storelist,"/stores")
api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList,"/items")
api.add_resource(Registeruser,"/register")
if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)