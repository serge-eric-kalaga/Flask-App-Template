from flask_restx import Namespace, Resource, fields
from ..models import Utilisateur
from ..tools import response, responseListModel, responseModel
from flask import request

utilisateur_namespace = Namespace(name="Utilisateur", description="Utilisateur Namespace")

utilisateur_model = utilisateur_namespace.model("Utilisateur", {
    "username" :fields.String(required=True),
    "email" : fields.String(),
})

register_utilisateur_model = utilisateur_namespace.model("Utilisateur", {
    "username" :fields.String(required=True),
    "password" :fields.String(required=True),
    "email" : fields.String(),
})

response_utilisateur = responseModel("Response utilisateur", utilisateur_namespace, utilisateur_model)
response_utilisateurs = responseListModel("Response utilisateurs", utilisateur_namespace, utilisateur_model)

@utilisateur_namespace.route("/", methods=["GET", "POST"])
class GetCreateUser(Resource):
    
    @utilisateur_namespace.marshal_list_with(response_utilisateurs)
    def get(self):
        return response(status=True, data=Utilisateur.getAll(), status_code=200)
    
    
    @utilisateur_namespace.expect(register_utilisateur_model)
    def post(self):
        data = request.get_json()
        user = Utilisateur(username = data.get('username'), 
                           password = data.get('password'), 
                           email = data.get('email'))
        user.save()
        return response(status=True, status_code=201, data="Utilisateur created !")
    

@utilisateur_namespace.route("/<string:username>/", methods=["PUT", "GET", "DELETE"])
class ShowUpdatedeleteUser(Resource):
    
    @utilisateur_namespace.marshal_list_with(response_utilisateurs)
    def get(self, username):
        return response(status=True, data=Utilisateur.getOne(username=username), status_code=200)
    
    def delete(self, username):
        Utilisateur.delete(username=username)
        return response(status=True, status_code=200, data="Utilisateur deleted !")
    
    @utilisateur_namespace.expect(register_utilisateur_model)
    def put(self, username):
        user = Utilisateur.getOne(username=username)
        data = request.get_json()
        user.edit(
            username = data.get("username"),
            password = data.get("password"),
            email = data.get("email") or None,
        )
        return response(status=True, status_code=200, data="Utilisateur updated !")