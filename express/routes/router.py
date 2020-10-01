from typing import Callable
from express.decorators.route import Route 
from express.routes.handler import RouteHandler
from express.decorators.multi_route import MultiRoute

class Router(object):

  def __init__(self, handler: RouteHandler) -> None: 
      self._handler = handler 

  def get(self, route: str) -> Route:
    return Route("GET", route, self._handler)

  def post(self, route: str) -> Route:
    return Route("POST", route, self._handler)

  def put(self, route: str) -> Route:
    return Route("PUT", route, self._handler)

  def multi(self, methods: list, route: str) -> MultiRoute:
    return MultiRoute(methods, route, self._handler)

