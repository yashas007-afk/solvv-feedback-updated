from typing import List

from sqlalchemy.orm import Session

from ..models.feedback import Feedback
from ..schemas.feedback import (
    FeedbackCreate,
    FeedbackUpdate,
)
from ..exceptions.custom_exceptions import FeedbackNotFoundError


def create_feedback(db: Session, feedback_in: FeedbackCreate) -> Feedback:
    new_feedback = Feedback(
        title=feedback_in.title,
        client_type=feedback_in.client_type,
        course_name=feedback_in.course_name,
        date=feedback_in.date,
        client_name=feedback_in.client_name,
        questions=feedback_in.questions,
        time=feedback_in.time,
    )
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    return new_feedback


def list_feedbacks(db: Session) -> List[Feedback]:
    return db.query(Feedback).all()


def get_feedback_or_raise(db: Session, feedback_id: int) -> Feedback:
    feedback = db.query(Feedback).filter(Feedback.id == feedback_id).first()
    if not feedback:
        raise FeedbackNotFoundError(feedback_id)
    return feedback


def update_feedback(
    db: Session, feedback_id: int, updated: FeedbackUpdate
) -> Feedback:
    db_feedback = get_feedback_or_raise(db, feedback_id)
    update_data = updated.model_dump(exclude_unset=True, exclude_none=True)
    for field_name, value in update_data.items():
        setattr(db_feedback, field_name, value)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback


def delete_feedback(db: Session, feedback_id: int) -> None:
    db_feedback = get_feedback_or_raise(db, feedback_id)
    db.delete(db_feedback)
    db.commit()

