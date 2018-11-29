from flask_restful import Api

from myapp.views import HumenAPI, HobbyAPI, ThreeAPI, FourAPI, HumenNewAPI

api = Api()
def init_api(app):
    api.init_app(app)

api.add_resource(HumenAPI, "/", "/humen/<int:id>")
api.add_resource(HobbyAPI, "/hobby/")
api.add_resource(ThreeAPI, "/three/" )
api.add_resource(FourAPI, "/four/")
api.add_resource(HumenNewAPI, "/new_humen")
