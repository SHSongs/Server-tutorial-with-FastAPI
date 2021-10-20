import urllib.request as ul
import json
import time

def get_food():
    url = f"http://127.0.0.1:8000/get_food"

    request = ul.Request(url)
    response = ul.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        responsedata = response.read()

        my_json = responsedata.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        if data["flag"] == "success":
            print(data)
            return data["food"]

    return "fail"


while True:
    print(get_food())
    time.sleep(5)