from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body align = 'center' style="background-color: azure;">
<h1>Laptop Specifications</h1>
<table border="10" cellpadding="10" align="center" bgcolor="orange">
    <tr>
        <td>System Config</td>
        <td>Description</td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</td>
    </tr>
    <tr>
        <td>Installed Ram</td>
        <td>16GB</td>
    </tr>
    <tr>
        <td>System Type</td>
        <td>64-bit x64 Operating System</td>
    </tr>
    <tr>
        <td>Windows Edition</td>
        <td>Windows 11 Home Single Language</td>
    </tr>
</body>
</html>'''


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()