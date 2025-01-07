from fastapi import FastAPI
from dotenv import load_dotenv
import os
from routers import users, onboarding, leads, campaigns, offers, messages, funnels, pages, elements, automations, triggers, actions, workflows

app = FastAPI()

# Load environment variables
load_dotenv()

# Include routers
app.include_router(users.router)
app.include_router(onboarding.router)
app.include_router(leads.router)
app.include_router(campaigns.router)
app.include_router(offers.router)
app.include_router(messages.router)
app.include_router(funnels.router)
app.include_router(pages.router)
app.include_router(elements.router)
app.include_router(automations.router)
app.include_router(triggers.router)
app.include_router(actions.router)
app.include_router(workflows.router)

@app.get("/")
async def root():
    return {"message": "STEPS Marketing System Online"}

print(f"SECRET_KEY loaded: {os.getenv('SECRET_KEY') is not None}")
