from fastapi import FastAPI,UploadFile,Form,Response #image 에다가 파일을 업로드 하기 위해 uploadFile 을 넣어야 함
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from typing import Annotated
import sqlite3

con = sqlite3.connect('db.db', check_same_thread=False)
cur = con.cursor()

app = FastAPI()

#mount에 소스를 넣어야 한다. mount 위까지만 실행됨, 밑에 작성하면 실행안됨

# 어떻게 인코딩을 할지 정하는거 
SERCRET = "super-coding"
manager = LoginManager(SERCRET,'/login')

@manager.user_loader()
def query_user(id):
    con.row_factory = sqlite3.Row
    cur = con.cursor() 
    user = cur.execute(f"""
                       SELECT * from users WHERE id = '{id}'
                       """).fetchone()
    return user

@app.post('/login')
def login(id:Annotated[str,Form()],
           password:Annotated[str,Form()]):
    #해당 유저가 db에 존재하는지
    user = query_user(id)
    if not user:
        raise InvalidCredentialsException #에러 메세지 확인 / 자동으로 401 생성해서 내보냄
    elif password != user['password']:   #else if
        raise InvalidCredentialsException
    
    return ''

@app.post('/signup')
def signup(id:Annotated[str,Form()],
           password:Annotated[str,Form()],
           name : Annotated[str,Form()],
           email : Annotated[str,Form()]):
    #db 저장 - users
    cur.execute(f"""
                INSERT INTO users(id,name,emil,password)
                VALUES ('{id}','{name}','{email}','{password}')          
                """)
    con.commit()
    return '200'

@app.post('/items')
async def create_item(image:UploadFile, 
                title:Annotated[str,Form()], #타이틀 정보는 form data 형식으로 문자열로 나타낸다.
                price:Annotated[int,Form()], 
                description:Annotated[str,Form()],
                place:Annotated[str,Form()],
                insertAt:Annotated[int,Form()]
        ):
    
    image_bytes = await image.read() #이미지는 블롭 타입으로 굉장히 크기 때문에 이미지를 읽을 시간이 필요
    cur.execute(f"""     
                INSERT INTO items
                (title, image, price, description,place,insertAt)
                VALUES 
                ('{title}','{image_bytes.hex()}',{price},'{description}','{place}',{insertAt})
                """) 
    con.commit()#디비에 넣는 방법
    #insert into items에 values 값을 넣어준다는 의미 / {} 문자열을 나타내는 표시

    return'200'

@app.get('/items') #모든 데이터를 가져와라
async def get_items():
    # 컬럼명도 같이 가져옴
    con.row_factory = sqlite3.Row
    cur = con.cursor() #디비를 가져오면서 위치를 잡아주는
    rows = cur.execute(f"""
                       SELECT * from items;
                       """).fetchall()
    return JSONResponse(jsonable_encoder(dict(rows) for row in rows)) #파이썬에서 오브젝트 기능하는 dictionary 사용하면 좋다.

@app.get('/images/{item_id}')
async def get_image(item_id):
    cur = con.cursor()
    image_bytes = cur.execute(f"""
                              SELECT image from items WHERE id = {item_id}
                              """).fetchone()[0]
    
    #16진법 변환
    return Response(content=bytes.fromhex(image_bytes))
    
app.mount("/market-clone", StaticFiles(directory="frontend", html=True),name="frontend") 

