from express.routes.handler import RouteHandler 
from express.routes.router import Router
from express.exceptions.errors import AppError
from express.tcpserver.server import Server

class App:
  
  _router: Router = Router()
  _handler: RouteHandler = RouteHandler()
  _server: Server or None = None

  def router(self) -> Router:
    return self._router 

  def handler(self) -> RouteHandler:
    return self._handler

  def listen(self, port: int = 3000) -> None:
    if type(port) != int:
      raise AppError("Mismatch: Type '{}' passed when int was expected.".format(type(port)))
      
    self._server = Server(port)
    
    print("Listening on localhost:{}.".format(port))

    self._server.start()
