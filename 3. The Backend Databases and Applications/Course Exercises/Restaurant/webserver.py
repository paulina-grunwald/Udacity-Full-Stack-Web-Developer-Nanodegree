# Build web server 

# Import modules
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# Import common gate interface library
import cgi

# import CRUD Operations 
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Handler Class
class WebServerHandler(BaseHTTPRequestHandler):
    # Handle all GET requests
    def do_GET(self):
        # Look for URL that ends with restaurant
        if self.path.endswith("/restaurant"):
            # Query all restaurants name
            restaurants = session.query(Restaurant).all()
            output += "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"
                    # Add Edit and Delete Links
                    output += "<a href ='#'>Edit</a>"
                    output += "</br>"
                    output += "<a href ='#'>Delete</a>"
                    output += "</br>"
                output += "</body></html>"
                self.wfile.write(output)
                return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)




    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
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