from flask import Flask
from flask_odoowebservice.odooResources import OdooListResource,OdooRetrieveResource,\
OdooDeleteResource, OdooAttributes, webClient, OdooAuth, OdooApi

app = Flask(__name__)
app.config.from_object('config.Developement')

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
OdooApi.add_resource(OdooAuth,'/auth/')

app.run('0.0.0.0',port=8000)
