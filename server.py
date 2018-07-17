# -*- coding: UTF-8 -*-
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver 

import argparse
import main


tornado.options.define("port", default=5006, help="变量保存端口，默认8000",type = int)

class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin","*")
        self.set_header("Access-Control-Allow-Headers","*")
        self.set_header('Access-Control-Allow-Methods','POST,GET,OPTIONS')
        self.set_header("Content-Type","application/json;charset=utf-8")
       

    def get(self):
        self.write("Hello, world")

class ParseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin","*")
        self.set_header("Access-Control-Allow-Headers","*")
        self.set_header('Access-Control-Allow-Methods','POST,GET,OPTIONS')
        self.set_header("Content-Type","application/json;charset=utf-8")
        

    def get(self):
        self.write("parse data")

    def post(self):
        print("post data")

class trainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin","*")
        self.set_header("Access-Control-Allow-Headers","*")
        self.set_header('Access-Control-Allow-Methods','POST,GET,OPTIONS')
        self.set_header("Content-Type","application/json;charset=utf-8")

    def get(self):
        self.write("train data")

    def post(self):
        self.set_status(200)
        self.write("train data")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/parse", ParseHandler),
        (r"/train", trainHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()