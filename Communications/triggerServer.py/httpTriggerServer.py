from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse
import urllib
import urllib2
from urllib2 import urlopen, HTTPError

URL="https://api.particle.io/v1/devices/51ff6f065082554910260887/led/"
ACCESS_TOKEN="2228662ce1e5a04e7fb21f9b81aa3bc390b72506"
COMMAND = "command=on"
class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		print("Just received a GET request")
		qs={}
		path = self.path
		if '?' in path:
			path, tmp = path.split('?')
			qs = urlparse.parse_qs(tmp)
		param = qs['params'][0].split(',')
		time   = int(param[0])
		device = int(param[1])
		self.processGet(time,device)		
		print qs
	
		print "End of parsing get"
	def processGet(self,t,d):
		print "time: %d"%t
		print "device: %d"%d
		data = urllib.urlencode({
			'access_token' : ACCESS_TOKEN,
			'command':'on'
			}
			);	
		content =urllib.urlopen(url=URL,data=data).read()
		print content
					
	
	def log_request(self, code=None, size=None):
		print('Req')
if __name__ == "__main__":
	try:
		server = HTTPServer(('localhost', 8080), MyHandler)
		print('Started http server')
		server.serve_forever()
	except KeyboardInterrupt:
		print('^C received, shutting down server')
		server.socket.close()

