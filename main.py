import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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


