# 쿠키
from typing import Optional
from fastapi import Cookie, FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}


@app.post("/cookie/")
def create_cookie():
    content = {"message": "Come to the dark side, we have cookies"}
    response = JSONResponse(content=content)
    response.set_cookie(key="ads_id", value="fake-cookie-session-value")
    return response
