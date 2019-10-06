import tornado.web
import tornado
from service.LuminolService import *

class AnomalyHandler(tornado.web.RequestHandler):
    
    def post(self):
        timeseriesDict = tornado.escape.json_decode(self.request.body)
        self.write(generateJsonResult(formatAnomalies(AnomalyDetector(timeseriesDict).get_anomalies()), timeseriesDict))