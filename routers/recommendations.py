from fastapi import APIRouter, Body, HTTPException
from models.recommendation import RecommendationModel

router = APIRouter()
recommendation_model = RecommendationModel()

@router.on_event("startup")
async def startup_event():
    recommendation_model.load_data("user_item_interactions.csv")
    recommendation_model.train()

@router.post("/recommendations")
async def get_recommendations(user_id: int = Body(...)):
    if user_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid user_id. It must be a positive integer.")
    recommendations = recommendation_model.recommend(user_id)
    return {"recommendations": recommendations}
</create_file>

<create_file>
<path>routers/lead_scoring.py</path>
<content>
from fastapi import APIRouter, Body, HTTPException
from models.lead_scoring import LeadScoringModel

router = APIRouter()
lead_scoring_model = LeadScoringModel()

@router.on_event("startup")
async def startup_event():
    lead_scoring_model.load_data("path/to/your/lead_data.csv")
    lead_scoring_model.train()

@router.post("/lead_score")
async def get_lead_score(lead_data: list = Body(...)):
    if not isinstance(lead_data, list) or not lead_data:
        raise HTTPException(status_code=400, detail="Invalid lead_data. It must be a non-empty list.")
    score = lead_scoring_model.score_lead(lead_data)
    return {"lead_score": score}
</create_file>
