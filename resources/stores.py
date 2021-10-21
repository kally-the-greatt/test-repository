from flask_restful import Resource
from models.stores import storeModel
class stores(Resource):
    def get(self,name):
        store=storeModel.find_by_name(name)
        if store:
            return store.json()
        return{"message":"store not found"},404
    def post(self,name):
        if storeModel.find_by_name(name):
            return {"message":"store already exists"}
        store=storeModel(name)
        try:
            store.save_to_db()
        except:
            {"message":"there was an error "}
        return store.json()
    def delete(self,name):
        store= storeModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message":"store has been deleted"}
class storelist(Resource):
    def get(self):
        return {"stores":[store.json() for store in storeModel.query.all()]}
