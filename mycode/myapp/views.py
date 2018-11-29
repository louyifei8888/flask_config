# from myapp.ext import api
from .models import *
from flask import Blueprint, request
from flask_restful import Resource, fields, marshal_with
from .myfields import *
from .myparse import *

blue = Blueprint("myapp", __name__)
def init_blue(app):
    app.register_blueprint(blue)



class HumenAPI(Resource):

    @marshal_with(one_fields)
    def get(self, id):
        h = Humen.query.get(id)
        return h



class HobbyAPI(Resource):

    @marshal_with(two_fields)
    def get(self):
        hobby = ["抽烟", "喝酒", "敲代码"]

        return {"data": hobby}



class ThreeAPI(Resource):

    @marshal_with(three_fields)
    def get(self):
        id = int(request.args.get("id"))
        humen = Humen.query.get_or_404(id)
        return {"data": humen, "msg": "呵呵哒"}


class FourAPI(Resource):

    @marshal_with(four_fields)
    def get(self):
        humens = Humen.query.all()
        return {"data": humens, "iiiii":"ok"}

class HumenNewAPI(Resource):

    @marshal_with(one_fields)
    def post(self):
#         创建数据
#       解析参数
        args = one_parse.parse_args()
        humen = Humen(
            name=args.get("name"),
            age=args.get("age")
        )
        return humen

    @marshal_with(one_fields)
    def put(self):
#         更新数据
#         解析参数
        args = dict(two_parse.parse_args())
        id = args.get("id")
#         找要查的数据
        humen = Humen.query.get_or_404(id)
#       get("age", humen.age)
        print(args)
        print(type(args))
        humen.age = args.get("age") if args.get("age") else  humen.age
        humen.name = args.get("name") if args.get("name") else humen.name
        db.session.add(humen)
        db.session.commit()
        return humen

    def delete(self):
#         解析参数
        args = three.parse_args()
#         找到数据
        humen = Humen.query.get_or_404(args.get("id"))
#         删除数据
        db.session.delete(humen)
        db.session.commit()
        return {"code": 1}





