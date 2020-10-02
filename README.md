# ExpressPy

ExpressJS -- but for Python

Used to NodeJS's Express syntax and want a similar experience when using Python? Well look no further! The aim of this library is to provide a very similar feel and working to the popular NodeJS web framework Express but in the Python programming language.

Pull requests are encouraged and appreciated considering some of us have almost no idea what we are doing or have school/a job that makes this a little harder to develop fast

I think it's pretty coolio considering theres no other library that aims to do this or a library that makes web frameworks this easy

--- 

# Python VS NodeJS examples

## ExpressPY

```py
@Router.get(route="/", handler=Handler)
def test(req, res):
  print(req)
```

## ExpressJS

```js
app.get("/", (req, res) => {
  console.log(req)
});
```

Pretty similar and simple eh?
