from flask_restful import reqparse

one_parse = reqparse.RequestParser()
one_parse.add_argument("name", required=True, help="name 字段是必填", location="form")
one_parse.add_argument("age", type=int, required=True, help="age is needed", location="form")

two_parse = one_parse.copy()
two_parse.add_argument("id", type=int, required=True)
two_parse.replace_argument("name", location="form")
two_parse.replace_argument("age", type=int, location="form")

three = two_parse.copy()
three.replace_argument("name")
three.remove_argument("age")