from flask_restx import Resource, Namespace
from ..tools import response


is_on_namespace = Namespace(name="API is available", description="Tester si l'api est en ligne")

@is_on_namespace.route("/")
class IsOn(Resource): 

    def get(self):
        return response(status=True, data="API is available")