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



# Development

The following files are required:

- `main.py`: containing the FastAPI app

- `requirements.txt`

- `dockup.yml`

    - example

        ```
        name: flet-fastapi-example
        path: /flet-fastapi-example
        type: flet_abs
        ```

    - `name` must match the parent folder name
    - `path` is the url at which the app will be available.
    - `type`: must be `flet_abs` for this type of application



# Testing and Deployment

## Launch the app in development mode

```
cd src/flet-fastapi-example
uvicorn main:app --reload --port 8004
```

The app will be available at `localhost:8004/flet-fastapi-example/`.

The app will reload itself automatically every time you save the code.



## Publish the app using Dockup

### About Dockup

Dockup is a CLI tool and Python module which allows to effortlessly publish applications as Docker container.

Please note that you must first install Dockup and a reverse proxy before publishing your app. 

Check https://github.com/flokapi/dockup for the installation



### Publish locally

Locally

```
cd src
tar -czf flet-fastapi-example.tar.gz flet-fastapi-example
python3 -m dockup install flet-fastapi-example.tar.gz
```

The app will be available at `http://localhost/flet-fastapi-example/`



### Publish on your server

Locally

```
cd src
tar -czf flet-fastapi-example.tar.gz flet-fastapi-example
```

On your server, once the the archive has been copied

```
python3 -m dockup install flet-fastapi-example.tar.gz
```

The app will be available at `https://example.com/flet-fastapi-example/`



# Resources

Flet documentation

- https://flet.dev/docs/guides/python/deploying-web-app/running-flet-with-fastapi/
- https://flet.dev/docs/guides/python/async-apps/



Dockup

- https://github.com/flokapi/dockup
