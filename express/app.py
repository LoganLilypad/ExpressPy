from express.routes.handler import RouteHandler 
from express.routes.router import Router
from express.exceptions.errors import AppError
from express.tcpserver.server import Server
import socket 

class App:
  
  _handler: RouteHandler = RouteHandler()
  _router: Router = Router(_handler) # Realized it would probably be better to do it like this rather then having the user pass the handler.
  _server: Server or None = None
  _MAX_PORT = 65536

  def router(self) -> Router:
    """ Returns Router instance. """
    return self._router 

  def handler(self) -> RouteHandler:
    """ Returns RouteHandler instance. """
    return self._handler

  def port_in_use(self, port: int) -> bool:
    """ Checks if the port is currently in use. """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return not bool(sock.connect_ex( ('localhost', port) ))

  def is_valid_port(self, port: int) -> bool:
      """ Makes sure the port is valid. """
      return type(port) == int and port > 0 and port < self._MAX_PORT

  def listen(self, port: int = 3000) -> None:
    """ Attempt to serve the webserver on a specific port. """

    if not self.is_valid_port(port):
      raise AppError("Mismatch: Type '{}' passed when int was expected.".format(type(port)))
      
    if not self.port_in_use(port):
        self._server = Server(port)
        print("Listening on localhost: {}.".format(port))

        self._server.start_server_thread(self)
        #  print("Listening on localhost:{}.".format(port)) | Moved this line above: It doesn't get executed since .start() has a while True loop.
    else:
        raise AppError("Port '{}' is already in use.".format(port))

  def new(self):
    return App()
