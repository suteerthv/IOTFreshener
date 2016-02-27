from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse
import urllib
import urllib2
from urllib2 import urlopen, HTTPError
import json


HOST='0.0.0.0'
PORT=8181
#(id,deviceID,freq)
DEVICES=[('51ff6f065082554910260887',0)]
URL="https://api.particle.io/v1/devices/{!s}/led/"
FREQ = 1
ACCESS_TOKEN=0


class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		print("Just received a GET request")
		qs={}
		path = self.path
		if '?' in path:
			path, tmp = path.split('?')
			qs = urlparse.parse_qs(tmp)
		param = qs['params'][0].split(',')
		time   = (param[0])
		device = int(param[1])
		con = self.processGet(time,device)
		print con
		self.send_response(200)
		
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write("<html><head><title>Title goes here.</title></head>")
		self.wfile.write("<body><p>%s</p>"%con)
		self.wfile.write("</body></html>")
		print qs
		print "End of parsing get"

	def processGet(self,t,d):
		print "time: %s"%t
		print "device: %d"%d
		data={
			'access_token' : DEVICES[d][ACCESS_TOKEN],
			'command':DEVICES[d][FREQ]
		}

		print data	
		data = urllib.urlencode(data);
		try:
			content =urllib.urlopen(url=(URL.format(DEVICES[d])),data=data).read()
		except :
			content = "{'id':-1}"	
		return content
					
	
	def log_request(self, code=None, size=None):
		print('Req')



if __name__ == "__main__":
	try:
		server = HTTPServer((HOST, PORT), MyHandler)
		print('Started http server')
		server.serve_forever()
	except KeyboardInterrupt:
		print('^C received, shutting down server')
		server.socket.close()

