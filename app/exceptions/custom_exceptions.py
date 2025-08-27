class FeedbackNotFoundError(Exception):
    def __init__(self, feedback_id: int):
        self.feedback_id = feedback_id
        super().__init__(f"Feedback with ID {feedback_id} not found")

