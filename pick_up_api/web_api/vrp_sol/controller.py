from flask import Blueprint,request,jsonify,render_template
import json
import time
import datetime
import pandas as pd
import folium
#
from .model import Pick_up_lts,Pick_up
#
from pick_up_api.pickUp_app.PickUp import vrp_by_geopy
from pick_up_api.Tools.jwt_authorization import jwt_required
#
pick_up_blueprints=Blueprint(
    'pick_up',
    __name__,
    template_folder='../templates',
    url_prefix="/pick_up"
)
#
round=None
#
colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen',
'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'black', 'lightgray']
#
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJhYmRvdXkifQ.GpRh6JiLkfN5hT-OqaCCOuvRMxzaW46YscPBoWYjrl4
#
'''@pick_up_blueprints.before_request
def before_vrp():
    global round
    #
    #when server crached
    #
    print(round)
    if round is None and Pick_up.objects():
        #
        pick_up=Pick_up.objects.get()
        #
        data=pd.DataFrame(pick_up['data'])
        #
        round=vrp_by_geopy(
            clients=pick_up['clients'],
            cars=pick_up['cars'],
            coordonne=pick_up['coordonne'],
            init=pick_up['init'],
            df=data,
            vrp_affec_sol=pick_up['vrp_sol']
        )
        return jsonify(round._vrp_affec_sol),200
    elif round is not None:
        return jsonify({'message':'we cant add new round'})'''
    #
@pick_up_blueprints.route('/',methods=['POST'])
#@jwt_required
#def vrp_sol_api(token):
def vrp_sol_api():
    #
    global round
    print('request ==> ',request.headers)
    print('form ==>',request.form)
    #
    clients = request.form['clients']
    latitude = request.form['l']
    longitude = request.form['g']
    init = 2
    #init = request.form['init']
    cars = request.form['cars']
    cars_latitude = request.form['cl']
    cars_longitude = request.form['ci']
    wilaya = str(request.form["wilaya"])
    slot = str(request.form['slot'])
    #
    print('client -->',clients)
    print('latitude -->',latitude)
    print('longitude -->',longitude)
    #
    clients = [str(x) for x in clients.split(',')]
    #
    latitude = [float(x) for x in latitude.split(',')]
    #
    longitude = [float(x) for x in longitude.split(',')]
    #
    coordonne = list(zip(latitude, longitude))
    #
    client_data = list(zip(clients, coordonne))
    #
    #init = tuple(float(x) for x in init.split(','))
    #
    cars = [str(x) for x in cars.split(',')]
    #
    cars_latitude = [float(x) for x in cars_latitude.split(',')]
    #
    cars_longitude = [float(x) for x in cars_longitude.split(',')]
    #
    cars_coordonne = list(zip(cars_latitude,cars_longitude))
    #
    car_data = list(zip(cars,cars_coordonne))
    #
    coordonne = cars_coordonne + coordonne
    #
    clients = cars + clients
    #
    print('lts client -->', client_data)
    print('lts car -->', car_data)
    #
    tour = vrp_by_geopy(clients,client_data, cars, car_data, coordonne, init)
    #
    # creat matrix of the distance by geopy
    #
    matrix = tour.create_distance_matrix()
    #
    # convert the matrix to dataframe
    #
    df = tour.matrix_to_df(matrix)
    #
    # create dict client and all distance between other clients
    #
    dict_client_dict = tour.convert(df)
    #
    # create vector of the distance between depo and client
    #
    #vec_dis_depo = tour.vector_init_distance()
    #
    # create vector of the all distance between cars and clients
    #
    vec_dis_cars = [{x: y} for x, y in dict_client_dict.items() if x in cars]
    #
    # remove all driver in the list of clients
    #
    tour.remove_car(cars)
    print('cars -->',cars)
    print('dataFrame -->',tour._df.columns)
    print('dataFrame -->', tour._df.index)
    #
    # drop the driver in the matrix
    #
    tour.drop_car(cars)
    #
    tour._coordonne = tour._coordonne[len(cars):]
    #
    # converte the new matrix without cars to dict
    #
    dict_client_dict = tour.convert(tour.df)
    #
    # sort the vector of the client
    #
    sort_cars = tour.cars_sorted(vec_dis_cars)
    #
    # create dict of any car with init client
    #
    #init_vrp = tour.vrp_init(vec_dis_depo, df)
    init_cars = tour.vrp_init_cars(sort_cars)
    #
    # affectation the rest clients use the vrp methode
    #
    #tour.affectation_client(init_cars, dict_client_dict)
    #
    resultat = tour.affectation_client_with_data(init_cars,dict_client_dict,client_data,car_data)
    #add the sol in json for show
    #
    print(type(tour._vrp_affec_sol))
    print('old resultat ==>',tour._vrp_affec_sol)
    print('resultat ==>',resultat)
    #
    #vrp_dict_affec_json = json.dumps(tour._vrp_affec_sol)
    vrp_dict_affec_json = json.dumps(resultat)
    #
    #affest the object tour to global variable round
    #
    round = tour
    #
    #conver dataframe to dict
    #
    data = tour._df.to_dict()
    #
    #create new object in database lts
    #
    print('init ==>',tour._init)
    print('coordeonne ==>',tour._coordonne)
    print('data ==>',data)
    '''pick=Pick_up_lts(
        clients= tour._clients,
        cars= tour._cars,
        init= tour._init,
        coordonne=tour._coordonne,
        data= data,
        vrp_sol= tour._vrp_affec_sol
    )
    #
    #save the database
    #
    pick.save()'''
    #
    '''pick_up=Pick_up(
        clients=tour._clients,
        cars=tour._cars,
        #init=tour._init,
        coordonne=tour._coordonne,
        data= data,
        vrp_sol=tour._vrp_affec_sol,
        wilaya=wilaya,
        slot=slot
    )'''
    #
    #pick_up.save()
    #
    #
    return vrp_dict_affec_json
    #return render_template('index.html')
#