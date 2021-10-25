

from flask_restful import Resource, reqparse


from models.user import UserModel
class Registeruser(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("username",
    type=str
,
required=True,
help="field must be selected ")
    parser.add_argument("password",
    type=str
,
required=True,
help="field must be selected ")
    def  post(self):
        data=Registeruser.parser.parse_args()
        if UserModel.find_username(data["username"]):
            return {"message":"this user already exist"},400
        user=UserModel(**data)
        user.save_to_db()
        return {"message":"user has been created"},201