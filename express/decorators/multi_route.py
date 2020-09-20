from typing import Callable
from express.exceptions.errors import RouteValidationError, RouteHandlerError, RouteError
from express.routes.handler import RouteHandler
from express.request import Request

class MultiRoute(object):
  
  methods = []

  def __init__(self, methods, route: str, handler: RouteHandler) -> None:
    if route.startswith("/") and type(route) == str:

      self.route = route
      self.handler = handler 

      for method in methods: 
        if Request.is_valid_method(method):

          if isinstance(handler, RouteHandler):

            self.methods.append(method)

          else:

            raise RouteHandlerError(str(handler))

        else:
          raise RouteError("Method '{}' is not accepted.".format(str(method)))
    else:
      raise RouteValidationError(str(route))

  def __call__(self, func: Callable) -> Callable:
    self.handler.registerMultiRoute(self.methods, self.route, func)
    def decorator_f(*any) -> None:
      func(*any)
    
    return decorator_f
