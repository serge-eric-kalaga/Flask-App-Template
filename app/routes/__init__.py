from flask_jwt_extended import JWTManager
from flask_restx import Namespace, fields, Api, Resource
from flask_jwt_extended.exceptions import NoAuthorizationError 
from jwt.exceptions import ExpiredSignatureError
from werkzeug.exceptions import NotFound, InternalServerError, Unauthorized, BadRequest
from ..tools import response
from .is_on import is_on_namespace
from .utilisateur import utilisateur_namespace

authorizations = {
        "Bearer Auth":
        {
            'type':"apiKey",
            'in':'header',
            'name':'Authorization',
            'description':'Add a JWT with a ** Bearer **\n add Bearer before adding the token'
        }
}


api = Api(title="Vote en ligne", description="Appli de vote en ligne", authorizations=authorizations, security='Bearer Auth')



#================================ ADD NAMESPACES TO API 
api.add_namespace(is_on_namespace, path="/is_on" )
api.add_namespace(utilisateur_namespace, path="/utilisateur" )
    


#================================ ERRORS HANDLING

error_model = api.model("error_model", 
{
    "status":fields.Boolean(),
    "message":fields.String()
})


@api.errorhandler(NotFound)
@api.marshal_with(error_model)
def notFound(error):
    return {"status":False, "message":f"{error}"}

@api.errorhandler(InternalServerError)
@api.marshal_with(error_model)
def internalError(error):
    return {"status":False, "message":f"{error}"}
    
@api.errorhandler(NoAuthorizationError)
@api.marshal_with(error_model)
def noauthorization(error):
    return {'status':False, 'message':'missing JWT identification error'}

@api.errorhandler(ExpiredSignatureError)
@api.marshal_with(error_model)
def expiredSignature(error):
    return {'status':False, 'message': 'JWT signature Expired'}

@api.errorhandler(Unauthorized)
@api.marshal_with(error_model)
def unAuthorizedAccess(error):
    return {"status":False, "message":f"{error}"}

@api.errorhandler(BadRequest)
@api.marshal_with(error_model)
def badRequest(error):
    return {"status":False, "message":f"{error}"}



