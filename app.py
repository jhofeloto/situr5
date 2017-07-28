#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

import re #retira etiquetas HTML de la descripción

from flask import Flask
from flask import request
from flask import make_response

import urllib

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)#Invoca función de consulta y muestra speech al situr3

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "buscarAtractivos":
        return {}
    result = req.get("result")#invocar el result del json
    parameters = result.get("parameters")#invocar el parameters dentro de result
    atractivos = parameters.get("atractivos")#DATO TRAÍDO DE API.AI - ATRACTIVOS
    keyword = parameters.get("keyword")#DATO TRAÍDO DE API.AI - ATRACTIVOS


    url = "http://situr.boyaca.gov.co/wp-json/wp/v2/atractivo_turistico?orderby=relevance&orderby=relevance&offset=0&search=laguna%20negra"
    response = urllib.urlopen(url)
    content = response.read()
    data = json.loads(content.decode("utf8"))

    #print(data)
    dato1= data[1]['title']['rendered']
    dato2= data[2]['title']['rendered']
    dato3= data[3]['title']['rendered']
    dato4= data[4]['title']['rendered']
    dato5= data[5]['title']['rendered']
    dato6= data[6]['title']['rendered']
    dato7= data[7]['title']['rendered']
    dato8= data[8]['title']['rendered']
    dato9= data[9]['title']['rendered']
    dato10= data[10]['title']['rendered']

    speech = dato1+" . "+dato2

    print(speech)
        
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')



#print data(['title']['rendered'])

#if __name__ == '__app__':
#    ruta = 'http://situr.boyaca.gov.co/wp-json/wp/v2/atractivo_turistico?orderby=relevance&orderby=relevance&offset=0&search=laguna'
#    cargar_datos(ruta)

#for i in xrange(len(test)):
#  print test[i]
#test = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10']
