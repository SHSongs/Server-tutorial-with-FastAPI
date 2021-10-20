from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

food_lst = []


@app.get("/order_food", response_class=HTMLResponse)
def order_food(request: Request):
    return templates.TemplateResponse("order_food.html", {"request": request})


@app.post("/submit")
def submit_food(food: str = Form(...)):
    food_lst.append(food)
    s = f"{food} 주문 완료"
    print(s)
    return RedirectResponse("/end", status_code=302)


@app.get("/end", response_class=HTMLResponse)
async def end():
    return "제출 완료하였습니다"


@app.get("/get_food")
def form_get():
    if len(food_lst) > 0:
        return {"flag": "success", "food": food_lst.pop(0)}
    else:
        return {"flag": "fail"}
