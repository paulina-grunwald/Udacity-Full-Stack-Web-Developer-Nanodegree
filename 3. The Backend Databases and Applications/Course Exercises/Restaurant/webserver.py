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
        try:
            # Look for URL that ends with restaurant
            if self.path.endswith("/restaurants"):
                # Query all restaurants name
                restaurants = session.query(Restaurant).all()
                output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br>"
                    # Add Edit link
                    output += "<a href ='#'>Edit</a>"
                    output += "</br>"
                    # Add Delete link
                    output += "<a href ='#'>Delete</a>"
                    output += "</br>"
                    output += "</body></html>"
                    self.wfile.write(output)
                return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)






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
