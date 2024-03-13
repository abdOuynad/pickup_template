import requests
from urllib import request,parse
import json
import opcode
import io
from geopy.distance import geodesic,distance
import numpy as np
#
"""url='http://localhost:4000/'
try:
    u=request.urlopen(url)
    data=u.read()
    tour=json.load(io.BytesIO(data))
    print(tour)
except:
    print('the connection filed')"""
a=(12.5,14.454)
b=(75,25)
c=geodesic(a,b)
d=distance(a,b)
c=str(c)
print(float(c.strip("km")))
