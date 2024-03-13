from flask import Flask,jsonify
from web_api import create_app
from xmlrpc.client import ServerProxy
#
app=create_app()
#
if __name__=='__main__':
    #
    app.run(port=1000)