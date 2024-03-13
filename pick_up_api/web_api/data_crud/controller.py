from flask import request,jsonify,Blueprint
from ..vrp_sol.model import Pick_up,Pick_up_lts
#
pick_up_db_blueprint=Blueprint(
    'pick_up_db',
    __name__,
    url_prefix='/vrp_db'
)
#
@pick_up_db_blueprint.route('/all')
def show_all_data():
    data=Pick_up_lts.objects()
    #
    return jsonify(data),200
#
@pick_up_db_blueprint.route('/pickup')
def pick_up_show():
    data=Pick_up.objects()
    #
    return jsonify(data),200
#
@pick_up_db_blueprint.route('/one')
def find_one():
    #
    id=request.args['id']
    #
    pickup=Pick_up_lts.objects(
        id=id
    ).first()
    #
    return jsonify(pickup)
@pick_up_db_blueprint.route('/delete')
def pickUp_delete():
    #
    pick_up=Pick_up.objects.limit(1)
    if pick_up:
        #
        pick_up.delete()
        #
        return jsonify({'message':'done'})
    #
    return jsonify({'message':'the object not find'})