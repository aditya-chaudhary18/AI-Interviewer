from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime
from app.models.practice import PracticeStatus

class ResumeDataCreate(BaseModel):
    parsed_json: str
    skills: List[str]
    experience: List[Any]
    education: List[Any]

class PracticeSessionCreate(BaseModel):
    job_role: str
    candidate_id: int
    resume_file: Any # UploadFile

class PracticeSessionResponse(BaseModel):
    id: int
    job_role: str
    status: PracticeStatus
    created_at: datetime
    resume_text: Optional[str] = None
    
    class Config:
        from_attributes = True
