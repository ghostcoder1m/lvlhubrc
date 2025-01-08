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
