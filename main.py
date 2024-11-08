from fastapi import FastAPI,UploadFile,Form
from fastapi.staticfiles import StaticFiles
from typing import Annotated


app = FastAPI()

@app.post('/items')
def create_item(
    image:UploadFile,
    title:Annotated[str,Form()],
    price:Annotated[int,Form()],
    description:Annotated[str,Form()],
    place:Annotated[str,Form()]):
    print(image,title,price,description,place)
    return '200'

# API를 만들때는 app.mount위에다 만들어야 한다.
app.mount("/", StaticFiles(directory="frontend",html=True), name="frontend")

