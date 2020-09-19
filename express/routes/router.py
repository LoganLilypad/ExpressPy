from typing import Callable
from express.decorators.route import Route 
from express.decorators.multi_route import MultiRoute

class Router(object):

  def __init__(self) -> None: pass 

  def get(self, route: str, handler: Callable) -> Route:
    return Route("GET", route, handler)

  def post(self, route: str, handler: Callable) -> Route:
    return Route("POST", route, handler)

  def put(self, route: str, handler: Callable) -> Route:
    return Route("PUT", route, handler)

  def multi(self, methods: list, route: str, handler: Callable) -> MultiRoute:
    return MultiRoute(methods, route, handler)

