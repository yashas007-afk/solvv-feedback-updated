from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas import feedback as schemas
from ..init.database import get_db
from ..services.feedback import (
    create_feedback,
    list_feedbacks,
    get_feedback_or_raise,
    update_feedback as update_feedback_service,
    delete_feedback as delete_feedback_service,
)

router = APIRouter(tags=["feedback"]) 

@router.post("/feedback/preview", response_model=schemas.FeedbackPreview)
def preview_feedback(feedback: schemas.FeedbackCreate):
    return feedback

@router.post("/feedback/submit", response_model=schemas.FeedbackOut)
def submit_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    return create_feedback(db, feedback)

@router.get("/feedbacks", response_model=List[schemas.FeedbackOut])
def get_feedbacks(db: Session = Depends(get_db)):
    return list_feedbacks(db)

@router.get("/feedbacks/{feedback_id}", response_model=schemas.FeedbackOut)
def get_feedback(feedback_id: int, db: Session = Depends(get_db)):
    return get_feedback_or_raise(db, feedback_id)

@router.put("/feedbacks/{feedback_id}", response_model=schemas.FeedbackOut)
def update_feedback(feedback_id: int, updated: schemas.FeedbackUpdate, db: Session = Depends(get_db)):
    return update_feedback_service(db, feedback_id, updated)

@router.delete("/feedbacks/{feedback_id}")
def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    delete_feedback_service(db, feedback_id)
    return {"message": f"Feedback with ID {feedback_id} deleted successfully"}