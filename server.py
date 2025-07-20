from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os

def run_server():
    # Change directory to where the HTML file is located
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create and start the server
    server = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    print('Server running at http://localhost:8000')
    
    # Open browser
    webbrowser.open('http://localhost:8000')
    
    # Start serving
    server.serve_forever()

if __name__ == '__main__':
    run_server()
