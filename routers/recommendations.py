from fastapi import APIRouter
from models.recommendation import RecommendationModel

router = APIRouter()
recommendation_model = RecommendationModel()

@router.on_event("startup")
async def startup_event():
    recommendation_model.load_data("user_item_interactions.csv")
    recommendation_model.train()

@router.post("/recommendations")
async def get_recommendations(user_id: int):
    recommendations = recommendation_model.recommend(user_id)
    return {"recommendations": recommendations}
