
from fastapi import FastAPI, HTTPException, Response
import requests
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

RECIPAL_API_KEY = os.getenv("RECIPAL_API_KEY")
BASE_URL = "https://www.recipal.com/api/v1"
HEADERS = {"Authorization": f"Bearer {RECIPAL_API_KEY}"}


@app.get("/recipal/recipes")
def get_recipes():
    url = f"{BASE_URL}/recipes"
    response = requests.get(url, headers=HEADERS)
    print("RESPONSE STATUS:", response.status_code)
    print("RESPONSE TEXT:", response.text)
    if response.status_code != 200:
        return Response(
            content=f"Recipal API error: {response.status_code}\n{response.text}",
            media_type="text/plain",
            status_code=500
        )
    return response.json()


@app.get("/recipal/recipe/{recipe_id}")
def get_recipe_by_id(recipe_id: int):
    url = f"{BASE_URL}/recipes/{recipe_id}"
    response = requests.get(url, headers=HEADERS)
    print("RESPONSE STATUS:", response.status_code)
    print("RESPONSE TEXT:", response.text)
    if response.status_code != 200:
        return Response(
            content=f"Recipal API error: {response.status_code}\n{response.text}",
            media_type="text/plain",
            status_code=404
        )
    return response.json()


@app.get("/recipal/recipe/{recipe_id}/ingredients")
def get_ingredients_for_recipe(recipe_id: int):
    url = f"{BASE_URL}/recipes/{recipe_id}/recipe_ingredients"
    response = requests.get(url, headers=HEADERS)
    print("RESPONSE STATUS:", response.status_code)
    print("RESPONSE TEXT:", response.text)
    if response.status_code != 200:
        return Response(
            content=f"Recipal API error: {response.status_code}\n{response.text}",
            media_type="text/plain",
            status_code=500
        )
    return response.json()
