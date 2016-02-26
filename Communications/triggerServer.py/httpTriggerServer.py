from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse
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

