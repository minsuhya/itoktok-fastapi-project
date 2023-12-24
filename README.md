# FastApi + Vue + Tailwindcss 환경

<!-- vim-markdown-toc GFM -->

- [FastApi Service Routing](#fastapi-service-routing)

<!-- vim-markdown-toc -->

### FastApi Service Routing

1. You don't need to create route to serve/render homepage/static-folder explicitly. When you mark a directory as static it will automatically get the first argument as route of the app.mount() in this case it's app.mount("/"). So, when you enter the base url like http://127.0.0.1:8000/ you will get the static files.
2. app instance of the FastAPI() class. Yes, you can have as many instance as you want in a single FASTAPI app.
3. api_app instance of the FastAPI() for other api related task.

The reason 2 & 3 need because if you want to stick with just app instance, \
when user req for the url http://127.0.0.1:8000/, user will get the the static file, \
then when user will req for http://127.0.0.1:8000/hello then the server will try to find hello inside static-folder, \
but there is no hello inside static-folder!, eventually it will be a not-found type response. \
That's why it's need to be created another instance of FastAPI api_app, and registered with prefix /api, \
so every req comes from http://127.0.0.1:8000/api/xx, decorator @api_app will be fired!
instance declaration and mount() method calling order is important.

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='homepage-app')

# for ui
app = FastAPI(title="homepage-app")

# for api
api_app = FastAPI(title="api-app")

# for api and route that starts with "/api" and not static
app.mound("/api", api_app)

# for static files and route that starts with "/"
app.mount("/", StaticFiles(directory="static-folder", html=True), name="static-folder") 

# for your other api routes you can use `api_app` instance of the FastAPI
@api_app.get("/hello")
async def say_hello():
    print("hello")
    return {"message": "Hello World"}

```


