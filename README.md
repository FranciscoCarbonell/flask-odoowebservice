# flask-odoowebservice

**requirements**

* flask
* pymongo
* mongokat
* flask-mongokat
* mongodb server install in computer
* flask-jwt-extended

**install**

`python setup.py install`

or

`pip install flask-odoowebservice`

**config**

```
ODOO_URL - default: http://localhost
ODOO_PORT - default: 8069
ODOO_DB - default: odoo8db

```

**more config**

* flask-jwt-extended: https://flask-jwt-extended.readthedocs.io/en/latest/options.html#general-options
* flask-mongokat: https://github.com/FranciscoCarbonell/flask-mongokat

**example**

```python

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

```
you can also use the webservice directly

```python

from flask import Flask,jsonify
from flask_odoowebservice.webService import OdooWebServiceClient

app = Flask(__name__)

odoo_client = OdooWebServiceClient(app)

@app.route('/')
def index():
    uid = odoo_client.get_uid('yourusername','yourpassword')
    return jsonify(uid=uid),200

app.run('localhost',port=8000)

```







