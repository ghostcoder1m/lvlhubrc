from fastapi import FastAPI
from dotenv import load_dotenv
import os

app = FastAPI()

# Load environment variables
load_dotenv()

@app.get("/")
async def root():
    return {"message": "STEPS Marketing System Online"}

print(f"SECRET_KEY loaded: {os.getenv('SECRET_KEY') is not None}")
