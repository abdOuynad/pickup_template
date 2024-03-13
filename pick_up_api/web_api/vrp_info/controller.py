from flask import Blueprint,jsonify,request
#
import json
#
from ..vrp_sol import controller as vrp
#
pickup_info_blueprint=Blueprint(
    'pickup_info',
    __name__,
    url_prefix='/pick_info'
)
#
@pickup_info_blueprint.route('/')
def pickup_info():
    #
    if vrp.round is None:
        return jsonify({'message':'create vrp object and try again'})
    else:
        vrp.round.vrp_sol_info_dict()
        return json.dumps(vrp.round._vrp_info)