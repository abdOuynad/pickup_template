from flask import Blueprint,request,jsonify,redirect,url_for,render_template
#
from pick_up_api.Tools.jwt_authorization import jwt_required
#
main_blueprint=Blueprint(
    'main',
    __name__,
    static_folder='../static',
    template_folder='../templates',
)
#
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJhYmRvdXkifQ.GpRh6JiLkfN5hT-OqaCCOuvRMxzaW46YscPBoWYjrl4
#
@main_blueprint.before_request
#def before_main():
    #print("before_request executing!")
#
@main_blueprint.route('/')
#@jwt_required
#def home(token):
def home():
    return render_template("index.html")
    #return jsonify({'message':'Hello in pick up Service'}),200
#
