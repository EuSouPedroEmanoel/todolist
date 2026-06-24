from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from todolist.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'olá mundo'}


@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def say_hello_world_in_html():
    return """
            <html>
                <head>
                    <title>Hello World</title>
                </head>
                <body>
                    <p>olá mundo</p>
                </body>
            </html>
        """
