
from functools import wraps
import jwt
from flask import request,jsonify
#
#'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoiYWJkb3V5In0.a20czASam6wvbPddYFwM4eFs6V6p5M7foOstQEc-558'
def jwt_required(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        token=None
        if request.headers['Authorization']:
            token=request.headers['Authorization']
            #
        if token is None:
            return jsonify({'message':'we dnt have any jwt key'})
            #
        try:
            jwt_encode=jwt.encode({'key':'abdouy'},app.config['SECRET_KEY'],algorithm='HS256')
            if jwt_encode == token:
                return f(*args,**kwargs)
        except:
            return jsonify({'message': 'error the key not working try again '})
        #
    return wrapper()


