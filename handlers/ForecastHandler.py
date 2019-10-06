import tornado.web
import tornado
from service.ProphetService import *

class ForecastHandler(tornado.web.RequestHandler):
    
    def post(self):
        timeseriesDict = tornado.escape.json_decode(self.request.body)
        result = forecastTimeserie(timeseriesDict)

        self.write(result)