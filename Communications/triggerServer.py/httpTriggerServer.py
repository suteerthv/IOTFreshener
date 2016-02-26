from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse
class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		print("Just received a GET request")
		qs={}
		path = self.path
		if '?' in path:
			#path, tmp =
			print path.split('?')
	#		print tmp
#			qs = urlparse.parse_qs(tmp)
		print path,qs
#		time = (qs['ntimes'][0:0])
#		device = (qs['device'][0:0])
	#	processGet(time,device)		
		print qs
	
		print "End of parsing get"
	def processGet(t,d):
		print "time:"%t
		print "device"%d
				
		
	
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

