from flask import Flask,request,jsonify
from functools import wraps
import json
import jwt
from pick_up.pick_up_class import vrp_by_geopy
#
#
round=None
#
app=Flask('__name__')
#
app.config['SECRET_KEY']='85274f4ac35210609bcd9e8197ea6a0a'
#
#
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
        jwt_encode=jwt.encode({'key':'abdouy'},app.config['SECRET_KEY'],algorithm='HS256')
        print(jwt_encode)
        token=token.split('Bearer ')[1]
        if jwt_encode == token:
            return f(token,*args,**kwargs)
        #
        print(token)
        print(jwt_encode)
        return jsonify({'message': 'error the key not working try again '})
        #
    return decorator

#
@app.route('/')
def home():
    #

    #
    return jsonify({'message':'hello World'})
#
@app.route('/',methods=['POST'])
@jwt_required
def vrp_sol(token):
    #
    global round
    #
    clients = request.form['clients']
    latitude = request.form['l']
    longitude = request.form['g']
    init = request.form['init']
    cars = request.form['cars']
    #
    #
    clients = [str(x) for x in clients.split(',')]
    #
    latitude = [float(x) for x in latitude.split(',')]
    #
    longitude = [float(x) for x in longitude.split(',')]
    #
    coordonne = list(zip(latitude, longitude))
    #
    init = tuple(float(x) for x in init.split(','))
    #
    cars = [str(x) for x in cars.split(',')]
    #
    print('client ==>', clients)
    print('latitude ==>', latitude)
    print('longitude ==>', longitude)
    print('coordonne ==>', coordonne)
    print('init ==>', init)
    print('cars ==>', cars)
    #
    tour = vrp_by_geopy(clients, cars, coordonne, init)
    #
    matrix = tour.create_distance_matrix()
    #
    df = tour.matrix_to_df(matrix)
    #
    dict_client_dict = tour.convert(df)
    #
    vec_dis_depo = tour.vector_init_distance()
    tour.vec_dipo=vec_dis_depo
    #
    # create dict of any car with init client
    #
    init_vrp = tour.vrp_init(vec_dis_depo, df)
    #
    tour.affectation_client(init_vrp, dict_client_dict)
    #
    d = {}
    for v in tour.vrp_affec_sol:
        d[list(v.keys())[0]] = list(v.values())[0]
    #
    vrp_dict_affec_json = json.dumps(d)
    #
    round=tour
    #
    return vrp_dict_affec_json
#
@app.route('/delete',methods=['POST'])
@jwt_required
def delete_client(token):
    global round
    client=request.form['client']
    k=request.form['k']
    #
    client=str(client)
    k=int(k)
    #
    if round is None:
        return 'we dont have data for delete client'
    else:
        round.find_and_annulation(client,round.df,k)
        d = {}
        for v in round.vrp_affec_sol:
            d[list(v.keys())[0]] = list(v.values())[0]
        #
        vrp_dict_affec_json = json.dumps(d)
        #
        return vrp_dict_affec_json
@app.route('/add',methods=['POST'])
@jwt_required
def add_client(token):
    #
    global round
    #
    client=str(request.form['client'])
    latitude=float(request.form['l'])
    longitude = float(request.form['g'])
    avnc = [int(x) for x in request.form['avnc'].split(',')]
    coordonne = (latitude,longitude)
    #
    if round is None:
        return jsonify({'message':'you dont have the model use create vrp round first'})
    #
    else:
        round.add_clien_to_vrp(client, avnc,coordonne)
        d = {}
        for v in round.vrp_affec_sol:
            d[list(v.keys())[0]] = list(v.values())[0]
        #
        vrp_dict_affec_json = json.dumps(d)
        #
        return vrp_dict_affec_json
#
@app.route('/info')
def vrp_info():
    global round
    if round is None:
        return jsonify({'message':'No information create Model vrp first'})
    else:
        round.vrp_sol_info(round.vec_dipo, round.df)
        print(round.vrp_info)
        d = {}
        for i,v in enumerate(round.vrp_info):
            n={}
            for x,y in v.items():
                n[x]=y
            d[i]=n
        #
        vrp_dict_affec_json = json.dumps(d)
        #
        return vrp_dict_affec_json
#
if __name__ == '__main__':
    #
    app.run(debug=True)
