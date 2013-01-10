#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.escape

import sys, os
from optparse import OptionParser
        
class index(tornado.web.RequestHandler):
    def get(self):
        dic = dict(
            message='hey Jeremy, work on your portfolio!',
            note='your VM will be ready soon.')
#	message =('<object data="'+static_url("Jeremy_Rubin_Resume.pdf")+'" type="application/pdf" width="100%" height="100%">'+ 
 # '<p>It appears you don't have a PDF plugin for this browser.' +
#  'No biggie... you can <a href="myfile.pdf">click here to' +
#  'download the PDF file.</a></p>' +
#  '</object>')
        self.render('static/ios.html')

        
#########################################

settings = {
    "debug": True, # os.environ.get("SERVER_SOFTWARE", "").startswith("Development/"),
    "static_path": os.path.join(os.path.dirname(__file__), "static",),
}
application = tornado.web.Application([
(r"/", index),
], **settings)    


    
if __name__ == "__main__":
    
    parser = OptionParser(add_help_option=False)
    parser.add_option("-h", "--host", dest="host", default='')
    parser.add_option("-p", "--port", dest="port", default='80')
    (options, args) = parser.parse_args()
    
    HOST    = options.host
    PORT    = int(options.port)
    
    mode = ''
    if settings['debug']:
        mode = '(debug)'
    
    print 'rubinte.ch running at %s:%s %s' % (HOST,PORT,mode)
    
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(PORT, address=HOST)
    tornado.ioloop.IOLoop.instance().start()




