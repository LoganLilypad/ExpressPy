from express.app import App as ExpressApp
from express.request import Request


App     = ExpressApp()
Router  = App.router()

@Router.get(route="/")
def test(t):
  pass


@Router.get(route="/honk")
def honk(req, res):
  res.send(b'hi')

@Router.multi(methods=["GET", "POST"], route="/test")
def testing(req, res):
    pass

App.listen(3002)


