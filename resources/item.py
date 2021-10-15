

from flask_jwt import jwt_required
from flask_restful import Resource,reqparse
from models.item import ItemModel
class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("price",
        type=float,
        required=True,
        help="This field can't be left blank")
    parser.add_argument("store_id",
        type=int,
        required=True,
        help="an item must have a store id")
       
    @jwt_required()
    def get(self,name):
        items=ItemModel.find_by_name(name)
        if items:
            return items.json()
        return{"message":"item not found"},404
   
    def post(self,name):
        if ItemModel.find_by_name(name):
            return {"message":f"this {name} already exists"},400
        data=Item.parser.parse_args()
        item=ItemModel( name,**data)
        try:
            ItemModel.save_to_db(item)
        except:
            return{"message":"an error has occurred while inserting item"},500
       
        return item.json(), 201
    
    def delete(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        
        return{"message":"has been deleted"}
    def put(self,name):
       
        data=Item.parser.parse_args()
        item=ItemModel.find_by_name(name)
       
        if item is None:
           item= ItemModel(name,**data)
        else:
            item.price=ItemModel(**data)
        item.save_to_db()
        return item.json()
        

    
class ItemList(Resource):
    def get(self):
      
        return {"items":[x.json() for x in ItemModel.query.all()]}