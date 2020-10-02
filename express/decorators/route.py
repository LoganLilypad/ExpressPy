from typing import Callable
from express.exceptions.errors import RouteValidationError, RouteHandlerError, RouteError
from express.routes.handler import RouteHandler
from express.request import Request

class Route(object):
  

  def __init__(self, method: str, route: str, handler: RouteHandler) -> None:
    if route.startswith("/") and type(route) == str:

      if Request.is_valid_method(method):

        if isinstance(handler, RouteHandler):

          self.route = route
          self.method = method
          self.handler = handler 

        else:

          raise RouteHandlerError(str(handler))

      else:
        raise RouteError(f"Method '{str(method)}' is not accepted.")

    else:
      raise RouteValidationError(str(route))

  def __call__(self, func: Callable) -> Callable:
    self.handler.registerRoute(self.method, self.route, func)
    def decorator_f(*any) -> None:
      func(*any)
    
    return decorator_f
