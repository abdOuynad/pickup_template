from flask import request,jsonify,copy_current_request_context
from functools import wraps
from pick_up_api.config import SECRET_KEY
#
import jwt
import json
import secrets
#
def jwt_required(f):
    @wraps(f)
    def decorator(*args,**kwargs):
        token=None
        #
        if 'Authorization' in request.headers:
            token=request.headers['Authorization']
            #
        if token is None:
            return jsonify({'message':'we dnt have any jwt key'})
            #
        print('SECRET KEY ==>',SECRET_KEY)
        jwt_encode=jwt.encode({'key':'abdouy'},SECRET_KEY,algorithm='HS256')
        token=token.split('Bearer ')[1]
        if jwt_encode == token:
            return f(token,*args,**kwargs)
        #
        print(token)
        print(jwt_encode)
        return jsonify({'message': 'error the key not working try again '})
        #
    return decorator