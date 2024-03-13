from .. import mongo
from flask import jsonify
import datetime
#
class Pick_up_lts(mongo.Document):
    #
    clients=mongo.ListField()
    cars=mongo.ListField()
    init=mongo.ListField()
    coordonne = mongo.ListField()
    data=mongo.DictField()
    vrp_sol=mongo.DictField()
    date=mongo.DateTimeField(default=datetime.datetime.now())
    #
class Pick_up(mongo.Document):
    #
    clients = mongo.ListField()
    cars = mongo.ListField()
    init = mongo.ListField()
    coordonne = mongo.ListField()
    data = mongo.DictField()
    vrp_sol = mongo.DictField()
    wilaya = mongo.StringField()
    slot = mongo.StringField()
    date = mongo.DateTimeField(default=datetime.date.today())