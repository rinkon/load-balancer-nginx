from fastapi import FastAPI, Request

app = FastAPI()


@app.get('/hello')
def hello(request: Request):
    port = request.scope.get("server")[1]
    server_no = port - 8000 + 1
    # server_no = request.url.port - 8000 + 1

    return {
        "server_no": server_no
    }