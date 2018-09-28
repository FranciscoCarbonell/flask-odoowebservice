from flask import Flask,make_response,current_app
from flask_odoowebservice.odooResources import OdooListResource,OdooRetrieveResource,\
OdooDeleteResource,OdooAttributes,OdooAuthResource,webClient
from flask_mongokat import MongokatApp

app = Flask(__name__)
app.config.from_object('config.Developement')
mongoapp = MongokatApp(app)

webClient.init_app(app)

class Odoo(OdooListResource):
    pass

class OdooRetrieve(OdooRetrieveResource):
    pass

class OdooDelete(OdooDeleteResource):
    pass

class Attributes(OdooAttributes):
    pass

webClient.add_resource(Odoo,'/<module>/')
webClient.add_resource(OdooRetrieve,'/<module>/<int:pk>/')
webClient.add_resource(OdooDelete,'/delete/<module>/<int:pk>/')
webClient.add_resource(Attributes,'/<module>/attributes/')
webClient.add_resource(OdooAuthResource,'/auth/')

webClient.init_routes()

app.run('localhost',port=8000)