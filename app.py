import motor.motor_tornado

import tornado.ioloop
import tornado.web
import tornado.httpserver

from handlers.AnomalyHandler import AnomalyHandler
from handlers.ForecastHandler import ForecastHandler    
from controllers.HealthController import HealthController

from healthcheck import HealthCheck, TornadoHandler

class Application(tornado.web.Application):
    def __init__(self):
        # args = dict(db=db)

        handlers = [
            (r"/detect", AnomalyHandler),
            (r"/forecast", ForecastHandler),
            (r"/health", TornadoHandler, dict(checker=HealthCheck()))
        ]

        tornado.web.Application.__init__(self, handlers)

if __name__ == "__main__":
    
    # # Mongo DB
    # database_string = 'mongodb://localhost:27017'
    # client = motor.motor_tornado.MotorClient(database_string)
    # db = client['collection-name']
    
    app = tornado.httpserver.HTTPServer(Application())
    app.listen(7777)

    print('Server running...')

    tornado.ioloop.IOLoop.current().start()