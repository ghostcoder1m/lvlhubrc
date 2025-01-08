from fastapi import FastAPI
from dotenv import load_dotenv
import os
from routers import users, leads, campaigns, workflows, triggers, actions

app = FastAPI()

# Load environment variables
load_dotenv()

# Include routers
app.include_router(users.router)
app.include_router(leads.router)
app.include_router(campaigns.router)
app.include_router(workflows.router)
app.include_router(triggers.router)
app.include_router(actions.router)

@app.get("/")
async def root():
    return {"message": "STEPS Marketing System Online"}

print(f"SECRET_KEY loaded: {os.getenv('SECRET_KEY') is not None}")
