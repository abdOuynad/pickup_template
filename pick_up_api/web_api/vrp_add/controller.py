import datetime

from flask import Blueprint,request,jsonify
import json
import ast
import pandas as pd
#s
from pick_up_api.pickUp_app.PickUp import vrp_by_geopy
#
from..vrp_sol import controller as vrp
#
from ..vrp_sol.model import Pick_up
#
from ..vrp_sol.controller import round
#
from pick_up_api.Tools.jwt_authorization import jwt_required
#
pickup_add_blueprint=Blueprint(
    'pick_up_add',
    __name__,
    url_prefix='/pick_add'
)
#
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJhYmRvdXkifQ.GpRh6JiLkfN5hT-OqaCCOuvRMxzaW46YscPBoWYjrl4
#
@pickup_add_blueprint.before_request
def before_add():
    print('beford add =>',vrp.round)
    if vrp.round is None:
        return {'info':"error we dnt have Object for add"}

#
@pickup_add_blueprint.route('/',methods=['POST'])
#@jwt_required
#def pick_up_add(token):
def pick_up_add():
    #
    client = str(request.form['client'])
    #
    latitude = str(request.form['l'])
    #
    longitude = str(request.form['g'])
    #
    #pos = [int(x) for x in request.form['pos'].split(',')]
    #
    #status = [str(x) for x in request.form['sattus'].split(',')]
    #
    #wilaya = str(request.form['wilaya'])
    #
    #slot = str(request.form['slot'])
    #
    #coordonne = [(x,y) for x,y in zip(latitude, longitude)]
    coordonne = (latitude,longitude)
    new_client_data = (client,coordonne)
    #
    #
    print(client)
    print(coordonne)
    print(latitude)
    print(longitude)
    print('new data =>',new_client_data)
    print('old coordonne ==>',vrp.round._client_data)
    vrp.round._client_data.append(new_client_data)
    print('new coordonne ==>', vrp.round._client_data)
    #print(pos)
    #print(wilaya)
    #print(slot)
    #print(vrp.round)
    '''print(datetime.date.today())
    print(Pick_up.objects.get(date = datetime.date.today()))
    pick_up = Pick_up.objects.get(date=datetime.date.today(), wilaya=wilaya, slot=slot)
    print('pickup in data ==>',pick_up)'''

    v = vrp.round.add_clien_to_vrp_dict_with_template(client, (latitude,longitude))
    d = vrp.round.add_client_visualisation()
    return json.dumps({'driver': v, 'sol': d['sol'],'iframe':d['iframe']})
    #
