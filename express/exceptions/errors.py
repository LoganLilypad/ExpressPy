class RequestValidationError(Exception):
  """Raised when invalid method is passed to handler."""

  _cause = "Invalid method '{}' passed in request string."

  def __init__(self, method_type: str, message: str = _cause) -> None:
    self.method = method_type
    super().__init__(message.format(method_type))

class DispatchValidationError(Exception):
  """Raised when invalid method is passed to dispatcher."""

  _cause = "Invalid method '{}' passed to dispatch."

  def __init__(self, instance: str, message: str = _cause) -> None:
    super().__init__(message.format(instance))

class RouteValidationError(Exception):
  """Raised when invalid route is passed to decorator."""

  _cause = "Invalid route '{}' passed to decorator."
 
  def __init__(self, route: str, message: str = _cause) -> None:
    super().__init__(message.format(route))

class RouteHandlerError(Exception):
  """Raised when invalid handler is passed as decorator parameter."""

  _cause = "Invalid handler '{}' passed as decorator parameter."

  def __init__(self, handle: str, message: str = _cause) -> None:
    super().__init__(message.format(handle))

class RouteError(Exception):
  """Generic route error."""

  def __init__(self, message: str) -> None:
    super().__init__(message)

class AppError(Exception):
  """Generic app error."""

  def __init__(self, message: str) -> None:
    super().__init__(message)  