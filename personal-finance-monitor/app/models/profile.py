from pydantic import BaseModel

class Profile(BaseModel):
    user_id: int
    name: str
    email: str
    budget: float
    investments: dict
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True