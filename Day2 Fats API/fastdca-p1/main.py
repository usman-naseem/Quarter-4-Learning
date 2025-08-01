from fastapi import FastAPI

app = FastAPI()

# Decorator
# API Method
# End Point
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")  #Path Parameters
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}