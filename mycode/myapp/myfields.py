from copy import deepcopy
from flask_restful import fields

one_fields = {
    "id": fields.Integer,
    # "name": fields.String
    "ch_name": fields.String(attribute="name")
}

two_fields = {
    "data":fields.List(fields.String),
    "code": fields.Integer(default=1),
    "msg": fields.String(default="ok")
}
"""
{
    "msg":"ok",
    "data":[
        "抽烟",
        "喝酒",
        "敲代码"
    ],
    "code":1
}
"""


three_fields = {
    "code": fields.Integer(default=1),
    "msg": fields.String(default="OK"),
    "data": fields.Nested(one_fields)
}

"""
{
    "msg":"呵呵哒",
    "data":{
        "id":1,
        "ch_name":"tom"
    },
    "code":1
}
"""

four_fields = deepcopy(three_fields)
four_fields['data'] = fields.List(fields.Nested(one_fields))

"""
{
    "code":1,
    "msg":"OK",
    "data":[
        {
            "id":1,
            "ch_name":"tom"
        },
        {
            "id":2,
            "ch_name":"lisi"
        }
    ]
}
"""