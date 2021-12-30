from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "AI SERVER root router"  # JSON, html 문서,


@app.get("/ai")
def ai():
    print("인공지능 처리를 하는 중입니다.")

    # out = model(x)

    out = "당신은 " + "cat" + " 입니다"
    return out


@app.post("/write-todo")
def root():
    print("write todo")
    content = {"message": "Hello World"}
    headers = {"X-Cat-Dog": "alone in the world", "Content-Language": "en-US",
               "Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=content, headers=headers)


uvicorn.run(app, host="0.0.0.0", port=8000)
