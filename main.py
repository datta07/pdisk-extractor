import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app=FastAPI()
session=requests.session()

@app.get("/getLink")
def getMkVlink(id):
	res=session.get("https://pdisk.pro/"+id)
	soup=BeautifulSoup(res.text,"lxml")
	try:
		return {
		"status":"success",
		"data":soup.findAll("img",{"class":"vanb"})[-1]["onclick"].split("intent://")[1].split("#Intent")[0]}
	except Exception:
		return {
		"status":"failure",
		"data":"please contact datta, there is some error"}

