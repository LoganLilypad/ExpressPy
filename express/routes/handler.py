from express.dispatcher.dispatch import Dispatcher, Listener
from typing import Callable 
from express.exceptions.errors import RouteError, MethodValidationError
from inspect import isclass

class RouteHandler:

  _dispatcher: Dispatcher or None = None
  _listener: Listener = Listener(_dispatcher)
  _handledRoutes: dict = dict()
  _multiRoutes: dict = dict()

  def __init__(self, dispatcher: Dispatcher = Dispatcher()) -> None:
    self._dispatcher = dispatcher 

  def isValidMethod(self, method: str) -> bool: 
    return method != None or type(method) == str or len(method) > 0

  def isValidMethodList(self, methods: list) -> bool: 
    return methods != None or len(methods) != 0 or type(methods) == list

  def isValidFunction(self, potential_method: Callable) -> bool:
    return callable(potential_method) and (not isclass(potential_method))

  def registerRoute(self, method: str, route: str, route_handle: Callable) -> None:

    if not self.isValidFunction(route_handle):
      raise RouteError("Invalid route handle passed to registerRoute(...)")

    if not self.isValidMethod(method):
      raise RouteError("Invalid route method passed to registerRoute(...)")

    route = route.replace("/", "", 1)

    if self.hasSingleRoute(route) or self.hasMultiRoute(route):
        is_single_route = self.hasSingleRoute(route)
        name = self.getByName(route)["handle"].__name__

        if is_single_route:
            
            raise RouteError(f"Route '{route}' is already managed by {name}")
        else:
            # Honestly, it probably shouldn't make it here considering this is the function used for 
            # Multi routes, but oh well.
            raise RouteError(f"Route '{route}' is already managed by {name}")
    else:
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


    if not self.isValidFunction(route_handle):
      raise RouteError("Invalid route handle passed to registerMultiRoute(...)")

    route = route.replace("/", "", 1)

    if not self.isValidMethodList(methods):
        raise MethodValidationError("Invalid route method list passed to registerMultiRoute(...)")

    if self.hasSingleRoute(route) or self.hasMultiRoute(route):
        is_single_route = self.hasSingleRoute(route)
        
        if is_single_route:
            # Honestly, it would be weird if it made it here but might aswell include the functionality anyways.
            raise RouteError("Route '{}' is already managed by {}".format(route, self.getByName(route)["handle"].__name__))
        else:
            raise RouteError("Multi Route '{}' is already managed by {}".format(route, self.getByName(route)["handle"].__name__))
    else:
      self._multiRoutes[route] = { "methods": methods, "route": route, "handle": route_handle }
      self._dispatcher.register(route, route_handle)

  def getByName(self, route: str) -> dict or None:

    if self.hasSingleRoute(route):
        return self._handledRoutes[route]
    elif self.hasMultiRoute(route):
        return self._multiRoutes[route]
    else:
        return None

  def is_accepted(self, route: str, method: str = "GET") -> bool:
      if self.hasSingleRoute(route):
          return method == self._handledRoutes["method"]
      elif self.hasMultiRoute(route):
          return method in self._multiRoutes["methods"]
      else:
          return False      

  def clear(self):
    self._dispatcher = Dispatcher()
    self._listener = Listener(self._dispatcher)
    self._multiRoutes = dict()
    self._handledRoutes = dict()