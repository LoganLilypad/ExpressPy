from express.dispatcher.dispatch import Dispatcher, Listener
from typing import Callable 
from express.exceptions.errors import RouteError

class RouteHandler:

  _dispatcher: Dispatcher or None = None
  _listener: Listener = Listener(_dispatcher)
  _handledRoutes: dict = dict()
  _multiRoutes: dict = dict()

  def __init__(self, dispatcher: Dispatcher = Dispatcher()) -> None:
    self._dispatcher = dispatcher 

  def isValidMethod(self, method: str) -> bool: 
    return method == None or type(method) != str or len(method) == 0

  def isValidMethodList(self, methods: list) -> bool: 
    return methods == None or len(methods) == 0 or type(methods) != list

  def registerRoute(self, method: str, route: str, route_handle: Callable) -> None:
    if self.isValidMethod(method):
      raise RouteError("Invalid method passed to registerRoute(...)")

    route = route.replace("/", "", 1)

    try:
      if self._handledRoutes[route] != None:
        raise RouteError(
          "Route '{}' is already handled by method '{}'".format(route, self._handledRoutes[route]["handle"].__name__)
        )
    except KeyError:
        self._handledRoutes[route] = { "method": method, "route": route, "handle": route_handle }
        self._dispatcher.register(route, route_handle)

  def hasSingleRoute(self, route: str) -> None:
    try:
      self._handledRoutes[route]
      return True
    except KeyError:
      return False

  def hasMultiRoute(self, route: str) -> None:
    try:
      self._multiRoutes[route]
      return True
    except KeyError:
      return False  

  def registerMultiRoute(self, methods: list, route: str, route_handle: Callable) -> None:
    route = route.replace("/", "", 1)

    if self.isValidMethodList(methods):
      raise RouteError("Invalid methods passed to registerRoute(...)")
    if self.hasSingleRoute(route):
      raise RouteError("Route '{}' is already handled by method '{}'".format(route,self._handledRoutes[route]["handle"].__name__))
    elif self.hasMultiRoute(route):
      raise RouteError("MultiRoute '{}' is already handled by method '{}'".format(route,self._multiRoutes[route]["handle"].__name__))
    else:
      self._multiRoutes[route] = { "methods": methods, "route": route, "handle": route_handle }
      self._dispatcher.register(route, route_handle)


  def test(method: str = "GET", data: str or None = None) -> None:
    pass