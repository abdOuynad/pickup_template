from flask import Blueprint,request,jsonify
from ..vrp_sol import controller as vrp
import json
##
pickup_tools_blueprint=Blueprint(
    'Pick_up_Tools',
    __name__,
    url_prefix='/tools'
)
##
@pickup_tools_blueprint.route('/next',methods=['POST'])
def nextStep():
    #
    car = request.form['car']
    print(car)
    print('===>',type(vrp.round))
    if vrp.round is None:
        return jsonify({'message':'no round u have creat new round'})
    else:
        vrp.round.next_step(car)
        print(vrp.round._vrp_affec_sol)
        return ('done')


