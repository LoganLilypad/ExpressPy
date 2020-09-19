from pyeventdispatcher import dispatch, Event, register as _register

from typing import Callable

from express.exceptions.errors import DispatchValidationError


class Dispatcher:

  def __init__(self) -> None:
    pass

  def dispatch(self, event: str, value: any) -> None:
    dispatch(Event(event, value))

  def register(self, event: str, handler) -> None:
    _register(event, handler)  


class Listener:

  _dispatcher: Dispatcher or None = None

  def __init__(self, dispatcher: Dispatcher) -> None:
    self._dispatcher = dispatcher

  @property
  def dispatcher(self) -> Dispatcher:
    return self._dispatcher

  def register(self, event: str, handler: Callable) -> None:
    if callable(handler):
      self.dispatcher.register(event, handler)
    else: 
      raise DispatchValidationError(str(handler))

class DispatcherEvent(Event):
  pass
  
