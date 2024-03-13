from flask import Blueprint,jsonify,request
#
import json
#
import pandas as pd
#
import datetime
#
from ..vrp_sol import controller as vrp
#
from pick_up_api.pickUp_app.PickUp import vrp_by_geopy
#
from pick_up_api.Tools.jwt_authorization import jwt_required
#
from ..vrp_sol.model import Pick_up
#
pickup_delet_blueprint=Blueprint(
    'pickup_delet',
    __name__,
    url_prefix='/delete'
)
#
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJhYmRvdXkifQ.GpRh6JiLkfN5hT-OqaCCOuvRMxzaW46YscPBoWYjrl4
#
@pickup_delet_blueprint.before_request
def beford_delete():
    if(vrp.round is None):
        return {'error':'error we dnt have object'}
#
@pickup_delet_blueprint.route('/',methods=['POST'])
#@jwt_required
#def pick_up_delete(token):
def pick_up_delete():
    #
    #
    client = str(request.form['client'])
    #
    #pos = [int(x) for x in request.form['pos'].split(',')]
    #
    #wilaya = str(request.form['wilaya'])
    #
    #slot = str(request.form['slot'])
    #
    #
    print(client)
    #print(pos)
    #print(wilaya)
    #print(slot)
    #print(vrp.round)
    #
    #
    # print(Pick_up.objects.get(date = datetime.date.today()))
    #pick_up = Pick_up.objects.get(date= datetime.date.today(), wilaya=wilaya, slot=slot)
    #
    #data = pd.DataFrame(pick_up['data'])
    #
    #
    #round.find_and_annulation_dict(client, pos)
    resultat = vrp.round.find_and_annulation_dict_with_template(client)
    d = vrp.round.add_client_visualisation()
    #
    #
    if(isinstance(resultat,str)):
        return json.dumps({'sol': 'error','iframe':d['iframe']})
    else:
        return json.dumps({'sol': d['sol'],'iframe':d['iframe']})
    #