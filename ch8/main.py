# 쿠키를 이용한 저장
from typing import Optional
from fastapi import Cookie, FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json


class Memo(BaseModel):
    title: str
    body: Optional[str] = None


class Post(BaseModel):
    ip: str
    t: Optional[BaseModel] = None


app = FastAPI()


@app.get("/read_memo/")
async def read_items(user_ip: Optional[str] = Cookie(None)):
    print("user_ip", user_ip)
    my_post = []
    with open("posts.json", "r") as json_file:
        posts = json.load(json_file)
        for post in posts:
            if post['ip'] == user_ip:
                my_post.append(post)

    return my_post


@app.get("/write_memo/")
def read_memo(title: str, body: str, request: Request):
    content = {"message": "메모를 서버에 저장합니다."}
    response = JSONResponse(content=content)
    print(request.client.host)

    # 쿠키 저장
    response.set_cookie(key="user_ip", value=request.client.host)

    post = Post(ip=request.client.host, t=Memo(title=title, body=body))

    try:
        with open("posts.json", "r") as json_file:
            posts = json.load(json_file)
    except:
        posts = []
    finally:
        posts.append(post.dict())

    print(posts)

    with open("posts.json", "w") as json_file:
        j = json.dumps(posts)  # str
        posts = json.loads(j)  # list[dict]
        json.dump(posts, json_file)

    return response
