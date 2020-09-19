from express.routes.handler import RouteHandler 
from express.routes.router import Router
from express.exceptions.errors import AppError
from express.tcpserver.server import Server
import socket 


class App:
  
  _router: Router = Router()
  _handler: RouteHandler = RouteHandler()
  _server: Server or None = None

  def router(self) -> Router:
    return self._router 

  def handler(self) -> RouteHandler:
    return self._handler

  def port_in_use(self, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return not bool(sock.connect_ex( ('localhost', port) ))

  def is_valid_port(self, port: int) -> bool:
      return type(port) == int or port > 0 or port < 65536

  def listen(self, port: int = 3000) -> None:
    if not self.is_valid_port(port):
      raise AppError("Mismatch: Type '{}' passed when int was expected.".format(type(port)))
      
    if not self.port_in_use(port):
        self._server = Server(port)
        print("Listening on localhost:{}.".format(port))
        self._server.start()
    else:
        raise AppError("Port '{}' is already in use.".format(port))
