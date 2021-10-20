from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "hi fast api"


@app.get("/{root_id}")
def read_id(root_id: int):
    return {"root_id": root_id}


@app.get("/apple")
def apple_router():
    return "사과를 위한 page \n 사과(沙果, apple)는 사과나무의 열매로, 세계적으로 널리 재배되는 열매 가운데 하나이다. 평과(苹果), 빈파(頻婆)라고도 한다. 사과열매는 가을에 익는데, " \
           "보통 지름이 5~9센티미터이다. 극히 드물지만 15센티에 이르기도 한다. 씨앗에는 미량의 사이안화물이 함유되어 있다. 샐러드, 주스, 파이, 카레 등의 재료로 쓰인다. (위키백과) "


def order(name, cnt):
    pass


@app.get("/order_apple/{cnt}")
def read_id(cnt: int):
    order("apple", cnt)  # 사과 주문 함수
    return f"사과를 {cnt}개 주문합니다."


from typing import Optional


@app.get("/items")
def read_item(item: Optional[str] = None, color: Optional[str] = None):
    return f"{item}을(를) {color} 색상으로 주문합니다."
