from fastapi import FastAPI,UploadFile,Form
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
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

@app.get('/items')
async def get_items():
    # 컬럼명도 같이 가져온다
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = cur.execute(f"""
                       SELECT * FROM carotitems;
                       """).fetchall()
    return JSONResponse(jsonable_encoder(dict(row) for row in rows))
# API를 만들때는 app.mount위에다 만들어야 한다.
app.mount("/", StaticFiles(directory="frontend",html=True), name="frontend")

