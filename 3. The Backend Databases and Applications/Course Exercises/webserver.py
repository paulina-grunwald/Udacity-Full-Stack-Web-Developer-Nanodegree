# Build web server 

# Import modules
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# Import common gate interface library
import cgi

# Handler Class
class WebServerHandler(BaseHTTPRequestHandler):
    # Handle all GET requests
    def do_GET(self):
        # Look for URL that ends with 'hello'
        if self.path.endswith("/hello"):
            # Send a response code 200 indicating a successful git request
            self.send_response(200)
            # Reply in form of html to client
            self.send_header('Content-type', 'text/html')
            # Send blank line
            self.end_headers()
            message = ""
            # Add message
            message += "<html><body>Hello!</body></html>"
            # Send message to the client
            self.wfile.write(message)
            print message
            return
        # Look for URL that ends with 'hola' 
        # Add hola funtionality
        if self.path.endswith("/hola"):
            # Send a response code 200 indicating a successful git request
            self.send_response(200)
            # Reply in form of html to client
            self.send_header('Content-type', 'text/html')
            # Send blank line
            self.end_headers()
            message = ""
            # Add message
            message += "<html><body>&#161Hola! <a href = '/hello'>Back to Hello</a></body></html>"
            # Send message to the client
            self.wfile.write(message)
            print message
            return
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            # When receive POST request send off response code
            # that indicates a successful post
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # cgi.parse_header function oarses an HTML form header, such as content type
            # into a main valye and dictionary of parameters
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            # Check if this is form data being received
            if ctype == 'multipart/form-data':
                # Collet all fields in the form
                fields = cgi.parse_multipart(self.rfile, pdict)
                # Get a value of specific fields
                messagecontent = fields.get('message')
            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
        except:
            pass

# Main method 
def main():
    # Add try/except block
    try:
        # Define port
        port = 8080
        # Set host address to empty and specify port
        # Create webserver 
        server = HTTPServer(('', port), WebServerHandler)
        # Add print statement to see if the server is running
        print "Web Server running on port %s" % port
        # Keep listening until CTRL+C or exiting application
        server.serve_forever()
    # Add except
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        # Shut down server
        server.socket.close()

# Run main method when python executes the script
if __name__ == '__main__':
    main()