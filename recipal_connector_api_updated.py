
from fastapi import FastAPI, HTTPException
import requests
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Allow CORS for testing with GPT or local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

RECIPAL_API_KEY = os.getenv("RECIPAL_API_KEY")
BASE_URL = "https://www.recipal.com"
HEADERS = {"Authorization": f"Bearer {RECIPAL_API_KEY}"}


@app.get("/recipal/recipes")
def get_recipes():
    url = f"{BASE_URL}/api/recipes"
    response = requests.get(url, headers=HEADERS)
    print("RESPONSE STATUS:", response.status_code)
    print("RESPONSE TEXT:", response.text)
    if response.status_code != 200:
        raise HTTPException(
            status_code=500,
            detail=f"Recipal API error: {response.status_code} - {response.text}"
        )
    return response.json()


@app.get("/recipal/ingredients")
def get_ingredients():
    url = f"{BASE_URL}/api/ingredients"
    response = requests.get(url, headers=HEADERS)
    print("RESPONSE STATUS:", response.status_code)
    print("RESPONSE TEXT:", response.text)
    if response.status_code != 200:
        raise HTTPException(
            status_code=500,
            detail=f"Recipal API error: {response.status_code} - {response.text}"
        )
    return response.json()


@app.get("/recipal/recipe_ingredients")
def get_recipe_ingredients():
    url = f"{BASE_URL}/api/recipe_ingredients"
    response = requests.get(url, headers=HEADERS)
    print("RESPONSE STATUS:", response.status_code)
    print("RESPONSE TEXT:", response.text)
    if response.status_code != 200:
        raise HTTPException(
            status_code=500,
            detail=f"Recipal API error: {response.status_code} - {response.text}"
        )
    return response.json()


@app.get("/recipal/recipe/{recipe_id}")
def get_recipe_by_id(recipe_id: int):
    url = f"{BASE_URL}/api/recipes/{recipe_id}"
    response = requests.get(url, headers=HEADERS)
    print("RESPONSE STATUS:", response.status_code)
    print("RESPONSE TEXT:", response.text)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return response.json()
