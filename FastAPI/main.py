from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float



@app.get("/")
async def read_root():
    return "MY API 사이트에 방문하신 것을 환영합니다."

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str,  None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    result = {"item_id": item_id, **item.dict()}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}