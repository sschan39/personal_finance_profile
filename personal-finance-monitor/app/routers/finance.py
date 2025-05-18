from fastapi import APIRouter, HTTPException
from app.models.profile import Profile
from app.services.yahoo_finance import fetch_financial_data
from app.database import save_profile, get_profile

router = APIRouter()

@router.post("/profiles/", response_model=Profile)
async def create_profile(profile: Profile):
    try:
        saved_profile = await save_profile(profile)
        return saved_profile
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/profiles/{profile_id}", response_model=Profile)
async def read_profile(profile_id: int):
    profile = await get_profile(profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.get("/financial-data/{symbol}")
async def get_financial_data(symbol: str):
    try:
        data = await fetch_financial_data(symbol)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))