from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.campaign import Campaign as DBCampaign
from schemas.campaign import Campaign, CampaignCreate, CampaignUpdate

router = APIRouter(prefix="/campaigns", tags=["campaigns"])

@router.post("/", response_model=Campaign)
def create_campaign(campaign: CampaignCreate, db: Session = Depends(get_db)):
    new_campaign = DBCampaign(**campaign.dict())
    db.add(new_campaign)
    db.commit()
    db.refresh(new_campaign)
    return new_campaign

@router.get("/", response_model=list[Campaign])
def get_campaigns(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    campaigns = db.query(DBCampaign).offset(skip).limit(limit).all()
    return campaigns

@router.get("/{campaign_id}", response_model=Campaign)
def get_campaign(campaign_id: int, db: Session = Depends(get_db)):
    campaign = db.query(DBCampaign).filter(DBCampaign.id == campaign_id).first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign

@router.put("/{campaign_id}", response_model=Campaign)
def update_campaign(campaign_id: int, campaign_update: CampaignUpdate, db: Session = Depends(get_db)):
    campaign = db.query(DBCampaign).filter(DBCampaign.id == campaign_id).first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    for key, value in campaign_update.dict(exclude_unset=True).items():
        setattr(campaign, key, value)
    db.commit()
    db.refresh(campaign)
    return campaign

@router.delete("/{campaign_id}")
def delete_campaign(campaign_id: int, db: Session = Depends(get_db)):
    campaign = db.query(DBCampaign).filter(DBCampaign.id == campaign_id).first()
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    db.delete(campaign)
    db.commit()
    return {"message": "Campaign deleted"}
