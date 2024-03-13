from flask import Flask,jsonify,request
from flask_mongoengine import MongoEngine
#
#
app=Flask('__name__')
#
#app.config['SECRET_KEY']='abdouy'
#
app.config['MONGODB_SETTINGS']={
    'host':'mongodb://localhost:27017/tp',
}
#
mongo=MongoEngine()
#
mongo.init_app(app)
#
#
class User(mongo.Document):
    name=mongo.StringField()
    password=mongo.StringField()
    def __repr__(self):
        return {
            "name": self.name,
            "password":self.password
        }
#
@app.route('/test')
def index():
    u=User(name='abdouy',password='abdouy')
    u.save()
    return jsonify(u)
#
@app.route('/')
def aff():
    name=request.args['name']
    print(name)
    user= User.objects(name=name).first()
    return jsonify(user)
#
if __name__ =='__main__':
    app.run(debug=True,port=5005)
