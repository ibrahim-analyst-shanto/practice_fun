from fastpi import FastAPI

app = FastAPI()


@app.get("/")
def greet():
    return {"message": "Hello, World!"}
