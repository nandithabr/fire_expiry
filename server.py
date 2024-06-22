import http.server
import socketserver
import json
import sqlite3

PORT = 8000

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/add':
            self.handle_add()
        elif self.path == '/retrieve':
            self.handle_retrieve()
        else:
            self.send_response(404)
            self.end_headers()

    def handle_add(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        Id = data['id']
        ExpiryDate = data['expiryDate']
        RefillingDate = data['refillingDate']
        LastRefilledDate = data['lastRefilledDate']
        Location = data['location']
        NearbyStation = data['nearbyStation']
        
        con = sqlite3.connect('FireExtinguisherDB.db')
        cr = con.cursor()
        cr.execute('INSERT INTO info (Id, ExpiryDate, RefillingDate, LastRefilledDate, Location, NearbyStation) VALUES (?, ?, ?, ?, ?, ?)', (Id, ExpiryDate, RefillingDate, LastRefilledDate, Location, NearbyStation))
        con.commit()
        con.close()
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"message": "Data added successfully"}')

    def handle_retrieve(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        Id = data['id']
        
        con = sqlite3.connect('FireExtinguisherDB.db')
        cr = con.cursor()
        cr.execute('SELECT * FROM info WHERE Id = ?', (Id,))
        result = cr.fetchone()
        con.close()
        
        if result:
            response = {
                'id': result[0],
                'expiryDate': result[1],
                'refillingDate': result[2],
                'lastRefilledDate': result[3],
                'location': result[4],
                'nearbyStation': result[5]
            }
        else:
            response = {'message': 'No data found'}
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
