# About

This is an example of how to combine Flet and FastAPI for complex applications which require both an API and a user interface. In this architecture, the API and the user interface are defined in a single app, while being clearly separated. As a result, the back end and the front end can be implemented and published all in one.

When using FastAPI to publish Flet Apps, the Python code is running on the server side and the browser is only displaying it. As a result, the Flet app can access the API internally as a function and doesn't need HTTP requests to communicate with the server.



# The Code

### Accessing to API functions from the Flet GUI

Each function used by the API can be registered using the  `@api.register` decorator

```python
@api.register
@app.get(f'{path}/set-value')
async def set_value(value: int):
    global counter
    counter = value
    return {'message': f'Updated counter value to {value}'}
```

`api.get()` will then produce a dictionary of functions which is passed over to the Flet GUI when creating it.

The Flet app can then save the API functions dictionary as an attribute and make a call to the API whenever needed.

```python
await self.api['set_value'](30)
```

This is equivalent to `https://example.com/flet-fastapi-example/set-value?value=30`



### Serving a Flet App from FastAPI

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()


async def main(page: ft.Page):
    await gui.init(page, cfg, api.get())

app.mount(f'{path}/', flet_fastapi.app(main))
```



### Idle functions

The code also shows how to create idle functions both in the API (`main.py`) and in the Flet App (`gui.py`)

Please note the difference:

- There is only one API idle function running, because there is only one instance of the API
- Each Flet App instance (opened Flet Application) has its own idle function



# Testing and Deployment

## Launch the app in development mode

```
cd src/flet-fastapi-example
uvicorn main:app --reload --port 8004
```

The app will be available at `localhost:8004/`.

The app will reload itself automatically every time you save the code.



# Resources

Flet documentation

- https://flet.dev/docs/guides/python/deploying-web-app/running-flet-with-fastapi/
- https://flet.dev/docs/guides/python/async-apps/
