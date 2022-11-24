from typing import Dict, Any
from flask_restx import fields
from datetime import datetime


def response(status:bool=0, data:Any="", status_code=200) -> Dict:
    var = {'status':status, "date_query":str(datetime.utcnow()), 'status_code':status_code, 'data':data}
    return var

def responseModel(name:str, api:object, dataModel:Any,)->Dict:
    reps = api.model(name ,{'status':fields.Boolean(), 'date_query' : fields.String(), 'data':fields.Nested(dataModel)})
    return reps

def responseListModel(name:str, api:object, dataModel:Any)->Dict:
    reps = api.model(name ,{'status':fields.Boolean(), 'date_query' : fields.String(), 'data':fields.List(fields.Nested(dataModel))})
    return reps