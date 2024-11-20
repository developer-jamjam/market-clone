from fastapi import FastAPI,UploadFile,Form
from fastapi.staticfiles import StaticFiles
from typing import Annotated
import sqlite3

con = sqlite3.connect('carotclone.db',check_same_thread=False)
cur = con.cursor()

app = FastAPI()

@app.post('/items')
async def create_item(
        image:UploadFile,
        title:Annotated[str,Form()],
        price:Annotated[int,Form()],
        description:Annotated[str,Form()],
        place:Annotated[str,Form()],
        insertAt:Annotated[int,Form()]
        ):
    
    image_bytes= await image.read()
    cur.execute(f"""
                INSERT INTO 
                carotitems(title,image,price,description,place,insertAt)
                VALUES ('{title}','{image_bytes.hex()}',{price},'{description}','{place}',{insertAt})
                """)
    con.commit()
    return '200'

# API를 만들때는 app.mount위에다 만들어야 한다.
app.mount("/", StaticFiles(directory="frontend",html=True), name="frontend")

