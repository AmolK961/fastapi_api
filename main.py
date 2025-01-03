from fastapi import  FastAPI
from  typing import Optional
from  pydantic import BaseModel

class Item(BaseModel):
    name:str
    description: Optional[str]=None
    price:float
    tax:Optional[float]=None


app=FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict




@app.get("/")
async def root():
    return {"message":"Hello from Fastapi"}


# path parameter  get an item by id
# @app.get('/item/{item_id}')
# def get_item_by_id(id):
#     return {'item_id':id}

# path parameters with type
@app.get('/item/{item_id}')
async  def item(item_id : int):
    return  {"item_id":item_id}

# Use pydantic to Declare JSON Data Models (Data Shapes)


