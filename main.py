from avtorizacia import authenticate, identity
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from user import UserRegister




app = Flask(__name__)
app.secret_key = 'NIKA'
api = Api(app)


jwt = JWT(app, authenticate, identity) # /auth

items = []

rand = 0


class Item(Resource):
    @jwt_required()
    def get (self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'Messages': 'Ar moidzebna'}

    def post(self,name):
        global rand
        data = request.get_json(force = True) # moaq damatebiti informacia 
        item = {'id': str(rand), 'name': name, 'price': data['price'], 'age': data['age']}
        rand += 1
        items.append(item)
        return {'messages': 'Warmatebit Daemata'}

    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name'] != name, items)) # marto gansxvavebulebs tovebs
        return {"messages": "Item deleted"}

    def put(self,name):
        global items
        data = request.get_json(force = True) # moaq damatebiti informacia 
        print(items)
        item = next(filter(lambda x: x['name'] == name, items), None) # tovebs marto msgavss
        print(item)
        if item is None:
            item = {'name': name, 'price': data['price'], 'age': data['age']}
            items.append(item)
        else:
            item.update(data)
        return {'messages': 'Warmatebit ganaxlda'}



api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')

app.run(port = 5000, debug = True)
