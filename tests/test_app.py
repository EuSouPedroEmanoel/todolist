from http import HTTPStatus

from fastapi.testclient import TestClient

from todolist.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)

    response = client.get('/')
    assert response.json() == {'message': 'olá mundo'}
    assert response.status_code == HTTPStatus.OK


def test_html_deve_retornar_ola_mundo():
    client = TestClient(app)

    respomse = client.get('/html')
    assert respomse.text == (
        """
            <html>
                <head>
                    <title>Hello World</title>
                </head>
                <body>
                    <p>olá mundo</p>
                </body>
            </html>
        """
    )
