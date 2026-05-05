from fastapi import FastAPI, Request

app = FastAPI()


@app.get('/')
def hello(request: Request):
    server_no = request.url.port - 8000 + 1
    return {
        "server_no": server_no
    }