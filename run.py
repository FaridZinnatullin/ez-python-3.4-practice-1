from wsgiref import simple_server
from composites.service_api import create_app


app = create_app()
httpd = simple_server.make_server('0.0.0.0', 1234, app)
httpd.serve_forever()

