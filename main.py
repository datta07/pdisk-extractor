import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time

app=FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

session=requests.session()

@app.get("/getLink")
def getMkVlink(id,max_tries=10):
	res=session.get("https://pdisk.pro/"+id)
	soup=BeautifulSoup(res.text,"lxml")
	try:
		return {
		"status":"success",
		"data":soup.findAll("img",{"class":"vanb"})[-1]["onclick"].split("intent://")[1].split("#Intent")[0]}
	except Exception:
		if (max_tries>0):
			print("Iterating one more time")
			time.sleep(1)
			return getMkVlink(id,max_tries-1)
		else:
			return {
				"status":"failure",
				"data":"please contact datta, there is some error"}


@app.api_route("/tvschedule/{path_params:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
@app.api_route("/tvschedule", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
async def tvschedule(request: Request, path_params: str = None):
    response_message = {
        "status": "error",
        "message": "This API has been moved to https://rapidapi.com/Garuda07/api/indian-tv-schedule-api due to unforeseen circumstances.",
        "migration_info": {
            "moved_since": "2024-10-31",
            "new_api_url": "https://rapidapi.com/Garuda07/api/indian-tv-schedule-api",
            "documentation_url": "https://rapidapi.com/Garuda07/api/indian-tv-schedule-api/docs"
        },
        "status_code": 301,  # 301 Moved Permanently status code for API relocation
        "request_id": request.headers.get("X-Request-ID", "N/A")
    }
    return JSONResponse(content=response_message, status_code=301)


