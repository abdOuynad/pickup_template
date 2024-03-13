from flask import Flask,Blueprint
from flask_mongoengine import MongoEngine
#from pick_up_api import config
#blueprint call
#
mongo=MongoEngine()
#
def create_app():
    from .vrp_sol.controller import pick_up_blueprints
    from .main.controller import main_blueprint
    from .vrp_add.controller import pickup_add_blueprint
    from .vrp_del.controller import pickup_delet_blueprint
    from .vrp_info.controller import pickup_info_blueprint
    from .data_crud.controller import pick_up_db_blueprint
    from .vrp_tools.controller import pickup_tools_blueprint
    #
    #
    app=Flask('__name__')
    #
    #
    app.config.from_pyfile('config.py')
    #
    app.register_blueprint(pick_up_blueprints)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(pickup_add_blueprint)
    app.register_blueprint(pickup_delet_blueprint)
    app.register_blueprint(pickup_info_blueprint)
    app.register_blueprint(pick_up_db_blueprint)
    app.register_blueprint(pickup_tools_blueprint)
    #
    mongo.init_app(app)
    #
    return app